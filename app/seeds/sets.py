from app.models import db, Set, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_sets():
    set1 = Set(
        name='firstSet', description='this is an example set with a random description aaaaaaaaaaaaaaaaaaaaaaaaa', userId=2)
    set2 = Set(
        name='secondSet', description='this is an example set with a random description aaaaaaaaaaaaaaaaaaaaaaaaa', userId=2)
    set3 = Set(
       name='firstSet', description='this is an example set with a random description aaaaaaaaaaaaaaaaaaaaaaaaa', userId=1)

    set4 = Set(
       name='thirdSet', description='this is an example set with a random description aaaaaaaaaaaaaaaaaaaaaaaaa', userId=2)
    set5 = Set(
       name='fourthSet', description='this is an example set with a random description aaaaaaaaaaaaaaaaaaaaaaaaa', userId=2)
    set6 = Set(
       name='secondSet', description='this is an example set with a random description aaaaaaaaaaaaaaaaaaaaaaaaa', userId=1)
    set7 = Set(
       name='thirdSet', description='this is an example set with a random description aaaaaaaaaaaaaaaaaaaaaaaaa', userId=1)
    set8 = Set(
       name='forthSet', description='this is an example set with a random description aaaaaaaaaaaaaaaaaaaaaaaaa', userId=1)
    set9 = Set(
       name='fifthSet', description='this is an example set with a random description aaaaaaaaaaaaaaaaaaaaaaaaa', userId=2, draft = True)

    allSets = [set1,set2,set3,set4,set5,set6,set7,set8,set9]
    [db.session.add(aset) for aset in allSets]
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_sets():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.sets RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM sets"))

    db.session.commit()
