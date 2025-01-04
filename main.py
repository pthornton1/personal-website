from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

# TODO LIST:
# 1. Save to git
# 1. Change the verbatum on the website
# 2. Change the images on the website
# 3. Make the bottom links work
# 4. Make the form work
# 5. Host on Python Anywere
