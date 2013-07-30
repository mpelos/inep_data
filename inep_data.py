from flask import Flask, render_template
from models import School

app = Flask(__name__)

@app.route("/")
def index():
    schools = School.objects.where("this.name != null").order_by("name")
    return render_template('index.html', schools = schools)

if __name__ == '__main__':
    app.run()
