
# Create requirements.txt file for Streamlit Cloud
requirements_content = '''streamlit==1.28.0
pandas==2.1.1
plotly==5.17.0
numpy==1.24.3
'''

with open('requirements.txt', 'w') as f:
    f.write(requirements_content)

print("✓ requirements.txt created")
