from flask import Flask
from flask import request
import os
from flask import render_template, send_from_directory
from flask import abort, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')

# @app.route('/user/<username>', methods=['GET', 'POST'])
# def show_user_profile(username):
#     if request.method == 'POST':
#         return 'HTTP POST for user %s with password %s' % (username, request.form['password'])
#     else:
#         return 'HTTP GET for user %s' % username

@app.route('/error_denied')
def error_denied():
    abort(401)

@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# 
#<!-- <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico'}}"> --
#
#
# 

if __name__ == '__main__':
    app.run(debug=True)