import json
import os

class Cache:
    """A class that manages file operations revolving around JSON files.
    
    Attributes
    ------------
    file: :class:`str`
        The name of the JSON file. The path is already given.
    """
    def __init__(self, file):
        self.filename = f'cache/{file}'

        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({}, f, indent=3)

    def _test_if_empty(self):
        with open(self.filename) as f:
            try:
                data = json.load(f)
            except:  # if the file is somehow 0 bytes
                with open(self.filename, 'w') as ff:
                    data = json.loads('{"profiles": []}')
                    json.dump(data, ff, indent=3)
                    return True
        return False

    def cached(self, key):
        """
        Check if an item is in the database.
        """
        empty = self._test_if_empty()
        if empty: return False

        with open(self.filename) as f:
            data = json.load(f)
        if key in data.keys():
            return True
        return False

    def all(self):
        """
        Return the whole database.
        """
        empty = self._test_if_empty()
        if empty: return {}

        with open(self.filename) as f:
            data = json.load(f)

        return data

    def store(self, dictionary):
        """
        Add to the database.
        """
        empty = self._test_if_empty()
        if empty: return {}

        with open(self.filename) as f:
            data = json.load(f)

        data.update(dictionary)

        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=3)
    
    def remove(self, key):
        """
        Remove a key from the database.
        If not found, nothing will happen.
        """
        empty = self._test_if_empty()
        if empty: return {}

        with open(self.filename) as f:
            data = json.load(f)

        if key not in data:
            return
        del data[key]

        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=3)

    def get(self, key, *keys):
        """
        Retrieve values in the database.
        :param key: A required key to get from the database
        :param keys: Optional other keys to get stacking up from the first key
        For example: get('1', '2', 3) is equal to data['1']['2'][3]
        """
        keys = list(keys)
        keys.insert(0, key)
        with open(self.filename) as f:
            data = json.load(f)
        if not self.cached(key):
            return ""
        evalulated = 'data' + ''.join([f'[{ascii(keyy) if type(keyy) == str else keyy}]' for keyy in keys])
        return eval(evalulated)
    
    def clear(self):
        """
        Clear the database.
        """
        empty = self._test_if_empty()
        if empty: return {}

        data = {}

        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=3)