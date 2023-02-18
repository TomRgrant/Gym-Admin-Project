from models.member import Member
from models.gym_class import Gym_class
from models.visit import Visit

import repositories.member_repository as member_repository


member_repository.delete_all()

member1 = Member("Tom", "Grant", True)
member_repository.save(member1)

member2 = Member("Jill", "Rudy", True)
member_repository.save(member2)