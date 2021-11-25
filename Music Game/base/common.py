import re
import requests

def gather_input(input_string, datatype=int, req=[], notreq=[]):
    """
    Create an input and return the users input - it will catch for invalid inputs.

    Parameters
    -----------
    input_string: :class:`str`
        This will be passed into the builtin input() function. 
    datatype: Any
        The data type to convert the input into - if it cannot be converted it will ask the user again.
    req: :class:`list`
        A list with all possible inputs and if the user input is not a match it will ask again.
        - If [], anything is allowed.
    notreq: :class:`list`
        A list with all inputs that should NOT be allowed
        - If [], nothing will happen.
    
    Returns
    -------
    Any
        The input that was received from the user. 
    """
    while True:
        try: menu = datatype(input(input_string).strip())
        except:
            print("Invalid input.")
            continue
        if req != []:
            if menu not in req:
                print("Invalid input.")
                continue
        elif notreq != []:
            if menu in notreq:
                print("Invalid input.")
                continue
        return menu

def fetch_artists_top_tracks(*artist_ids):
    """

    Returns the top 10 tracks from an artist or multiple artists.

    Parameters
    -----------
    artist_ids: List[:class:`str`]
        A list of artist IDs to fetch the top 10 tracks from.
        Artist IDs are not the name of the artist - it is their spotify ID which is
        accessible by clicking 'Copy link to artist' on their spotify profile.

    Returns
    -------
    :class:`dict`
        The dictionary that was generated. Formatted like {song: artist(s)}
    :class:`int`
        A 0 will be returned if the bearer token was outdated.
    """
    with open("cache/token.txt") as f: # retreiving bearer token stored in text file
        token = f.read().strip()

    url = "https://api.spotify.com/v1/artists/%s/top-tracks?market=ES"
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
    }
    
    new_data = {}
    for artist_id in artist_ids:
        try:
            data = requests.get(url % artist_id, headers=headers).json()['tracks']
        except:
            print("BEARER TOKEN OUTDATED - UNABLE TO FETCH DATA FROM SPOTIFY API\n")
            return 0
            
        for value in data: # only including X entries (songs)
            # removing the irrelevant information from the song name such as "remix" or random open and closed brackets
            track_name = value['name'].replace("Remix", "")
            artists = ', '.join([artist['name'] for artist in value['artists']])
            if ' - ' in track_name:
                track_name = track_name[:track_name.index(" - ")]
            if track_name == '34+35':
                new_data[' + '.join(track_name.split('+'))] = artists
                continue
            if irrelevant := re.search('\(.+\)', track_name):
                track_name = track_name.replace(irrelevant[0], "")
            track_name = ' '.join(map(lambda word: ''.join([letter if letter.isalpha() or letter.isnumeric() or letter == "&" else '' for letter in word]), track_name.split()))
            new_data[track_name.strip()] = artists
            # including all artists involved seperated by a ,
    return new_data