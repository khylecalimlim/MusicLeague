import sys
import pandas as pd
import matplotlib.pyplot as plt

# Hard coded column names which are used for tracking player's guesses 
PLAYER_GUESS_COLS = ('Who do you think entered song 1?', 'Song 2?', 'Song 3?', 'Song 4?', 'Song 5?', 'Song 6?', 
                        'Song 7?', 'Song 8?', 'Song 9?', 'Song 10?', 'Song 11?', 'Song 12?', 'Song 13?', 'Song 14?')

COLUMN_NUMBER_OFFSET = 4 # Column Number (0-indexed) - minus offset = song # 
NUM_PLAYERS = 7
CURRENT_WEEK = 2
NUM_SONGS_SUBMITTED_WEEKLY = NUM_PLAYERS * 2

class PlayerData:
    def __init__(self, name):
        self.name = name
        self.week = -1
        self.total_times_player_was_guessed = 0
        self.correct_guesses = 0
        self.correctly_guessed = 0
        self.players_guessed_correctly = [] 
        self.players_guessed_incorrectly = []
        self.song_numbers = []
        self.all_guesses = []
        self.players_who_guessed_you_correct = []
        self.players_who_guessed_you_incorrect = [] # TODO: IMPLEMENT THIS
        self.player_people_thought_was_you = None # TODO: IMPLEMENT THIS

    def __str__(self):
        player_name = f"\nName:  {self.name}\n"
        music_league_week = f"Music League Week Number:  {self.week}\n"
        player_was_guessed = f"Times \"{self.name}\" was guessed this week: {self.total_times_player_was_guessed}\n"
        player_correct_guesses = f"Correct Guesses: {self.correct_guesses}\n"
        player_was_guessed_correctly = f"Times Correctly Guessed: {self.correctly_guessed}\n"
        guessed_others_correct_list = f"List of all players guessed correctly:\n\t{self.players_guessed_correctly}\n"
        guessed_others_wrong_list = f"List of all players guessed incorrectly:\n\t{self.players_guessed_incorrectly}\n"
        all_players_guessed = f"List of all players you guessed:\n\t{self.all_guesses}\n"
        who_guessed_you = f"List of all players who guessed you correctly:\n\t{self.players_who_guessed_you_correct}\n"
        songs_submitted = f"You submitted songs with indices: {self.song_numbers}"
        return player_name + music_league_week + player_was_guessed + player_correct_guesses + player_was_guessed_correctly + guessed_others_correct_list + guessed_others_wrong_list + all_players_guessed + who_guessed_you + songs_submitted
    
# Global dictionary which contains PlayerData objects
_players = {} # K: player name; V:List where each entry in the list corresponds to a PlayerData objects for a given week

#  
# Main function which runs the logic to parse and manipulate data
#
def format_music_league_data(music_data_file):

    # Use Pandas to parse the CSV into data frames
    df = pd.read_csv(music_data_file)

    # Map each player's name to a list which will eventually hold a PlayerData Object for each week
    player_names = df['Who are you?'].unique()
    for name in player_names: 
        _players[name] = []

    print('\nNames:\n', player_names)

# Week specific CSV parsing
    # TODO: can collect more data by using song name information
        # Then hitting Spotify's API to get more info about that song
    week_number = CURRENT_WEEK
    process_weekly_csv_data(week_number, df)

# Week Specific Player Data Parsing   
    # OTHER TODO's after I collect all the data:
    # Determine who was guessed correctly
        # the most
        # The least
    # Determine who the best guesser was

    # TODO: After collecting ALL data (including spotify)
        # FIND A WAY TO USE TENSORFLOW?!?
    process_weekly_player_data(week_number)


    print_player_info()
    # TODO: Maybe use MatPlotLib to create fun graphs for each players statistics
    return None

#
# Iterate through the PlayerData objects for the given week
# and determine more interesting info for each player
#
def process_weekly_player_data(week_number):
    # When I know what metadata I need then collect it
    # for curr_player_name in _players.keys():
    #     curr_player_datas_list = _players[curr_player_name]
    #     for curr_player_week_data in curr_player_datas_list:
    #         if curr_player_week_data.week == week_number:
    #             pass

        # OR replace above if statement with:
            # If player_data.week != week_number
                # continue
            # Else this is the correct week
                # do extra_parsing
                # break (break from nested while loop for this player since we have finished extra parsing for them)
    return

