import pandas as pd




def create_segments(df):
    """
    Assign a business segment to each customer
    based on spending and order frequency.
    """


    df = df.copy()


    # Calculate spending thresholds
    high_spend = df["total_spend"].quantile(0.70)
    low_spend = df["total_spend"].quantile(0.30)


    # Calculate order-frequency thresholds
    high_orders = df["total_orders"].quantile(0.70)
    low_orders = df["total_orders"].quantile(0.30)


    # Business rules
    def assign_segment(row):


        # High-value customer:
        # High spending AND frequent orders
        if (
            row["total_spend"] >= high_spend
            and row["total_orders"] >= high_orders
        ):
            return "High Value"


        # Occasional customer:
        # Low spending AND few orders
        elif (
            row["total_spend"] <= low_spend
            and row["total_orders"] <= low_orders
        ):
            return "Occasional"


        # Everyone else
        else:
            return "Regular"


    # Apply the business rules
    df["segment"] = df.apply(
        assign_segment,
        axis=1
    )


    return df




def create_segment_summary(df):
    """
    Create a summary of customers by segment.
    """


    segment_summary = (
        df.groupby("segment")
        .agg(
            customers=("customer_id", "count"),
            total_revenue=("total_spend", "sum"),
            average_spend=("total_spend", "mean"),
            average_orders=("total_orders", "mean")
        )
        .reset_index()
    )


    # Round numerical values
    segment_summary["total_revenue"] = (
        segment_summary["total_revenue"].round(2)
    )


    segment_summary["average_spend"] = (
        segment_summary["average_spend"].round(2)
    )


    segment_summary["average_orders"] = (
        segment_summary["average_orders"].round(2)
    )


    return segment_summary

