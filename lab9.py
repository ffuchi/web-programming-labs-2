from flask import render_template, Blueprint, request, abort, jsonify


lab9 = Blueprint("lab9", __name__)


@lab9.route("/lab9/")
def main():
    return render_template('lab9/index.html')