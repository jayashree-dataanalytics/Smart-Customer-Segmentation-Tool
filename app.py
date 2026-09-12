import streamlit as st


from src.data_processing import (
    load_data,
    clean_data,
    create_customer_metrics
)


from src.segmentation import (
    create_segments,
    create_segment_summary
)


from src.ai_insights import (
    generate_insights
)




# ==========================================
# Page Configuration
# ==========================================


st.set_page_config(
    page_title="Smart Customer Segmentation",
    page_icon="🛍️",
    layout="wide"
)




# ==========================================
# Load Customer Data
# ==========================================


def load_customer_data():


    st.sidebar.header("📂 Customer Data")


    uploaded_file = st.sidebar.file_uploader(
        "Upload transaction CSV",
        type=["csv"]
    )


    if uploaded_file is not None:


        df = load_data(uploaded_file)


        st.sidebar.success(
            "Uploaded dataset loaded!"
        )


    else:


        df = load_data(
            "data/customers.csv"
        )


        st.sidebar.info(
            "Using sample dataset"
        )


    return df




# ==========================================
# Process Data
# ==========================================


def process_data(df):


    # Clean transaction data
    df = clean_data(df)


    # Create customer-level metrics
    customer_metrics = create_customer_metrics(
        df
    )


    # Create customer segments
    customer_segments = create_segments(
        customer_metrics
    )


    # Create segment summary
    segment_summary = create_segment_summary(
        customer_segments
    )


    return (
        df,
        customer_metrics,
        customer_segments,
        segment_summary
    )




# ==========================================
# Header
# ==========================================


def show_header():


    st.title(
        "🛍️ Smart Customer Segmentation Tool"
    )


    st.write(
        "Understand your customers using "
        "Pandas, business rules and Generative AI."
    )




# ==========================================
# Overview
# ==========================================


def show_overview(
    df,
    customer_metrics
):


    st.subheader("📊 Business Overview")


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Transactions",
        f"{len(df):,}"
    )


    col2.metric(
        "Customers",
        f"{len(customer_metrics):,}"
    )


    col3.metric(
        "Total Revenue",
        f"₹{df['amount'].sum():,.0f}"
    )


    col4.metric(
        "Average Order Value",
        f"₹{df['amount'].mean():,.0f}"
    )




# ==========================================
# Transaction Data
# ==========================================


def show_transaction_data(df):


    st.subheader("🧾 Transaction Data")


    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )




# ==========================================
# Customer Segmentation
# ==========================================


def show_customer_segments(
    customer_segments
):


    st.subheader("👥 Customer Segments")


    st.dataframe(
        customer_segments,
        use_container_width=True,
        hide_index=True
    )




# ==========================================
# Segment Summary
# ==========================================


def show_segment_summary(
    segment_summary
):


    st.subheader("📈 Segment Summary")


    st.dataframe(
        segment_summary,
        use_container_width=True,
        hide_index=True
    )


    st.subheader(
        "Customers by Segment"
    )


    chart_data = (
        segment_summary
        .set_index("segment")["customers"]
    )


    st.bar_chart(chart_data)


# ==========================================
# AI Insights
# ==========================================


def show_ai_insights(segment_summary):


    st.subheader(
        "🤖 AI-Powered Business Insights"
    )


    st.write(
        "Enter your Gemini API key and let AI "
        "analyze the customer segments."
    )


    # API key input
    api_key = st.text_input(
        "🔑 Gemini API Key",
        type="password",
        placeholder="Enter your Gemini API key"
    )


    # Generate insights button
    if st.button(
        "✨ Generate AI Insights"
    ):


        if not api_key:


            st.warning(
                "Please enter your Gemini API key first."
            )


            return


        with st.spinner(
            "Gemini is analyzing your customer segments..."
        ):


            try:


                insights = generate_insights(
                    segment_summary,
                    api_key
                )


                st.markdown(insights)


            except Exception as e:


                st.error(
                    "Something went wrong while "
                    "generating AI insights."
                )


                st.exception(e)


# ==========================================
# Main Application
# ==========================================


def main():


    # --------------------------------------
    # Header
    # --------------------------------------


    show_header()


    # --------------------------------------
    # Load data
    # --------------------------------------


    df = load_customer_data()


    # --------------------------------------
    # Process data
    # --------------------------------------


    (
        df,
        customer_metrics,
        customer_segments,
        segment_summary
    ) = process_data(df)


    # --------------------------------------
    # Create tabs
    # --------------------------------------


    overview_tab, transactions_tab, segmentation_tab, ai_tab = st.tabs(
        [
            "📊 Overview",
            "🧾 Transactions",
            "👥 Segmentation",
            "🤖 AI Insights"
        ]
    )


    # --------------------------------------
    # Overview Tab
    # --------------------------------------


    with overview_tab:


        show_overview(
            df,
            customer_metrics
        )


    # --------------------------------------
    # Transactions Tab
    # --------------------------------------


    with transactions_tab:


        show_transaction_data(
            df
        )


    # --------------------------------------
    # Segmentation Tab
    # --------------------------------------


    with segmentation_tab:


        show_customer_segments(
            customer_segments
        )


        st.divider()


        show_segment_summary(
            segment_summary
        )


    # --------------------------------------
    # AI Insights Tab
    # --------------------------------------


    with ai_tab:


        show_ai_insights(
            segment_summary
        )




# ==========================================
# Application Entry Point
# ==========================================


if __name__ == "__main__":
    main()

