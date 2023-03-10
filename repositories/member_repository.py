from db.run_sql import run_sql

from models.member import Member
from models.gym_class import GymClass
from models.visit import Visit

def save(member):
    sql = """INSERT INTO members (first_name, last_name, membership)
             VALUES (%s, %s, %s) RETURNING *"""
    values = [member.first_name, member.last_name, member.membership]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row["membership"], row['id'])
        members.append(member)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['membership'], row['id'])
    return member

def update(member):
    sql = """UPDATE members SET (first_name, last_name, membership)
             = (%s, %s, %s) WHERE id = %s"""
    values = [member.first_name, member.last_name, member.membership, member.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)