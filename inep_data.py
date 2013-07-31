from flask import Flask, render_template, jsonify, request
from models import School, City

app = Flask(__name__)

@app.route("/")
def index():
    schools = School.objects.where("this.name != null").order_by("name")
    return render_template('index.html', schools = schools)

@app.route("/schools/<int:code>")
def school_show(code):
    try:
        school = School.objects.get(code = code)
        city = City.objects.get(code = school.city_code)
    except:
        return "Not Found", 404

    json = {
        "school": {
            "name": school.name,
            "scores": school.scores,
            "relative_scores": [(n * 100) / sum(school.scores) for n in school.scores]
        },

        "city": {
            "name": city.name,
            "scores": city.scores,
            "relative_scores": [(n * 100) / sum(city.scores) for n in city.scores]
        }
    }

    return jsonify(json)

if __name__ == '__main__':
    app.run()
