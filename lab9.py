from flask import render_template, Blueprint, request, abort, jsonify


lab9 = Blueprint("lab9", __name__)

@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/error.html'), 404


@lab9.route("/lab9/")
def main():
    return render_template('lab9/index.html')

