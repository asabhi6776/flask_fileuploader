from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

users = {
    'admin': 'password1',
}
# Set the upload folder
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = 'data'

@app.route('/login')
def login():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    #     if username in users and users[username] == password:
    #         session['username'] = username
    #         flash('You have been logged in!')
    #         return redirect(url_for('index'))
    #     else:
    #         flash('Invalid username or password.')
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    file_sizes = {}
    for file in files:
        file_sizes[file] = os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], file))
    return render_template('login.html', files=files, file_sizes=file_sizes, app=app, os=os)
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
