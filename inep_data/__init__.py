from flask import Flask, render_template, jsonify, request
from models import School, City, State

app = Flask(__name__)

@app.route("/")
def index():
    schools = School.objects.where("this.name != null").order_by("name")
    return render_template('index.html', schools = schools)

@app.route("/schools")
def school_list():
    if request.args.get("name"):
        schools = School.objects(name__contains = request.args.get("name").upper())
    else:
        schools = School.objects

    json = []

    for school in list(schools):
        city = school.city.name if school.city else ""
        state = school.state.acronym if school.state else ""

        json.append({
            "id": school.code,
            "text": "%s (%s / %s)" % (school.name, city, state)
        })

    return jsonify({ "schools": json })

@app.route("/schools/<int:code>")
def school_show(code):
    try:
        school = School.objects.get(code = code)
    except:
        return "Not Found", 404

    school_scores = [score["value"] for score in school.scores]
    relative_school_scores = [(n * 100) / sum(school_scores) for n in school_scores]
    city_scores = [score["value"] for score in school.city.scores]
    relative_city_scores = [(n * 100) / sum(city_scores) for n in city_scores]

    json = {
        "school": {
            "name": school.name,
            "scores": school_scores,
            "relative_scores": relative_school_scores
        },

        "city": {
            "name": school.city.name,
            "scores": city_scores,
            "relative_scores": relative_city_scores
        }
    }

    return jsonify(json)

def run():
    app.run(debug = True)
