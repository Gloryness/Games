from base.cache import Cache
from base.common import fetch_artists_top_tracks
from auth import Authorization
from game import Menu

if __name__ == '__main__':
    artists = {
        "Taylor Swift": "06HL4z0CvFAxyc27GXpf02",
        "Charlie Puth": "6VuMaDnrHyPL1p4EHjYLi7",
        "Marshmello": "64KEffDW9EtZ1y2vBYgq8T",
        "Ariana Grande": "66CXWjxzNUsdJxJ2JdwvnR"
    }

    top_artists = fetch_artists_top_tracks(*list(artists.values()))
    music_cache = Cache("top-artists.json")
    if top_artists: # setting a condition as sometimes it wont return a value (in that case it's okay, it's already stored)
        music_cache.clear()
        music_cache.store(top_artists) # STORING songs with the artists in a json file
    
    auth_cache = Cache("authentication.json")
    player_cache = Cache("players.json")

    auth_required = True
    while True:
        if auth_required:
            auth_setup = Authorization(auth_cache, player_cache)
            username, password = auth_setup.get_authorization()
            auth_required = False

        menu = Menu(username, music_cache.all())
        out = menu.start()

        if out == 'continue':
            continue
        elif out == 'done':
            print("Logging out...")
            break
        elif out == 'deleted':
            auth_required = True
            continue