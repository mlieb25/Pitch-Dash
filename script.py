
import os
import zipfile

# Create the main Streamlit app.py file
app_code = '''import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="PayFlow Canada - Series A Pitch",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    h1 {
        color: #1f77b4;
        padding-bottom: 1rem;
    }
    h2 {
        color: #2c3e50;
        padding-top: 2rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #1f77b4;
    }
    .highlight-box {
        background-color: #e3f2fd;
        padding: 2rem;
        border-radius: 1rem;
        border-left: 5px solid #1f77b4;
        margin: 2rem 0;
    }
    .cta-box {
        background-color: #c8e6c9;
        padding: 2rem;
        border-radius: 1rem;
        border-left: 5px solid #4caf50;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    financials = pd.read_csv('financials_10yr.csv')
    financials['Date'] = pd.to_datetime(financials['Date'])
    
    key_metrics = pd.read_csv('key_metrics_10yr.csv')
    key_metrics['Date'] = pd.to_datetime(key_metrics['Date'])
    
    roi_data = pd.read_csv('roi_comparison_10yr.csv')
    
    funding_rounds = pd.read_csv('funding_rounds_updated.csv')
    
    return financials, key_metrics, roi_data, funding_rounds

financials, key_metrics, roi_data, funding_rounds = load_data()

# Current month marker
CURRENT_MONTH = 18

# Header Section
st.markdown("<h1 style='text-align: center;'>🚀 PayFlow Canada</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666;'>Revolutionizing SMB Payments in Canada</h3>", unsafe_allow_html=True)

# Series A Opportunity Callout
st.markdown("""
<div class='highlight-box'>
    <h2 style='margin:0; padding:0; border:none; color:#1f77b4;'>💎 Series A Investment Opportunity</h2>
    <h3 style='margin-top:1rem;'>$10M for 20% Equity @ $50M Valuation</h3>
    <p style='font-size:1.1rem; margin-top:1rem;'>Join us at the perfect inflection point - proven traction, massive market, exceptional team.</p>
</div>
""", unsafe_allow_html=True)

# Key Metrics Cards
st.markdown("### 📊 Current Performance (Month 18 - End of Seed Round)")
col1, col2, col3, col4 = st.columns(4)

current_revenue = financials.loc[CURRENT_MONTH - 1, 'Revenue']
current_customers = key_metrics.loc[CURRENT_MONTH - 1, 'Customers']
current_ltv_cac = key_metrics.loc[CURRENT_MONTH - 1, 'LTV_CAC_Ratio']

with col1:
    st.metric("Monthly Revenue", f"${current_revenue:,.0f}", "+32% MoM")
with col2:
    st.metric("Active Customers", f"{current_customers:,}", "+850 customers")
with col3:
    st.metric("LTV/CAC Ratio", f"{current_ltv_cac:.1f}x", "Excellent")
with col4:
    st.metric("5-Year ROI (Series A)", "850%+", "vs 320% Series B")

# Section 1: WHY INVEST NOW
st.markdown("## 🎯 Why Invest in Series A NOW?")
st.markdown("**The earlier you invest, the higher your returns.** Compare 5-year ROI across funding rounds:")

# ROI Comparison Chart
roi_5yr = roi_data[roi_data['Years'] == 5].copy()
roi_5yr = roi_5yr[roi_5yr['Round'].isin(['Series A', 'Series B', 'Series C'])]

fig_roi = go.Figure()

fig_roi.add_trace(go.Bar(
    x=roi_5yr['Round'],
    y=roi_5yr['ROI_Percentage'],
    text=[f"{val:,.0f}%" for val in roi_5yr['ROI_Percentage']],
    textposition='outside',
    marker_color=['#4caf50', '#ff9800', '#f44336'],
    name='5-Year ROI %'
))

fig_roi.update_layout(
    title="5-Year ROI Comparison: Invest Early = Higher Returns",
    xaxis_title="Funding Round",
    yaxis_title="ROI Percentage (%)",
    height=400,
    showlegend=False,
    plot_bgcolor='white'
)

st.plotly_chart(fig_roi, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Series A Advantages:**
    - ✅ 20% equity at $50M valuation
    - ✅ 850%+ projected 5-year ROI
    - ✅ 9.5x return multiple
    - ✅ Proven traction with Seed success
    """)
with col2:
    st.markdown("""
    **Wait for Series B?**
    - ⚠️ Same 20% equity costs $30M (3x more)
    - ⚠️ Only 320% projected 5-year ROI
    - ⚠️ 4.2x return multiple
    - ⚠️ Miss the highest growth phase
    """)

# Section 2: PROVEN TRACTION
st.markdown("## 📈 Proven Traction: Revenue Growth")
st.markdown("**We've exceeded all Seed round targets.** Solid line = actual performance. Dashed line = projections.")

# Revenue chart with historical vs projected
fig_revenue = go.Figure()

# Historical revenue (solid line)
historical_data = financials[financials['Is_Historical'] == True]
projected_data = financials[financials['Is_Historical'] == False]

fig_revenue.add_trace(go.Scatter(
    x=historical_data.index,
    y=historical_data['Revenue'],
    mode='lines',
    name='Actual Performance',
    line=dict(color='#2ecc71', width=3),
    fill='tozeroy',
    fillcolor='rgba(46, 204, 113, 0.2)'
))

fig_revenue.add_trace(go.Scatter(
    x=projected_data.index,
    y=projected_data['Revenue'],
    mode='lines',
    name='Projected',
    line=dict(color='#3498db', width=2, dash='dash'),
    fill='tozeroy',
    fillcolor='rgba(52, 152, 219, 0.1)'
))

# Add vertical line at current month
fig_revenue.add_vline(
    x=CURRENT_MONTH,
    line_dash="dot",
    line_color="red",
    line_width=2,
    annotation_text="YOU ARE HERE - Series A",
    annotation_position="top"
)

fig_revenue.update_layout(
    title="Monthly Revenue: Historical Performance + 10-Year Projection",
    xaxis_title="Months Since Launch",
    yaxis_title="Monthly Revenue ($)",
    height=500,
    hovermode='x unified',
    plot_bgcolor='white'
)

st.plotly_chart(fig_revenue, use_container_width=True)

# Section 3: MARKET OPPORTUNITY
st.markdown("## 🌍 Market Opportunity")

col1, col2 = st.columns([2, 1])

with col1:
    # Market sizing chart
    market_data = pd.DataFrame({
        'Market': ['Total Addressable\\nMarket (TAM)', 'Serviceable Addressable\\nMarket (SAM)', 'Serviceable Obtainable\\nMarket (SOM)'],
        'Value': [45, 12, 0.6],  # in billions
        'Label': ['$45B', '$12B', '$600M']
    })
    
    fig_market = go.Figure()
    
    fig_market.add_trace(go.Bar(
        x=market_data['Market'],
        y=market_data['Value'],
        text=market_data['Label'],
        textposition='outside',
        marker_color=['#1f77b4', '#ff7f0e', '#2ca02c'],
        showlegend=False
    ))
    
    fig_market.update_layout(
        title="Canadian B2B Payments Market",
        yaxis_title="Market Size (Billions CAD)",
        height=400,
        plot_bgcolor='white'
    )
    
    st.plotly_chart(fig_market, use_container_width=True)

with col2:
    st.markdown("### Market Insights")
    st.markdown("""
    - **$45B TAM**: Total Canadian B2B payments market
    - **$12B SAM**: SMB-focused payments segment
    - **$600M SOM**: Our 5-year target
    - **18% CAGR**: Annual market growth
    - **2.5%** market share target by Year 5
    """)

# Section 4: CUSTOMER GROWTH
st.markdown("## 👥 Customer Acquisition")

fig_customers = go.Figure()

# Historical customers
historical_customers = key_metrics[key_metrics['Is_Historical'] == True]
projected_customers = key_metrics[key_metrics['Is_Historical'] == False]

fig_customers.add_trace(go.Scatter(
    x=historical_customers.index,
    y=historical_customers['Customers'],
    mode='lines+markers',
    name='Actual Customers',
    line=dict(color='#2ecc71', width=3),
    marker=dict(size=6)
))

fig_customers.add_trace(go.Scatter(
    x=projected_customers.index,
    y=projected_customers['Customers'],
    mode='lines',
    name='Projected Customers',
    line=dict(color='#3498db', width=2, dash='dash')
))

fig_customers.add_vline(
    x=CURRENT_MONTH,
    line_dash="dot",
    line_color="red",
    line_width=2,
    annotation_text="Series A Opportunity",
    annotation_position="top"
)

fig_customers.update_layout(
    title="Customer Growth: From 35 to 1M+ over 10 Years",
    xaxis_title="Months Since Launch",
    yaxis_title="Number of Customers",
    height=450,
    hovermode='x unified',
    plot_bgcolor='white'
)

st.plotly_chart(fig_customers, use_container_width=True)

# Section 5: KEY METRICS
st.markdown("## 🎯 Key Unit Economics (Current)")

col1, col2, col3, col4 = st.columns(4)

current_cac = key_metrics.loc[CURRENT_MONTH - 1, 'CAC']
current_ltv = key_metrics.loc[CURRENT_MONTH - 1, 'LTV']
current_churn = key_metrics.loc[CURRENT_MONTH - 1, 'Churn_Rate']
current_volume = key_metrics.loc[CURRENT_MONTH - 1, 'Transaction_Volume']

with col1:
    st.metric(
        "Customer Acquisition Cost (CAC)",
        f"${current_cac:.0f}",
        delta="-15% vs Q1",
        delta_color="inverse"
    )

with col2:
    st.metric(
        "Lifetime Value (LTV)",
        f"${current_ltv:.0f}",
        delta="+25% vs Q1",
        delta_color="normal"
    )

with col3:
    st.metric(
        "LTV / CAC Ratio",
        f"{current_ltv_cac:.1f}x",
        delta="World-class (>3x)",
        delta_color="off"
    )

with col4:
    st.metric(
        "Monthly Churn Rate",
        f"{current_churn:.1f}%",
        delta="-2% vs Q1",
        delta_color="inverse"
    )

st.markdown("""
**Industry Benchmarks:**
- LTV/CAC > 3.0 = Excellent ✅
- CAC Payback < 12 months = Strong ✅
- Monthly Churn < 5% = Healthy ✅

**PayFlow Canada exceeds all benchmarks.**
""")

# Section 6: CALL TO ACTION
st.markdown("## 💼 Investment Terms")

st.markdown("""
<div class='cta-box'>
    <h3>Series A Round Details</h3>
    <ul style='font-size:1.1rem; line-height:2rem;'>
        <li><strong>Amount Raising:</strong> $10,000,000 CAD</li>
        <li><strong>Pre-Money Valuation:</strong> $50,000,000 CAD</li>
        <li><strong>Equity Offered:</strong> 20%</li>
        <li><strong>Use of Funds:</strong> Product development (40%), Sales & Marketing (40%), Team expansion (20%)</li>
        <li><strong>Expected Close:</strong> Q1 2025</li>
        <li><strong>Projected 5-Year ROI:</strong> 850%+</li>
    </ul>
    <h3 style='margin-top:2rem;'>Ready to Invest?</h3>
    <p style='font-size:1.1rem;'>Contact: <strong>invest@payflowcanada.com</strong></p>
    <p style='font-size:1.1rem;'>Schedule a call: <strong>calendly.com/payflow-series-a</strong></p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>PayFlow Canada Inc.</strong> | Toronto, ON | Fintech - B2B Payments</p>
    <p><em>This presentation contains forward-looking statements and projections based on current market conditions and assumptions.</em></p>
</div>
""", unsafe_allow_html=True)
'''

# Write the app.py file
with open('app.py', 'w') as f:
    f.write(app_code)

print("✓ app.py created successfully!")
