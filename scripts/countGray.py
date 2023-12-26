import pandas as pd

# Function to determine if a color is a shade of gray
def is_gray(hex_color):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return r == g == b

# Load the CSV file
emoji_data = pd.read_csv('../data/emojiColor.csv')

# Identify and count the shades of gray
gray_colors = emoji_data[emoji_data['Hex Color'].apply(is_gray)]

# Print the number of shades of gray
print(f"Number of shades of gray: {len(gray_colors)}")

# Print the shades of gray
print("Shades of gray:")
print(gray_colors['Hex Color'])
