from flask import Flask, jsonify, request
from datetime import date
import datetime

app = Flask(__name__)

day = date.today().strftime("%A")


@app.route("/api")
def my_api():

    name = request.args.get("slack_name")
    track = request.args.get("track")

    return jsonify(
        slack_name=name,
        current_day=day,
        utc_time=datetime.datetime.utcnow().isoformat() + "Z",
        track=track,
        github_file_url="https://github.com/Gbeminiyi-A/stage-one.py/blob/master/main.py",
        github_repo_url="https://github.com/Gbeminiyi-A/stage-one.py",
        status_code=200
    )


if __name__ == '__main__':
    app.run(debug=True)
