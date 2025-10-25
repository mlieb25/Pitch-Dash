
# Now create the complete ZIP package with all files
import zipfile
import os

files_to_include = [
    'app.py',
    'requirements.txt',
    'README.md',
    'financials_10yr.csv',
    'key_metrics_10yr.csv',
    'roi_comparison_10yr.csv',
    'funding_rounds_updated.csv',
    'target_markets.csv',
    'competitors.csv',
    'roadmap.csv',
    'team_data_10yr.csv',
    'company_info.json',
    'market_data.json',
    '.streamlit/config.toml'
]

zip_filename = 'payflow-streamlit-complete.zip'

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_include:
        if os.path.exists(file):
            zipf.write(file, file)
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ MISSING: {file}")

print("\n" + "="*70)
print("🎉 COMPLETE STREAMLIT PACKAGE READY!")
print("="*70)
print(f"\nPackage: {zip_filename}")
print(f"Total files: {len([f for f in files_to_include if os.path.exists(f)])}")
print("\n📦 Package Contents:")
print("   ✓ app.py - Main Streamlit dashboard")
print("   ✓ requirements.txt - Python dependencies")
print("   ✓ README.md - Complete deployment guide")
print("   ✓ 8 CSV data files (10-year projections)")
print("   ✓ 2 JSON config files")
print("   ✓ .streamlit/config.toml - Theme settings")
print("\n🚀 DEPLOYMENT STEPS:")
print("   1. Download payflow-streamlit-complete.zip")
print("   2. Extract all files")
print("   3. Create GitHub repository")
print("   4. Upload all files to GitHub")
print("   5. Go to https://share.streamlit.io/")
print("   6. Deploy your repository")
print("   7. Get your public URL!")
print("\n💡 Your URL will be:")
print("   https://[your-github-username]-[repo-name].streamlit.app")
print("\n" + "="*70)
