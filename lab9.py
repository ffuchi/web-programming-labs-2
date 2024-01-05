from flask import render_template, Blueprint, request, abort, jsonify


lab9 = Blueprint("lab9", __name__)

@lab9.app_errorhandler(404)
def not_found(err):
    return render_template('lab9/error404.html'), 404

@lab9.app_errorhandler(500)
def server_error(err):
    return render_template('lab9/error500.html'), 500


@lab9.route('/lab9/500')
def server_error():
    return render_template('lab9/error500.html')


@lab9.route("/lab9/")
def main():
    return render_template('lab9/index.html')

