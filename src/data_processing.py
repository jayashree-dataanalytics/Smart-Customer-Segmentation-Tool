import pandas as pd




def load_data(file):
    """
    Load transaction data from a CSV file.
    """
    df = pd.read_csv(file)


    return df




def clean_data(df):
    """
    Clean missing values in the transaction data.
    """


    df = df.copy()


    # Fill missing category with the most common category
    df["category"] = df["category"].fillna(
        df["category"].mode()[0]
    )


    # Fill missing city
    df["city"] = df["city"].fillna("Unknown")


    # Fill missing discount
    df["discount_pct"] = df["discount_pct"].fillna(0)


    # Recalculate missing transaction amount
    missing_amount = df["amount"].isna()


    df.loc[missing_amount, "amount"] = (
        df.loc[missing_amount, "quantity"]
        * df.loc[missing_amount, "unit_price"]
        * (
            1
            - df.loc[missing_amount, "discount_pct"] / 100
        )
    )


    return df




def create_customer_metrics(df):
    """
    Convert transaction-level data
    into customer-level metrics.
    """


    customer_metrics = (
        df.groupby("customer_id")
        .agg(
            total_spend=("amount", "sum"),
            total_orders=("transaction_id", "count"),
            total_quantity=("quantity", "sum"),
            average_order_value=("amount", "mean")
        )
        .reset_index()
    )


    # Number of unique product categories
    category_count = (
        df.groupby("customer_id")["category"]
        .nunique()
        .reset_index(name="category_count")
    )


    # Add category count to customer metrics
    customer_metrics = customer_metrics.merge(
        category_count,
        on="customer_id",
        how="left"
    )


    return customer_metrics

