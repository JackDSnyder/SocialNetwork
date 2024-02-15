import random
names = [
    'John', 'Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'William', 'Sophia', 'James', 'Isabella',
    'Oliver', 'Mia', 'Benjamin', 'Charlotte', 'Elijah', 'Amelia', 'Lucas', 'Harper', 'Mason', 'Evelyn',
    'Logan', 'Abigail', 'Alexander', 'Emily', 'Ethan', 'Elizabeth', 'Jacob', 'Avery', 'Michael', 'Sofia',
    'Daniel', 'Ella', 'Henry', 'Madison', 'Jackson', 'Scarlett', 'Sebastian', 'Victoria', 'Jack', 'Aria',
    'Aiden', 'Grace', 'Matthew', 'Chloe', 'Samuel', 'Camila', 'David', 'Penelope', 'Joseph', 'Riley',
    'Carter', 'Luna', 'Owen', 'Hannah', 'Wyatt', 'Nora', 'Jayden', 'Lily', 'John', 'Zoey', 'Luke', 'Mila',
    'Gabriel', 'Layla', 'Anthony', 'Aubrey', 'Isaac', 'Lillian', 'Grayson', 'Addison', 'Levi', 'Eleanor',
    'Christopher', 'Natalie', 'Joshua', 'Brooklyn', 'Andrew', 'Stella', 'Lincoln', 'Hazel', 'Mateo', 'Ellie',
    'Ryan', 'Paisley', 'Jaxon', 'Audrey', 'Nathan', 'Skylar', 'Aaron', 'Violet', 'Isaiah', 'Claire',
    'Charles', 'Bella', 'Hunter', 'Aurora', 'Christian', 'Lucy', 'Thomas', 'Anna'
]

for name in names:
    print(f"INSERT INTO users('{name}@gmail.com')")

for i in range(len(names)):
    num = random.randrange(1,999)
    print(f"INSERT INTO accounts('{i+1}','{name}{name}{num}' )")