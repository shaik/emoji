// imageCropper.js

var cropper;

document.addEventListener('DOMContentLoaded', function() {
    var cropper;
    var imageInput = document.getElementById('imageInput');
    var cropButton = document.getElementById('cropButton');

    if (imageInput && cropButton) {
        imageInput.addEventListener('change', function(event) {
            var files = event.target.files;
            if (files && files.length > 0) {
                var file = files[0];
                var reader = new FileReader();
                reader.onload = function(e) {
                    document.getElementById('image').src = e.target.result;
                    document.getElementById('image').style.display = 'block';
                    if (cropper) {
                        cropper.destroy();
                    }
                    cropper = new Cropper(document.getElementById('image'), {
                        viewMode: 1
                    });
                    document.getElementById('cropButton').style.display = 'block';
                    document.getElementById('gridSizeSelect').style.display = 'block';
                    document.getElementById('gridSizeLabel').style.display = 'block'; // Show the label

                };
                reader.readAsDataURL(file);
            }
        });

        cropButton.addEventListener('click', function() {
            var canvas = cropper.getCroppedCanvas();
            var gridSizeSelect = document.getElementById('gridSizeSelect'); // Get the select element

            // Check if gridSizeSelect is available and get its value
            var gridSize = gridSizeSelect ? gridSizeSelect.value : 'default_value'; // Replace 'default_value' with your default

            canvas.toBlob(function(blob) {
                var formData = new FormData();
                formData.append('croppedImage', blob, 'croppedImage.png');
                formData.append('gridSize', gridSize); // Include grid size in the FormData

                $.ajax({
                    url: '/upload_cropped',
                    method: 'POST',
                    data: formData,
                    processData: false,
                    contentType: false,
                    success: function(data) {
                        document.body.innerHTML = data;
                    },
                    error: function(xhr, status, error) {
                        console.error("Error occurred:", error);
                    }
                });
            });
        });
    } else {
        console.error('Required elements not found in the DOM');
    }
});