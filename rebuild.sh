rm -f social_network.db
sqlite3 social_network.db < schema.sql

# Create new new users, accounts, posts, followers, and likes
python3 jscript.py populate







