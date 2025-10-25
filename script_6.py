
# Need to regenerate the data files - they were created earlier but not in current session
# Let me recreate all the data quickly

import pandas as pd
import numpy as np
import json
from datetime import datetime

np.random.seed(42)

# Company info
company_info = {
    "name": "PayFlow Canada",
    "tagline": "Revolutionizing SMB Payments in Canada",
    "founded": "2024",
    "location": "Toronto, ON",
    "sector": "Fintech - B2B Payments",
    "stage": "Seeking Series A"
}

# Market data
market_data = {
    "total_addressable_market": 45000000000,
    "serviceable_addressable_market": 12000000000,
    "serviceable_obtainable_market": 600000000,
    "target_market_share_5yr": 0.025,
    "cagr": 0.18
}

# Save JSON files
with open('company_info.json', 'w') as f:
    json.dump(company_info, f, indent=2)
with open('market_data.json', 'w') as f:
    json.dump(market_data, f, indent=2)

# Generate all data for 10 years (120 months)
months = 120
current_month = 18
dates = pd.date_range(start='2024-01-01', periods=months, freq='ME')

# Revenue
revenue = []
base_revenue = 8000
for i in range(months):
    if i < 6:
        if i == 0:
            revenue.append(base_revenue)
        else:
            growth = np.random.uniform(0.12, 0.18)
            revenue.append(revenue[-1] * (1 + growth))
    elif i < 18:
        growth = np.random.uniform(0.28, 0.35)
        revenue.append(revenue[-1] * (1 + growth))
    elif i < 36:
        revenue.append(revenue[-1] * 1.22)
    elif i < 54:
        revenue.append(revenue[-1] * 1.16)
    elif i < 72:
        revenue.append(revenue[-1] * 1.12)
    else:
        growth_rate = max(0.05, 0.12 - (i - 72) * 0.001)
        revenue.append(revenue[-1] * (1 + growth_rate))

# Costs
cogs, sales_marketing, rd_costs, admin_costs = [], [], [], []
for i, r in enumerate(revenue):
    if i < current_month:
        cogs.append(r * np.random.uniform(0.28, 0.32))
        sales_marketing.append(r * np.random.uniform(0.38, 0.45))
        rd_costs.append(r * np.random.uniform(0.22, 0.28))
        admin_costs.append(r * np.random.uniform(0.12, 0.18))
    else:
        scale_factor = min(1.0, (i - current_month) / 60)
        cogs.append(r * (0.30 - 0.05 * scale_factor))
        sales_marketing.append(r * (0.40 - 0.10 * scale_factor))
        rd_costs.append(r * (0.25 - 0.05 * scale_factor))
        admin_costs.append(r * (0.15 - 0.05 * scale_factor))

total_costs = [cogs[i] + sales_marketing[i] + rd_costs[i] + admin_costs[i] for i in range(months)]
profit = [revenue[i] - total_costs[i] for i in range(months)]

# Financials DataFrame
financials = pd.DataFrame({
    'Date': dates,
    'Revenue': revenue,
    'COGS': cogs,
    'Sales_Marketing': sales_marketing,
    'RD': rd_costs,
    'Admin': admin_costs,
    'Total_Costs': total_costs,
    'Profit': profit,
    'Is_Historical': [i < current_month for i in range(months)]
})
financials['Cumulative_Revenue'] = financials['Revenue'].cumsum()
financials['Cumulative_Costs'] = financials['Total_Costs'].cumsum()
financials['Cumulative_Profit'] = financials['Profit'].cumsum()

# Customers
customers = []
base_customers = 35
for i in range(months):
    if i == 0:
        customers.append(base_customers)
    elif i < current_month:
        growth = np.random.uniform(0.18, 0.25)
        customers.append(int(customers[-1] * (1 + growth)))
    else:
        if i < 36:
            growth = 0.20
        elif i < 54:
            growth = 0.17
        elif i < 72:
            growth = 0.14
        else:
            growth = max(0.08, 0.14 - (i - 72) * 0.0008)
        customers.append(int(customers[-1] * (1 + growth)))

# Key Metrics
key_metrics = pd.DataFrame({
    'Date': dates,
    'Customers': customers,
    'Transaction_Volume': [r * (15 if i < current_month else 18) for i, r in enumerate(revenue)],
    'CAC': [max(45, 220 - i*1.5) for i in range(months)],
    'LTV': [min(4500, 450 + i*35) for i in range(months)],
    'Is_Historical': [i < current_month for i in range(months)]
})
key_metrics['LTV_CAC_Ratio'] = key_metrics['LTV'] / key_metrics['CAC']
key_metrics['Churn_Rate'] = [max(1.5, 9.0 - i*0.08) for i in range(months)]

