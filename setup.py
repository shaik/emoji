import os

def create_folder_structure():
    # List of directories to create
    directories = [
        "templates",
        "static",
        "data"
    ]

    # Create each directory
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

    # List of files to create
    files = {
        "emojiArtKD.py": "# Main Flask application\n",
        "static/style.css": "/* CSS file for styling */\n",
        "data/emojiColor.csv": "Emoji,Hex Color\n",
        "requirements.txt": "# List of dependencies\n"
    }

    # Create each file
    for file_path, content in files.items():
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Created file: {file_path}")

    print("Setup completed.")

if __name__ == "__main__":
    create_folder_structure()
