import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import requests
import os
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="MarketIntel | Analytics Suite",
    page_icon="iq",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Currency Conversion
GBP_TO_INR = 105.0

# === LOTTIE ANIMATION (Professional & Subtle) ===
@st.cache_data
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Use a clean data visualization animation
lottie_data = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_tloigoib.json") 

# === CUSTOM CSS (High Visibility & Clean Fonts) ===
st.markdown("""
    <style>
    /* Global Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #333;
    }
    
    /* Metrics Styling - Professional Card */
    div[data-testid="stMetricValue"] {
        font-size: 32px;
        color: #1a73e8; /* Google Blue */
        font-weight: 700;
    }
    
    /* Chart Container Styling */
    .plotly-graph-div {
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 10px;
        background-color: white;
    }
    
    </style>
    """, unsafe_allow_html=True)

# === LOAD DATA ===
db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'books.db')

if not os.path.exists(db_path):
    st.error("System Initialization Failed: Database connection error.")
    st.stop()

@st.cache_data
def load_data():
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT title, price, rating, category, upc, description FROM books", conn)
        conn.close()
        df['price_inr'] = df['price'] * GBP_TO_INR
        return df
    except:
        return pd.DataFrame()

df = load_data()

# === HEADER SECTION (Clean & Modern) ===
col_anim, col_title = st.columns([1, 6])
with col_anim:
    if lottie_data:
        st_lottie(lottie_data, height=100, key="data_viz")
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/3063/3063822.png", width=80)

with col_title:
    st.title("MarketIntel™ Analytics Platform")
    st.markdown("**Web Scraping & Data Analysis Project**")

st.markdown("---")

# === KEY PERFORMANCE INDICATORS (KPIs) ===
if not df.empty:
    total_val = df['price_inr'].sum()
    avg_p = df['price_inr'].mean()
    count = len(df)
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Tracked Inventory", f"{count:,}", help="Total unique SKUs in database")
    kpi2.metric("Market Valuation", f"₹{total_val:,.0f}", help="Total estimated market value of tracked items")
    kpi3.metric("Avg. Unit Price", f"₹{avg_p:,.0f}", help="Average listing price across all categories")
    kpi4.metric("Active Categories", len(df['category'].unique()), help="Number of distinct product segments")

st.markdown("---")

# === MAIN WORKSPACE ===
tab_opp, tab_market, tab_data = st.tabs(["🚀 Opportunity Detection Engine", "📊 Market Trends Analysis", "📂 Data Export"])

# --- TAB 1: OPPORTUNITY DETECTION ENGINE (Core Feature) ---
with tab_opp:
    st.subheader("Primary Analytical Module")
    st.info("Identifies high-quality assets (Rating ≥ 4/5) with acquisition costs below market average.")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown("**Search Parameters**")
        budget = st.slider("Max Acquisition Cost (₹)", 500, 5000, 2000, 100)
        min_rating = st.selectbox("Minimum Quality Standard", [5, 4, 3], index=1)
    
    with c2:
        # Logic: High Rating AND Low Price
        opps = df[(df['rating'] >= min_rating) & (df['price_inr'] <= budget)].copy()
        
        # Calculate "Profitability Index" (Composite metric)
        # Higher Rating + Lower Price = Higher Score
        opps['Profitability_Index'] = (opps['rating'] * 20) + (1 - (opps['price_inr'] / 5000)) * 50
        opps = opps.sort_values(by='Profitability_Index', ascending=False)
        
        match_count = len(opps)
        
        st.success(f"System identified {match_count} potential arbitrage opportunities.")
        
        if match_count > 0:
            st.dataframe(
                opps[['title', 'category', 'price_inr', 'rating', 'Profitability_Index']].head(15).style.background_gradient(cmap='Greens', subset=['Profitability_Index']),
                use_container_width=True,
                height=400
            )
            
            # Usefulness: Export Report Button
            csv = opps.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download Opportunity Report (CSV)",
                csv,
                "arbitrage_report.csv",
                "text/csv",
                key='download-csv'
            )
        else:
            st.warning("No opportunities found match current criteria.")

# --- TAB 2: MARKET TRENDS ANALYSIS ---
with tab_market:
    st.subheader("Market Dynamics Analysis")
    st.caption("Strategic insights into pricing strategies and category performance.")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("**Pricing Strategy Distribution**")
        # Histogram improved for visibility
        fig = px.histogram(df, x="price_inr", nbins=40,
                           color_discrete_sequence=['#1a73e8'],
                           labels={'price_inr': 'Unit Price (₹)', 'count': 'Number of Books'})
        fig.update_layout(
            showlegend=False,
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis_title="Price Range (₹)",
            yaxis_title="Inventory Count",
            bargap=0.1,
            hoverlabel=dict(bgcolor="white", font_size=12) # Clean tooltip
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col_right:
        st.markdown("**Category Matrix: Price vs. Quality**")
        st.caption("Each point represents the average performance of a distinct category.") # Added tooltip text
        
        # Aggregation for scatter plot
        cat_stats = df.groupby('category').agg(
            Avg_Price=('price_inr', 'mean'),
            Avg_Rating=('rating', 'mean'),
            Volume=('title', 'count')
        ).reset_index()
        
        # Scatter Plot improved for visibility
        fig2 = px.scatter(cat_stats, x="Avg_Price", y="Avg_Rating",
                          size="Volume", color="Avg_Rating",
                          hover_name="category",
                          size_max=60, # Increase visual size of bubbles
                          color_continuous_scale="RdYlGn",
                          labels={
                              "Avg_Price": "Average Price (₹)",
                              "Avg_Rating": "Quality Score (1-5)",
                              "Volume": "Book Volume"
                          })
        fig2.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(showgrid=True, gridcolor='#eee', title="Category Average Price (₹)"), # Explicit Label
            yaxis=dict(showgrid=True, gridcolor='#eee', range=[0.5, 5.5], title="Category Quality Rating (1-5)"), # Explicit Label
            hoverlabel=dict(bgcolor="white", font_size=12) # Clean tooltip
        )
        st.plotly_chart(fig2, use_container_width=True)

# --- TAB 3: DATA EXPORT ---
with tab_data:
    st.subheader("Global Inventory Database")
    
    st.dataframe(df, use_container_width=True, height=600)
    
    csv_full = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        "📥 Export Full Database (CSV)",
        csv_full,
        "full_market_data.csv",
        "text/csv",
        key='download-full'
    )

st.markdown("---")
st.caption("MarketIntel™ Analytics Platform • Web Scraping & Data Analysis • v2.3")
