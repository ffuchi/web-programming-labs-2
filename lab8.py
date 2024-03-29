from flask import render_template, Blueprint, request, abort, jsonify
from datetime import datetime

lab8 = Blueprint("lab8", __name__)


@lab8.route("/lab8/")
def main():
    return render_template('lab8/index.html')


courses = [
    {"name": "c++", "videos": 3,"price": 3000, "created_date": datetime.now()},
    {"name": "basic", "videos": 30,"price": 0, "created_date": datetime.now()},
    {"name": "c#", "videos": 8, "created_date": datetime.now()} 
    #если цена не указана, то курс бесплатный
]


#Весь список курсов
@lab8.route('/lab8/api/courses/', methods=['GET'])
def  get_courses():
    return jsonify(courses)


#Конкретный курс по номеру
@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if course_num < 0 or course_num > len(courses)-1:
        abort(404, "Course not found")
    return courses[course_num]


#Удаление курса
@lab8.route('/lab8/api/courses/<int:course_num>', methods=['DELETE'])
def del_course(course_num):
    if course_num < 0 or course_num > len(courses)-1:
        abort(404, "Course not found")
    del courses[course_num]
    return '', 204


#Редактирование существующего курса
@lab8.route('/lab8/api/courses/<int:course_num>', methods=['PUT'])
def put_course(course_num):
    course = request.get_json()
    if course_num < 0 or course_num > len(courses)-1:
        abort(404, "Course not found")
    course["created_date"] = courses[course_num]["created_date"] 
    courses[course_num] = course
    return courses[course_num]


#Добавление нового курса
@lab8.route('/lab8/api/courses/', methods=['POST'])
def add_course():
    course = request.get_json()
    course["created_date"] = datetime.now()
    courses.append(course)
    return {"num": len(courses)-1}
