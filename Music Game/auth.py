import sys
from base.common import gather_input

class Authorization:
    """This class deals with the authorization menu (Register or Log in)

    Attributes
    ------------
    cache: :class:`Cache`
        An already defined cache object that manages the file where 
        authentication is kept.
    score_cache: :class:`Cache`
        An already defined cache object that manages the file where scores are kept.

    """
    def __init__(self, cache, score_cache):
        self.cache = cache
        self.score = score_cache
    
    def get_authorization(self):
        """
        Shows an authorization menu used to determine 
        whether the user wants to log in or register and deals with the input.
        """
        while True:
            option = gather_input("Authorization:\n- Register [0]\n- Log In [1]\n- Exit [2]\n", req=[0, 1, 2])

            if option == 2:
                sys.exit(1)
            
            if not option:
                username = gather_input("Username: ", datatype=str, notreq=[""])
                if self.cache.cached(username): # checking if username is already taken
                    print("Username is already taken! Sorry about that.\n")
                    continue
                password = gather_input("Password: ", datatype=str, notreq=[""])
                print(f"You have successfully registered as {username}!")
                self.cache.store({username: password}) # registering them and remembering for next time
                self.score.store({username: {"total_score": 0, "highest_score": 0}})
                break
            elif option:
                username = input("Username: ")
                if not self.cache.cached(username): # checking if username doesnt exist
                    print("Username does not exist.\n")
                    continue
                password = input("Password: ")
                if self.cache.get(username) == password:
                    print(f"You have successfully logged in as {username}!")
                    break
                else:
                    print("Incorrect password.\n")
                    continue
        return (username, password)