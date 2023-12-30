from flask import render_template, request, redirect, flash, url_for
from .forms import UploadForm
from .utils import allowed_file, create_emoji_image
from .config import Config
import os
from werkzeug.utils import secure_filename

def configure_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def upload_file():
        form = UploadForm()
        if form.validate_on_submit():
            file = form.file.data
            grid_width = int(form.grid_width.data)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
                file.save(filepath)

                return redirect(url_for('process_image', filename=filename, grid_width=grid_width))
            else:
                flash('Invalid file type')
        return render_template('emojiArt.html', form=form)

    @app.route('/process_image/<filename>/<int:grid_width>')
    def process_image(filename, grid_width):
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        if os.path.exists(filepath) and allowed_file(filename):
            emoji_html, processing_time = create_emoji_image(filepath, grid_width, 'original')  # Default to 'original'
            return render_template('result.html', emoji_html=emoji_html, processing_time=processing_time)
        else:
            flash('File not found or invalid file type.')
            return redirect(url_for('upload_file'))

    @app.route('/upload_cropped', methods=['POST'])
    def upload_cropped_image():
        try:
            if 'croppedImage' not in request.files:
                return "No cropped image found", 400
            file = request.files['croppedImage']
            if file.filename == '':
                flash('No selected file')
                return redirect(url_for('upload_file'))
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
                file.save(filepath)
                grid_size = int(request.form.get('gridSize', 32))
                if grid_size in Config.ALLOWED_GRID_WIDTHS:
                    grid_size = int(grid_size)
                else:
                    # Default to size 32 if the input is not valid
                    grid_size = 32
                color_mapping = request.form.get('colorMapping', 'original')
                emoji_html, processing_time = create_emoji_image(filepath, grid_size, color_mapping)
                return render_template('result.html', emoji_html=emoji_html, processing_time=processing_time)
            else:
                flash('Invalid file type')
                return redirect(url_for('upload_file'))
        except Exception as e:
            flash('An error occurred while processing the image.')
            return redirect(url_for('upload_file'))
