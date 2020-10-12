import random
import keyword
import decimal
import string
import time

rc = random.choice
rd = random.randint

class Games:
    """
    This class holds all the games you can play.
    """
    def __init__(self):
        self.games = [eval(f'self.{function}', {"self": self}) # Since it cannot find "self", we must provide it manually.
                      for function in filter(lambda x: not (x.startswith('_')), dir(Games))]
                      # Finding all methods that don't start with '_' (dunder methods or private methods)

    def __iter__(self):
        return iter(self.games)

    def __len__(self):
        return len(self.games)

    def _process_output(self, output, output_result, correct_answers, is_second=False):
        for item in output.items():
            if is_second:
                if type(item[1]) == list:
                    if str(item[1]) == str(output_result):
                        correct_answers.append(item[0])
            else:
                if str(output_result) == str(item[1]):
                    correct_answers.append(item[0])

    def play_guess_number(self, start=1, end=100, ask_for_input=False):
        """
        Guess the random number game.

        :param start: Range start value
        :param end: Range end value
        :param ask_for_input: A boolean that if true will use input to get the start and end values.
        """
        print("\n-- Guess The Number --")
        if ask_for_input:
            while True:
                try:
                    start = int(input("Range start value: "))
                    end = int(input("Range end value: "))
                    break
                except ValueError:
                    print("Incorrect input, try again.")
                    continue

        if not (isinstance(start, int) and isinstance(end, int)):
            raise ValueError('Start and End values must be an integer.')

        print(f"\nA random number has been generated between {start} and {end}.", "Your task is to guess it. Good luck!\n", sep='\n')
        answer = rd(start, end)

        # Variables we're using to count the amount of times for something.
        total = 0
        lower = 0
        higher = 0

        guessed = False
        while not guessed:
            try:
                guess = int(input("Guess the number: "))
            except ValueError:
                print("Incorrect input, try again.")
                continue
            total += 1
            if guess > answer:
                lower += 1
                print("Lower...")
            elif guess < answer:
                higher += 1
                print("Higher...")
            elif guess == answer:
                print("Correct!")
                print(f"Total guessed that were higher: {higher}")
                print(f"Total guessed that were lower: {lower}")
                print(f"Total guessed: {total}")

                time.sleep(1.0)
                guessed = True

    def play_guess_used_function(self, input_type=str):
        """
        Guess a function that was used to convert X to Y.

        :param input_type: The input type. One of [str, int, float, list, tuple]

        Examples:
            [1, 3, 2] ----> [1, 2, 3]
            And then you should guess the function used to get the output.
            In this case, the function used was 'sorted'.
            If there was 2 or more possible functions that could've been used, then either one will work as the answer!
        """
        print(f"\n-- Guess the function that was used to convert X to Y --\n")
        if not isinstance(input_type(), (str, int, float, list, tuple)):
            raise ValueError("Incorrect value type.")

        keywords = [i for i in filter(lambda x: not (any(map(x.__contains__, [
                                                                        'Error', 'Warning', # Remove any built-in that contains these.
                                                                        'Stop', 'System', 'exec', 'property', 'copyright', 'credits',
                                                                        'Not', 'Keyboard', 'eval', 'compile', 'object', 'license',
                                                                        'Exception', '__', 'slice', 'open', 'quit', 'super',
                                                                        'help', 'dir', 'method', 'input', 'exit', 'open', 'byte'
                                                                       ] + keyword.kwlist))), dir(__builtins__))
        ]

        output = {}
        correct_answers = []
        is_second = False

        if type(input_type()) == str:
            keywords.append('list')
            # You could say this is an inefficient way of doing it, but I can't really use the requests
            # module in this case (builtin modules only) soo it makes it a little awkward to try and get random phrases.
            input_ = rc([
                'Hello', 'Hello World!', 'Python', '12 34 56 78 90',
                'This is the input..', 'An elephant has ears now?? Impossible.',
                'I didn\'t see u there', 'Fustrating, right?',
                'It\'s worth it.', 'I think?', 'This is TOTALLY a list...'
            ] + [''.join([rc(string.ascii_letters*4 + string.punctuation) for i in range(rd(4, 15))]) for i in range(10)])

            for function in keywords:
                if try_convert(f'{function}({ascii(input_)})'):
                    result = eval(f'{function}({ascii(input_)})')
                    if str(result).__contains__('object'):
                        if function in ['sorted', 'reversed']:
                            result = ''.join(list(result))
                        else:
                            result = list(result)
                    elif str(result).__contains__(function):
                        result = str(result).strip(function + '()')
                    output[function] = result


            output_result = output[rc(list(output.keys()))]

            self._process_output(output, output_result, correct_answers)

        elif isinstance(input_type(), (int, float)):
            if type(input_type()) == float:
                input_ = rc([float(decimal.Decimal(random.randrange(30, 12234))/100) for i in range(rd(4, 22))])
                second_param = rc([float(decimal.Decimal(random.randrange(30, 5674))/100) for i in range(rd(4, 44))])
            else:
                input_ = rc([rd(1, rd(40, 100)) for i in range(rd(4, 22))])
                second_param = rc([rd(1, rd(40, 123)) for i in range(rd(4, 44))])

            for function in keywords:
                func_no_params = f'{function}({input_})'
                func_params = f'{function}({input_}, {second_param})'
                if (a := try_convert(func_no_params)) or (try_convert(func_params)):
                    if a:
                        is_second = False
                    else:
                        is_second = True
                    result = eval(func_params if is_second else func_no_params)
                    if 'range' in str(result):
                        result = list(result)
                    output[function] = repr(result) if function in ['repr', 'ascii', 'chr'] else [result, "params"] if is_second else result
                    is_second = False

            output_result = output[rc(list(output.keys()))]
            if type(output_result) == list:
                try:
                    if output_result[1] == 'params':
                        is_second = True
                    else:
                        is_second = False
                except:
                    is_second = False

            self._process_output(output, output_result, correct_answers, is_second=is_second)

        elif isinstance(input_type(), (list, tuple)):
            keywords.remove('iter'); keywords.remove('map'); keywords.remove('filter')
            keywords.append('list')

            input_ = rc([
                # Random numbers and strings OR only random numbers OR only strings
                [rc([''.join([rc(string.ascii_letters*4 + string.punctuation) for i in range(rd(4, 15))]), rd(1, 100)]) for i in range(rd(3, 10))],
                [rc([rd(1, 20), rd(20, 50), rd(50, 100), rd(100, 1000)]) for i in range(rd(3, 15))],
                [''.join([rc(string.ascii_letters*4 + string.punctuation) for i in range(rd(4, 15))]) for i in range(rd(2, 6))]
            ])
            if type(input_type()) == tuple: # Converting to tuple is the input_type is a tuple.
                input_ = tuple(input_)

            for function in keywords:
                func_no_params = f'{function}({input_})'
                if try_convert(func_no_params):
                    result = eval(func_no_params)
                    if str(result).__contains__('object'):
                        result = list(result)
                    if function == 'frozenset':
                        result = str(result).strip(f'{function}()')
                    output[function] = repr(result) if function in ['repr', 'ascii'] else result

            output_result = output[rc(list(output.keys()))]

            self._process_output(output, output_result, correct_answers)

        print([input_ if not is_second else (input_, second_param)][0], '--------------------------->',
              [output_result if not is_second else output_result[0]][0])
        tries = 5
        while tries > 0:
            answer = input("Name the function used to get the result: ").lower()
            if answer in correct_answers:
                print("Correct!")
                break
            else:
                tries -= 1
                if not bool(tries):
                    print(f"The correct answer was {' or '.join(correct_answers)}")
                else:
                    print(f"Incorrect. {tries} tries left!")
                    if tries == 1:
                        print(f"Hint: One of the functions starts "
                              f"with \'{correct_answers[0] if type(correct_answers) == str else correct_answers[0][0]}\'.")

