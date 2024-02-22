import sqlite3
from datetime import datetime
import argparse
import random

# To Do
# Report Functionality
# One more special query

conn = sqlite3.connect('social_network.db')
cursor = conn.cursor()

def populate():
    # Create Users and Accounts
    emails = ["josh214@gmail.com","sarah987@yahoo.com","mike_smith@hotmail.com","emily.jones123@outlook.com","alexander123@aol.com","lisa_miller22@gmail.com","ryan.martin456@yahoo.com","amanda.johnson789@hotmail.com","chris87@outlook.com","jennifer_smith222@aol.com","david.wilson456@gmail.com","olivia.morris789@yahoo.com","matthew.james234@hotmail.com","emma.thompson567@outlook.com","john_doe345@aol.com","natalie.brown678@gmail.com","michael_smith789@yahoo.com","jessica_jackson345@hotmail.com","brandon.miller678@outlook.com","sophia789@aol.com","william_johnson123@gmail.com","lauren.martin234@yahoo.com","ryan_smith789@hotmail.com","katie.brown456@outlook.com","jacob_jones789@aol.com","madison.smith123@gmail.com","andrew_thomas234@yahoo.com","olivia.martin456@hotmail.com","daniel.johnson789@outlook.com","samantha345@aol.com","james_smith234@gmail.com","emily_brown456@yahoo.com","nathan.johnson789@hotmail.com","ava.jones234@outlook.com","ethan_smith456@aol.com","ella.morris789@gmail.com","logan.jones234@yahoo.com","mia_smith456@hotmail.com","alexander345@outlook.com","abigail.jones789@aol.com",
    "dylan.martin234@gmail.com","victoria789@yahoo.com","christopher.smith456@hotmail.com","grace345@outlook.com","daniel.miller789@aol.com","zoe.jones234@gmail.com","mason456@yahoo.com","amelia.morris789@hotmail.com","logan345@outlook.com","ava789@aol.com","noah.jones234@gmail.com","sophie.miller456@yahoo.com","joseph789@hotmail.com","ella.jones234@outlook.com", "samuel456@aol.com", "emily345@gmail.com", "zoey.morris789@yahoo.com", "benjamin345@outlook.com", "olivia.martin456@aol.com", "carter234@gmail.com","hannah_miller456@yahoo.com","jack789@hotmail.com","ava.brown234@outlook.com","luke_smith456@aol.com","grace234@gmail.com","lucas_morris789@yahoo.com","owen345@hotmail.com","charlotte.jones234@outlook.com","gabriel456@aol.com",
    "scarlett.morris789@gmail.com","liam234@yahoo.com","audrey.brown456@hotmail.com","henry789@outlook.com","ella.jones234@aol.com","wyatt456@gmail.com","zoey.morris789@yahoo.com","elijah345@hotmail.com","mia345@outlook.com","amelia789@aol.com","jacob234@gmail.com","chloe.miller456@yahoo.com","jackson789@hotmail.com","mia234@outlook.com","jacob.morris789@aol.com","william456@gmail.com","aubrey.brown456@yahoo.com","liam789@hotmail.com","charlotte234@outlook.com","ethan.morris789@aol.com","madison234@gmail.com","hannah.miller456@yahoo.com","carter789@hotmail.com","emily234@outlook.com","samuel.morris789@aol.com", "oliver456@gmail.com","ava.brown456@yahoo.com","benjamin789@hotmail.com","ella234@outlook.com","mason.morris789@aol.com","mia234@gmail.com","gabriel456@yahoo.com","scarlett789@hotmail.com","jack234@outlook.com","zoey.miller789@aol.com"]
    
    usernames = ["apple123", "banana456", "cherry789", "grape234", "orange567", "pineapple890", "strawberry123", "watermelon456", "blueberry789", "raspberry234","kiwi567", "mango890", "apricot123", "peach456", "pear789", "plum234", "lemon567", "lime890", "coconut123", "papaya456","melon789", "avocado234", "fig567", "date890", "cranberry123", "elderberry456", "guava789", "honeydew234", "nectarine567", "lychee890","persimmon123", "boysenberry456", "mulberry789", "kumquat234", "tangerine567", "cantaloupe890", "dragonfruit123", "pomegranate456", "passionfruit789", "kiwifruit234",
    "grapefruit567", "apricot890", "gooseberry123", "starfruit456", "rhubarb789", "blackberry234", "currant567", "mandarin890", "pawpaw123", "persimmon456","plantain789", "pomelo234", "quince567", "tamarillo890", "ugli123", "acai456", "bilberry789", "carissa234", "durian567", "jaboticaba890","kiwano123", "loganberry456", "mangosteen789", "papaya234", "passionfruit567", "pummelo890", "tamarind123", "yuzu456", "zucchini789", "almond234","cashew567", "chestnut890", "hazelnut123", "macadamia456", "peanut789", "pecan234", "pistachio567", "walnut890", "sunflower123", "daffodil456",
    "daisy789", "tulip234", "rose567", "lily890", "orchid123", "iris456", "hydrangea789", "jasmine234", "lilac567", "carnation890","sunflower123", "dahlia456", "chrysanthemum789", "poinsettia234", "aster567", "peony890", "gladiolus123", "cosmos456", "snapdragon789", "zinnia234","hibiscus567", "lavender890", "bougainvillea123", "freesia456", "gardenia789", "magnolia234", "marigold567", "narcissus890", "oleander123", "orchid456","petunia789", "rhododendron234", "tulip567", "violet890", "zinnia123", "daisy456", "tulip789", "rose234", "lily567", "orchid890",
    "iris123", "sunflower456", "hydrangea789", "jasmine234", "lilac567", "carnation890", "sunflower123", "dahlia456", "chrysanthemum789", "poinsettia234","aster567", "peony890", "gladiolus123", "cosmos456", "snapdragon789", "zinnia234", "hibiscus567", "lavender890", "bougainvillea123", "freesia456","gardenia789", "magnolia234", "marigold567", "narcissus890", "oleander123", "orchid456", "petunia789", "rhododendron234", "tulip567", "violet890", "crocus123", "daisy456", "lilac789", "sunflower234", "tulip567","rose890", "lily123", "orchid456", "iris789", "hydrangea234","jasmine567", "dahlia890", "chrysanthemum123", "poinsettia456", "aster789",
    "peony234", "gladiolus567", "cosmos890", "snapdragon123", "zinnia456","hibiscus789", "lavender234", "bougainvillea567", "freesia890", "gardenia123","magnolia456", "marigold789", "narcissus234", "oleander567", "orchid890","petunia123", "rhododendron456", "tulip789", "violet234", "zinnia567","daisy890", "tulip123", "rose456", "lily789", "orchid234","iris567", "sunflower890", "hydrangea123", "jasmine456", "lilac789","carnation234", "sunflower567", "dahlia890", "chrysanthemum123", "poinsettia456"]
    for i in range(100):
        cursor.execute("INSERT INTO users (email) VALUES (?)", (emails[i],))
        conn.commit()
        cursor.execute("INSERT INTO accounts (user_id, username) VALUES ((SELECT id FROM users WHERE email = ?),?)", (emails[i],usernames[2*i]))
        conn.commit()
        cursor.execute("INSERT INTO accounts (user_id, username) VALUES ((SELECT id FROM users WHERE email = ?),?)", (emails[i],usernames[2*i+1]))
        conn.commit()

    # Create Posts
    lines = ["wants to punch", "wants to hug", "is thinking about", "is playing football with", "is whispering to"]
    for i in range(150):
        timestamp = datetime.now()
        content = f"{random.choice(usernames)} {random.choice(lines)} {random.choice(usernames)}"
        cursor.execute("SELECT id FROM accounts WHERE username = ?", (random.choice(usernames),))
        user_id = cursor.fetchone()
        cursor.execute("INSERT INTO posts (creator, timestamp, content) VALUES (?, ?, ?)", (user_id[0], timestamp, content))
        conn.commit()

    # Create Follows
    for i in range(200):
        follower = usernames[i]
        followings = []
        for j in range(random.randrange(1,7)):
            following = random.choice(usernames)
            while following == follower or following in followings:
                following = random.choice(usernames)
            followings += following
            cursor.execute("""
                   INSERT INTO followers (follower_id, follower_username, following_id,following_username) 
                   VALUES ((SELECT id FROM accounts WHERE username = ?), ?,(SELECT id FROM accounts WHERE username = ?),?)
                   """, 
                   (follower,follower,following,following))
            conn.commit()

    # Create Likes
    for i in range(200):
        liker = usernames[i]
        liked = []
        for i in range(random.randrange(7,9)):
            post_id = random.randrange(1,156)
            while post_id in liked:
                post_id = random.randrange(1,156)
            cursor.execute("INSERT INTO likes (post_id, liker) VALUES (?, (SELECT id FROM accounts WHERE username = ?))", (post_id, liker))
            conn.commit()



