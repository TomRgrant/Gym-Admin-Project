from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
from models.visit import Visit
import repositories.member_repository as member_repository
import repositories.visit_repository as visit_repository
import repositories.gym_class_repository as gym_class_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/show.html", members = members)

@members_blueprint.route("/members", methods=['POST'])
def create_new_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership = request.form['membership']
    member = Member(first_name, last_name, membership)
    member_repository.save(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>")
def show_id(id):
    member = member_repository.select(id)
    enrolled_classes = visit_repository.select_all_classes(id)
    classes = gym_class_repository.select_all()
    return render_template("members/show_id.html", member = member, enrolled_classes = enrolled_classes, classes = classes)

@members_blueprint.route("/create_new_member")
def create_member():
    return render_template("members/add_new_member.html")

@members_blueprint.route("/delete_member/<id>", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")

@members_blueprint.route("/edit_member/<id>")
def show_update_member_form(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member = member)

@members_blueprint.route("/edit_member/<id>", methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership = request.form['membership']
    member = Member(first_name, last_name, membership, id)
    member_repository.update(member)
    return redirect("/members")

@members_blueprint.route("/join_new_class/<id>", methods=['POST'])
def add_member_to_class(id):
    member = member_repository.select(id)
    gym_class_id = request.form['join_class']
    print(gym_class_id)
    gym_class = gym_class_repository.select(gym_class_id)
    visit = Visit(member, gym_class)
    visit_repository.save(visit)
    return redirect(f"/members/{id}")