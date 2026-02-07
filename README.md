# 📊 Book Market Analytics Platform

An end-to-end web scraping and data analytics project developed as part of a final-year engineering / internship assessment. The project focuses on collecting public e-commerce data, processing it into a structured format, and visualizing meaningful market insights through an interactive dashboard.

## 📌 Project Overview

This project demonstrates a complete **data engineering pipeline** starting from web scraping to data analysis and visualization.

Book data is collected from a publicly available website, where unstructured HTML content is scraped, cleaned, transformed, and stored in a structured SQLite database. The processed data is then analyzed and visualized using a Streamlit-based dashboard to support market-level insights.

A rule-based **Opportunity Detection Module** is implemented to identify high-rated books that are priced below the market average.

*Note: This project uses data from publicly accessible web pages and is intended strictly for educational and academic purposes.*

## ✨ Key Features

- Automated web scraping with pagination handling  
- Data cleaning and normalization (rating conversion, currency conversion)  
- Structured storage using SQLite  
- Interactive dashboard for market analysis  
- Rule-based identification of underpriced, high-rated books  
- CSV export for further analysis  

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Web Scraping:** Scrapy  
- **Data Processing:** Pandas, NumPy  
- **Database:** SQLite  
- **Visualization & UI:** Streamlit, Plotly  
- **Automation:** PowerShell (optional)

## 🧠 Technical Highlights

- **Pagination Handling:** Scraped data across multiple pages to ensure complete dataset collection  
- **Data Quality Enforcement:** Cleaned raw HTML data and standardized ratings and prices  
- **Decoupled Architecture:** Scraping and dashboard layers operate independently using a shared database  


## 📊 Dashboard Capabilities

- Inventory size and average pricing metrics  
- Category-wise distribution analysis  
- Price vs rating comparison  
- Identification of potential value opportunities  


## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

git clone https://github.com/yourusername/book-market-analytics.git
cd book-market-analytics

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run the Scraper
cd scraper
scrapy crawl books

### 4️⃣ Launch the Dashboard
streamlit run dashboard/app.py

### 📈 Learning Outcomes

Hands-on experience with web scraping and HTML parsing

Understanding of ETL (Extract, Transform, Load) pipelines

Practical exposure to data cleaning and database management

Building interactive dashboards for data-driven insights
