from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

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
    return render_template("members/show_id.html", member = member)

@members_blueprint.route("/create_new_member")
def create_member():
    return render_template("members/add_new_member.html")

@members_blueprint.route("/delete_member/<id>", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")