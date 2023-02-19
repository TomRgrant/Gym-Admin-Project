from db.run_sql import run_sql

from models.member import Member
from models.gym_class import GymClass
from models.visit import Visit

def save(gym_class):
    sql = """INSERT INTO gym_classes (title, class_description, instructor, class_date)
             Values (%s, %s, %s, %s) RETURNING *"""
    values = [gym_class.title, gym_class.description, gym_class.instructor, gym_class.class_date]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    gym_classes = []
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    for row in results:
        gym_class = GymClass(row['title'], row['class_description'], row['instructor'], row['class_date'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes




def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)