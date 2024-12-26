#!/usr/bin/env python3
"""Quick Black History Facts
Creator: Brittany Gates (https://github.com/brittbot-bgates) | (https://www.linkedin.com/in/brittanycgates) | (https://brittbot.com/)
About: This web app displays a random Black History Fact every 10 seconds.
"""

from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index() -> render_template:
    """Displays the index.html template.
    :return: A random Black History fact displayed on the homepage.
    """

    with open("static/files/black_history_facts.txt", "r") as facts:
        fact_list = facts.readlines()
    return render_template('index.html', black_history_fact=random.choice(fact_list))


if __name__ == "__main__":
    index()
