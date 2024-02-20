sqlite3 social_network.db < schema.sql

# Create new newUsers
echo "Users being made..."
python3 jscript.py create_user --email amelia@gmail.com
python3 jscript.py create_user --email leo@gmail.com
python3 jscript.py create_user --email maya@gmail.com
python3 jscript.py create_user --email ethan@gmail.com
python3 jscript.py create_user --email olivia@gmail.com
echo "======================================================="

# Create new acounts
echo ""
echo "Accounts being made..."
python3 jscript.py create_account --email amelia@gmail.com --username secretgarden
python3 jscript.py create_account --email amelia@gmail.com --username peachysunset
python3 jscript.py create_account --email leo@gmail.com --username ivorywhisper
python3 jscript.py create_account --email leo@gmail.com --username tranquilmeadow
python3 jscript.py create_account --email maya@gmail.com --username whimsicalshade
python3 jscript.py create_account --email maya@gmail.com --username amberhush
python3 jscript.py create_account --email ethan@gmail.com --username shadowglimpse
python3 jscript.py create_account --email ethan@gmail.com --username gentlewhirl
python3 jscript.py create_account --email olivia@gmail.com --username cozyfern
python3 jscript.py create_account --email olivia@gmail.com --username silentwaves
echo "======================================================="

#Post to the accounts
echo ""
echo "Post being made..."
python3 jscript.py create_post --username secretgarden --content "Enchanted Garden"
python3 jscript.py create_post --username peachysunset --content "Sunset Bliss"
python3 jscript.py create_post --username tranquilmeadow --content "Meadow Tranquility"
python3 jscript.py create_post --username ivorywhisper --content "Whispers of Ivory"
python3 jscript.py create_post --username shadowglimpse --content "Glimpse in Shadows"
python3 jscript.py create_post --username whimsicalshade --content "Shades of Whimsy"
python3 jscript.py create_post --username amberhush --content "Hushed Amber"
python3 jscript.py create_post --username silentwaves --content "Silent Waves"
python3 jscript.py create_post --username gentlewhirl --content "Gentle Whirlwind"
python3 jscript.py create_post --username cozyfern --content "Fern Coziness"

# Posting another set for each account
python3 jscript.py create_post --username peachysunset --content "Golden Horizon"
python3 jscript.py create_post --username whimsicalshade --content "Playful Shadows"
python3 jscript.py create_post --username secretgarden --content "Mystical Oasis"
python3 jscript.py create_post --username ivorywhisper --content "Whispers of Elegance"
python3 jscript.py create_post --username tranquilmeadow --content "Serene Meadow Retreat"
python3 jscript.py create_post --username cozyfern --content "Fern Cozy Corner"
python3 jscript.py create_post --username amberhush --content "Hushed Amber Glow"
python3 jscript.py create_post --username silentwaves --content "Silent Waves Symphony"
python3 jscript.py create_post --username shadowglimpse --content "Glimpse into Twilight"
python3 jscript.py create_post --username gentlewhirl --content "Gentle Whirlwind Dance"
echo "======================================================="

# Following Accounts
echo ""
echo "User Following Eachother..."
python3 jscript.py follow_account --follower secretgarden --following peachysunset
python3 jscript.py follow_account --follower secretgarden --following ivorywhisper
python3 jscript.py follow_account --follower secretgarden --following tranquilmeadow
python3 jscript.py follow_account --follower secretgarden --following whimsicalshade
python3 jscript.py follow_account --follower secretgarden --following amberhush
python3 jscript.py follow_account --follower secretgarden --following shadowglimpse
python3 jscript.py follow_account --follower secretgarden --following gentlewhirl
python3 jscript.py follow_account --follower secretgarden --following cozyfern
python3 jscript.py follow_account --follower secretgarden --following silentwaves

python3 jscript.py follow_account --follower peachysunset --following ivorywhisper
python3 jscript.py follow_account --follower peachysunset --following whimsicalshade
python3 jscript.py follow_account --follower peachysunset --following tranquilmeadow
python3 jscript.py follow_account --follower peachysunset --following amberhush
python3 jscript.py follow_account --follower peachysunset --following shadowglimpse
python3 jscript.py follow_account --follower peachysunset --following gentlewhirl

python3 jscript.py follow_account --follower ivorywhisper --following tranquilmeadow
python3 jscript.py follow_account --follower ivorywhisper --following whimsicalshade
python3 jscript.py follow_account --follower ivorywhisper --following amberhush

python3 jscript.py follow_account --follower tranquilmeadow --following ivorywhisper
python3 jscript.py follow_account --follower tranquilmeadow --following whimsicalshade
python3 jscript.py follow_account --follower tranquilmeadow --following amberhush

python3 jscript.py follow_account --follower whimsicalshade --following amberhush
python3 jscript.py follow_account --follower whimsicalshade --following tranquilmeadow
python3 jscript.py follow_account --follower whimsicalshade --following shadowglimpse

python3 jscript.py follow_account --follower amberhush --following whimsicalshade
python3 jscript.py follow_account --follower amberhush --following tranquilmeadow
python3 jscript.py follow_account --follower amberhush --following shadowglimpse

python3 jscript.py follow_account --follower shadowglimpse --following gentlewhirl
python3 jscript.py follow_account --follower shadowglimpse --following cozyfern
python3 jscript.py follow_account --follower shadowglimpse --following silentwaves

python3 jscript.py follow_account --follower gentlewhirl --following shadowglimpse
python3 jscript.py follow_account --follower gentlewhirl --following cozyfern
python3 jscript.py follow_account --follower gentlewhirl --following silentwaves

python3 jscript.py follow_account --follower cozyfern --following silentwaves

python3 jscript.py follow_account --follower silentwaves --following cozyfern
echo "======================================================="

#Show post
echo ""
echo "Showing secretgarden followings post..."
python3 jscript.py show_followers_post --username secretgarden
echo "======================================================="

# Unfollow 
echo ""
python3 jscript.py unfollow_account --follower secretgarden --following silentwaves
echo "======================================================="
echo ""
echo "Showing secretgarden followers post..."
python3 jscript.py show_followers_post --username secretgarden
echo "======================================================="







