from db.run_sql import run_sql

from models.member import Member
from models.gym_class import GymClass
from models.visit import Visit

import repositories.member_repository as member_repository

def save(visit):
    sql = "INSERT INTO visits (member_id, gym_class_id) VALUES (%s, %s) RETURNING *"
    values = [visit.member.id, visit.gym_class.id]
    results = run_sql(sql, values)
    visit.id = results[0]['id']
    return visit

def select_all_members(id):
    members = []
    sql = "SELECT member_id FROM visits WHERE gym_class_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        member = member_repository.select(row['member_id'])
        members.append(member)
    return members
