import sys
import random
from base.common import gather_input
from base.cache import Cache

class Menu:
    """This class manages the frontend and backend of the Game Menu.
    
    Attributes
    ------------
    username: :class:`str`
        The username of the player who is currently logged in.
    music_data: :class:`dict`
        A dictionary previously generated formatted like {song: artist(s)}
    """
    def __init__(self, username, music_data):
        self.username = username
        self.songs = music_data
    
    def play_game(self):
        score = 0
        while True:
            if len(self.songs) == 0:
                print("\nGG! You've successfully guessed all the songs.")
                return score
            song, artists = random.choice(list(self.songs.items()))
            del self.songs[song]
            for new_score in range(3, 0, -2): # First loop: 3, second loop: 1 to represent the score to give if guessed correctly on that iteration.
                song_name_hidden = ' '.join(map(lambda k: ''.join([i if num == 0 else '_' for num, i in enumerate(k)]), song.split())) # it will only show the first letter of each word
                answer = input(f"\nArtist(s): {artists}\n" \
                            f"HIDDEN Song name: {song_name_hidden}\n" \
                            "Answer: ")
                if answer.lower().strip() == song.lower().strip():
                    print(f"\nCorrect! You have gained +{new_score} score.")
                    score += new_score # adding to total score gained this session
                    print(f"Session Score: {score}")
                    play_again = gather_input("\nWant to play another round?\n- Yes [1]\n- No [0]\n", req=[0, 1])
                    if play_again:
                        break
                    elif not play_again:
                        return score
                else:
                    print("Incorrect.")
            else: # If the user ran out of guesses
                print(f"\nYou ran out of guesses!\nThe song name was \"{song}\"")
                return score
    
    def start(self):
        while True:
            option = gather_input("\nMenu:\n- Play Music Game [0]\n- View score history [1]\n- View top 5 best scores [2]\n- Delete account [3]\n- Purge account [4]\n- Exit [5]\n", req=[0, 1, 2, 3, 4, 5])
            
            if option == 5: # EXIT option
                sys.exit(1)
            
            elif option == 4: # PURGE ACCOUNT option
                confirmation = gather_input("Are you SURE that you want to purge your account?\nThis action will set your total score and highest score to 0 and cannot be reversed.\n- YES [0]\n- NO [1]\n", req=[0, 1])
                if not confirmation: # YES option
                    score_cache = Cache("players.json")
                    score_cache.store({self.username: {"total_score": 0, "highest_score": 0}})
                    print("Successfully purged account.\n")
                elif confirmation: # NO option
                    continue

            elif option == 3: # DELETE ACCOUNT option
                confirmation = gather_input("Are you SURE that you want to delete your account including your score history?\nThis action cannot be reversed.\n- YES [0]\n- NO [1]\n", req=[0, 1])
                if not confirmation: # YES option
                    auth_cache = Cache("authentication.json")
                    score_cache = Cache("players.json")
                    auth_cache.remove(self.username)
                    score_cache.remove(self.username)
                    print("Successfully deleted account.\n")
                    return 'deleted'
                elif confirmation: # NO option
                    continue
            
            elif option == 2: # VIEW TOP 5 BEST SCORES option
                print("\n-- Top 5 best scores --")
                score_cache = list(sorted(Cache("players.json").all().items(), key=lambda k: k[1]['highest_score'], reverse=True))
                for num in range(1, 6):
                    try:
                        score_cache[num-1] # testing if Xth index is accessible
                    except IndexError:
                        print("-- Not enough users --")
                        break
                    current_user = score_cache[num-1]
                    print(f"{num}. {current_user[0]}: {current_user[1]['highest_score']}")

            elif option: # VIEW SCORE HISTORY option
                score = Cache("players.json").all()[self.username]
                print(f"\nTotal score: {score['total_score']}\nHighest score: {score['highest_score']}")
            
            elif not option: # PLAY MUSIC GAME option
                score_accumulated = self.play_game()
                score = Cache("players.json")
                current_total_score = score.get(self.username, 'total_score')
                current_highest_score = score.get(self.username, 'highest_score')
                if score_accumulated > current_highest_score:
                    print(f"Well done! You've achieved a new high score of {score_accumulated}.")
                highest_score = score_accumulated if score_accumulated > current_highest_score else current_highest_score
                score.store(
                    {
                    self.username: {
                        'total_score': current_total_score + score_accumulated,
                        'highest_score': highest_score
                        }
                    }
                )