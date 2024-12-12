from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def countdown():
    # Pass the Christmas date to the template
    christmas_date = datetime(2024, 12, 25, 0, 0, 0).strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", christmas_date=christmas_date)

if __name__ == "__main__":
    app.run(debug=True)