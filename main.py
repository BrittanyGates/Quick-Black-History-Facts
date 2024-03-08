#!/usr/bin/env python3
"""
Title: Black History Facts Generator
Creator: Brittany Gates (https://github.com/brittbot-bgates) | (https://bcgates.com)
About: Displays a random Black History Fact every 10 seconds.
"""

from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    """
    Opens and reads the files/bhfg_facts.txt file, loops over the entire file to read each line, collects all the 
    lines as a list, and then randomly chooses a fact to display on index.html.

    :return: Display a random Black History fact to the home.html page.
    """

    with open("static/files/fact_list.txt", "r") as facts:
        fact_list = facts.readlines()
    return render_template('index.html', black_history_fact=random.choice(fact_list))


if __name__ == "__main__":
    main()