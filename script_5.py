
# The data files are in the current directory from earlier - let me find them and add them
import os

# List all files in current directory
print("Files in current directory:")
for file in sorted(os.listdir('.')):
    if file.endswith(('.csv', '.json')):
        print(f"  {file}")

print("\n" + "="*60)
