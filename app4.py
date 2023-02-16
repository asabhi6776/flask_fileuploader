from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route for the login page
@app.route('/')
def login():
    # Get the list of uploaded files
    files = os.listdir(app.config['UPLOAD_FOLDER'])

    # Render the login template with the list of files
    return render_template('login.html', files=files)

# Route for the upload page
@app.route('/upload')
def upload_file():
    return render_template('upload.html')

# Route for handling the file upload
@app.route('/uploader', methods=['POST'])
def upload_file_handler():
    # Get the uploaded file
    file = request.files['file']

    # Save the file to the upload folder
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Redirect to the upload page with a success message
    return redirect(url_for('upload_file', message='File uploaded successfully.'))

if __name__ == '__main__':
    app.run(debug=True)
