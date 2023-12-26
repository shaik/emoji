import time  # Import the time module
import pandas as pd
from PIL import Image
from scipy.spatial import KDTree
from .config import Config

# Global variables for color trees
emoji_data = None
color_tree = None
normalized_color_tree = None

def hex_to_rgb(hex_color):
    """Convert hex color to RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def setup_color_trees():
    """Setup color KD trees for emoji mapping."""
    global emoji_data, color_tree, normalized_color_tree

    # Load emoji color data
    emoji_data = pd.read_csv(Config.DATA_FILE)

    # Create tree for original colors
    emoji_data['RGB'] = emoji_data['Hex Color'].apply(hex_to_rgb)
    color_tuples = list(emoji_data['RGB'])
    color_tree = KDTree(color_tuples)

    # Create tree for normalized colors
    emoji_data['Normalized RGB'] = emoji_data['Normalized Color'].apply(hex_to_rgb)
    normalized_color_tuples = list(emoji_data['Normalized RGB'])
    normalized_color_tree = KDTree(normalized_color_tuples)

def find_closest_emoji(rgb_pixel, tree):
    """Find the closest emoji for a given RGB pixel."""
    distance, index = tree.query(rgb_pixel)
    return emoji_data.iloc[index]['Emoji']

def create_emoji_image(filepath, grid_width, color_mapping):
    """Create an emoji image from an image file."""
    # Select the appropriate color tree
    tree_to_use = normalized_color_tree if color_mapping == 'normalized' else color_tree

    start_time = time.time()

    with Image.open(filepath) as img:
        img = img.resize((grid_width, int(grid_width * img.size[1] / img.size[0])), 0)
        img = img.convert("RGB")
        emoji_html = "<div class='emoji-grid'>"

        for y in range(img.size[1]):
            emoji_html += "<div class='emoji-row'>"
            for x in range(img.size[0]):
                rgb = img.getpixel((x, y))
                emoji = find_closest_emoji(rgb, tree_to_use)
                emoji_html += f"<span>{emoji}</span>"
            emoji_html += "</div>"
        emoji_html += '</div>'

    end_time = time.time()
    processing_time = round(end_time - start_time, 2)

    return emoji_html, processing_time

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS
