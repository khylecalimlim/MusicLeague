###
### Represents formatted data for ONE player for ONE week of guessing data
###
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
