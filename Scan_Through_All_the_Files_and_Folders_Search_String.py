--->Multile folder listing and searching using text                                                                                                                                                                                                                                                                                                                                                                                                   #!/usr/bin/env python
# coding: utf-8

### Import required modules
import os
import shutil
from pathlib import Path

### Configuration
search_string = "LEARNEREA"
source_root = r"D:\Learnerea\others"
destination_root = r"D:\Learnerea\youOutputs"

# Create destination directory if it doesn't exist
Path(destination_root).mkdir(parents=True, exist_ok=True)

### List all files containing the search string
matching_files = []

for dirpath, dirnames, filenames in os.walk(source_root):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        try:
            # Try to read the file as text
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                if search_string in f.read():
                    matching_files.append(file_path)
        except (UnicodeDecodeError, PermissionError, IsADirectoryError):
            # Skip binary files or files that can't be read
            continue

### Copy matching files to destination
for source_path in matching_files:
    # Create destination path while preserving relative directory structure
    relative_path = os.path.relpath(source_path, source_root)
    destination_path = os.path.join(destination_root, relative_path)
    
    # Create necessary subdirectories
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Copy the file
    shutil.copy2(source_path, destination_path)
    print(f"Copied: {source_path} -> {destination_path}")

print(f"\nDone! Copied {len(matching_files)} files to {destination_root}")
