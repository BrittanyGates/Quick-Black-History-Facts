#!/usr/bin/env python3
"""Quick Black History Facts
Creator: Brittany Gates (https://github.com/BrittanyGates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: This web app displays a random Black History Fact every 10 seconds.
"""

from flask import Flask, render_template, Response, jsonify
import random

app = Flask(__name__)


def get_random_black_history_fact() -> str:
    """Gets a random Black History Fact from text file.
    :return: The random Black History fact as a string.
    """
    with open("static/files/black_history_facts.txt", "r") as facts:
        fact_list = facts.readlines()

    return random.choice(fact_list).strip()


@app.route("/chosen-fact")
def get_black_history_fact() -> Response:
    """Allows the JavaScript event handler to run the main function.
    :return: The random Black History fact as JSON.
    """
    black_history_fact = get_random_black_history_fact()
    return jsonify({"value": black_history_fact})


@app.route("/", methods=["GET", "POST"])
def main() -> render_template:
    """Displays the index.html template.
    :return: A random Black History fact displayed on the homepage.
    """
    black_history_fact = get_random_black_history_fact()
    return render_template('index.html', black_history_fact=black_history_fact)


if __name__ == "__main__":
    main()
