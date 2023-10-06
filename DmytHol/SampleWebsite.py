from flask import Flask, render_template

app = Flask(__name__)

# Define the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define the first page
@app.route('/page1')
def page1():
    return render_template('page1.html')

# Define the second page
@app.route('/page2')
def page2():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run()