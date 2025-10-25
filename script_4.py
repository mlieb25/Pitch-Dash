
# Create a comprehensive deployment package ZIP file
import zipfile
import os
from pathlib import Path

# List of all files to include in the package
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

# Create ZIP file
zip_filename = 'payflow-streamlit-complete.zip'

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_include:
        if os.path.exists(file):
            zipf.write(file, file)
            print(f"  ✓ Added: {file}")
        else:
            print(f"  ✗ Missing: {file}")

print(f"\n{'='*60}")
print(f"✅ Complete Streamlit package created: {zip_filename}")
print(f"{'='*60}")
print("\nPackage Contents:")
print("  - app.py (main Streamlit application)")
print("  - requirements.txt (dependencies)")
print("  - README.md (deployment instructions)")
print("  - 10 CSV data files")
print("  - 2 JSON configuration files")
print("  - .streamlit/config.toml (theme settings)")
print("\nTotal files:", len(files_to_include))
print("\nNext Steps:")
print("1. Download the ZIP file")
print("2. Extract all files")
print("3. Upload to GitHub")
print("4. Deploy to share.streamlit.io")
print("5. Get your public URL!")
