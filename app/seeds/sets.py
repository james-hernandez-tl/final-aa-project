from app.models import db, Set, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_sets():
   sets = []
   sets.append(Set(name='Algebraic Equations', description='Solve equations with variables and constants.', userId=8))
   sets.append(Set(name='Geometry Fundamentals', description='Explore basic concepts of shapes, angles, and measurements.', userId=9))
   sets.append(Set(name='Calculus Concepts', description='Dive into the world of limits, derivatives, and integrals.', userId=10))
   sets.append(Set(name='Probability & Statistics', description='Learn about the principles of data analysis and probability.', userId=11))
   sets.append(Set(name='Number Theory', description='Discover the properties and patterns of integers.', userId=12))
   sets.append(Set(name='Linear Algebra', description='Study vectors, matrices, and linear transformations.', userId=13))
   sets.append(Set(name='Trigonometry Basics', description='Explore trigonometric functions and their applications.', userId=1))
   sets.append(Set(name='Math Puzzles', description='Challenge yourself with fun and brain-teasing math problems.', userId=2))
   sets.append(Set(name='Financial Mathematics', description='Understand concepts like interest, investments, and loans.', userId=3))
   sets.append(Set(name='Geometry Proofs', description='Master the art of proving geometric theorems.', userId=4))
   sets.append(Set(name='Ancient Civilizations', description='Explore the rise and fall of ancient cultures and empires.', userId=5))
   sets.append(Set(name='World Wars I and II', description='Learn about the causes, events, and impact of both world wars.', userId=6))
   sets.append(Set(name='Renaissance Era', description='Dive into the cultural, artistic, and intellectual revival of the Renaissance.', userId=7))
   sets.append(Set(name='Colonial America', description='Discover the history of early settlements and the founding of the United States.', userId=8))
   sets.append(Set(name='Medieval Europe', description='Study the Middle Ages, feudalism, and knights of medieval Europe.', userId=9))
   sets.append(Set(name='Cold War Era', description='Examine the geopolitical tensions and conflicts during the Cold War.', userId=10))
   sets.append(Set(name='Industrial Revolution', description='Explore the transformation of economies and societies through industrialization.', userId=11))
   sets.append(Set(name='Civil Rights Movement', description='Learn about the fight for equality and social justice in the 20th century.', userId=12))
   sets.append(Set(name='World History Timelines', description='Get an overview of key historical events from various eras.', userId=13))
   sets.append(Set(name='Ancient Egypt', description='Discover the culture, pharaohs, and achievements of ancient Egypt.', userId=1))
   sets.append(Set(name='Programming Languages', description='Learn about various programming languages and their features.', userId=2))
   sets.append(Set(name='Version Control with Git', description='Master Git for efficient code version management and collaboration.', userId=3))
   sets.append(Set(name='Web Development Basics', description='Explore HTML, CSS, and JavaScript for building web applications.', userId=4))
   sets.append(Set(name='Object-Oriented Programming', description='Understand OOP concepts like classes, objects, and inheritance.', userId=5))
   sets.append(Set(name='Database Management', description='Study database design, SQL queries, and data manipulation.', userId=6))
   sets.append(Set(name='Software Design Patterns', description='Learn common design patterns for writing maintainable code.', userId=7))
   sets.append(Set(name='Backend Development', description='Delve into server-side programming and APIs for applications.', userId=8))
   sets.append(Set(name='Frontend Frameworks', description='Explore popular frontend frameworks like React, Angular, and Vue.', userId=9))
   sets.append(Set(name='Test-Driven Development', description='Discover TDD principles for building reliable and robust software.', userId=10))
   sets.append(Set(name='Agile Methodology', description='Understand Agile practices for efficient software development.', userId=11))
   sets.append(Set(name='Birds of Prey', description='Learn about powerful raptors and their hunting techniques.', userId=12))
   sets.append(Set(name='Songbirds', description='Explore melodious songbirds and their beautiful vocalizations.', userId=13))
   sets.append(Set(name='Waterfowl', description='Discover ducks, geese, and swans that inhabit wetlands.', userId=1))
   sets.append(Set(name='Tropical Birds', description='Dive into the vibrant world of exotic birds from tropical regions.', userId=2, draft = True))
   sets.append(Set(name='Flightless Birds', description='Study birds that have adapted to a flightless lifestyle.', userId=3))
   sets.append(Set(name='Migratory Birds', description='Learn about birds that undertake incredible seasonal migrations.', userId=4))
   sets.append(Set(name='Bird Anatomy', description='Explore the various parts of a bird and their functions.', userId=5))
   sets.append(Set(name='Endangered Birds', description='Understand the conservation status of rare and endangered bird species.', userId=6))
   sets.append(Set(name='Birds in Mythology', description='Discover birds that hold special significance in cultural myths.', userId=7))
   sets.append(Set(name='Bird Watching Tips', description='Get tips for observing and identifying birds in the wild.', userId=8))
   sets.append(Set(name='Cuisines of the World', description='Explore diverse culinary traditions from around the globe.', userId=9))
   sets.append(Set(name='Healthy Eating Habits', description='Learn about nutritious foods and balanced dietary choices.', userId=10))
   sets.append(Set(name='Baking Essentials', description='Discover key ingredients and techniques for baking delicious treats.', userId=11))
   sets.append(Set(name='Exotic Fruits', description='Explore unique and flavorful fruits from different regions.', userId=12))
   sets.append(Set(name='Comfort Food Classics', description='Dive into nostalgic and comforting dishes that warm the heart.', userId=13))
   sets.append(Set(name='Cooking Techniques', description='Master essential cooking methods and skills in the kitchen.', userId=1))
   sets.append(Set(name='Global Spices and Herbs', description='Learn about the aromatic seasonings used in various cuisines.', userId=2))
   sets.append(Set(name='Dessert Delights', description='Indulge in delectable desserts and sweet treats from around the world.', userId=3))
   sets.append(Set(name='Plant-Based Recipes', description='Explore delicious vegetarian and vegan dishes for a green diet.', userId=4))
   sets.append(Set(name='Gourmet Ingredients', description='Discover luxurious and high-quality ingredients for upscale dishes.', userId=5))


   [db.session.add(aset) for aset in sets]
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
