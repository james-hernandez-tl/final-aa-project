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

    #set13

    questions = [
    'What was the Renaissance?',
    'Describe the role of the Medici family in the Renaissance.',
    'Who was Leonardo da Vinci?',
    'Explain the concept of humanism during the Renaissance.',
    'What is the significance of the Sistine Chapel ceiling?',
    'Who wrote "The Prince" and what were its themes?',
    'Describe the artistic style of the Renaissance.',
    'What was the impact of the printing press on the Renaissance?',
    'Explain the development of perspective in Renaissance art.',
    'What was the scientific contribution of Copernicus during the Renaissance?'
]

    answers = [
    'The Renaissance was a cultural and intellectual movement that began in Italy and marked a revival of art, literature, and learning.',
    'The Medici family were powerful patrons of the arts and played a significant role in promoting Renaissance culture.',
    'Leonardo da Vinci was a polymath known for his art, inventions, and scientific observations.',
    'Humanism emphasized the study of classical texts, individualism, and the potential of human achievements.',
    'The Sistine Chapel ceiling, painted by Michelangelo, is one of the greatest works of Renaissance art.',
    '"The Prince" was written by Niccolò Machiavelli and discussed political power and leadership strategies.',
    'The Renaissance emphasized realistic portrayal of human figures, perspective, and chiaroscuro (light and shadow).',
    'The printing press allowed for the rapid dissemination of knowledge, contributing to the spread of Renaissance ideas.',
    'Perspective techniques in art allowed for the accurate depiction of three-dimensional space on a two-dimensional surface.',
    'Copernicus proposed the heliocentric model of the solar system, challenging the geocentric view and contributing to modern astronomy.'
    ]

    for i in range(len(questions)):
        cards.append(Card(setId=13, question=questions[i], answer=answers[i]))

    #set14

    questions = [
    'What were the motivations for European colonization of the Americas?',
    'Describe the establishment of Jamestown, the first permanent English settlement in North America.',
    'What were the main economic activities in colonial New England?',
    'Explain the significance of the Mayflower Compact.',
    'Describe the triangular trade route and its impact.',
    'What was the Great Awakening?',
    'Explain the role of the Navigation Acts in colonial trade.',
    'Describe the Salem witch trials.',
    'What was the impact of the French and Indian War on the American colonies?',
    'Explain the concept of mercantilism in colonial economics.'
]

    answers = [
    'Motivations for European colonization included economic opportunities, religious freedom, and the search for new trade routes.',
    'Jamestown was established in 1607 by the Virginia Company and faced early challenges before becoming successful.',
    'Colonial New England relied on industries such as shipbuilding, fishing, and trade.',
    'The Mayflower Compact established a self-governing agreement among the Pilgrims in Plymouth.',
    'The triangular trade involved the exchange of goods between Europe, Africa, and the Americas, including the transatlantic slave trade.',
    'The Great Awakening was a religious revival that emphasized individual spiritual experience and had social and political impacts.',
    'The Navigation Acts were designed to regulate colonial trade and benefit the British economy.',
    'The Salem witch trials were a series of witchcraft accusations and trials in colonial Massachusetts.',
    'The French and Indian War led to increased tensions between the colonies and Britain, contributing to the American Revolution.',
    'Mercantilism promoted the idea of accumulating wealth through exports, imports, and colonial resources.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=14, question=questions[i], answer=answers[i]))

    #set15

    questions = [
    'What was feudalism in medieval Europe?',
    'Describe the role of knights in the feudal system.',
    'Explain the significance of medieval castles.',
    'What was the role of the Catholic Church in medieval society?',
    'Describe the system of manorialism.',
    'What were the main events of the Crusades?',
    'Explain the concept of chivalry.',
    'Describe the Black Death and its impact on medieval Europe.',
    'What were guilds in medieval cities?',
    'Explain the decline of feudalism and the transition to the Renaissance.'
]

    answers = [
    'Feudalism was a social, economic, and political system based on land ownership and loyalty.',
    'Knights were armored warriors who served lords in exchange for land and protection.',
    'Medieval castles served as defensive structures, residences for nobles, and symbols of power.',
    'The Catholic Church played a central role in religious, cultural, and political life in medieval Europe.',
    'Manorialism was an economic system based on self-sufficient manors or estates.',
    'The Crusades were a series of religious and military campaigns to reclaim Jerusalem and the Holy Land.',
    'Chivalry was a code of conduct that emphasized virtues such as honor, courage, and loyalty.',
    'The Black Death (Bubonic Plague) was a deadly pandemic that devastated Europe and led to significant social and economic changes.',
    'Guilds were associations of craftsmen and merchants that regulated trade and protected members.',
    'The decline of feudalism was influenced by factors such as the Black Death, economic changes, and the rise of centralized monarchies.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=15, question=questions[i], answer=answers[i]))

    #set16

    questions = [
    'What was the Cold War and when did it take place?',
    'Describe the ideological differences between the United States and the Soviet Union during the Cold War.',
    'What was the policy of containment?',
    'Explain the significance of the Cuban Missile Crisis.',
    'Describe the space race between the United States and the Soviet Union.',
    'What was the arms race during the Cold War?',
    'Explain the concept of mutually assured destruction (MAD).',
    'Describe the role of the Berlin Wall in the Cold War.',
    'What was the Korean War and its outcome?',
    'Explain the collapse of the Soviet Union and the end of the Cold War.'
]

    answers = [
    'The Cold War was a period of geopolitical tension and rivalry between the United States and the Soviet Union, lasting from the end of World War II to 1991.',
    'The United States promoted democracy and capitalism, while the Soviet Union advocated for communism and a planned economy.',
    'Containment was a policy to prevent the spread of communism by containing its influence and expansion.',
    'The Cuban Missile Crisis was a 1962 confrontation between the U.S. and the Soviet Union over Soviet missiles in Cuba, narrowly avoiding nuclear conflict.',
    'The space race involved competition between the U.S. and the Soviet Union to achieve significant milestones in space exploration.',
    'The arms race was a competition to develop and acquire nuclear weapons and military technology.',
    'Mutually assured destruction (MAD) is a doctrine that posits the use of nuclear weapons by two opposing sides would result in the complete destruction of both.',
    'The Berlin Wall was a symbol of the division between East and West Berlin during the Cold War.',
    'The Korean War was a conflict between North Korea (backed by China and the Soviet Union) and South Korea (supported by the United Nations), resulting in an armistice and a divided Korea.',
    'The collapse of the Soviet Union was influenced by economic challenges, political reforms, and internal pressures, leading to the end of the Cold War.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=16, question=questions[i], answer=answers[i]))

    #set17

    questions = [
    'What was the Industrial Revolution and when did it occur?',
    'Describe the key innovations and technologies of the Industrial Revolution.',
    'Explain the concept of urbanization during the Industrial Revolution.',
    'Describe the working conditions in early factories.',
    'What were the social and economic impacts of the Industrial Revolution?',
    'Explain the role of child labor during the Industrial Revolution.',
    'Describe the growth of railroads and their significance in the Industrial Revolution.',
    'What were the factors that led to the rise of industrial capitalism?',
    'Explain the connection between the Industrial Revolution and imperialism.',
    'Describe the environmental impact of the Industrial Revolution.'
]

    answers = [
    'The Industrial Revolution was a period of significant technological, economic, and social change that occurred from the late 18th to the 19th century.',
    'Key innovations included the steam engine, cotton gin, spinning jenny, and mechanized loom.',
    'Urbanization refers to the migration of people from rural areas to cities, driven by factory jobs and economic opportunities.',
    'Early factories had poor working conditions, long hours, low pay, and unsafe environments.',
    'The Industrial Revolution led to urbanization, increased production, and changes in transportation and communication.',
    'Child labor was widespread during the Industrial Revolution, with children working in factories and mines under harsh conditions.',
    'Railroads expanded transportation networks, facilitated trade, and contributed to economic growth.',
    'Factors such as technological innovations, access to resources, and investment led to the rise of industrial capitalism.',
    'The Industrial Revolution fueled imperialism as industrialized nations sought raw materials and markets for their goods.',
    'The Industrial Revolution contributed to pollution, deforestation, and other environmental challenges.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=17, question=questions[i], answer=answers[i]))

    #set18

    questions = [
    'What was the Civil Rights Movement and when did it take place?',
    'Describe the goals and objectives of the Civil Rights Movement.',
    'Explain the significance of the Brown v. Board of Education Supreme Court case.',
    'Describe the Montgomery Bus Boycott and its impact.',
    'What was the role of Martin Luther King Jr. in the Civil Rights Movement?',
    'Explain the concept of nonviolent resistance and civil disobedience.',
    'Describe the events of the March on Washington for Jobs and Freedom.',
    'What were the key achievements of the Civil Rights Act of 1964?',
    'Explain the Voting Rights Act of 1965 and its impact.',
    'Describe the challenges and obstacles faced by activists during the Civil Rights Movement.'
]

    answers = [
    'The Civil Rights Movement was a social and political movement in the United States that aimed to end racial segregation and discrimination, occurring primarily from the 1950s to the 1960s.',
    'The movement sought equal rights and opportunities for African Americans, including desegregation, voting rights, and an end to racial discrimination.',
    'Brown v. Board of Education was a landmark case that declared racial segregation in public schools unconstitutional.',
    'The Montgomery Bus Boycott was a protest against segregated buses in Alabama, leading to a Supreme Court ruling against segregation on public transportation.',
    'Martin Luther King Jr. was a prominent civil rights leader known for advocating nonviolent protest and civil disobedience.',
    'Nonviolent resistance and civil disobedience involved using peaceful methods to protest injustice and advocate for change.',
    "The March on Washington for Jobs and Freedom included Martin Luther King Jr.'s \"I Have a Dream\" speech and highlighted the need for civil rights legislation.'",
    'The Civil Rights Act of 1964 outlawed discrimination based on race, color, religion, sex, or national origin.',
    'The Voting Rights Act of 1965 aimed to eliminate racial discrimination in voting and led to increased African American voter registration.',
    'Activists faced violence, legal challenges, and resistance from segregationists during the Civil Rights Movement.'
]

    for i in range(len(questions)):
         cards.append(Card(setId=18, question=questions[i], answer=answers[i]))

    #set19

    questions = [
    'What is the significance of the Agricultural Revolution?',
    'Describe the achievements of ancient Mesopotamia.',
    'What were the major events of the Middle Ages?',
    'Explain the significance of the Renaissance.',
    'Describe the Age of Exploration and its impact.',
    'What were the causes and effects of the Industrial Revolution?',
    'Explain the events leading up to World War I.',
    'Describe the impact of World War II on global geopolitics.',
    'What were the major events of the Cold War?',
    'Explain the fall of the Berlin Wall and its implications.'
]

    answers = [
    'The Agricultural Revolution marked the transition from nomadic hunting and gathering to settled farming, leading to permanent settlements and increased food production.',
    'Ancient Mesopotamia achieved writing (cuneiform), legal codes (Code of Hammurabi), and innovations in irrigation and architecture.',
    'The Middle Ages saw the rise of feudalism, the Crusades, and the development of Gothic architecture.',
    'The Renaissance was a cultural and artistic revival in Europe, emphasizing humanism, art, literature, and scientific inquiry.',
    'The Age of Exploration led to global exploration, colonization, and the exchange of goods, people, and cultures between the Old World and the New World.',
    'The Industrial Revolution brought mechanization, urbanization, and significant changes to economies and societies.',
    'Events leading to World War I included militarism, alliances, imperialism, and the assassination of Archduke Franz Ferdinand.',
    'World War II had profound effects on international relations, including the emergence of the United States and Soviet Union as superpowers.',
    'The Cold War involved tensions between the United States and the Soviet Union, the space race, and proxy conflicts.',
    'The fall of the Berlin Wall symbolized the end of the Cold War division in Europe and led to the reunification of Germany.'
]

    for i in range(len(questions)):
       cards.append(Card(setId=19, question=questions[i], answer=answers[i]))

    #set20

    questions = [
    'What was the significance of the Nile River to ancient Egypt?',
    'Describe the social structure of ancient Egyptian society.',
    'What were hieroglyphics and how were they used?',
    'Explain the role of pharaohs in ancient Egypt.',
    'Describe the construction of the pyramids and their purpose.',
    'What were the major achievements of ancient Egyptian culture?',
    'Explain the concept of mummification and its religious significance.',
    'Describe the gods and goddesses of ancient Egyptian mythology.',
    'What was the Rosetta Stone and why is it important?',
    'Explain the decline and fall of ancient Egypt.'
]

    answers = [
    'The Nile River was vital for agriculture, transportation, and providing fertile soil through annual flooding.',
    'Ancient Egyptian society had a hierarchical structure with pharaohs, nobles, priests, scribes, artisans, and peasants.',
    'Hieroglyphics were a system of writing using pictorial symbols, often inscribed on tombs and monuments.',
    'Pharaohs were rulers of ancient Egypt believed to be divine and responsible for maintaining maat (order) in society.',
    'The pyramids were monumental tombs built for pharaohs to ensure their safe passage to the afterlife.',
    'Achievements included monumental architecture, mathematics, medicine, and advancements in art and literature.',
    'Mummification preserved bodies for the afterlife and was linked to Egyptian beliefs in the journey to the realm of Osiris.',
    'Ancient Egyptians worshiped a pantheon of gods and goddesses, each associated with specific aspects of life and nature.',
    'The Rosetta Stone contained inscriptions in three scripts and helped decipher hieroglyphics, contributing to the understanding of ancient Egyptian language.',
    'Factors such as foreign invasions, political instability, and economic challenges contributed to the decline and fall of ancient Egypt.'
]

    for i in range(len(questions)):
       cards.append(Card(setId=20, question=questions[i], answer=answers[i]))


    #set21

    questions = [
    'What is a programming language and its purpose?',
    'Describe the difference between high-level and low-level programming languages.',
    'Explain the concept of variables and data types in programming.',
    'Describe the role of loops in programming.',
    'What is object-oriented programming (OOP) and its principles?',
    'Explain the purpose of functions or methods in programming.',
    'Describe the differences between compiled and interpreted programming languages.',
    'What are some examples of popular programming languages?',
    'Explain the concept of abstraction in programming.',
    'Describe the importance of comments in writing code.'
]

    answers = [
    'A programming language is a formal system used to write instructions for a computer to perform specific tasks.',
    'High-level languages are more user-friendly and abstract, while low-level languages are closer to machine code and provide greater control over hardware.',
    'Variables store data values, and data types define the kind of data that can be stored (e.g., integers, strings, booleans).',
    'Loops allow programmers to repeat a sequence of instructions, such as "for" and "while" loops.',
    'Object-oriented programming (OOP) organizes code around objects, encapsulation, inheritance, and polymorphism.',
    'Functions or methods are blocks of code that can be reused to perform specific tasks or calculations.',
    'Compiled languages are translated into machine code before execution, while interpreted languages are executed line by line by an interpreter.',
    'Examples of programming languages include Python, Java, C++, JavaScript, and Ruby.',
    'Abstraction hides complex implementation details and focuses on essential features for ease of use.',
    'Comments provide explanations within code to improve readability and understanding.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=21, question=questions[i], answer=answers[i]))

    #set22

    questions = [
    'What is version control and why is it important?',
    'Explain the purpose of a Git repository.',
    'Describe the difference between Git and GitHub.',
    'What is a commit in Git?',
    'Explain the concept of branching and merging in Git.',
    'Describe the process of creating a pull request on GitHub.',
    'What is a merge conflict and how is it resolved?',
    'Explain the use of "git clone" and "git pull" commands.',
    'Describe the role of "gitignore" files in Git.',
    'What are some common Git workflows for collaboration?'
]

    answers = [
    'Version control is the management of changes to software code over time, important for tracking history and collaboration.',
    'A Git repository is a storage location for a collection of files and the history of changes made to them.',
    'Git is a distributed version control system, while GitHub is a platform for hosting Git repositories and collaborating on code.',
    'A commit in Git is a snapshot of the code at a specific point in time, along with a description of the changes made.',
    'Branching allows developers to work on separate copies of the code, and merging combines changes from one branch into another.',
    'A pull request on GitHub is a request to merge changes from one branch into another, allowing code review and collaboration.',
    'A merge conflict occurs when Git cannot automatically merge changes, and it must be resolved manually by the developer.',
    '"git clone" downloads a copy of a remote repository to a local machine, while "git pull" updates a local repository with changes from a remote.',
    '"gitignore" files specify patterns of files that should be excluded from version control.',
    'Common Git workflows include feature branching, Gitflow, and GitHub flow, each with its approach to collaboration.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=22, question=questions[i], answer=answers[i]))

    #set23

    questions = [
    'What is HTML and its role in web development?',
    'Explain the purpose of CSS in web design.',
    'Describe the box model in CSS.',
    'What is responsive web design?',
    'Explain the difference between inline, block, and inline-block elements in HTML.',
    'Describe the role of JavaScript in web development.',
    'What is the Document Object Model (DOM) in web development?',
    'Explain the concept of event handling in JavaScript.',
    'Describe the use of libraries and frameworks in web development.',
    'What are some common tools used for web development?'
]

    answers = [
    'HTML (Hypertext Markup Language) is used to structure content on web pages, defining elements like headings, paragraphs, and links.',
    'CSS (Cascading Style Sheets) is used to style and format the appearance of HTML elements on a web page.',
    'The box model in CSS defines how elements are displayed as rectangular boxes, including content, padding, borders, and margins.',
    'Responsive web design ensures that web pages adapt to different screen sizes and devices, providing an optimal user experience.',
    'Inline elements are displayed within the flow of text, block elements create new lines, and inline-block elements have block-like layout but inline behavior.',
    'JavaScript adds interactivity and dynamic behavior to web pages, allowing manipulation of content, animations, and interaction with users.',
    'The Document Object Model (DOM) represents the structure of a web page as objects, allowing scripts to modify and interact with the page content.',
    'Event handling in JavaScript involves responding to user actions, such as clicks or keyboard input, by executing specific code.',
    'Libraries and frameworks provide pre-written code and tools to simplify and speed up web development tasks.',
    'Common web development tools include text editors, integrated development environments (IDEs), version control systems, and browser developer tools.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=23, question=questions[i], answer=answers[i]))

    #set24

    questions = [
    'What is object-oriented programming (OOP) and why is it used?',
    'Explain the concepts of classes and objects in OOP.',
    'Describe the principle of encapsulation in OOP.',
    'What is inheritance and how does it promote code reuse?',
    'Explain the concept of polymorphism in OOP.',
    'Describe the difference between method overloading and method overriding.',
    'What is a constructor in OOP?',
    'Explain the purpose of access modifiers in OOP.',
    'Describe the SOLID principles in object-oriented design.',
    'What are some examples of programming languages that support OOP?'
]

    answers = [
    'Object-oriented programming (OOP) is a programming paradigm that organizes code around objects, data, and their interactions, promoting modularity and reusability.',
    'Classes define blueprints for objects, while objects are instances of classes that contain data (attributes) and behaviors (methods).',
    'Encapsulation involves bundling data and methods that operate on the data within a single unit (class), hiding internal details.',
    'Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass), enabling code reuse and creating hierarchies.',
    'Polymorphism allows objects of different classes to be treated as objects of a common superclass, enabling dynamic behavior and method overriding.',
    'Method overloading involves defining multiple methods with the same name but different parameters, while method overriding involves providing a new implementation of a method in a subclass.',
    'A constructor is a special method used to initialize objects when they are created, setting initial values for object attributes.',
    'Access modifiers control the visibility and accessibility of class members (attributes and methods), enhancing encapsulation and preventing unauthorized access.',
    'SOLID is an acronym for five principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) that guide object-oriented design.',
    'Examples of OOP-supporting programming languages include Java, C++, Python, C#, and Ruby.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=24, question=questions[i], answer=answers[i]))

    #set25

    questions = [
    'What is a database and why is it used?',
    'Describe the differences between relational and non-relational databases.',
    'Explain the purpose of database normalization.',
    'What is SQL and its role in database management?',
    'Describe the process of creating a table in a relational database.',
    'Explain the concept of primary keys and foreign keys.',
    'Describe the SELECT statement in SQL and its use.',
    'What are SQL joins and why are they important?',
    'Explain the differences between INNER JOIN, LEFT JOIN, and RIGHT JOIN.',
    'Describe the process of inserting, updating, and deleting data in a database.'
]

    answers = [
    'A database is a structured collection of data stored electronically, used to store, manage, and retrieve information efficiently.',
    'Relational databases use tables to store data with predefined schemas, while non-relational databases use various structures like documents, key-value pairs, or graphs.',
    'Database normalization is the process of organizing data to reduce redundancy and improve data integrity.',
    'SQL (Structured Query Language) is a domain-specific language used for managing and querying relational databases.',
    'Creating a table involves defining columns and their data types, constraints, and indexes.',
    'A primary key uniquely identifies records in a table, while foreign keys establish relationships between tables.',
    'The SELECT statement retrieves data from a database table based on specified criteria.',
    'SQL joins combine data from multiple tables based on related columns, enabling the retrieval of combined information.',
    'INNER JOIN returns matching rows from both tables, LEFT JOIN returns all rows from the left table and matching rows from the right table, and RIGHT JOIN returns all rows from the right table and matching rows from the left table.',
    'Data can be inserted into a database using INSERT, updated using UPDATE, and deleted using DELETE statements.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=25, question=questions[i], answer=answers[i]))

    #set26

    questions = [
    'What are software design patterns and why are they used?',
    'Explain the purpose of the Singleton design pattern.',
    'Describe the Observer design pattern and its use cases.',
    'What is the Model-View-Controller (MVC) design pattern?',
    'Explain the Factory Method design pattern.',
    'Describe the Decorator design pattern and its benefits.',
    'What is the Strategy design pattern?',
    'Explain the Adapter design pattern and its role.',
    'Describe the Command design pattern and its advantages.',
    'What are some common examples of creational, structural, and behavioral design patterns?'
]

    answers = [
    'Software design patterns are reusable solutions to common problems that arise during software design and development, promoting code modularity and maintainability.',
    'The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.',
    'The Observer pattern defines a one-to-many dependency between objects, where changes in one object trigger updates in other dependent objects.',
    'The Model-View-Controller (MVC) pattern separates an application into three components: Model (data and logic), View (presentation), and Controller (user input handling).',
    'The Factory Method pattern provides an interface for creating objects, allowing subclasses to determine the type of objects to be created.',
    'The Decorator pattern allows behavior to be added to individual objects, dynamically enhancing their functionality.',
    'The Strategy pattern defines a family of algorithms, encapsulating each algorithm separately and making them interchangeable.',
    'The Adapter pattern allows incompatible interfaces to work together by providing a wrapper that converts one interface into another.',
    'The Command pattern encapsulates a request as an object, allowing parameterization of clients with different requests and queuing of requests.',
    'Creational patterns include Singleton, Factory Method, and Abstract Factory. Structural patterns include Decorator, Adapter, and Proxy. Behavioral patterns include Observer, Strategy, and Command.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=26, question=questions[i], answer=answers[i]))

    #set27

    questions = [
    'What is backend development and its role in web applications?',
    'Explain the client-server architecture.',
    'Describe the role of a web server in backend development.',
    'What is an API (Application Programming Interface) and its use in backend development?',
    'Explain the difference between stateless and stateful communication in APIs.',
    'Describe the process of handling authentication and authorization in backend development.',
    'What is the role of a database in backend development?',
    'Explain the concept of routing in backend development.',
    'Describe the purpose of middleware in backend frameworks.',
    'What are some popular programming languages and frameworks for backend development?'
]

    answers = [
    'Backend development involves creating and managing the server-side components of web applications, handling data storage, processing, and interactions.',
    'Client-server architecture involves communication between a client (user interface) and a server (backend) over a network.',
    'A web server processes requests from clients and delivers responses, serving as the backend for web applications.',
    'An API is a set of rules and protocols that allow different software applications to communicate and interact with each other.',
    'Stateless communication does not store session data, while stateful communication retains session data between requests.',
    'Authentication verifies user identity, while authorization controls access to resources based on permissions.',
    'Databases store and manage structured data, providing persistence for web applications.',
    'Routing maps URLs to specific functions or actions in the backend, determining how requests are processed.',
    'Middleware provides functions that sit between the web framework and the application code, enabling various features and extensions.',
    'Popular backend programming languages include Python, Java, Node.js, Ruby, and PHP, with frameworks like Django, Spring Boot, Express, Ruby on Rails, and Laravel.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=27, question=questions[i], answer=answers[i]))

    #set28

    questions = [
    'What is a frontend framework and its purpose?',
    'Describe the core concepts of component-based architecture.',
    'Explain the virtual DOM and its role in optimizing frontend performance.',
    'What is React and what are its main features?',
    'Describe the key features of the Angular framework.',
    'Explain the concept of declarative rendering in frontend development.',
    'What is Vue.js and how does it differ from other frontend frameworks?',
    'Describe the process of state management in frontend frameworks.',
    'Explain the concept of props and state in React components.',
    'What are some advantages and disadvantages of using frontend frameworks?'
]

    answers = [
    'A frontend framework is a collection of tools and libraries that provides structure and standardization for building user interfaces.',
    'Component-based architecture involves breaking UIs into reusable, self-contained components, promoting modularity and maintainability.',
    'The virtual DOM is an abstract representation of the actual DOM, allowing efficient updates and minimizing re-renders for better performance.',
    'React is a JavaScript library for building user interfaces, known for its component-based approach, one-way data flow, and virtual DOM.',
    'Angular is a TypeScript-based framework for building dynamic web applications, offering features like two-way data binding, dependency injection, and modules.',
    'Declarative rendering involves describing the UI based on its state, allowing the framework to handle updates automatically.',
    'Vue.js is a progressive frontend framework that focuses on simplicity and flexibility, allowing developers to adopt its features incrementally.',
    'State management involves managing the data and state of a frontend application, often using tools like Redux, MobX, or Vuex.',
    'Props are read-only properties passed from parent to child components, while state represents mutable data within a component.',
    'Advantages of frontend frameworks include rapid development, code organization, and community support, while disadvantages include increased complexity and potential performance overhead.'
]

    for i in range(len(questions)):
       cards.append(Card(setId=28, question=questions[i], answer=answers[i]))

    #set29

    questions = [
    'What is Test-Driven Development (TDD) and why is it used?',
    'Describe the three stages of the TDD cycle.',
    'Explain the concept of writing tests before writing code in TDD.',
    'What are unit tests and why are they important in TDD?',
    'Describe the purpose of assertions in tests.',
    'Explain the role of test fixtures and setup/teardown methods.',
    'What is test coverage and why is it a useful metric?',
    'Describe the benefits of practicing TDD in software development.',
    'Explain the concept of "red-green-refactor" in TDD.',
    'What are some challenges and misconceptions about TDD?'
]

    answers = [
    'Test-Driven Development (TDD) is a software development practice where tests are written before code is implemented, promoting code quality, reliability, and maintainability.',
    'The TDD cycle consists of Red (write a failing test), Green (write the minimum code to pass the test), and Refactor (improve the code while maintaining passing tests).',
    'In TDD, tests are written before writing the corresponding functionality to ensure that the code meets the desired behavior.',
    'Unit tests are tests that focus on individual components or units of code, helping to catch bugs early and ensure correct behavior.',
    'Assertions are statements that check whether a specific condition is true, allowing tests to validate the expected behavior of the code.',
    'Test fixtures are pre-defined states or conditions that set up the environment for running tests, while setup and teardown methods initialize and clean up the test environment.',
    'Test coverage measures the proportion of code that is executed by tests, helping identify areas that may need more testing.',
    'TDD leads to more reliable and maintainable code, improved documentation, reduced bugs, and better-designed software.',
    'The "red-green-refactor" cycle refers to writing a failing test (red), writing code to pass the test (green), and then improving the code\'s structure and design (refactor).',
    'Challenges of TDD include a learning curve, time investment, and potential resistance, while misconceptions may include thinking TDD eliminates all bugs or slows down development significantly.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=29, question=questions[i], answer=answers[i]))

    #set30

    questions = [
    'What is Agile methodology and why is it used in software development?',
    'Describe the Agile Manifesto and its guiding principles.',
    'Explain the concept of iterative and incremental development in Agile.',
    'What are Scrum, Kanban, and XP, and how do they relate to Agile?',
    'Describe the roles of the Product Owner, Scrum Master, and Development Team in Scrum.',
    'Explain the purpose of Agile ceremonies like Sprint Planning and Daily Standups.',
    'What is a user story in Agile, and how is it used?',
    'Describe the concept of continuous integration and continuous delivery (CI/CD) in Agile development.',
    'Explain the importance of feedback and adaptation in Agile methodology.',
    'What are some benefits and challenges of implementing Agile in software development?'
]

    answers = [
    'Agile methodology is an iterative and incremental approach to software development that emphasizes collaboration, flexibility, customer feedback, and delivering value early.',
    'The Agile Manifesto is a set of four values (Individuals and interactions, Working software, Customer collaboration, Responding to change) and twelve principles that guide Agile development practices.',
    'Iterative development involves repeating cycles of planning, development, and testing, while incremental development adds new features in small increments.',
    'Scrum, Kanban, and XP (Extreme Programming) are popular Agile frameworks, each with its approach to managing work, roles, and processes.',
    'In Scrum, the Product Owner defines and prioritizes features, the Scrum Master facilitates the process, and the Development Team implements the work.',
    'Agile ceremonies like Sprint Planning, Daily Standups, Sprint Review, and Sprint Retrospective provide opportunities for collaboration, planning, and reflection.',
    'A user story is a brief description of a desired feature from the user\'s perspective, often written in the format "As a [user], I want [feature] so that [benefit]." User stories help prioritize and plan work.',
    'Continuous integration (CI) involves merging code changes frequently and automatically running tests, while continuous delivery (CD) ensures that code can be deployed to production at any time.',
    'Feedback and adaptation are central to Agile, allowing teams to gather insights from stakeholders and adjust the development process to meet changing requirements.',
    'Benefits of Agile include improved collaboration, customer satisfaction, and adaptability, while challenges may include managing expectations and ensuring consistent communication.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=30, question=questions[i], answer=answers[i]))

    #set31

    questions = [
    'What are birds of prey and their characteristics?',
    'Describe the difference between diurnal and nocturnal raptors.',
    'Explain the hunting techniques of eagles.',
    'What is unique about owls\' adaptations for night hunting?',
    'Describe the role of vultures in ecosystems.',
    'Explain the physical features that aid falcons in high-speed hunting.',
    'What are the primary food sources of hawks?',
    'Describe the hunting strategies of harriers.',
    'Explain the relationship between falcons and falconry.',
    'What are some conservation challenges faced by birds of prey?'
]

    answers = [
    'Birds of prey, also known as raptors, are carnivorous birds that hunt and feed on other animals. They often have sharp talons and strong beaks.',
    'Diurnal raptors are active during the day, while nocturnal raptors are active at night. Diurnal raptors include eagles, hawks, and falcons, while owls are nocturnal.',
    'Eagles use keen eyesight to locate prey from great heights, then swoop down to capture it with their talons.',
    'Owls have excellent night vision and silent flight, allowing them to hunt effectively in darkness. Their facial disc helps funnel sound to their ears.',
    'Vultures play a crucial role in scavenging and cleaning up carcasses, preventing the spread of diseases.',
    'Falcon adaptations include streamlined bodies, powerful wings, and specialized air sacs that enable rapid dives and high-speed pursuits.',
    'Hawks feed on a variety of small mammals, birds, and insects, using their keen vision to locate prey from perches or while soaring.',
    'Harriers are known for their low, gliding flight over open areas, using their keen eyesight to spot small mammals and birds in the grass.',
    'Falconry is a hunting method that involves training falcons to hunt alongside humans, showcasing the raptors\' natural hunting abilities.',
    'Conservation challenges for birds of prey include habitat loss, pesticide exposure, illegal hunting, and collisions with man-made structures.'
]

    for i in range(len(questions)):
       cards.append(Card(setId=31, question=questions[i], answer=answers[i]))

    #set32

    questions = [
    'What are songbirds and why are they called songbirds?',
    'Describe the unique vocalizations of the mockingbird.',
    'Explain the melodious song of the nightingale.',
    'What is the role of the canary in music and culture?',
    'Describe the appearance and song of the American robin.',
    'Explain the song-learning process of songbirds.',
    'What are some examples of songbirds that are known for their mimicry?',
    'Describe the vibrant plumage and song of the Northern cardinal.',
    'Explain the purpose of song in the lives of songbirds.',
    'What are some conservation efforts to protect songbird populations?'
]

    answers = [
    'Songbirds are a diverse group of birds known for their complex and melodious vocalizations. They are called songbirds due to their singing abilities.',
    'The mockingbird is known for its ability to mimic the sounds of other birds and even mechanical noises.',
    'The nightingale is renowned for its beautiful and intricate song, often associated with poetry and literature.',
    'Canaries have been kept as pets and bred for their singing abilities, contributing to music and cultural traditions.',
    'The American robin has a distinct red breast and sings a cheerful song that signals the arrival of spring.',
    'Songbirds learn their songs through a process involving listening, memorization, and imitation during a critical period in their development.',
    'Examples of songbirds that mimic other sounds include the Northern mockingbird, European starling, and superb lyrebird.',
    'The Northern cardinal is known for its bright red plumage and clear, whistling song that varies in different regions.',
    'Song plays a crucial role in attracting mates, defending territory, and communicating with other birds.',
    'Conservation efforts to protect songbirds include habitat preservation, reducing pesticide use, and raising awareness about the importance of their role in ecosystems.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=32, question=questions[i], answer=answers[i]))

    #set33

    questions = [
    'What are waterfowl and their characteristics?',
    'Describe the differences between ducks, geese, and swans.',
    'Explain the purpose of webbed feet in waterfowl.',
    'What are some unique adaptations of diving ducks?',
    'Describe the migration patterns of waterfowl.',
    'Explain the concept of dabbling behavior in ducks.',
    'What is the role of down feathers in waterfowl?',
    'Describe the vocalizations of Canada geese.',
    'Explain the nesting habits of waterfowl.',
    'What are some conservation challenges faced by waterfowl populations?'
]

    answers = [
    'Waterfowl are birds that inhabit wetlands and bodies of water, including ducks, geese, and swans. They have waterproof feathers and specialized bills.',
    'Ducks, geese, and swans are all waterfowl, but they differ in size, shape, plumage, and behavior. Ducks are typically smaller and have broad bills, while geese are larger with long necks, and swans are graceful with long necks and elegant posture.',
    'Webbed feet provide waterfowl with efficient propulsion in water, enabling them to swim and dive.',
    'Diving ducks have adaptations like dense bones, air sacs, and specialized feathers that allow them to dive for food underwater.',
    'Waterfowl engage in migratory behavior, often traveling long distances between breeding and wintering grounds.',
    'Dabbling behavior involves ducks tipping forward in the water to feed on aquatic vegetation and invertebrates.',
    'Down feathers provide insulation and buoyancy to waterfowl, helping them stay warm and afloat.',
    'Canada geese communicate with honking calls, often flying in a distinctive V-shaped formation during migration.',
    'Waterfowl build nests near water using materials like reeds, grass, and down feathers. Some species nest in tree cavities.',
    'Conservation challenges for waterfowl include habitat loss, pollution, hunting, and collisions with power lines or buildings.'
]

    for i in range(len(questions)):
       cards.append(Card(setId=33, question=questions[i], answer=answers[i]))

    #set34

    questions = [
    'What are tropical birds and which regions do they inhabit?',
    'Describe the vibrant plumage of the Scarlet Macaw.',
    'Explain the unique courtship dance of the Red-capped Manakin.',
    'What is the significance of the Keel-billed Toucan\'s colorful bill?',
    'Describe the adaptation of the Blue-crowned Motmot\'s tail feathers.',
    'Explain the role of the Eclectus Parrot in tropical ecosystems.',
    'What is the life cycle of a hummingbird, and how do they feed?',
    'Describe the vocalizations of the Sulphur-crested Cockatoo.',
    'Explain the symbiotic relationship between birds of paradise and their environment.',
    'What are some conservation efforts to protect tropical bird species?'
]

    answers = [
    'Tropical birds inhabit equatorial and subtropical regions characterized by warm and humid climates, such as rainforests and tropical islands.',
    'The Scarlet Macaw has brilliant red, blue, and yellow plumage, making it a sought-after species in the pet trade.',
    'The Red-capped Manakin performs elaborate courtship dances involving leaps, flips, and rapid wing movements to attract females.',
    'The Keel-billed Toucan\'s bill is large, colorful, and lightweight, aiding in thermoregulation and attracting mates.',
    'The Blue-crowned Motmot has long tail feathers with distinctive "raquet" tips, used for communication and display.',
    'The Eclectus Parrot feeds on a variety of fruits, helping to disperse seeds and promote forest regeneration.',
    'Hummingbirds have a short life cycle, with rapid growth and development. They feed on nectar using their specialized long bills and extendable tongues.',
    'The Sulphur-crested Cockatoo is known for its loud screeching calls, used for communication and social bonding.',
    'Birds of paradise have evolved intricate plumage and courtship displays to attract mates, contributing to the biodiversity of tropical ecosystems.',
    'Conservation efforts include habitat protection, anti-poaching measures, and raising awareness about the importance of tropical bird species.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=34, question=questions[i], answer=answers[i]))

    #set35

    questions = [
    'What are flightless birds and what led to their inability to fly?',
    'Describe the characteristics of the ostrich, the world\'s largest flightless bird.',
    'Explain the adaptations of the kiwi for a nocturnal and ground-dwelling lifestyle.',
    'What is the role of the cassowary in its rainforest ecosystem?',
    'Describe the unique appearance of the emu and its habitat.',
    'Explain the reasons for the extinction of the Great Auk, a flightless bird from the Northern Hemisphere.',
    'What are the threats to the survival of the flightless kakapo?',
    'Describe the physical features of the Rhea, a flightless bird native to South America.',
    'Explain the conservation efforts to protect the flightless kakapo.',
    'What are some examples of other flightless birds and their adaptations?'
]

    answers = [
    'Flightless birds are species that have lost the ability to fly due to evolutionary adaptations and changes in their habitat. The loss of flight often resulted from the absence of predators or the availability of abundant food on the ground.',
    'The ostrich is the largest flightless bird and has long legs, a long neck, and two-toed feet. It is a fast runner and uses its wings for balance.',
    'The kiwi is adapted for a nocturnal lifestyle with a keen sense of smell and long, slender bill for probing in the ground for insects and worms.',
    'The cassowary is a large, colorful flightless bird that plays a role in seed dispersal in rainforests. It has powerful legs and a casque on its head.',
    'The emu has a brownish-black plumage and a bare neck. It is native to Australia and is well-adapted to running and foraging for food.',
    'The Great Auk, a flightless bird from the Northern Hemisphere, was hunted for its feathers, eggs, and meat, leading to its extinction in the mid-19th century.',
    'The flightless kakapo, a parrot from New Zealand, faces threats from habitat loss, predators, and low reproductive rates.',
    'The Rhea has a long neck, strong legs, and a large body. It is capable of running at high speeds and is found in grasslands and shrublands.',
    'Conservation efforts for the kakapo include predator control, habitat restoration, and a recovery program involving intensive management.',
    'Other flightless birds include the takahe, the weka, and the moa, each with unique adaptations suited to their respective environments.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=35, question=questions[i], answer=answers[i]))

    #set36

    questions = [
    'What are migratory birds and why do they undertake long journeys?',
    'Describe the migration of the Arctic Tern, known for its incredible annual migration.',
    'Explain the phenomenon of bird migration and navigation.',
    'What is the importance of stopover sites for migratory birds?',
    'Describe the migration routes of the Sandhill Crane.',
    'Explain the concept of flyways and how they influence bird migration.',
    'What are some challenges faced by migratory birds during their journeys?',
    'Describe the role of photoperiod and environmental cues in triggering bird migration.',
    'Explain the concept of leapfrog migration in bird populations.',
    'What are some conservation efforts to protect migratory birds and their habitats?'
]

    answers = [
    'Migratory birds are species that travel long distances between their breeding and wintering grounds in search of suitable habitats and food sources. They migrate to take advantage of seasonal resources and avoid harsh conditions.',
    'The Arctic Tern migrates between the Arctic and Antarctic regions, covering a distance of up to 44,000 miles (70,900 kilometers) in a year.',
    'Birds use a variety of cues, including celestial landmarks, Earth\'s magnetic field, and visual landmarks, to navigate during migration. Sun compass orientation and star navigation are common strategies.',
    'Stopover sites are crucial resting points where migratory birds refuel and rest during their journeys. These sites provide necessary resources for energy replenishment.',
    'The Sandhill Crane migrates along the Central and Mississippi Flyways in North America, moving between breeding areas in northern regions and wintering sites in the southern United States.',
    'Flyways are specific migration routes that birds follow, often along coastlines, mountain ranges, or river valleys. They guide birds during their journeys and connect breeding and wintering habitats.',
    'Migratory birds face challenges such as habitat loss, climate change, hunting, pollution, collisions with buildings, and predation during their journeys.',
    'Photoperiod (day length) and environmental cues like temperature changes trigger hormonal responses in birds, signaling the need to migrate.',
    'Leapfrog migration occurs when populations of migratory birds from higher latitudes "leapfrog" over populations from lower latitudes during migration, allowing for reduced competition for resources.',
    'Conservation efforts include protecting critical stopover sites, creating migratory corridors, reducing habitat destruction, and advocating for international cooperation to safeguard migratory routes.'
]

    for i in range(len(questions)):
       cards.append(Card(setId=36, question=questions[i], answer=answers[i]))

    #set37

    questions = [
    'What are the main parts of a bird\'s body?',
    'Describe the functions of a bird\'s feathers.',
    'Explain the purpose of a bird\'s beak or bill.',
    'What are the functions of a bird\'s wings and tail?',
    'Describe the unique anatomy of a bird\'s respiratory system.',
    'Explain how a bird\'s digestive system is adapted for its diet.',
    'What is the function of a bird\'s crop and gizzard?',
    'Describe the specialized feet and claws of different bird species.',
    'Explain the structure and function of a bird\'s syrinx.',
    'What are some adaptations of flightless birds in terms of anatomy?'
]

    answers = [
    'Key parts of a bird\'s body include the head, neck, wings, tail, legs, and feet.',
    'Feathers serve multiple functions, including insulation, camouflage, flight, and display.',
    'A bird\'s beak or bill is adapted for specific feeding habits, such as cracking seeds, probing for insects, or catching fish.',
    'Wings provide lift and propulsion for flight, while the tail helps with balance and steering.',
    'Birds have a unique respiratory system with air sacs that allow for a continuous flow of oxygen, aiding efficient gas exchange during both inhalation and exhalation.',
    'A bird\'s digestive system includes specialized organs like the proventriculus (stomach) and gizzard (grinding organ), as well as a one-way digestive flow to maximize nutrient absorption.',
    'The crop stores and softens food before digestion, while the gizzard grinds food with the help of swallowed stones.',
    'Bird feet vary in structure and function, from the perching feet of songbirds to the webbed feet of waterfowl and the strong talons of raptors.',
    'The syrinx is the avian vocal organ located at the base of the trachea, allowing birds to produce a wide range of sounds and calls.',
    'Flightless birds, such as ostriches and penguins, have modified anatomy that reflects their reliance on running or swimming rather than flying.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=37, question=questions[i], answer=answers[i]))

    #set38

    questions = [
    'What does it mean for a bird species to be endangered?',
    'Describe the factors that contribute to the endangerment of bird species.',
    'Explain the concept of habitat loss and its impact on bird populations.',
    'What role do invasive species play in the endangerment of native bird species?',
    'Describe the challenges faced by migratory birds during their long journeys.',
    'Explain the impact of pollution on bird populations.',
    'What is the illegal wildlife trade and how does it affect endangered bird species?',
    'Describe conservation efforts to protect the California Condor, an endangered bird species.',
    'Explain the importance of captive breeding programs for endangered birds.',
    'What are some success stories of bird species that have been brought back from the brink of extinction?'
]

    answers = [
    'An endangered bird species is one that is at risk of extinction in the near future due to declining population numbers and threats to its survival.',
    'Factors contributing to endangerment include habitat destruction, pollution, climate change, hunting, and competition with invasive species.',
    'Habitat loss occurs when natural environments are destroyed or altered, leading to reduced resources and suitable nesting sites for birds.',
    'Invasive species can outcompete native birds for resources, introduce new diseases, and disrupt ecosystems.',
    'Migratory birds face threats along their migration routes, including habitat loss, hunting, and collisions with buildings or power lines.',
    'Pollution from sources like pesticides, plastics, and oil spills can harm birds through contamination of food sources and habitat.',
    'Illegal wildlife trade involves the capture and sale of protected bird species for profit, leading to population decline and further endangerment.',
    'Conservation efforts for the California Condor include captive breeding, habitat protection, and ongoing monitoring of released individuals.',
    'Captive breeding programs help increase the population of endangered birds and provide a potential source for reintroduction into the wild.',
    'Success stories include the recovery of the Bald Eagle and the Whooping Crane through conservation efforts, habitat restoration, and legal protection.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=38, question=questions[i], answer=answers[i]))

    #set39

    questions = [
    'Which birds are commonly associated with myths and legends?',
    'Describe the role of the Phoenix in various cultural mythologies.',
    'Explain the symbolism of the Raven in different cultures.',
    'What significance do owls hold in mythology and folklore?',
    'Describe the story of Icarus and the symbolism of his wings.',
    'Explain the role of the Peacock in ancient Greek and Hindu mythologies.',
    'What myths or stories feature the Thunderbird?',
    'Describe the connection between the Garuda and Hindu mythology.',
    'Explain the cultural significance of the Crane in Asian traditions.',
    'What are some common themes and lessons found in bird-related myths?'
]

    answers = [
    'Birds such as eagles, ravens, owls, and peacocks are often featured in myths and legends from various cultures.',
    'The Phoenix is a mythical bird associated with rebirth and immortality. It is said to be consumed by flames and later rises from its own ashes.',
    'In different cultures, the Raven can symbolize wisdom, magic, or transformation. In Norse mythology, Odin had two ravens that brought him knowledge.',
    'Owls are often associated with wisdom and foresight. In some cultures, they are seen as omens, while in others, they are revered for their nocturnal prowess.',
    'The story of Icarus involves a young man who flew too close to the sun with wings made of feathers and wax. It serves as a cautionary tale against hubris.',
    'The Peacock is a symbol of beauty and immortality in ancient Greek mythology. In Hinduism, it is associated with deities like Lakshmi and Saraswati.',
    'The Thunderbird is a powerful creature in the mythology of various Indigenous peoples in North America. It is often associated with thunder and lightning.',
    'Garuda is a bird-like creature in Hindu mythology, often depicted as the mount of the god Vishnu. It symbolizes power and protection.',
    'The Crane is a symbol of longevity, happiness, and loyalty in Asian cultures, particularly in China and Japan.',
    'Common themes include transformation, rebirth, wisdom, and the relationship between humans and the natural world. Myths involving birds often convey moral lessons.'
]

    for i in range(len(questions)):
       cards.append(Card(setId=39, question=questions[i], answer=answers[i]))

    #set40

    questions = [
    'What are the essential tools for bird watching?',
    'Explain the importance of field guides and binoculars in bird watching.',
    'Describe how to choose a suitable spotting location for bird watching.',
    'What are some common bird behaviors to observe?',
    'Explain the technique of "pishing" to attract birds.',
    'What is the role of patience and stillness in successful bird watching?',
    'Describe the difference between songbirds and raptors in terms of identification.',
    'Explain the concept of bird migration and its impact on bird watching.',
    'What are some ethical considerations for bird watchers?',
    'How can technology, such as birding apps, enhance the bird watching experience?'
]

    answers = [
    'Essential tools include binoculars, field guides, a notebook, and a smartphone or camera.',
    'Field guides provide information about bird species, while binoculars help you observe birds from a distance.',
    'Choose locations with diverse habitats, such as forests, wetlands, or grasslands, to increase the variety of bird species you can observe.',
    'Observe behaviors like feeding, nesting, mating displays, and interactions with other birds.',
    'Pishing involves making high-pitched sounds to mimic distress calls, attracting curious birds for observation.',
    'Patience and stillness are key to avoiding scaring away birds and allowing them to become comfortable in your presence.',
    'Songbirds are typically smaller, have melodious calls, and are often found in trees, while raptors are larger birds of prey with sharp talons and beaks.',
    'Bird migration involves seasonal movements between breeding and wintering grounds, allowing for opportunities to observe different species.',
    'Ethical considerations include avoiding disturbance to nesting birds, respecting habitats, and adhering to birding codes of conduct.',
    'Birding apps provide instant access to bird calls, identification guides, and maps, enhancing the ability to identify and learn about birds.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=40, question=questions[i], answer=answers[i]))

    #set41

    questions = [
    'What factors contribute to the diversity of global cuisines?',
    'Describe the culinary traditions of Mediterranean cuisine.',
    'Explain the key ingredients and dishes in Japanese cuisine.',
    'What are the unique flavors and techniques of Indian cuisine?',
    'Describe the characteristics of Mexican cuisine.',
    'Explain the concept of fusion cuisine and give an example.',
    'What are the staple foods and flavors of Thai cuisine?',
    'Describe the use of spices in Middle Eastern cuisine.',
    'Explain the influence of French cuisine on culinary traditions worldwide.',
    'What are some traditional cooking methods and utensils used in different cuisines?'
]

    answers = [
    'Diversity in global cuisines is influenced by geography, climate, culture, historical trade routes, and available ingredients.',
    'Mediterranean cuisine emphasizes fresh ingredients, olive oil, whole grains, fruits, vegetables, and lean proteins like fish and legumes.',
    'Japanese cuisine features ingredients like rice, fish, seaweed, soybeans, and flavors such as umami. Sushi, sashimi, and tempura are popular dishes.',
    'Indian cuisine is known for its use of spices, herbs, and complex flavors. Dishes like curry, biryani, and masala are staples.',
    'Mexican cuisine combines indigenous ingredients like corn, beans, and chili peppers with Spanish influences, resulting in dishes like tacos and mole.',
    'Fusion cuisine blends ingredients and techniques from different culinary traditions. An example is the combination of Japanese and Peruvian flavors in "Nikkei" cuisine.',
    'Thai cuisine features a balance of sweet, sour, spicy, and salty flavors. Staple ingredients include rice, fish sauce, lime, and chili peppers.',
    'Middle Eastern cuisine uses spices like cumin, coriander, and saffron to create rich and aromatic dishes. Hummus, falafel, and kebabs are common.',
    'French cuisine has had a significant impact on global culinary traditions, influencing techniques, sauces, and cooking methods.',
    'Traditional cooking methods include grilling, steaming, stir-frying, and baking. Utensils like woks, tandoors, and tagines are used in various cuisines.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=41, question=questions[i], answer=answers[i]))

    #set42

    questions = [
    'What are the principles of a balanced and nutritious diet?',
    'Describe the importance of consuming a variety of fruits and vegetables.',
    'Explain the role of whole grains in a healthy diet.',
    'What are sources of lean protein and their benefits?',
    'Describe the significance of healthy fats in the diet.',
    'Explain the importance of staying hydrated and its impact on overall health.',
    'What are some ways to reduce added sugars in the diet?',
    'Describe portion control and its role in maintaining a healthy weight.',
    'Explain the concept of mindful eating and its benefits.',
    'What are some tips for making healthier choices when dining out?'
]

    answers = [
    'A balanced diet includes a variety of foods from all food groups, including fruits, vegetables, whole grains, lean proteins, and healthy fats.',
    'Fruits and vegetables provide essential vitamins, minerals, and antioxidants that support overall health and reduce the risk of chronic diseases.',
    'Whole grains are rich in fiber, vitamins, and minerals. They help maintain stable blood sugar levels and promote digestive health.',
    'Sources of lean protein include poultry, fish, beans, legumes, and tofu. Lean protein supports muscle growth and repair.',
    'Healthy fats, such as those found in avocados, nuts, and olive oil, are essential for brain health, hormone production, and absorption of fat-soluble vitamins.',
    'Staying hydrated is vital for digestion, circulation, temperature regulation, and overall bodily functions.',
    'Reducing added sugars involves choosing whole fruits over sugary snacks, reading nutrition labels, and being mindful of hidden sugars in processed foods.',
    'Portion control helps manage calorie intake and maintain a healthy weight. It involves being mindful of portion sizes and listening to hunger cues.',
    'Mindful eating involves paying attention to the sensory experience of eating and recognizing hunger and fullness cues. It can promote healthier eating habits.',
    'When dining out, opt for grilled or steamed dishes, choose smaller portion sizes, and prioritize vegetables and lean protein. Limit sugary drinks and desserts.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=42, question=questions[i], answer=answers[i]))

    #set43

    questions = [
    'What are the basic ingredients for baking?',
    'Explain the role of flour in baking.',
    'Describe the purpose of baking powder and baking soda.',
    'What is the function of eggs in baking?',
    'Explain the importance of fats (butter, oil) in baked goods.',
    'Describe the role of sugar in baking.',
    'What is the purpose of leavening agents in baking?',
    'Explain the difference between natural and Dutch-processed cocoa powder.',
    'Describe the function of salt in baked goods.',
    'What is the significance of proper measurement in baking?'
]

    answers = [
    'Basic ingredients include flour, sugar, eggs, fat (butter or oil), leavening agents, and flavorings.',
    'Flour provides structure, texture, and thickness to baked goods.',
    'Baking powder and baking soda are leavening agents that help dough and batter rise, resulting in a light and airy texture.',
    'Eggs contribute moisture, binding, and structure to baked goods. They also add richness and flavor.',
    'Fats add moisture, tenderness, and flavor to baked goods. They also help with browning and texture.',
    'Sugar adds sweetness, flavor, and tenderness. It also helps retain moisture and contributes to browning.',
    'Leavening agents, like yeast, baking powder, and baking soda, release carbon dioxide gas, causing dough and batter to rise.',
    'Natural cocoa powder is acidic and adds a deep chocolate flavor, while Dutch-processed cocoa powder is alkalized and produces a milder taste.',
    'Salt enhances flavor and balances sweetness, while also controlling yeast fermentation and strengthening dough structure.',
    'Proper measurement ensures accurate ratios of ingredients, which is crucial for achieving consistent and successful baking results.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=43, question=questions[i], answer=answers[i]))

    #set44

    questions = [
    'What are some examples of exotic fruits?',
    'Describe the appearance and flavor of dragon fruit.',
    'Explain the unique characteristics of jackfruit.',
    'What is the taste and texture of durian?',
    'Describe the appearance and taste of lychee.',
    'Explain the health benefits of acai berries.',
    'What is the significance of mangosteen in Southeast Asian cuisine?',
    'Describe the flavor profile of passion fruit.',
    'Explain the uses of papaya in culinary applications.',
    'What are some ways to enjoy exotic fruits in desserts and beverages?'
]

    answers = [
    'Exotic fruits include dragon fruit, jackfruit, durian, lychee, acai berries, mangosteen, passion fruit, and papaya, among others.',
    'Dragon fruit has vibrant pink or yellow skin with white or red flesh speckled with black seeds. It has a mildly sweet and refreshing flavor.',
    'Jackfruit is large and spiky with fibrous yellow flesh that resembles pulled pork. It has a mild, slightly sweet flavor and is often used in savory dishes.',
    'Durian is known for its strong odor and divisive taste. It has a custard-like texture and a complex flavor profile that can range from sweet to savory.',
    'Lychee has a rough, pinkish-red shell with translucent white flesh. It has a fragrant, floral aroma and a sweet and juicy taste.',
    'Acai berries are rich in antioxidants, fiber, and healthy fats. They are associated with benefits for heart health and immune support.',
    'Mangosteen is prized for its sweet and tangy flavor. It is often referred to as the "queen of fruits" and is used in jams, juices, and desserts.',
    'Passion fruit has a wrinkled outer shell and a gelatinous interior filled with seeds. It has a tart and tropical flavor with floral undertones.',
    'Papaya is orange or pink with orange flesh and black seeds. It has a sweet and slightly musky flavor and is used in both sweet and savory dishes.',
    'Exotic fruits can be enjoyed fresh, in fruit salads, smoothies, sorbets, parfaits, and cocktails, adding unique flavors and textures to culinary creations.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=44, question=questions[i], answer=answers[i]))

    #set45

    questions = [
    'What are some examples of comfort food dishes?',
    'Describe the ingredients and preparation of macaroni and cheese.',
    'Explain the process of making a hearty chicken pot pie.',
    'What is the origin and significance of meatloaf in American cuisine?',
    'Describe the ingredients and flavors of mashed potatoes and gravy.',
    'Explain the components of a classic grilled cheese sandwich.',
    'What are the key ingredients in a bowl of creamy tomato soup?',
    'Describe the layers and flavors of a traditional lasagna.',
    'Explain the appeal of warm and gooey chocolate chip cookies.',
    'What are some cultural variations of rice pudding as a comfort dessert?'
]

    answers = [
    'Comfort food dishes include macaroni and cheese, chicken pot pie, meatloaf, mashed potatoes and gravy, grilled cheese sandwich, tomato soup, lasagna, and chocolate chip cookies.',
    'Macaroni and cheese is made with cooked macaroni pasta and a creamy cheese sauce, often made from cheddar or a combination of cheeses.',
    'Chicken pot pie consists of a flaky crust filled with chunks of cooked chicken, vegetables, and a savory sauce.',
    'Meatloaf is a ground meat mixture, often beef, combined with breadcrumbs, onions, and seasonings, baked in a loaf shape.',
    'Mashed potatoes are made by boiling and mashing potatoes with butter and milk, served with savory gravy made from pan drippings.',
    'A classic grilled cheese sandwich is made with slices of bread and melted cheese, often served with tomato soup for dipping.',
    'Creamy tomato soup is typically made with tomatoes, broth, onions, and cream. It has a smooth texture and tangy tomato flavor.',
    'Lasagna consists of layers of wide pasta sheets, ricotta cheese, tomato sauce, and mozzarella cheese, baked until bubbly and golden.',
    'Warm chocolate chip cookies are loved for their soft, chewy, and chocolatey goodness, often enjoyed fresh from the oven.',
    'Rice pudding is enjoyed in various cultures, such as arroz con leche in Latin America, kheer in India, and riz au lait in France, each with unique flavors and spices.'
]

    for i in range(len(questions)):
       cards.append(Card(setId=45, question=questions[i], answer=answers[i]))

    #set46

    questions = [
    'What is sautéing and how is it done?',
    'Describe the process of roasting in cooking.',
    'Explain the difference between boiling and simmering.',
    'What is blanching and how is it used in cooking?',
    'Describe the technique of braising.',
    'Explain the concept of deglazing and its purpose.',
    'What is the Maillard reaction and how does it enhance flavor?',
    'Describe the process of grilling and its benefits.',
    'Explain the technique of poaching and give an example.',
    'What are the principles of sous vide cooking?'
]

    answers = [
    'Sautéing involves cooking food quickly in a small amount of oil over high heat, with constant stirring or tossing.',
    'Roasting is cooking food in an oven, often at a higher temperature, to achieve browning and caramelization.',
    'Boiling involves cooking food in boiling water, while simmering is cooking food gently in water just below the boiling point.',
    'Blanching is briefly boiling food and then immediately cooling it in ice water to preserve color and texture.',
    'Braising is cooking food first by searing, then slow-cooking it in a flavorful liquid until tender.',
    'Deglazing involves adding liquid to a hot pan to release browned bits stuck to the bottom, creating a flavorful sauce.',
    'The Maillard reaction is a chemical reaction between amino acids and reducing sugars, creating the browning and savory flavors in cooked food.',
    'Grilling involves cooking food over an open flame or heat source, creating char marks and smoky flavors.',
    'Poaching is cooking food gently in liquid just below the boiling point, as seen in poached eggs or chicken.',
    'Sous vide cooking involves vacuum-sealing food in a plastic pouch and cooking it in a water bath at a precise temperature for consistent results.'
]

    for i in range(len(questions)):
       cards.append(Card(setId=46, question=questions[i], answer=answers[i]))

    #set47

    questions = [
    'What are spices and herbs?',
    'Describe the flavor profile of cinnamon.',
    'Explain the uses of cumin in various cuisines.',
    'What is the origin and significance of turmeric?',
    'Describe the taste and aroma of basil.',
    'Explain the role of coriander in cooking.',
    'What are the properties of paprika and its variations?',
    'Describe the uses of thyme in culinary applications.',
    'Explain the importance of saffron and its role in dishes.',
    'What are some popular spice blends from different cultures?'
]

    answers = [
    'Spices are dried seeds, roots, fruits, bark, or plant parts that add flavor and aroma to dishes. Herbs are fresh or dried leaves of plants, often used for seasoning.',
    'Cinnamon has a warm and sweet flavor with hints of spice and citrus. It is used in both sweet and savory dishes.',
    'Cumin has a nutty, earthy, and slightly spicy flavor. It is a staple in cuisines like Indian, Mexican, and Middle Eastern.',
    'Turmeric is a golden-colored spice with an earthy, bitter, and slightly peppery taste. It is a key ingredient in curry powders and has medicinal properties.',
    'Basil has a sweet, aromatic, and slightly peppery flavor with hints of anise and clove. It is commonly used in Mediterranean and Italian cuisines.',
    'Coriander has a citrusy, slightly sweet flavor with earthy undertones. Both the seeds and leaves (cilantro) are used in cooking.',
    'Paprika comes in sweet, smoked, and hot varieties. It adds color and mild heat to dishes, especially in Spanish and Hungarian cuisines.',
    'Thyme has a savory, earthy flavor with hints of lemon and mint. It is used in a variety of dishes, including soups, stews, and roasts.',
    'Saffron is a prized spice known for its vibrant color and subtle floral aroma. It is used to add flavor and color to dishes like paella and risotto.',
    'Examples of spice blends include garam masala (Indian), za\'atar (Middle Eastern), and five-spice powder (Chinese), each adding complexity to dishes.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=47, question=questions[i], answer=answers[i]))

    #set48

    questions = [
    'What are some popular international desserts?',
    'Describe the ingredients and preparation of tiramisu.',
    'Explain the process of making crème brûlée.',
    'What is the origin and significance of baklava?',
    'Describe the layers and flavors of a classic Black Forest cake.',
    'Explain the difference between gelato and ice cream.',
    'What are the ingredients and texture of panna cotta?',
    'Describe the characteristics of churros and their popular accompaniments.',
    'Explain the technique of making macarons.',
    'What are some creative ways to garnish and present desserts?'
]

    answers = [
    'Popular international desserts include tiramisu, crème brûlée, baklava, Black Forest cake, gelato, panna cotta, churros, and macarons.',
    'Tiramisu is made with layers of coffee-soaked ladyfingers and mascarpone cheese, dusted with cocoa powder.',
    'Crème brûlée is a creamy custard topped with a layer of caramelized sugar, achieved by using a culinary torch.',
    'Baklava is a sweet pastry made of layers of filo dough, nuts, and honey or syrup, with origins in the Middle East and Mediterranean.',
    'A Black Forest cake features layers of chocolate sponge cake, whipped cream, and cherries, often garnished with chocolate shavings.',
    'Gelato has less fat and air than ice cream, resulting in a denser and creamier texture. It is churned at a slower speed.',
    'Panna cotta is a creamy Italian dessert made with sweetened cream, milk, and gelatin, often served with fruit compote or sauce.',
    'Churros are deep-fried dough pastries, usually rolled in cinnamon sugar and served with chocolate or caramel dipping sauces.',
    'Macarons are delicate French meringue cookies with a crisp exterior and soft interior, sandwiching various flavored fillings.',
    'Creative garnishes include edible flowers, chocolate drizzles, fruit coulis, whipped cream, and artistic plating to enhance dessert presentation.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=48, question=questions[i], answer=answers[i]))

    #set49

    questions = [
    'What are some common plant-based protein sources?',
    'Describe the ingredients and preparation of a quinoa salad.',
    'Explain the process of making a hearty vegetable stir-fry.',
    'What is the origin and significance of tofu in vegetarian cuisine?',
    'Describe the taste and texture of a chickpea curry.',
    'Explain the use of nutritional yeast in plant-based cooking.',
    'What are the benefits of incorporating more whole grains into a plant-based diet?',
    'Describe the layers and flavors of a vegan lasagna.',
    'Explain the technique of substituting dairy in plant-based baking.',
    'What are some creative ways to enhance the flavor of plant-based dishes?'
]

    answers = [
    'Common plant-based protein sources include legumes (beans, lentils, chickpeas), tofu, tempeh, quinoa, nuts, seeds, and seitan.',
    'Quinoa salad is made with cooked quinoa, vegetables, herbs, and a tangy vinaigrette. It can be customized with various ingredients.',
    'Vegetable stir-fry involves quickly cooking a variety of vegetables in a hot pan with oil and soy sauce or other seasonings.',
    'Tofu, made from soybeans, is a versatile meat substitute in vegetarian and vegan dishes. It can be marinated, grilled, stir-fried, or used in soups.',
    'Chickpea curry features chickpeas cooked in a flavorful sauce made from tomatoes, onions, spices, and coconut milk. It has a hearty and rich taste.',
    'Nutritional yeast is a deactivated yeast with a cheesy, nutty flavor. It is often used to add umami and a cheesy taste to plant-based dishes.',
    'Whole grains like brown rice, quinoa, and whole wheat provide fiber, vitamins, and minerals, promoting digestive health and sustained energy.',
    'Vegan lasagna includes layers of lasagna noodles, plant-based cheese, tomato sauce, and layers of vegetables like spinach and zucchini.',
    'Dairy can be replaced with plant-based alternatives like almond milk, coconut yogurt, and cashew cream in recipes like cakes and muffins.',
    'Enhance flavor by using fresh herbs, aromatic spices, umami-rich ingredients (soy sauce, miso), citrus juices, and roasted vegetables.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=49, question=questions[i], answer=answers[i]))

    #set50

    questions = [
    'What are some examples of gourmet ingredients?',
    'Describe the flavor profile and uses of truffle oil.',
    'Explain the significance of saffron in upscale cooking.',
    'What is the origin and culinary importance of foie gras?',
    'Describe the texture and taste of caviar.',
    'Explain the use of edible gold leaf in gourmet cuisine.',
    'What are the characteristics of aged balsamic vinegar?',
    'Describe the flavor and aroma of vanilla bean.',
    'Explain the appeal of Kobe beef and its marbling.',
    'What are some luxurious desserts often made with gourmet ingredients?'
]

    answers = [
    'Gourmet ingredients include truffle oil, saffron, foie gras, caviar, edible gold leaf, aged balsamic vinegar, vanilla bean, Kobe beef, and more.',
    'Truffle oil is infused with truffle essence and has a strong, earthy flavor. It is used to add truffle aroma and taste to dishes.',
    'Saffron is a prized spice with a unique flavor and vibrant color. It is used sparingly in dishes like risotto and paella.',
    'Foie gras is a fattened duck or goose liver, considered a delicacy in French cuisine. It is often used in pâtés and terrines.',
    'Caviar consists of salt-cured fish eggs (roe), known for their delicate flavor and unique texture. They are often served as a luxury garnish.',
    'Edible gold leaf adds a touch of elegance and visual appeal to dishes. It is used to decorate desserts and beverages.',
    'Aged balsamic vinegar is thick, sweet, and complex, aged for several years. It is drizzled on dishes like salads, cheeses, and strawberries.',
    'Vanilla bean has a rich, sweet, and floral flavor, used to enhance the taste of baked goods, desserts, and beverages.',
    'Kobe beef, from Wagyu cattle, is known for its exceptional marbling and tenderness, resulting in a luxurious and flavorful steak experience.',
    'Luxurious desserts include gold-flecked chocolates, truffle-infused pastries, caviar-topped blinis, and foie gras crème brûlée.'
]

    for i in range(len(questions)):
        cards.append(Card(setId=50, question=questions[i], answer=answers[i]))


















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