def create_user(email):
    print(f"User created with the email {email}")
    cursor.execute("INSERT INTO users (email) VALUES (?)", (email,))
    conn.commit()

def list_users():
    cursor.execute("""SELECT * FROM users""")
    users = cursor.fetchall()
    for user in users:
        uId, uEmail = user
        print(f"Id: {uId}, Email: {uEmail}")


def create_account(email, username):
    print(f"Account created with the username {username} with the email {email}")
    cursor.execute("INSERT INTO accounts (user_id, username) VALUES ((SELECT id FROM users WHERE email = ?),?)", (email,username))
    conn.commit()

def list_accounts():
    cursor.execute("""SELECT id, username FROM accounts""")
    accounts = cursor.fetchall()
    for account in accounts:
        uId, uName = account
        print(f"Id: {uId}, Username: {uName}")

def create_post(username, content):
    if not username:
        print("Error: Username is required for creating a post.")
        return
    
    cursor.execute("SELECT id FROM accounts WHERE username = ?", (username,))
    user_id = cursor.fetchone()
    if user_id:
        timestamp = datetime.now()
        cursor.execute("INSERT INTO posts (creator, timestamp, content) VALUES (?, ?, ?)", (user_id[0], timestamp, content))
        conn.commit()
        print(f"Posted to account ({username}) with the caption {content} at " + str(timestamp))
    else:
        print(f"User with username {username} does not exist.")

