from models.member import Member
from models.gym_class import GymClass
from models.visit import Visit
import datetime

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.visit_repository as visit_repository


member_repository.delete_all()
gym_class_repository.delete_all()

member1 = Member("Tom", "Grant", True)
member_repository.save(member1)

member2 = Member("Jill", "Rudy", True)
member_repository.save(member2)

gym_class1 = GymClass("Spin Class", "Learn to spin", "Peter Gillaghan", datetime.date(2023, 3, 12))
gym_class_repository.save(gym_class1)

gym_class2 = GymClass("Hula Class", "Learn to spin a ring", "Gill Peterson", datetime.date(2023, 6, 15))
gym_class_repository.save(gym_class2)


visit1 = Visit(member1, gym_class2)
visit_repository.save(visit1)

visit2 = Visit(member2, gym_class2)
visit_repository.save(visit2)