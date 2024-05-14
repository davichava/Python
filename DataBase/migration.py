# from dataclasses import data

# from sqlalchemy import Engine
# from DataBase.models import Base, User

# Base.metdata.create_all(Engine)

# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bin=Engine)
# session = Session()

# for item in data:
#     user = User(id=item['id'], name=item['name'])
#     Session.add(user)

# session.commit()