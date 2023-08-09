from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    marnie = User(
        username='james', email='james@aa.io', password='password', image="https://i.imgur.com/Ni48C6r.jpeg")
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password')
    user3 =User(username='Demo2', email='demo2@aa.io', password='password'),
    user4 =User(username='JohnDoe', email='john.doe@example.com', password='securepassword'),
    user5 =User(username='JaneSmith', email='jane.smith@example.com', password='strongpassword'),
    user6 = User(username='MikeJohnson', email='mike.johnson@example.com', password='mysecretpass'),
    user7 = User(username='EmilyBrown', email='emily.brown@example.com', password='safepassword123'),
    user8 = User(username='RobertWilliams', email='robert.williams@example.com', password='mycoolpassword'),
    user9 = User(username='SarahLee', email='sarah.lee@example.com', password='pass1234'),
    user10 = User(username='ChrisTaylor', email='chris.taylor@example.com', password='mysecurepass'),
    user11 = User(username='JenniferDavis', email='jennifer.davis@example.com', password='myp@ssword'),
    user12 = User(username='DanielMiller', email='daniel.miller@example.com', password='password321'),
    user13 = User(username='LindaWilson', email='linda.wilson@example.com', password='pass4me')

    [db.session.add(newUser) for newUser in [demo,marnie,bobbie, user3,user4,user5,user6,user7,user8,user9,user10,user11,user12,user13]]
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
