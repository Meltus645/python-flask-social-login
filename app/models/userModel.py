from flask_login import UserMixin
# from app.utils.db import get_db

class UserModel(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id_ =id_
        self.name =name
        self.email =email
        self.profile_pic =profile_pic
    
    # def get(self, user_id):
    #     db =get_db() 
    #     user =db.execute("SELECT * FROM users WHERE id =?", (user_id,))  .fetchone()
    #     if not user: return 
    #     return UserModel(*user)
    
    # @staticmethod
    # def create(id_, name, email, profile_pic):
    #     db =get_db()
    #     db.execute("INSERT INTO users (id, name, email, profile_pic)" "VALUES (?, ?, ?, ?)", (id_, name, email, profile_pic))
    #     db.commit()