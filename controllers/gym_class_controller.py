from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository
import datetime

gym_classes_blueprint = Blueprint("gym_class", __name__)

@gym_classes_blueprint.route("/classes")
def classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/show.html", gym_classes = gym_classes)

@gym_classes_blueprint.route("/classes", methods=['POST'])
def save_new_class():
    title = request.form['title']
    description = request.form['description']
    instructor = request.form['instructor']
    class_date = request.form['class_date']
    split_date = class_date.split("-")
    class_date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    gym_class = GymClass(title, description, instructor, class_date)
    gym_class_repository.save(gym_class)
    return redirect("/classes")

@gym_classes_blueprint.route("/class/<id>")
def show_class_by_id(id):
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/show_id.html", gym_class = gym_class)

@gym_classes_blueprint.route("/add_new_class")
def new_class():
    return render_template("gym_classes/add_new_class.html")

@gym_classes_blueprint.route("/edit_class/<id>")
def edit_class(id):
    gym_class = gym_class_repository
    return render_template("gym_classes/edit.html")
