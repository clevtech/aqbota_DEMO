#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2018, KazPostBot"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"

from flask import Flask, render_template, request, Markup, jsonify
import time
import random
import lib.arduino_speak as ard
import datetime, socket


app = Flask(__name__)  # Creating new flask app
while True:
    try:
        box, light = ard.connect_to()
        break
    except:
        pass

# Choosing cell to load
@app.route("/<val>", methods=["GET", "POST"])
def robot(val = None):
    alert = "Открыть ячейки или вкл/выкл фары"
    if val:
        if val == "0":
            ard.action(0, box)
        elif val == "1":
            ard.action(1, box)
        elif val == "2":
            ard.action(2, box)
        elif val == "3":
            ard.action(3, box)
        elif val == "ON":
            ard.action(0, light)
        elif val == "OFF":
            ard.action(1, light)
    else:
        print(val)
        
    return render_template(
        "index.html", **locals())


# Main flask app
if __name__ == "__main__":
    app.run("0.0.0.0", port=7777, debug=True)