def loop(tasks=1, breaks=0, *args, **kwargs):
    """
    Loop a function X amount of times

    :param tasks: Amount of times to loop the function
    :param breaks: The amount of time to wait between each loop.
    """
    def wrapper(original_func, *args, **kwargs):
        for i in range(tasks):
            original_func(*args, **kwargs)
            time.sleep(breaks)
    return wrapper

def askHowManyLoops(game):
    while True:
        try:
            loop_times = int(input(f"\nHow many times would you like to play {game}? "))
            return loop_times
        except ValueError:
            print("Incorrect response, try again.")
            continue

def backToMenu():
    while True:
        try:
            back = int(input("\nBack to Menu?\nNo [0]\nYes [1]\n"))
        except ValueError:
            print("Incorrect input, try again."); continue
        if bool(back):
            return True
        else:
            print("Goodbye!")
            return False

def openMenu():
    while True:
        print("\n--- Menu ---")
        try:
            menu_option = int(input("Guess the random number [1]\nGuess the function that was used [2]\nPlay all [3]\nExit [4]\n"))
        except ValueError:
            print("Invalid response. Try again."); continue

        if menu_option == 1:
            loop_times = askHowManyLoops('Guess The Number')

            game = Games()

            @loop(tasks=loop_times, breaks=1)
            def play():
                game.play_guess_number(ask_for_input=True)

        elif menu_option == 2:
            loop_times = askHowManyLoops('Guess The Function')

            game = Games()

            @loop(tasks=loop_times, breaks=1)
            def play():
                game.play_guess_used_function(rc([str, int, float, list, tuple]))

        elif menu_option == 3:
            game = iter(Games()) # iterating through all the games
            for _ in range(len(Games())):
                nextiter = next(game)

                if 'play_guess_number' in str(nextiter):
                    loop_times = askHowManyLoops('Guess The Number')

                    @loop(tasks=loop_times, breaks=1.20)
                    def play():
                        nextiter(ask_for_input=True)

                elif 'play_guess_used_function' in str(nextiter):
                    loop_times = askHowManyLoops('Guess The Function')

                    @loop(tasks=loop_times, breaks=1.20)
                    def play():
                        nextiter(rc([str, int, float, list, tuple]))

                else:
                    nextiter()

        elif menu_option == 4:
            print("Goodbye!")
            return

        else:
            print("I don't know that option. Sorry.")
            time.sleep(0.75)
            continue

        back = backToMenu()
        if not back:
            break

def try_convert(evaluation):
    """
    Returns True or False depending if the evaluation was a success or not.
    Example:
         >>> try_convert("int('f')")
         >>> False
    """
    try:
        eval(evaluation)
    except:
        return False
    return True

if __name__ == '__main__':
    print("-- Welcome to the guessing game! --")

    while True:
        try:
            option = int(input("Would you like to continue and choose what to play?\nNo [0]\nYes [1]\n"))
        except ValueError:
            print("Invalid response. Try again."); continue

        if bool(option):
            openMenu()
            break
        else:
            print("Goodbye!")
            break
