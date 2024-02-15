import sqlite3
from datetime import datetime
import argparse

conn = sqlite3.connect('network.db')
cursor = conn.cursor()

def create_user(email):
    cursor.execute("INSERT INTO users (email) VALUES (?)", (email,))
    conn.commit()
    print("User created successfully")

def create_account(user_id, username):
    cursor.execute("INSERT INTO accounts (user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    print("Account created successfully")

def follow_account(follower_id, following_id):
    cursor.execute("INSERT INTO followers (follower_id, following_id) VALUES (?, ?)", (follower_id, following_id))
    conn.commit()
    print("Followed successfully")

def create_post(creator_id, content):
    timestamp = datetime.now()
    cursor.execute("INSERT INTO posts (creator, timestamp, content) VALUES (?, ?, ?)", (creator_id, timestamp, content))
    conn.commit()
    print("Post created successfully")
    
def like_post(post_id, liker_id):
    cursor.execute("INSERT INTO likes (post_id, liker) VALUES (?, ?)", (post_id, liker_id))
    conn.commit()
    print("Post liked successfully")

def report_post(post_id, reporter_id):
    cursor.execute("INSERT INTO reports (post_id, reporter) VALUES (?, ?)", (post_id, reporter_id))
    conn.commit()
    print("Post reported successfully")

# Need to modify to make the account viewing the feed
# not be able to see posts they have reported
def display_feed(account_id):
    cursor.execute("""SELECT p.id, p.creator, p.timestamp, p.content 
                      FROM posts p 
                      JOIN followers f ON p.creator = f.following_id 
                      WHERE f.follower_id = ? 
                      ORDER BY p.timestamp DESC""", (account_id,))
    feed = cursor.fetchall()
    for post in feed:
        print(post)


def main():
    parser = argparse.ArgumentParser(description='Simple social network CLI')
    parser.add_argument('action', choices=['create_user', 'create_account', 'follow_account', 'create_post', 'display_feed', 'like_post', 'report_post'],
                        help='Action to perform')
    parser.add_argument('--email', help='Email address (required for create_user)')
    parser.add_argument('--user_id', type=int, help='User ID (required for create_account, follow_account, create_post, and like_post)')
    parser.add_argument('--username', help='Username (required for create_account)')
    parser.add_argument('--follower_id', type=int, help='Follower ID (required for follow_account)')
    parser.add_argument('--following_id', type=int, help='Following ID (required for follow_account)')
    parser.add_argument('--content', help='Post content (required for create_post)')
    parser.add_argument('--post_id', type=int, help='Post ID (required for like_post and report_post)')
    args = parser.parse_args()

    if args.action == 'create_user':
        create_user(args.email)
    elif args.action == 'create_account':
        create_account(args.user_id, args.username)
    elif args.action == 'follow_account':
        follow_account(args.follower_id, args.following_id)
    elif args.action == 'create_post':
        create_post(args.user_id, args.content)
    elif args.action == 'display_feed':
        display_feed(args.user_id)
    elif args.action == 'like_post':
        like_post(args.post_id, args.user_id)
    elif args.action == 'report_post':
        report_post(args.post_id, args.user_id)

if __name__ == "__main__":
    main()

# Close the connection
conn.close()