# Funding Rounds
funding_rounds = pd.DataFrame({
    'Round': ['Pre-Seed', 'Seed', 'Series A', 'Series B', 'Series C'],
    'Amount': [500000, 2500000, 10000000, 30000000, 75000000],
    'Valuation': [3000000, 12000000, 50000000, 150000000, 400000000],
    'Equity': [16.7, 20.8, 20.0, 20.0, 18.8],
    'Month': [0, 6, 18, 36, 54],
    'Status': ['Complete', 'Complete', 'Current Opportunity', 'Projected', 'Projected']
})

# ROI Comparison
roi_comparison = []
for _, round_info in funding_rounds.iterrows():
    round_name = round_info['Round']
    investment = round_info['Amount']
    equity = round_info['Equity']
    start_month = round_info['Month']
    
    for years in [1, 3, 5, 7, 10]:
        months_after = years * 12
        end_month = min(start_month + months_after, 119)
        arr_at_end = revenue[end_month] * 12
        
        if arr_at_end < 10000000:
            multiple = 8
        elif arr_at_end < 50000000:
            multiple = 10
        else:
            multiple = 12
        
        company_value = arr_at_end * multiple
        equity_value = company_value * (equity / 100)
        absolute_return = equity_value - investment
        roi_percentage = (absolute_return / investment) * 100
        multiple_return = equity_value / investment
        
        roi_comparison.append({
            'Round': round_name,
            'Investment': investment,
            'Equity_Pct': equity,
            'Years': years,
            'End_Month': end_month,
            'ARR': arr_at_end,
            'Company_Valuation': company_value,
            'Equity_Value': equity_value,
            'Absolute_Return': absolute_return,
            'ROI_Percentage': roi_percentage,
            'Multiple': multiple_return,
            'Is_Historical': start_month < current_month
        })

roi_df = pd.DataFrame(roi_comparison)

# Other data
target_markets = pd.DataFrame({
    'Province': ['Ontario', 'Quebec', 'British Columbia', 'Alberta', 'Manitoba', 'Saskatchewan'],
    'SMBs': [450000, 280000, 180000, 150000, 45000, 38000],
    'Latitude': [43.6532, 46.8139, 49.2827, 53.9333, 49.8951, 52.9399],
    'Longitude': [-79.3832, -71.2080, -123.1207, -116.5765, -97.1384, -106.4509]
})

competitors = pd.DataFrame({
    'Company': ['PayFlow Canada', 'Square', 'Stripe', 'Moneris', 'Legacy Banks'],
    'Market_Share': [0.5, 18.0, 22.0, 15.0, 44.5],
    'Focus': ['SMB Innovation', 'SMB General', 'Developer First', 'Enterprise', 'Traditional'],
    'Speed': [95, 85, 90, 70, 50],
    'Cost_Effectiveness': [90, 75, 80, 60, 40],
    'Canadian_Focus': [100, 60, 50, 95, 100]
})

roadmap = pd.DataFrame({
    'Quarter': ['Q1 2024', 'Q3 2024', 'Q1 2025', 'Q3 2025', 'Q1 2026', 'Q3 2026'],
    'Milestone': [
        'Beta Launch - Payment Gateway',
        'Seed Round Close + 500 Customers',
        'Series A + Invoice Module',
        'Banking Integration (5 banks)',
        'AI Fraud Detection',
        'International Payments'
    ],
    'Status': ['Complete', 'Complete', 'Current Opportunity', 'Planned', 'Planned', 'Planned']
})

team_data = pd.DataFrame({
    'Date': dates,
    'Engineering': [int(3 * (1.06 ** i)) for i in range(months)],
    'Sales': [int(2 * (1.08 ** i)) for i in range(months)],
    'Operations': [int(1 * (1.05 ** i)) for i in range(months)],
    'Leadership': [min(8, 2 + i // 12) for i in range(months)],
    'Is_Historical': [i < current_month for i in range(months)]
})
team_data['Total_Team'] = team_data[['Engineering', 'Sales', 'Operations', 'Leadership']].sum(axis=1)

# Save all CSV files
financials.to_csv('financials_10yr.csv', index=False)
key_metrics.to_csv('key_metrics_10yr.csv', index=False)
roi_df.to_csv('roi_comparison_10yr.csv', index=False)
funding_rounds.to_csv('funding_rounds_updated.csv', index=False)
target_markets.to_csv('target_markets.csv', index=False)
competitors.to_csv('competitors.csv', index=False)
roadmap.to_csv('roadmap.csv', index=False)
team_data.to_csv('team_data_10yr.csv', index=False)

print("✓ All data files regenerated successfully!")
print("\nFiles created:")
print("  - financials_10yr.csv")
print("  - key_metrics_10yr.csv")
print("  - roi_comparison_10yr.csv")
print("  - funding_rounds_updated.csv")
print("  - target_markets.csv")
print("  - competitors.csv")
print("  - roadmap.csv")
print("  - team_data_10yr.csv")
print("  - company_info.json")
print("  - market_data.json")
