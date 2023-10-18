from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify
import json
import os.path
from werkzeug.utils import secure_filename  # Protects upload files

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'sdflkj29034laksdfj'  # Securely send messages between  DOM and user
save_file_path = os.path.join(app.root_path, "static", "user_files")


@app.route('/')
def index():
    return render_template('index.html', codes=session.keys())


@app.route('/your_url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        if os.path.exists('urls.json'):   # Loads json file if present
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form.get('code') in urls.keys():   # If value exists in json file, redirect to home page.
            flash('That short name already exists. Please select another name.')
            return redirect(url_for('index'))
        if 'url' in request.form.keys():   # Goes to all keys in form dictionary and
            # checks for a url Inside url dictionary for code attribute key.
            urls[request.form['code']] = {'url': request.form['url']}
        else:
            file = request.files['file']
            full_name = request.form['code'] + secure_filename(file.filename)
            file.save(os.path.join(save_file_path, full_name))
            urls[request.form['code']] = {'file': full_name}
        with open('urls.json', 'w') as url_file:  # Opens the urls json file
            json.dump(urls, url_file)
            session[request.form['code']] = True  # Saves code attribute as cookie

        return render_template('your_url.html', code=request.form['code'])  # Gets data from the shortened name field
        # and stores it in the code attribute.
    else:
        return redirect(url_for('index'))   # Redirects the user is they try to access the # /your_url page without
        # first enter data in the / page.


@app.route('/<string:code>')  # Looks at the string after /your_url/ and stores it as a variable name code.
def redirect_to_url(code):
    if os.path.exists('urls.json'):  # Checks for the code variable in the urls.json file
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():   # If url exist in json file redirect to url
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:   # If file key exists, redirect to file for to display on page
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file']))
    return abort(404)   # If file or url is not found for redirect displays 404 error


# Removes JSON file and clears cookies to reset code list
@app.route('/', methods=['GET', 'POST'])
def clear_list():
    open('urls.json', 'w').close()
    return render_template('index.html', codes=session.clear())


@app.errorhandler(404)   # Error handler for 404 code
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/api')   # Creates and API and stores urls.json keys in a list
def session_api():
    return jsonify(list(session.keys()))

# Resets the URL list
@app.route('/reset_url_list', methods=['POST'])
def reset_url_list():
    if request.form.get('reset') == 'true':
        session.clear()  # Clear the session to reset the URL list
        # Clear the contents of the 'urls.json' file
        with open('urls.json', 'w') as url_file:
            url_file.write("{}")
    return redirect(url_for('index'))


# this code is added to run from the pycharm
if __name__ == '__main__':
    app.run(debug=True)

