# Author: Olga Mokshantseva
# Date: 10/27/2022
# Description:

from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def get_quote():
    line = random_line("quotes.txt")

    return line


def random_line(fileName):
    with open(fileName) as f:
        lines = f.readlines()
        inx = random.randrange(0, len(lines))
        line = lines[inx]
    return line
