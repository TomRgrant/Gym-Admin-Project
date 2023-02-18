from db.run_sql import run_sql

from models.member import Member
from models.gym_class import Gym_class
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

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)