from flask import Flask, render_template, send_from_directory, request, redirect

app = Flask(__name__)


@app.route('/films/list')
def displayList():
    return send_from_directory("files", "index.html")


@app.route('/films/table')
def displayTable():
    with open("reviews.txt", "r") as f:
        reviews = [x.strip().split(",") for x in f.readlines()]

    return render_template("list.html", reviews=reviews)


@app.route('/films/submit', methods=['POST'])
def submitReview():
    film = request.form.get("film")
    stars = request.form.get("stars")

    line = f"{film},{stars}\n"

    with open("reviews.txt", "a+") as f:
        f.write(line)

    return redirect(request.referrer)