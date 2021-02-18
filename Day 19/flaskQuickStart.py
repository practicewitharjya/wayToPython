from flask import Flask
app = Flask(__name__)

# Homepage routing
@app.route('/')
def homePage():
    return "I am in the home Page!"

# Routing with custom page
@app.route('/mobile-phone')
def mobilePage():
    return "This is a Mobile Phone website"

@app.route('/tv')
def tvPage():
    return "This is a TV website"

@app.route('/laptop')
def laptopPage():
    return "This is a Laptop website"

@app.route('/dress')
def dressPage():
    return "This is a DressPage website"

@app.route('/fridge')
def fridgePage():
    return "This is a fridge website"

# Variable rules
@app.route('/<name>')
def samplePage(name):
    return f"This is a {name} website and I am using python"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(debug = True)