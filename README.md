# DataAuto Pilot AI 🤖

**An AI-powered data analysis assistant that helps users clean, explore, and understand CSV datasets.**

🔗 **Live Demo:** https://dataautopilotai-z6mm9kjco4tul2drmccufh.streamlit.app/

## 📌 Overview

DataAuto Pilot AI simplifies the data analysis workflow by combining automated data cleaning, exploratory data analysis (EDA), visual insights, and Gemini-powered question answering in one interactive application.

Users can upload a CSV file, inspect data quality, handle missing values and duplicates, explore charts, and ask questions about their data using natural language.

## ✨ Features

- **CSV Upload & Data Profiling:** View dataset dimensions, column names, and data quality.
- **Automated Data Cleaning:** Remove duplicate rows and handle missing values using median, mode, or row removal.
- **Exploratory Data Analysis:** Generate statistical summaries, distributions, categorical charts, and correlation analysis.
- **Smart Data Insights:** Identify common categories, price statistics, and highly rated products when supported by the dataset.
- **AI-Powered Q&A:** Ask questions about dataset statistics using the Gemini API and Python-calculated summaries.
- **Downloadable Reports:** Export cleaned CSV files and analysis reports.

## 🛠️ Tech Stack

- **Language:** Python
- **Data Processing:** Pandas
- **Visualization:** Plotly
- **Web Application:** Streamlit
- **Generative AI:** Google Gemini API
- **Version Control:** Git and GitHub
- **Deployment:** Streamlit Community Cloud

## ⚙️ How It Works

1. Upload a CSV dataset.
2. Review its structure and data quality.
3. Apply cleaning operations.
4. Explore statistical summaries and visualizations.
5. Ask Gemini questions about calculated findings.
6. Download the cleaned dataset or analysis report.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/shaikwaiza/DataAutoPilotAI.git
cd DataAutoPilotAI
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create `.streamlit/secrets.toml` and add:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
```

Use your own valid API key. Never commit this file to GitHub.

### 5. Start the application

```bash
streamlit run app.py
```

## 🔐 Security

API keys are stored in Streamlit secrets or local secrets configuration, not directly in the application source code. Secret files are excluded from version control.

## 🎯 Project Goal

To make data analysis more accessible by combining Python-based analytics, interactive visualization, automated data cleaning, and generative AI.

## 👩‍💻 Author

**Waiza Shaik**

B.Tech — Artificial Intelligence & Data Science

[GitHub Profile](https://github.com/shaikwaiza)
