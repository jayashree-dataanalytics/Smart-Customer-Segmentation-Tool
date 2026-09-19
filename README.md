# 🛍️ Smart Customer Segmentation Tool

An interactive Streamlit application that analyzes customer transaction data, segments customers using data-driven business rules, and layers on Generative AI (Gemini) to turn those segments into plain-English business insights.

🔗 **Live demo:** https://smart-customer-segmentation-tool-6ubnxxo5vkd3vyfjcothpn.streamlit.app/

---

## ✨ What it does

- **Upload your own transaction CSV**, or explore the app instantly with the built-in sample dataset (`data/customers.csv`)
- **Cleans & processes transaction data** and rolls it up into customer-level metrics (spend, order count, etc.)
- **Segments customers** into meaningful groups using pandas + business rules
- **Visual dashboards** — business overview KPIs (transactions, customers, revenue, AOV), a segment summary table, and a bar chart of customers per segment
- **AI-powered insights** — enter your own Gemini API key and let AI analyze the segment summary and generate business recommendations

## 🖥️ App Layout

The app is organized into four tabs:

| Tab | What you see |
|---|---|
| 📊 Overview | Key business metrics: transactions, customers, total revenue, average order value |
| 🧾 Transactions | The full (cleaned) transaction dataset |
| 👥 Segmentation | Per-customer segment assignment + segment summary table + customers-by-segment chart |
| 🤖 AI Insights | Enter a Gemini API key and generate an AI-written summary of what the segments mean for the business |

## 🛠️ Tech Stack

- **App framework:** [Streamlit](https://streamlit.io/)
- **Data processing:** pandas
- **AI insights:** Google Generative AI (Gemini) via `google-genai` — the API key is entered by the user in-app (not stored)

## 📁 Project Structure

```
Smart-Customer-Segmentation-Tool/
├── app.py                        # Streamlit entry point / UI (tabs, layout)
├── src/
│   ├── data_processing.py        # load_data, clean_data, create_customer_metrics
│   ├── segmentation.py           # create_segments, create_segment_summary
│   └── ai_insights.py            # generate_insights (Gemini)
├── data/
│   └── customers.csv             # sample dataset used when nothing is uploaded
└── requirements.txt
```

## 🚀 Run it locally

```bash
git clone https://github.com/jayashree-dataanalytics/Smart-Customer-Segmentation-Tool.git
cd Smart-Customer-Segmentation-Tool
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL Streamlit prints (usually `http://localhost:8501`). Upload your own transaction CSV in the sidebar, or leave it blank to explore the sample dataset. To use the AI Insights tab, paste a [Gemini API key](https://ai.google.dev/) into the field there.

## 👩‍💻 Author

**Jayashree Dhanasekar**

---

Feedback and suggestions welcome — feel free to open an issue or connect on LinkedIn!
