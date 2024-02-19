sqlite3 social_network.db < schema.sql

# Create new newUsers

python3 jscript.py create_user --email amelia@gmail.com
python3 jscript.py create_user --email leo@gmail.com
python3 jscript.py create_user --email maya@gmail.com
python3 jscript.py create_user --email ethan@gmail.com
python3 jscript.py create_user --email olivia@gmail.com
python3 jscript.py create_user --email jackson@gmail.com
python3 jscript.py create_user --email lily@gmail.com
python3 jscript.py create_user --email caleb@gmail.com
python3 jscript.py create_user --email grace@gmail.com
python3 jscript.py create_user --email sebastian@gmail.com

# Create new acounts
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
python3 jscript.py create_account --email jackson@gmail.com --username twinklingdusk
python3 jscript.py create_account --email jackson@gmail.com --username serenemist
python3 jscript.py create_account --email lily@gmail.com --username quietstream
python3 jscript.py create_account --email lily@gmail.com --username leafyshadow
python3 jscript.py create_account --email caleb@gmail.com --username daisydream
python3 jscript.py create_account --email caleb@gmail.com --username velvetwhisper
python3 jscript.py create_account --email grace@gmail.com --username moonlitrose
python3 jscript.py create_account --email grace@gmail.com --username smoothstone
python3 jscript.py create_account --email sebastian@gmail.com --username gigglybreeze
python3 jscript.py create_account --email sebastian@gmail.com --username cloudysky

#Post to the accounts
python3 jscript.py create_post --username secretgarden --content "Enchanted Garden"
python3 jscript.py create_post --username peachysunset --content "Sunset Bliss"
python3 jscript.py create_post --username ivorywhisper --content "Whispers of Ivory"
python3 jscript.py create_post --username tranquilmeadow --content "Meadow Tranquility"
python3 jscript.py create_post --username whimsicalshade --content "Shades of Whimsy"
python3 jscript.py create_post --username amberhush --content "Hushed Amber"
python3 jscript.py create_post --username shadowglimpse --content "Glimpse in Shadows"
python3 jscript.py create_post --username gentlewhirl --content "Gentle Whirlwind"
python3 jscript.py create_post --username cozyfern --content "Fern Coziness"
python3 jscript.py create_post --username silentwaves --content "Silent Waves"
python3 jscript.py create_post --username twinklingdusk --content "Dusk Twinkles"
python3 jscript.py create_post --username serenemist --content "Mist Serenity"
python3 jscript.py create_post --username quietstream --content "Stream of Quiet"
python3 jscript.py create_post --username leafyshadow --content "Shady Leaves"
python3 jscript.py create_post --username daisydream --content "Dreamy Daisies"
python3 jscript.py create_post --username velvetwhisper --content "Velvet Whispers"
python3 jscript.py create_post --username moonlitrose --content "Rose in Moonlight"
python3 jscript.py create_post --username smoothstone --content "Smooth Stones"
python3 jscript.py create_post --username gigglybreeze --content "Breezy Giggles"
python3 jscript.py create_post --username cloudysky --content "Cloudy Skies"
# Posting another set for each account
# python3 jscript.py create_post --username secretgarden --content "Mystical Oasis"
# python3 jscript.py create_post --username peachysunset --content "Golden Horizon"
# python3 jscript.py create_post --username ivorywhisper --content "Whispers of Elegance"
# python3 jscript.py create_post --username tranquilmeadow --content "Serene Meadow Retreat"
# python3 jscript.py create_post --username whimsicalshade --content "Playful Shadows"
# python3 jscript.py create_post --username amberhush --content "Hushed Amber Glow"
# python3 jscript.py create_post --username shadowglimpse --content "Glimpse into Twilight"
# python3 jscript.py create_post --username gentlewhirl --content "Gentle Whirlwind Dance"
# python3 jscript.py create_post --username cozyfern --content "Fern Cozy Corner"
# python3 jscript.py create_post --username silentwaves --content "Silent Waves Symphony"
# python3 jscript.py create_post --username twinklingdusk --content "Twinkling Dusk Beauty"
# python3 jscript.py create_post --username serenemist --content "Mist of Serenity"
# python3 jscript.py create_post --username quietstream --content "Tranquil Stream Harmony"
# python3 jscript.py create_post --username leafyshadow --content "Leafy Shadows Haven"
# python3 jscript.py create_post --username daisydream --content "Daisy Dreamland"
# python3 jscript.py create_post --username velvetwhisper --content "Velvet Whispers Delight"
# python3 jscript.py create_post --username moonlitrose --content "Moonlit Rose Serenade"
# python3 jscript.py create_post --username smoothstone --content "Smooth Stone Path"
# python3 jscript.py create_post --username gigglybreeze --content "Giggly Breeze Play"
# python3 jscript.py create_post --username cloudysky --content "Cloudy Sky Serenity"


# Following Accounts
python3 jscript.py follow_account --follower secretgarden --following peachysunset
python3 jscript.py follow_account --follower secretgarden --following ivorywhisper
python3 jscript.py follow_account --follower secretgarden --following whimsicalshade

python3 jscript.py follow_account --follower peachysunset --following secretgarden
python3 jscript.py follow_account --follower peachysunset --following ivorywhisper
python3 jscript.py follow_account --follower peachysunset --following whimsicalshade

python3 jscript.py follow_account --follower ivorywhisper --following tranquilmeadow
python3 jscript.py follow_account --follower ivorywhisper --following whimsicalshade
python3 jscript.py follow_account --follower ivorywhisper --following amberhush

python3 jscript.py follow_account --follower tranquilmeadow --following ivorywhisper
python3 jscript.py follow_account --follower tranquilmeadow --following whimsicalshade
python3 jscript.py follow_account --follower tranquilmeadow --following amberhush



