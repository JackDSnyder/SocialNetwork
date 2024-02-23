# SocialNetwork

### Script Commands

- python3 jscript.py populate
- python3 jscript.py create_user --email test@test.com
- python3 jscript.py create_account --email test@test.com --username testUsername
- python3 jscript.py create_post --username testUsername --content "anotherpost"
- python3 jscript.py delete_post --post_id 1
- pyton3 jscript.py list_accounts
- pyton3 jscript.py list_users
- python3 jscript.py follow_account --follower testUsername --following otherUser
- python3 jscript.py unfollow_account --follower testUsername --following otherUser
- python3 jscript.py like_post --post_id 1 --username usernameLiking
- python3 jscript.py report_post --post_id 1 --username userGettingReported
- python3 jscript.py show_user_feed --username testUsername
- python3 jscript.py catch_up_feed
