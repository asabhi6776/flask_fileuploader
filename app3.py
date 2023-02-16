from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/login')
def login():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    file_sizes = {}
    for file in files:
        file_sizes[file] = os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], file))
    return render_template('login.html', files=files, file_sizes=file_sizes, os=os)

if __name__ == '__main__':
    app.run(debug=True)
