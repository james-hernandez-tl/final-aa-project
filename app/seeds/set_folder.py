from app.models import db,Folder,Set,environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_set_folder():
    folder = Folder.query.filter(Folder.name == "Folder1").first()
    set1 = Set.query.filter(Set.name == "Algebraic Equations").first()
    set2 = Set.query.filter(Set.name == "Geometry Fundamentals").first()
    set3 = Set.query.filter(Set.name == "Migratory Birds").first()
    set4 = Set.query.filter(Set.name == "Backend Development").first()

    allSets = [set1,set2,set3,set4]
    [folder.foldersOfSets.append(aset) for aset in allSets]
    db.session.add(folder)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_set_folder():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.set_folders RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM set_folders"))

    db.session.commit()
