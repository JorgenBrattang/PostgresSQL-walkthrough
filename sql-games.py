from sqlalchemy import (
    create_engine, String, Integer, Column
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()


class Games(base):
    __tablename__ = "Games"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    playable = Column(Integer, primary_key=False)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

pop_one = Games(
    name="Population One",
    playable=1
)

blade_and_sorcery = Games(
    name="Blade and Sorcery",
    playable=2
)

session.add(blade_and_sorcery)
session.commit()

games = session.query(Games)
for game in games:
    print(game.id, game.name, game.playable, sep=" | ")
