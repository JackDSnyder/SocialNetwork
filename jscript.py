import sqlite3
from datetime import datetime
import argparse

conn = sqlite3.connect('social_network.db')
cursor = conn.cursor()

def create_user(email):
    print(f"User created with the email {email}")
    cursor.execute("INSERT INTO users (email) VALUES (?)", (email,))
    conn.commit()

def create_account(email, username):
    print(f"Account created with the username {username} with the email {email}")
    cursor.execute("INSERT INTO accounts (user_id, username) VALUES ((SELECT id FROM users WHERE email = ?),?)", (email,username))
    conn.commit()

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

def show_followers_post(username):
    cursor.execute("""
    SELECT f.following_username, p.timestamp, p.content 
    FROM posts p
    JOIN accounts a ON p.creator = a.id
    JOIN followers f ON a.username = f.following_username 
    WHERE f.follower_username = ?
    ORDER BY p.timestamp DESC
    """, (username,))

    feed = cursor.fetchall()
    for post in feed:
        following_username, timestamp, content = post
        print(f"User: {following_username} posted '{content}' at {timestamp}")


# Need to Do
def like_post(post_id, liker_id):
    cursor.execute("INSERT INTO likes (post_id, liker) VALUES (?, ?)", (post_id, liker_id))
    conn.commit()
    print(f"Post liked by {liker_id}")

def report_post(post_id, reporter_id):
    cursor.execute("INSERT INTO reports (post_id, reporter) VALUES (?, ?)", (post_id, reporter_id))
    conn.commit()
    print("Post reported successfully")

# Need to modify to make the account viewing the feed
# not be able to see posts they have reported
def display_feed():
    cursor.execute("""SELECT p.content, a.username, p.timestamp 
                   FROM posts p  
                   JOIN accounts a ON p.id = a.id""")
    feed = cursor.fetchall()
    for post in feed:
        content, username, timestamp = post
        print(f"User: {username} posted '{content}' at {timestamp}")


# ...

def main():
    parser = argparse.ArgumentParser(description='Simple social network CLI')
    parser.add_argument('action', choices=['create_user', 'create_account', 'follow_account', 'unfollow_account', 'create_post', 'display_feed', 'like_post', 'report_post','show_followers_post'],
                        help='Action to perform')
    parser.add_argument('--email', help='Email address (optional for create_user)')    
    parser.add_argument('--username', help='Username (required for create_account)')
    parser.add_argument('--content', help="The text that goes into a post")
    parser.add_argument('--follower', help='Follower ID (required for follow_account)')
    parser.add_argument('--following', help='Following ID (required for follow_account)')
    parser.add_argument('--post_id', type=int, help='Post ID (required for like_post and report_post)')
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
    elif args.action == 'show_followers_post':
        show_followers_post(args.username)
    elif args.action == 'display_feed':
        display_feed()

    elif args.action == 'like_post':
        like_post(args.post_id, args.user_id)
    elif args.action == 'report_post':
        report_post(args.post_id, args.user_id)
    

if __name__ == "__main__":
    main()

# Close the connection
conn.close()

