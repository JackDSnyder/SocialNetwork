import argparse
import sqlite3
from schema import schema



con = sqlite3.connect('social_networking.db')
def create(args): 
    d
    

def main():
    parser = argparse.ArgumentParser(
        prog='Social Network',
        description='UI for a social network'
    )
    # Creates new database
    parser.add_argument('create', help='create the database')
    parser.set_defaults(func=create)

    args = parser.parse_args()

    args.func(args)

if __name__ == "__main__":
    main()
