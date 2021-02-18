from flask import Flask

app = Flask(__name__)

# Homepage routing
@app.route('/')
def homePage():
    return '<h1 style="text-align: center">This is a Heading. and I am using flask</h1>' \
           '<p>This is a Paragraph.</p>' \
           '<img src="https://media.giphy.com/media/uBtpKRN5o7aLfWg3Tw/giphy.gif" width=400>'\
           '<h1 style = "background-color:DodgerBlue;"> Hello World </h1>'

# Variable rules
@app.route('/<name>')
def samplePage(name):
    return f"This is a {name} website and I am using python"



if __name__ == '__main__':
    app.run(debug = True)