#
# Creates the PlayerData objects for each player for the given week.
# The PlayerData objects get stored in the _players dict
#
def process_weekly_csv_data(week_number, df):
    # Get the data that's related to the selected week
    current_week_df = df[df['What Round / Week Is It? (This gets updated every week, just select the only option)'] == week_number]

    # Create a dictionary for which songs each player submitted each week (Key: Player name; Value: A list of ints which correspond to the song number they submitted)
    player_songs_dict = current_week_df.set_index('Who are you?')['Which Songs Did You Submit? (Reminder: You submitted 2 songs)'].to_dict()
    print("Player Song Dict: ", player_songs_dict)

    # Parse each player's weekly data
    player_names = _players.keys()
    for player_name in player_names:
        print(f'\nGathering DATA for: {player_name}')

        if player_name not in player_songs_dict.keys():
            print(f"\n {player_name} did not fill out the form for this week, so no Player Data created for WEEK {week_number}")
            continue
        new_player_data = PlayerData(player_name)

        # Determine total times player was guessed this week (Historically can be more than 2... even though... whatever idc)
        counts = sum(current_week_df[column].str.count(player_name).sum() for column in PLAYER_GUESS_COLS) 
            # TODO: Update this to no longer use "PLAYER_GUESS_COLS", so we can remove this hard-coded list
            #   Maybe update the current_week_df to only have the columns with song guesses
            # THEN use this same kind of current_week_df[column].str.count(player_name).sum() logic
            # or something similar to it in order to get the correct count

        new_player_data.total_times_player_was_guessed = counts
        new_player_data.week = week_number

        # Select the row for this player's guesses for this week
        curr_player_info = current_week_df[current_week_df['Who are you?'] == player_name]
        correctly_guessed_players = []
        incorrectly_guessed_players = []
        all_people_guessed = []

        # Go column by column and assess if the guess was correct or not
        for col_idx, col_items in enumerate(curr_player_info.items()):
            # Skip reading extraneous (non-song guessing) column data
            adjusted_col_idx = col_idx - COLUMN_NUMBER_OFFSET
            if adjusted_col_idx < 0 or adjusted_col_idx >= NUM_SONGS_SUBMITTED_WEEKLY:
                continue
            
            name_of_guessed_player = col_items[1].item()

            # If this player did not fill out the form for this week then we don't know what songs they submitted, so skip
            if name_of_guessed_player not in player_songs_dict.keys():
                #print(f"Missing CSV data for player: {name_of_guessed_player}")
                continue
        
            all_people_guessed.append(name_of_guessed_player) # Depending on User sentiment... maybe move this above the above if statement

            guessed_players_songs = [int(x) for x in player_songs_dict[name_of_guessed_player].split(',')]
            song_guess_number = adjusted_col_idx + 1 # Songs are numbered (1-indexed)
            #print(f"Col idx: {song_guess_number}, \tItems: {name_of_guessed_player}\t Their actual song's: {guessed_players_songs}")

            # if you guessed who submitted this song correctly
            if song_guess_number in guessed_players_songs:
                correctly_guessed_players.append((name_of_guessed_player, song_guess_number))
                new_player_data.correct_guesses += 1
            else:
                incorrectly_guessed_players.append((name_of_guessed_player, song_guess_number))

        # Store which songs this user entered, and determine which of the other players guessed this player's songs correctly
        for curr_player_submitted_song in player_songs_dict[player_name].split(','):
            new_player_data.song_numbers.append(int(curr_player_submitted_song))

            adjusted_player_song_guess_col_idx = int(curr_player_submitted_song) + COLUMN_NUMBER_OFFSET - 1
            # print(f"TRYING TO GET COL: ", curr_player_submitted_song)
            # print(current_week_df.iloc[:, adjusted_player_song_guess_col_idx])

            player_song_guess = current_week_df.iloc[:, adjusted_player_song_guess_col_idx]
            correct_players_df = current_week_df[player_song_guess == player_name]['Who are you?']
            for correct_player in correct_players_df.tolist():
                new_player_data.players_who_guessed_you_correct.append((correct_player, int(curr_player_submitted_song)))
                new_player_data.correctly_guessed += 1

        # We finished parsing this player's data for this week, so update player's data & vars
        new_player_data.players_guessed_correctly = correctly_guessed_players
        new_player_data.players_guessed_incorrectly = incorrectly_guessed_players
        new_player_data.all_guesses = all_people_guessed
        _players[player_name].append(new_player_data)
    return

# Function to count occurrences of a string in a Series
def count_occurrences(series, string):
    return series.str.count(string).sum()

# Function to display information for each player
def print_player_info():
    for player_name in _players.keys():
        # Get all the PlayerData objects for a given player
        all_player_info = _players[player_name]
        print("\nDisplaying player info for ", player_name)
        print(f"Found {len(all_player_info)} PlayerData object(s)...")
        for player_data in all_player_info:
            print(player_data)
    return

# Run it
print("start")

  # Get the file path from command line arguments (sys.argv)
file_path = sys.argv[1]
format_music_league_data(file_path)

