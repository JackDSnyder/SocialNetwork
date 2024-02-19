# SocialNetwork

<!-- For creating new users -->

python3 jscript.py create_user --email test@test.com

<!-- For creating accounts -->

python3 jscript.py create_account --email test@test.com --username

<!-- For posting  -->

python3 jscript.py create_post --username testUsername --content "anotherpost"

<!-- Following -->

python3 jscript.py follow_account --follower secretgarden --following ivorywhisper

<!-- Unfollow -->

python3 jscript.py unfollow_account --follower secretgarden --following ivorywhisper

<!-- To show post they are following -->

python3 jscript.py show_followers_post --username secretgarden
