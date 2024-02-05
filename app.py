from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from your_script import download_video  # Import your script function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Use single backslash

app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    youtube_link = request.form['youtube_link']

    # Specify the upload and download paths
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp.txt')
    # Specify your desired download path
    download_path = r'C:\Users\andri\Downloads'  # Use raw string literal


    # Save the YouTube link to a temporary file
    with open(upload_path, 'w') as file:
        file.write(youtube_link)

    # Call your script function to download the video
    success, message = download_video(youtube_link, download_path)

    # Remove the temporary file
    os.remove(upload_path)

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
