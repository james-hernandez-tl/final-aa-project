from app.models import db, Card, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_cards():
    card1 = Card(
        question='what is 5 + 5 ?', answer='10', setId = 1)
    card2 = Card(
        question='what is 5 + 5 ?', answer='10', setId = 2)
    card3 = Card(
        question='what is 5 + 5 ?', answer='10', setId = 3)
    card4 = Card(
        question='what is 5 + 5 ?', answer='10', setId = 4)
    card5 = Card(
        question='what is 5 + 5 ?', answer='10', setId = 5)
    card6 = Card(
        question='what is 5 + 5 ?', answer='10', setId = 6)
    card7 = Card(
        question='what is 5 + 5 ?', answer='10', setId = 7)
    card8 = Card(
        question='what is 5 + 5 ?', answer='10', setId = 8)
    card9 = Card(
        question='what is 5 + 5 ?', answer='10', setId = 9)
    card10 = Card(
        question='what is 5 + 7 ?', answer='12', setId = 1)
    card11 = Card(
        question='what is 10 + 10 ?', answer='20', setId = 1)
    card12 = Card(
        question='what is 18 + 5 ?', answer='23', setId = 1)

    allCards = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12]
    [db.session.add(acard) for acard in allCards]
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_cards():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.cards RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cards"))

    db.session.commit()