def delete_post(post_id):
    cursor.execute("""DELETE FROM posts WHERE id = ?""", (post_id,))
    conn.commit()
    print(f"Post {post_id} has been deleted")

def follow_account(follower, following):
    cursor.execute("""
                   INSERT INTO followers (follower_id, follower_username, following_id,following_username) 
                   VALUES ((SELECT id FROM accounts WHERE username = ?), ?,(SELECT id FROM accounts WHERE username = ?),?)
                   """, 
                   (follower,follower, following,following))
    conn.commit()
    print(f"{follower} is now following {following}")

def unfollow_account(follower,following):
    cursor.execute("""DELETE FROM followers WHERE follower_username = ? AND following_username = ?""", (follower,following))
    conn.commit()
    print(f"{follower} has now unfollowed {following}")

def like_post(post_id, liker):
    cursor.execute("INSERT INTO likes (post_id, liker) VALUES (?, (SELECT id FROM accounts WHERE username = ?))", (post_id, liker))
    conn.commit()
    print(f"Post liked by {liker}")

def report_post(post_id, reporter):
    cursor.execute("INSERT INTO reports (post_id, reporter) VALUES (?, (SELECT id FROM accounts WHERE username = ?))", (post_id, reporter))
    conn.commit()
    print("Post reported successfully")
    
    cursor.execute("SELECT COUNT(*) AS numReports FROM reports WHERE post_id = ?", (post_id,))
    report = cursor.fetchone()
    print("Number of Reports:", report[0])
    
    if report[0] == 3:
        cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        conn.commit() 
        print("Post has been removed because of reports.")



def show_user_feed(username):
    cursor.execute("""
    SELECT f.following_username, p.timestamp, p.content, p.id 
    FROM posts p
    JOIN accounts a ON p.creator = a.id
    JOIN followers f ON a.username = f.following_username 
    WHERE f.follower_username = ?
    ORDER BY p.timestamp DESC
    """, (username,))

    feed = cursor.fetchall()
    for post in feed:
        username, timestamp, content, id = post
        print(f"{username} posted '{content}' on {timestamp[5:7]}/{timestamp[8:10]}/{timestamp[:4]} at {timestamp[12:19]}, Id: {id}")
        

def catch_up_feed():
    print('\n')
    # By Month
    # now = str(datetime.now())[5:9]
    # By Day
    # now = str(datetime.now())[8:11]
    # By Minute
    now = str(datetime.now())[14:18]
    cursor.execute(f"""SELECT a.username,p.timestamp,p.content, COUNT(DISTINCT l.liker) AS likes FROM posts p 
                   JOIN likes l ON p.id = l.post_id 
                   JOIN accounts AS a on a.id = p.creator
                   WHERE p.timestamp LIKE "%{now}%"
                   GROUP BY p.id
                   ORDER BY likes DESC
                   LIMIT 10;""")
    feed = cursor.fetchall()
    for post in feed:
        username, timestamp, content, likes = post
        print(f"{username} posted '{content}' on {timestamp[5:7]}/{timestamp[8:10]}/{timestamp[:4]} at {timestamp[12:19]} and got {likes} likes")



def main():
    parser = argparse.ArgumentParser(description='Simple social network CLI')
    parser.add_argument('action', choices=['populate', 'create_user', 'create_account', 'follow_account', 'unfollow_account', 
                                           'create_post', 'catch_up_feed', 'like_post', 'report_post','show_user_feed',
                                           'delete_post', 'list_accounts', 'list_users'],
                        help='Action to perform')
    parser.add_argument('--email')    
    parser.add_argument('--username')
    parser.add_argument('--content')
    parser.add_argument('--follower')
    parser.add_argument('--following')
    parser.add_argument('--post_id')
    args = parser.parse_args()

    if args.action == 'create_user':
        create_user(args.email)
    elif args.action == 'create_account':
        create_account(args.email, args.username)
    elif args.action == 'create_post':
        create_post(args.username, args.content)
    elif args.action == 'follow_account':
        follow_account(args.follower, args.following)
    elif args.action == 'unfollow_account':
        unfollow_account(args.follower, args.following)
    elif args.action == 'show_user_feed':
        show_user_feed(args.username)
    elif args.action == 'catch_up_feed':
        catch_up_feed()
    elif args.action == 'like_post':
        like_post(args.post_id, args.username)
    elif args.action == 'report_post':
        report_post(args.post_id, args.username)
    elif args.action == 'delete_post':
        delete_post(args.post_id)
    elif args.action == 'populate':
        populate()
    elif args.action == 'list_accounts':
        list_accounts()
    elif args.action == 'list_users':
        list_users()
    

if __name__ == "__main__":
    main()

# Close the connection
conn.close()

