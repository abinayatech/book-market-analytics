# 📊 Book Market Analytics Platform

A web scraping and data analysis project that collects book data from a public website, processes it into a structured database, and visualizes market insights using an interactive dashboard.

---

## 📌 Project Overview

This project demonstrates an end-to-end data pipeline starting from **web scraping** to **data analysis and visualization**.

Book data is scraped from a publicly available website, cleaned and transformed using Python, stored in an SQLite database, and analyzed through a Streamlit-based dashboard. The system also includes a rule-based logic to identify **high-rated books priced below the market average**.

*Note: This project uses data from publicly accessible web pages and is intended only for educational and academic purposes.*

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Web Scraping:** Scrapy  
- **Data Processing:** Pandas, NumPy  
- **Database:** SQLite  
- **Visualization & UI:** Streamlit  
- **Automation:** PowerShell (optional)

---

## ✨ Key Features

- Automated web scraping with pagination handling  
- Data cleaning and normalization (price conversion, rating formatting)  
- Structured storage using SQLite database  
- Interactive dashboard for market analysis  
- Rule-based identification of high-rated, underpriced books  
- CSV export for further analysis  

---

## 🧠 Technical Highlights

- **Pagination Handling:** Scraped data across multiple pages to ensure complete data collection  
- **Data Cleaning:** Converted raw HTML data into consistent numeric formats  
- **Decoupled Architecture:** Scraping and dashboard layers operate independently using a shared database  

---

## 📊 Dashboard Insights

- Total inventory count  
- Average price analysis  
- Category-wise distribution  
- Price vs rating comparison  
- Identification of potential value books  

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/book-market-analytics.git
cd book-market-analytics
2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Scraper
cd scraper
scrapy crawl books

4️⃣ Launch the Dashboard
streamlit run app.py

📈 Learning Outcomes

Practical experience with web scraping and HTML parsing

Understanding of ETL (Extract, Transform, Load) pipelines

Hands-on data cleaning and database handling

Building interactive dashboards for data-driven insights