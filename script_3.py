
# Create .streamlit/config.toml for custom theme
import os

# Create .streamlit directory if it doesn't exist
os.makedirs('.streamlit', exist_ok=True)

config_content = '''[theme]
primaryColor="#1f77b4"
backgroundColor="#ffffff"
secondaryBackgroundColor="#f0f2f6"
textColor="#262730"
font="sans serif"

[server]
headless = true
port = 8501
enableCORS = false
'''

with open('.streamlit/config.toml', 'w') as f:
    f.write(config_content)

print("✓ .streamlit/config.toml created")
