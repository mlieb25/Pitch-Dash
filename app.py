import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="PayFlow Canada - Series A Pitch",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Header height offset (pixels) - adjust if your header or top callouts change height
HEADER_OFFSET = 140

# CSS for full-viewport layout and responsive grid
st.markdown(f"""
<style>
/* Make the app take the full viewport and remove body scroll */
html, body, .main, .block-container, .stApp {{
    height: 100%;
    margin: 0;
    padding: 0;
}}
.block-container {{
    padding-top: 8px;
    padding-left: 12px;
    padding-right: 12px;
    padding-bottom: 8px;
    height: 100vh;          /* full viewport */
    box-sizing: border-box;
    overflow: hidden;       /* prevent the main page from scrolling */
}}

/* Create equal-height column cells (2 rows). We subtract HEADER_OFFSET for header space.
   The calc divides remaining viewport into two equal rows. */
[data-testid="column"] > div {{
    height: calc((100vh - {HEADER_OFFSET}px) / 2);
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    padding: 8px 8px 8px 8px;
    min-height: 0; /* allow flex children to shrink properly */
}}

/* Make Plotly chart containers expand to fill the column cell */
.stPlotlyChart > div, .stPlotlyChart > div > div {{
    flex: 1 1 auto;
    height: 100% !important;
    min-height: 0;
}}

h1 {{
    color: #1f77b4;
    margin: 0;
    padding: 0;
}}
.highlight-box {{
    background-color: #e3f2fd;
    padding: 16px;
    border-radius: 8px;
    border-left: 5px solid #1f77b4;
    margin: 8px 0 12px 0;
}}
.metric-box {{
    background-color: #f7f9fc;
    padding: 12px;
    border-radius: 8px;
    border: 1px solid #e6eef8;
    text-align: center;
}}
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    financials = pd.read_csv('financials_10yr.csv')
    if 'Date' in financials.columns:
        financials['Date'] = pd.to_datetime(financials['Date'])

    key_metrics = pd.read_csv('key_metrics_10yr.csv')
    if 'Date' in key_metrics.columns:
        key_metrics['Date'] = pd.to_datetime(key_metrics['Date'])

    roi_data = pd.read_csv('roi_comparison_10yr.csv')
    funding_rounds = pd.read_csv('funding_rounds_updated.csv')

    return financials, key_metrics, roi_data, funding_rounds

financials, key_metrics, roi_data, funding_rounds = load_data()

# Current month marker (example)
CURRENT_MONTH = 18

# Header / Intro (kept compact to help fit into single viewport)
st.markdown("<h1 style='text-align: center;'>🚀 PayFlow Canada</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666; margin-top:4px;'>Revolutionizing SMB Payments in Canada</h3>", unsafe_allow_html=True)

# Series A Opportunity Callout (compact)
st.markdown("""
<div class='highlight-box'>
    <div style="font-weight:700; font-size:18px; color:#1f77b4;">💎 Series A Investment Opportunity</div>
    <div style="margin-top:6px; font-size:15px;">$10M for 20% Equity @ $50M Valuation</div>
</div>
""", unsafe_allow_html=True)

# Small metric strip (kept minimal height)
try:
    current_revenue = financials.loc[CURRENT_MONTH - 1, 'Revenue']
    current_customers = key_metrics.loc[CURRENT_MONTH - 1, 'Customers']
except Exception:
    current_revenue = None
    current_customers = None

cols = st.columns([1,1,1,1])
with cols[0]:
    st.markdown(f"<div class='metric-box'><strong>Month {CURRENT_MONTH}</strong><div style='font-size:16px'>Current</div></div>", unsafe_allow_html=True)
with cols[1]:
    st.markdown(f"<div class='metric-box'><strong>Revenue</strong><div>${current_revenue if current_revenue is not None else '—'}</div></div>", unsafe_allow_html=True)
with cols[2]:
    st.markdown(f"<div class='metric-box'><strong>Customers</strong><div>{int(current_customers) if pd.notna(current_customers) else '—'}</div></div>", unsafe_allow_html=True)
with cols[3]:
    st.markdown(f"<div class='metric-box'><strong>Valuation</strong><div>$50M (Target)</div></div>", unsafe_allow_html=True)

# Build the four main figures (no fixed heights; let the container/CSS size them)
# Revenue figure
if 'Date' in financials.columns and 'Revenue' in financials.columns:
    fig_revenue = px.line(financials, x='Date', y='Revenue', title='Revenue (10yr)')
else:
    fig_revenue = go.Figure()
    fig_revenue.update_layout(title='Revenue (data missing)')

fig_revenue.update_layout(autosize=True, margin=dict(l=20,r=20,t=40,b=20))

# Customers / Key Metrics figure
if 'Date' in key_metrics.columns and 'Customers' in key_metrics.columns:
    fig_customers = px.line(key_metrics, x='Date', y='Customers', title='Customers (10yr)')
else:
    fig_customers = go.Figure()
    fig_customers.update_layout(title='Customers (data missing)')

fig_customers.update_layout(autosize=True, margin=dict(l=20,r=20,t=40,b=20))

# ROI comparison figure
if 'Year' in roi_data.columns or 'Date' in roi_data.columns:
    # try using first numeric column as example
    numeric_cols = roi_data.select_dtypes(include='number').columns.tolist()
    if numeric_cols:
        fig_roi = px.line(roi_data, x=roi_data.columns[0], y=numeric_cols[0], title='ROI Comparison')
    else:
        fig_roi = go.Figure()
        fig_roi.update_layout(title='ROI (data missing)')
else:
    fig_roi = go.Figure()
    fig_roi.update_layout(title='ROI (data missing)')

fig_roi.update_layout(autosize=True, margin=dict(l=20,r=20,t=40,b=20))

# Funding rounds / Waterfall or table figure
if 'Round' in funding_rounds.columns:
    fig_funding = px.bar(funding_rounds, x='Round', y=funding_rounds.select_dtypes(include='number').columns.tolist()[0] if funding_rounds.select_dtypes(include='number').columns.any() else None, title='Funding Rounds')
    fig_funding.update_layout(autosize=True, margin=dict(l=20,r=20,t=40,b=20))
else:
    fig_funding = go.Figure()
    fig_funding.update_layout(title='Funding Rounds (data missing)')

# Layout the charts in a 2x2 grid using Streamlit columns. Each column cell's height is controlled by the CSS above.
row1 = st.columns(2, gap="large")
with row1[0]:
    st.plotly_chart(fig_revenue, use_container_width=True, config={'responsive': True, 'displayModeBar': False})
with row1[1]:
    st.plotly_chart(fig_customers, use_container_width=True, config={'responsive': True, 'displayModeBar': False})

row2 = st.columns(2, gap="large")
with row2[0]:
    st.plotly_chart(fig_roi, use_container_width=True, config={'responsive': True, 'displayModeBar': False})
with row2[1]:
    st.plotly_chart(fig_funding, use_container_width=True, config={'responsive': True, 'displayModeBar': False})

# Compact footer call-to-action (kept minimal)
st.markdown("<div style='margin-top:6px; font-size:14px; color:#444;'>Contact: invest@payflowcanada.com — Series A materials available on request.</div>", unsafe_allow_html=True)
