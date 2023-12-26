class Config:
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'webp'}
    ALLOWED_GRID_WIDTHS = {10, 24, 32, 40, 64, 80, 100, 120}
    SECRET_KEY = 'your_secret_key'
    DATA_FILE = "data/emojiNormalizedColor.csv"
