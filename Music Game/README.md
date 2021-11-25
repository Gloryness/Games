## Music Game

### How To Play
- A login menu with Register, Log In and Exit options will be shown at first. 
- Pretty self explanatory, just register if you haven't created an account yet or want to create another and then log in with the correct credentials. 
- You will then be taken a the main menu (or game menu) where the following options will be shown:
  - Play The Game
  - View your own score history
  - View top 5 best scores from all players (not total scores accumulated - the best session scores)
  - Purge account
  - Delete account
  - Exit
- To play the game, the artists of a song will be given to you however the song name will be filtered and only the first letter of each word will be shown.
  - Example: `Come & Go` --> `C___ & G_`, `34 + 35` --> `3_ + 3_` and then you must guess the actual song name (not case sensitive)
  - Correct on first attempt: 3 points
  - Correct on second attempt: 1 point
  - You will have 2 attempts to guess the song name before the game ends. If you guess correctly, you will be asked if you want to continue and if you want to then the session score will be saved otherwise it will not be saved.

### Backstory
Initially, this was a project I was tasked with (out of 3) in a computer science lesson and I thought this would be the most fun to create because although the instructions were pretty basic, one of them was "Store a list of song names and artists in an external file" and I instantly new what I was going to do. Instead of hardcoding each song and artist I will instead dynamically create the list by using spotify's API and getting the top 10 tracks for some popular well known artists. (I originally got the top 25 songs monthly, but literally 90% of the artists I had no clue they existed).

### Requirements
- Required external modules that are installable using pip:
  - `requests`
- If you wish to have it update `top-artists.json`, a valid bearer token must be given in `cache/token.txt`.
  - Redeemable from https://developer.spotify.com/console/get-artist-top-tracks/ but must have a spotify account to get token
