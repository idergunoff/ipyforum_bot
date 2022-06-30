from config import *


def get_user(teleg_id):
    return session.query(User).filter(User.telegram_id == teleg_id).first()


def get_admins():
    return session.query(User).filter(User.admin == True).all()



