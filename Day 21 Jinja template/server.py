from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(0, 100)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num = random_number, year = current_year)

@app.route('/guessname/<name>')
def guessname(name):
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]

    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    return render_template("guess.html", person_name=name, age = age, gender = gender)

@app.route('/blog')
def getBlog():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_post =  response.json()

    return render_template("blog.html", posts = all_post)


if __name__ == '__main__':
    app.run(debug=True)