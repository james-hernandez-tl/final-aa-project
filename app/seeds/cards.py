from app.models import db, Card, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_cards():
    cards = []

    # set1

    questions = [
    'What are algebraic equations?',
    'How do you solve equations with variables?',
    'Give an example of a simple algebraic equation.',
    'What role do constants play in algebraic equations?',
    'Explain the process of solving linear equations.',
    'What are the steps to solve quadratic equations?',
    'Why is it important to find solutions to algebraic equations?',
    'How do you determine if an equation has no solutions?',
    'What is the significance of variables in algebraic equations?',
    'Can algebraic equations be used in real-world scenarios?'
]

    answers = [
    'Algebraic equations are mathematical statements that involve variables and constants.',
    'Equations with variables are solved by finding values that make the equation true.',
    'Example: 2x + 3 = 7',
    'Constants are fixed values that do not change in the equation.',
    'Linear equations are solved by isolating the variable on one side of the equation.',
    'Steps for solving quadratic equations include factoring, completing the square, and using the quadratic formula.',
    'Solutions to equations help us find the values that satisfy given conditions.',
    'An equation with no solutions leads to a contradiction or inconsistency.',
    'Variables represent unknown quantities and allow us to solve for specific values.',
    'Yes, algebraic equations model various real-world situations and problems.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=1, question=questions[i], answer=answers[i]))

    #set2

    questions = [
    'What is the definition of geometry?',
    'What are the building blocks of geometry?',
    'Define a polygon.',
    'Explain the concept of angles.',
    'What is the sum of the interior angles of a triangle?',
    'What is the formula to calculate the area of a rectangle?',
    'Describe the properties of a circle.',
    'What is the perimeter of a square with a side length of 5 units?',
    'Define congruent shapes.',
    'Explain the Pythagorean theorem.'
]

    answers = [
    'Geometry is a branch of mathematics that deals with shapes, sizes, and properties of space.',
    'Points, lines, and planes are the basic building blocks of geometry.',
    'A polygon is a closed shape with straight sides.',
    'Angles are formed by two rays sharing a common endpoint.',
    'The sum of the interior angles of a triangle is 180 degrees.',
    'Area of a rectangle = length × width',
    'A circle is a set of points equidistant from a center point.',
    'Perimeter of a square = 4 × side length',
    'Congruent shapes are identical in shape and size.',
    'The Pythagorean theorem states that in a right triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.'
]

    for i in range(len(questions)):
         cards.append(Card(setId=2, question=questions[i], answer=answers[i]))

    #set3

    questions = [
    'What are the fundamental concepts of calculus?',
    'Define the concept of a limit in calculus.',
    'What is the derivative of a function?',
    'Explain the concept of differentiation.',
    'What is the product rule in calculus?',
    'What is the integral of a function?',
    'Describe the concept of integration.',
    'What is the fundamental theorem of calculus?',
    'Explain the concept of area under a curve.',
    'What is the chain rule in calculus?'
]

    answers = [
    'Calculus deals with the concepts of limits, derivatives, and integrals in mathematics.',
    'A limit describes the behavior of a function as its input approaches a certain value.',
    'The derivative of a function measures its rate of change at a specific point.',
    'Differentiation is the process of finding the derivative of a function.',
    'The product rule states how to find the derivative of a product of two functions.',
    'An integral represents the accumulation of quantities and is the reverse of differentiation.',
    'Integration involves finding the area under a curve and is used to compute accumulations.',
    'The fundamental theorem of calculus establishes a relationship between differentiation and integration.',
    'Area under a curve represents the accumulated quantity described by the function.',
    'The chain rule is used to find the derivative of a composition of two functions.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=3, question=questions[i], answer=answers[i]))

    #set4

    questions = [
    'What is probability?',
    'Define random variable in statistics.',
    'What is a frequency distribution?',
    'Explain the concept of mean in statistics.',
    'What is the difference between median and mode?',
    'What is standard deviation?',
    'Define normal distribution.',
    'What is the correlation coefficient?',
    'Explain the concept of sampling in statistics.',
    'What is the law of large numbers?'
]

    answers = [
    'Probability is the likelihood of an event occurring.',
    'A random variable is a variable whose possible values are outcomes of a random phenomenon.',
    'A frequency distribution shows the frequency of each value in a dataset.',
    'The mean is the average of a set of numbers.',
    'Median is the middle value in a dataset, and mode is the most frequent value.',
    'Standard deviation measures the dispersion or spread of a dataset.',
    'Normal distribution is a bell-shaped probability distribution.',
    'The correlation coefficient measures the strength and direction of a linear relationship.',
    'Sampling involves selecting a subset of individuals from a larger population.',
    'The law of large numbers states that as the number of trials increases, the observed frequency of an event gets closer to its theoretical probability.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=4, question=questions[i], answer=answers[i]))

    #set5

    questions = [
    'What is prime factorization?',
    'Define greatest common divisor (GCD).',
    'What is the difference between prime and composite numbers?',
    'Explain the concept of divisibility.',
    'What is the Euclidean algorithm?',
    'Define coprime or relatively prime numbers.',
    'What is the Sieve of Eratosthenes?',
    'Explain the concept of modular arithmetic.',
    'Define perfect number.',
    'What are twin primes?'
]

    answers = [
    'Prime factorization is expressing a number as a product of prime numbers.',
    'Greatest common divisor (GCD) is the largest positive integer that divides two or more numbers without leaving a remainder.',
    'Prime numbers have only two divisors (1 and itself), while composite numbers have more than two divisors.',
    'Divisibility is the property of one number being divisible by another without leaving a remainder.',
    'The Euclidean algorithm is used to find the GCD of two numbers.',
    'Coprime or relatively prime numbers have a GCD of 1.',
    'The Sieve of Eratosthenes is a method to find all prime numbers up to a certain limit.',
    'Modular arithmetic deals with remainders when dividing by a specific number.',
    'A perfect number is equal to the sum of its proper divisors.',
    'Twin primes are prime numbers that have a difference of 2.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=5, question=questions[i], answer=answers[i]))

    #set6

    questions = [
    'What are vectors in linear algebra?',
    'Define matrix in the context of linear algebra.',
    'Explain the concept of scalar multiplication.',
    'What are eigenvalues and eigenvectors?',
    'Define determinant of a matrix.',
    'What is the dot product of two vectors?',
    'Explain the concept of linear transformations.',
    'Define rank and nullity of a matrix.',
    'What is the identity matrix?',
    'Explain the concept of eigendecomposition.'
]

    answers = [
    'Vectors are quantities that have both magnitude and direction.',
    'A matrix is a rectangular array of numbers, symbols, or expressions arranged in rows and columns.',
    'Scalar multiplication is the multiplication of a vector by a scalar (real number).',
    'Eigenvalues are scalars that represent how a matrix scales an eigenvector. Eigenvectors are non-zero vectors that remain in the same direction after a linear transformation.',
    'Determinant of a matrix is a scalar value that can be computed from its elements and provides information about the matrix transformation.',
    'The dot product of two vectors is the product of their magnitudes and the cosine of the angle between them.',
    'Linear transformations are functions that map vectors to vectors while preserving linear relationships.',
    'Rank is the maximum number of linearly independent rows or columns in a matrix. Nullity is the dimension of the null space of a matrix.',
    'The identity matrix is a square matrix with ones on the diagonal and zeros elsewhere.',
    'Eigendecomposition is a factorization of a matrix into a canonical form using its eigenvalues and eigenvectors.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=6, question=questions[i], answer=answers[i]))



    #set7

    questions = [
    'What are sine, cosine, and tangent?',
    'Explain the concept of angle measurement in degrees.',
    'Define the Pythagorean identities in trigonometry.',
    'What is the unit circle?',
    'What is the Law of Sines?',
    'Define inverse trigonometric functions.',
    'What are the primary trigonometric ratios?',
    'Explain the concept of radian measure.',
    'What is the Law of Cosines?',
    'What is the domain of trigonometric functions?'
]

    answers = [
    'Sine, cosine, and tangent are trigonometric functions used to relate angles and sides of triangles.',
    'Angle measurement in degrees is a way to measure angles based on dividing a circle into 360 equal parts.',
    'Pythagorean identities are trigonometric equations involving sine, cosine, and tangent.',
    'The unit circle is a circle with a radius of 1 unit, used to define trigonometric functions.',
    'The Law of Sines states a relationship between the sides and angles of a triangle.',
    'Inverse trigonometric functions undo the effects of trigonometric functions.',
    'The primary trigonometric ratios are sine, cosine, and tangent.',
    'Radian measure is a way to measure angles based on the radius of a circle.',
    'The Law of Cosines relates the sides and angles of a triangle in a more general way than the Pythagorean theorem.',
    'The domain of trigonometric functions is all real numbers.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=7, question=questions[i], answer=answers[i]))

    #set8

    questions = [
    'What is the missing number in this sequence: 2, 4, 8, __, 32?',
    'How can you make the number 100 using four 9s?',
    'What is the next number in this sequence: 1, 1, 2, 3, 5, 8, __?',
    'If a rooster laid an egg on top of the barn roof, which way would it roll?',
    'What comes after a million, billion, and trillion?',
    'I have keys but open no locks. I have space but no room. You can enter, but you can’t go outside. What am I?',
    'What is the sum of all the numbers on a standard roulette wheel?',
    'How can you make 6 out of three 9s?',
    'What has keys but can’t open locks?',
    'What is the smallest positive integer that is divisible by all the numbers from 1 to 10?'
]

    answers = [
    '16',
    '99 + (9 / 9)',
    '13',
    'Roosters don’t lay eggs.',
    'Quadrillion',
    'A keyboard.',
    '666',
    '(9 - 9) / 9',
    'A piano.',
    '2520'
    ]

    for i in range(len(questions)):
        cards.append(Card(setId=8, question=questions[i], answer=answers[i]))


    #set9

    questions = [
    'What is compound interest?',
    'Define present value.',
    'Explain the concept of annuity.',
    'What is the difference between simple interest and compound interest?',
    'Define inflation.',
    'What are the different types of investment risks?',
    'Explain the concept of diversification.',
    'What is a stock market index?',
    'Define mutual funds.',
    'How does a credit score affect financial decisions?'
]

    answers = [
    'Compound interest is interest calculated on both the initial principal and the accumulated interest.',
    'Present value is the value of future cash flows discounted to the present at a specific rate.',
    'An annuity is a series of equal payments or receipts made at regular intervals.',
    'Simple interest is calculated only on the initial principal, while compound interest includes interest on interest.',
    'Inflation is the rate at which the general level of prices for goods and services is rising.',
    'Investment risks include market risk, interest rate risk, credit risk, liquidity risk, and more.',
    'Diversification is the practice of spreading investments across various assets to manage risk.',
    'A stock market index measures the performance of a specific group of stocks representing a particular market or sector.',
    'Mutual funds pool money from many investors to invest in a diversified portfolio of stocks, bonds, or other securities.',
    'A credit score reflects a person’s creditworthiness and impacts their ability to obtain loans and favorable interest rates.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=9, question=questions[i], answer=answers[i]))

    #set10

    questions = [
    'What is a geometry proof?',
    'Explain the concept of congruence in geometry.',
    'What is the Angle Addition Postulate?',
    'Define the Pythagorean Theorem.',
    'Explain the concept of similar triangles.',
    'What is the Side-Angle-Side (SAS) congruence criterion?',
    'Define the Reflexive Property of equality.',
    'Explain the Transitive Property of equality.',
    'What is the Vertical Angles Theorem?',
    'Define the Symmetric Property of equality.'
]

    answers = [
    'A geometry proof is a logical argument that demonstrates the validity of a mathematical statement using established axioms and theorems.',
    'Congruence in geometry refers to figures or angles that have the same shape and size.',
    'The Angle Addition Postulate states that if a point is in the interior of an angle, the angle formed by the two sides can be added to the given angle.',
    'The Pythagorean Theorem states that in a right triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides.',
    'Similar triangles have the same shape but possibly different sizes.',
    'The Side-Angle-Side (SAS) congruence criterion states that if two sides and the included angle of one triangle are congruent to two sides and the included angle of another triangle, then the triangles are congruent.',
    'The Reflexive Property of equality states that any quantity is equal to itself.',
    'The Transitive Property of equality states that if a = b and b = c, then a = c.',
    'The Vertical Angles Theorem states that vertical angles are congruent.',
    'The Symmetric Property of equality states that if a = b, then b = a.'
]

    for i in range(len(questions)):
       cards.append(Card(setId=10, question=questions[i], answer=answers[i]))

    #set11

    questions = [
    'What are the characteristics of a civilization?',
    'Describe the architecture of ancient Egypt.',
    'What were the major achievements of the Mesopotamian civilizations?',
    'Explain the significance of the Code of Hammurabi.',
    'What were the cultural contributions of ancient Greece?',
    'Describe the role of the Great Wall of China in ancient times.',
    'What were the key features of the Roman Republic?',
    'Explain the significance of the Silk Road.',
    'Describe the social structure of ancient Maya civilization.',
    'What were the causes and effects of the fall of the Roman Empire?'
]

    answers = [
    'Characteristics of a civilization include advanced social, political, economic, and cultural developments.',
    'Ancient Egyptian architecture featured pyramids, temples, and structures along the Nile River.',
    'Mesopotamian civilizations achieved writing systems, irrigation, and legal codes.',
    'The Code of Hammurabi was a comprehensive legal code that influenced subsequent legal systems.',
    'Ancient Greece contributed to philosophy, democracy, theater, and art.',
    'The Great Wall of China served as a defensive structure to protect against invasions.',
    'The Roman Republic had a Senate, consuls, and a system of checks and balances.',
    'The Silk Road was a trade route connecting East and West, facilitating cultural exchange.',
    'Ancient Maya society had rulers, priests, warriors, and commoners.',
    'The fall of the Roman Empire was influenced by internal strife, economic issues, and external invasions.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=11, question=questions[i], answer=answers[i]))

    #set12

    questions = [
    'What were the main causes of World War I?',
    'Describe the system of alliances in Europe before World War I.',
    'What were the major events of World War I?',
    'Explain the significance of the Treaty of Versailles.',
    'What factors led to the rise of Adolf Hitler and the Nazi Party?',
    'Describe the key events of World War II.',
    'What was the Holocaust?',
    'Explain the impact of the atomic bombings of Hiroshima and Nagasaki.',
    'Describe the formation of the United Nations after World War II.',
    'What were the long-term effects of World Wars I and II?'
]

    answers = [
    'Main causes of World War I included militarism, alliances, imperialism, and nationalism.',
    'The system of alliances created a complex web of political and military commitments among European powers.',
    'Major events of World War I included the assassination of Archduke Franz Ferdinand, trench warfare, and the Treaty of Versailles.',
    'The Treaty of Versailles imposed heavy penalties on Germany and contributed to resentment and economic challenges.',
    'The Treaty of Versailles imposed heavy penalties on Germany and contributed to resentment and economic challenges.',
    'World War II events included the invasion of Poland, Battle of Stalingrad, D-Day, and the Holocaust.',
    'The Holocaust was the systematic genocide of six million Jews by Nazi Germany.',
    "The atomic bombings of Hiroshima and Nagasaki led to Japan's surrender and the end of World War II.",
    'The United Nations was formed to promote international cooperation and prevent future conflicts.',
    'World Wars I and II had lasting effects on geopolitics, economies, and international relations.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=12, question=questions[i], answer=answers[i]))


    [db.session.add(acard) for acard in cards]
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
