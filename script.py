import argparse
import sqlite3

DB = 'social_network.db'

con = sqlite3.connect(DB)
cur = con.cursor()
def createUser(args):
    try:
        cur.execute('INSERT INTO users (email) VALUES (?)', (args.createUser,))
        con.commit()
        con.close()

        print(f"User created with email {args.createUser}")
    except sqlite3.Error as e:
        print(f"Error creating user: {e}")

def createAccount(user_id, username):
    cur.execute("INSERT INTO accounts (user_id, username) VALUES (?, ?)", (user_id, username))
    con.commit()
    print(f"{username} create with {user_id} successfully")

def main():
    parser = argparse.ArgumentParser(
        prog='Social Network',
        description='UI for a social network'
    )
    parser.add_argument('command', choices=['createUser','createAccount'], help='Specify the command')
    #Create User
    parser.add_argument('createUser', help='Email to be added')
    parser.add_argument('createAccount', help='Account to be added')
    
    args = parser.parse_args()

    if args.command == 'createUser':
        createUser(args)
    if args.command == 'createAccount':
        createAccount(args.user_id, args.username)
    else:
        print(f"Unknown command: {args.command}")

if __name__ == "__main__":
    main()
