COLUMN_NUMBER_OFFSET = 4 # Column Number (0-indexed) - minus offset = song #
NUM_PLAYERS = 7
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
        10: "",
        11: "inner_value1",
        12: "inner_value2",
        13: "inner_value1",
        14: "inner_value2"
    },
    3: { # Lorenzo's Round: Openers & Closers
        1: "inner_value1",
        2: "inner_value2",
        3: "inner_value2",
        4: "inner_value1",
        5: "inner_value2",
        6: "inner_value2",
        7: "inner_value1",
        8: "inner_value2",
        9: "inner_value1",
        10: "inner_value2",
        11: "inner_value1",
        12: "inner_value2",
        13: "inner_value1",
        14: "inner_value2"
    },
    4: { # Caroline's Round: Your Sci-Fi Soundtrack
        1: "inner_value1",
        2: "inner_value2",
        3: "inner_value2",
        4: "inner_value1",
        5: "inner_value2",
        6: "inner_value2",
        7: "inner_value1",
        8: "inner_value2",
        9: "inner_value1",
        10: "inner_value2",
        11: "inner_value1",
        12: "inner_value2",
        13: "inner_value1",
        14: "inner_value2"
    },
    5: { # Khyle's Round: The Ship of Theseus Trolley Problem
        1: "inner_value1",
        2: "inner_value2",
        3: "inner_value2",
        4: "inner_value1",
        5: "inner_value2",
        6: "inner_value2",
        7: "inner_value1",
        8: "inner_value2",
        9: "inner_value1",
        10: "inner_value2",
        11: "inner_value1",
        12: "inner_value2",
        13: "inner_value1",
        14: "inner_value2"
    }
}
