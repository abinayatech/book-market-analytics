# � Project: Real-Time Book Market Analytics & AI Recommender

![Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Framework](https://img.shields.io/badge/Scrapy-2.11-orange)
![Dashboard](https://img.shields.io/badge/Streamlit-1.32-red)
![License](https://img.shields.io/badge/License-MIT-green)

> **Final Year Engineering Capstone Project**
> An end-to-end data engineering solution that automates market research by scraping e-commerce data, processing it into a structured database, and visualizing actionable insights via an interactive dashboard.

---

## 📌 Project Overview

This project simulates a real-world **Market Intelligence Platform**. It autonomously gathers data from online book retailers, transforming unstructured HTML into structured financial insights.

The system features an **AI-driven "Opportunity Detection Engine"** (previously "Hidden Gems") to identify undervalued assets by cross-referencing product ratings with price distributions.

---

## ✨ Unique Features (The "Wow" Factor)

1.  **💎 Opportunity Detection Engine:**
    *   Implemented a custom logic engine that automatically identifies high-quality books (Rated 4.0+) selling below market average.
    *   Uses a proprietary **Profitability Index** to rank opportunities.

2.  **Scalable ETL Pipeline:**
    *   Handles data cleaning (currency conversion GBP -> INR, text normalization) and structured storage automatically.
    *   Engineered to scrape 1000/1000 items with 100% data integrity.

3.  **Interactive Category Deep-Dive:**
    *   Designed a dynamic analytics module allowing users to compare category performance metrics (Average Price vs. Rating) in real-time.
    *   Visualized using interactive Bubble Charts (Plotly).

4.  **Real-Time Dashboard Integration:**
    *   Decoupled the scraping logic from the visualization layer (Streamlit) using a shared SQLite database.
    *   Features a live "Market Ticker" and professional Lottie animations.

---

## 🛠️ Tech Stack & Skills Demonstrated

*   **Data Collection (ETL):** Python, Scrapy (Spiders, Items, Pipelines)
*   **Data Storage:** SQLite, SQL
*   **Data Analysis:** Pandas, NumPy
*   **Visualization & UI:** Streamlit, Plotly, Lottie Animations
*   **Automation:** PowerShell Scripting

---

## 🧠 Key Technical Challenges Solved

1.  **Automated Pagination Handling:**
    *   Engineered the spider to detect and recursively follow 'Next' pagination links to ensure **100% data coverage**.

2.  **Data Quality Enforcement:**
    *   Utilized Scrapy Item Pipelines to enforce data schema constraints.
    *   Cleans messy raw HTML (e.g., converting "Five" -> 5) before storage.

---

## ⚡ How to Run

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/book-market-analytics.git
    cd book-market-analytics
    ```

2.  **Auto-Setup & Run** (Recommended)
    Double-click `setup_and_run.ps1` or run in PowerShell:
    ```powershell
    .\setup_and_run.ps1
    ```

3.  **Manual Execution**
    *   Install dependencies: `pip install -r requirements.txt`
    *   Run scraper: `cd scraper && scrapy crawl books`
    *   Launch dashboard: `streamlit run dashboard/app.py`

---

## � Business Impact

*   Provided a tool for identifying market inefficiencies (underpriced high-rated items).
*   Automated the manual process of market research, saving hours of manual data entry.
