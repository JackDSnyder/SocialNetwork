-- Users: an email address, possibly other info, represents a human
-- Accounts: a username, possibly other info, can have multiple accounts per user
-- Followers: an account can follow another account. if two accounts follow each 
--     other that would be two distinct follow records
-- Posts: some text posted by an account, possibly more, should include a timestamp
-- Additional features: at least two additional tables supporting more code 
--     functionality. join tables (to support many-to-many relationships) do not count


CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL
);

CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    username TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE followers (
    follower_id INTEGER NOT NULL,
    following_id INTEGER NOT NULL,
    FOREIGN KEY (follower_id) REFERENCES accounts (id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (following_id) REFERENCES accounts (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY, 
    creator INTEGER NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    content TEXT,
    FOREIGN KEY (creator) REFERENCES accounts (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE likes (
    post_id INTEGER NOT NULL,
    liker INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE reports (
    post_id INTEGER NOT NULL,
    reporter INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (reporter) REFERENCES accounts (id) ON DELETE CASCADE ON UPDATE CASCADE
)

