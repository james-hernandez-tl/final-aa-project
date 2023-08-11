from app.models import db, Rating, environment, SCHEMA
from sqlalchemy.sql import text
import random


# Adds a demo user, you can add other users here if you want
def seed_ratings():
    def generate_ratings():
        ratings = []

        userId = 1
        setId = 1

        for _ in range(650):  # 13 users * 50 sets = 650 ratings
            rating = random.randint(1, 5)
            ratings.append(Rating(userId=userId, setId=setId, rating=rating))

            userId += 1
            if userId > 13:
               userId = 1
               setId += 1

        return ratings

# Generating the ratings
    ratings = generate_ratings()

    [db.session.add(arating) for arating in ratings]
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_ratings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.ratings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM ratings"))

    db.session.commit()
