# PayFlow Canada - Series A Investment Pitch Dashboard

A clean, professional Streamlit dashboard for presenting your Series A funding opportunity to investors.

## Features

- 📊 Interactive charts showing historical performance vs. projections
- 💰 ROI comparison across funding rounds
- 📈 10-year revenue and customer growth projections
- 🎯 Key unit economics and metrics
- 💼 Clear investment terms and call-to-action

## Files Included

- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `financials_10yr.csv` - Financial projections data
- `key_metrics_10yr.csv` - Customer and metric data
- `roi_comparison_10yr.csv` - ROI analysis data
- `funding_rounds_updated.csv` - Funding round information
- `target_markets.csv` - Geographic market data
- `competitors.csv` - Competitive landscape
- `roadmap.csv` - Product roadmap
- `team_data_10yr.csv` - Team growth projections
- `company_info.json` - Company metadata
- `market_data.json` - Market sizing data

## How to Deploy to Streamlit Cloud (Free)

### Step 1: Create a GitHub Repository

1. Go to https://github.com and create a new repository
2. Name it something like `payflow-pitch-dashboard`
3. Make it public or private (your choice)

### Step 2: Upload Files

Upload all the files from this package to your GitHub repository:
- app.py
- requirements.txt
- All CSV files
- All JSON files

### Step 3: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Click "Sign in with GitHub"
3. Click "New app"
4. Select your repository: `your-username/payflow-pitch-dashboard`
5. Set main file path: `app.py`
6. Click "Deploy"

### Step 4: Get Your Public URL

After deployment (takes 2-3 minutes), you'll get a public URL like:
```
https://your-username-payflow-pitch-dashboard.streamlit.app
```

You can share this URL with investors!

## Running Locally (Optional)

To run the dashboard on your local machine:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open in your browser at http://localhost:8501

## Customization

To customize the dashboard for your actual company:

1. Update the data in the CSV files with your real numbers
2. Modify company info in `company_info.json`
3. Adjust market data in `market_data.json`
4. Update contact information in `app.py` (search for "invest@payflowcanada.com")

## Support

For questions about deployment or customization, refer to:
- Streamlit Documentation: https://docs.streamlit.io/
- Streamlit Community: https://discuss.streamlit.io/

---

**Note:** This dashboard uses synthetic data for demonstration purposes. Replace with your actual company data before sharing with investors.
