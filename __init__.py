from .config import DBCOnnection 
from .entities import Users as UsersModel

class UserRepo:
    def insert_user(self, name):
        with DBCOnnection() as db:
            new_user = UsersModel(name=name)
            db.session.add(new_user)
            db.session.commit()