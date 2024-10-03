COLUMN_NUMBER_OFFSET = 4 # Column Number (0-indexed) - minus offset = song #
NUM_PLAYERS = 7
NUM_ROUNDS = 14
CURRENT_WEEK = 2
NUM_SONGS_SUBMITTED_WEEKLY = NUM_PLAYERS * 2
ENDING_GUESSING_COLUMN_IDX = COLUMN_NUMBER_OFFSET + NUM_SONGS_SUBMITTED_WEEKLY # IDX of last column used for guessing

# TODO: Might change PLAYLISTS to be grabbed/processed dynamically through spotify
    # If i did do this then I might add another question to google form saying the name of the playlist/week
    # in order to map the week to the playlist (since spotify probably won't number the playlists the way that we are)

# Hardcoded information about which SONG NAME correlates to which SONG NUMBER for EACH WEEK
    # Week Number:
        # Song idx number : Song Name & Artist
PLAYLISTS = {
    1: { # Anything Goes
        1: "Anything Goes - Sutton Foster, Anything Goes New Broadway Company Orchestra",
        2: "pick up the phone - Young Thug, Travis Scott",
        3: "Dance Yrself Clean - LCD Soundsystem",
        4: "Autumn in Virbank - Snivys",
        5: "Dance In Room Song - Sipper",
        6: "Night Dancer - imase",
        7: "Make U Mine - morgen",
        8: "Nobody's Soldier - Hozier",
        9: "Splashing Around - David Scott",
        10: "All These Things That I've Done - The Killers",
        11: "Shakes - Luke Hemmings",
        12: "Amphetamine Smiles - Taking Back Sunday",
        13: "The Night Me and Your Mama Met - Childish Gambino",
        14: "Angeleyes - ABBA"
    },
    2: { # Deborah's Round: Duality of Man REDO
        1: "Don't Know How To Keep Loving You - Julia Jacklin",
        2: "Same Old Love - Selena Gomez",
        3: "Contrast And Compare - Bright Eyes",
        4: "Mr. Blue Sky - Electric Light Orchestra",
        5: "Sanguine Paradise - Lil Uzi Vert",
        6: "(Eat Shit) We Did It - Born Ruffians",
        7: "What Makes You Beautiful - One Direction",
        8: "Friends - Verhoog",
        9: "Kiss You - One Direction",
        10: "DONTTRUSTME - 3OH!3",
        11: "The Scientist - Coldplay",
        12: "Sunbleached Girl - Shag Rock"
    },
    3: { # Lorenzo's Round: Openers & Closers
        1: "Hideaway - Kiesza",
        2: "Down On My Luck - VIC MENSA",
        3: "Shelter - Porter Robinson, Madeon",
        4: "Monster - Lady Gaga",
        5: "Doses & Mimosas - Cherub",
        6: "I Was Made For Lovin' You - from The Fall Guy - YUNGBLUD",
        7: "Eventually - Tame Impala",
        8: "Hold My Liquor - Kanye West",
        9: "Misty - Laufey",
        10: "Die Young - Kesha",
        11: "Don't Stop Me Now - Remastered 2011 - Queen",
        12: "Fell In the Sun - Big Grams"
    },
    4: { # Caroline's Round: Your Sci-Fi Soundtrack
        1: "10AM/Save The World (feat. Gucci Mane) - Metro Boomin, Gucci Mane",
        2: "I'm Still Standing - Elton John",
        3: "Survival - Muse",
        4: "Choke - I DONT KNOW BUT THEY FOUND ME",
        5: "Kill V. Maim - Grimes",
        6: "All for Leyna - Billy Joel",
        7: "One Way Or Another - Blondie",
        8: "Dance, Dance - Fall Out Boy",
        9: "Which Witch - Florence + The Machine",
        10: "Born to Run - Bruce Springsteen",
        11: "Terrible Things - Brick + Mortar",
        12: "Knights of Cydonia - Muse"
    },
    5: { # Khyle's Round: The Ship of Theseus Trolley Problem
        1: "Which Side are You On? - Pete Seeger",
        2: "A Change Is Gonna Come - Greta Van Fleet",
        3: "Cold Cold Cold - Cage The Elephant",
        4: "Gettin' Rich, Goin' Broke - Willow Avalon",
        5: "Gasoline - Brand New",
        6: "Stop That Train - AWOLNATION",
        7: "Quirky Worky Song - Danny Jacob",
        8: "The Adults Are Talking - The Strokes",
        9: "Pick Me - girl in red",
        10: "Gethsemane (I Only Want To Say) - Ian Gillan, Andrew Lloyd Weber, Tim Rice",
        11: "Doomsday - MF DOOM, Pebbles The Invisible Girl",
        12: "I Miss Those Days - Bleachers"
    }
}
