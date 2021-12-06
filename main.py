"""My Integration Project: A Musical Chord Transposer"""
__author__ = "Thomas Gargiulo"

# This program is a Musical Chord Progression Transposition Tool.
# The user will input a chord or series of chords, and then input how many
# "semi-tones" or "steps" to transpose the chords.

# If you are unfamiliar with this aspect of musical theory, this program
# essentially takes the user input, identifies it as a part of the list in
# argument "chord_list", and then substitutes it with the desired value to the
# left or right inside of "chord_list" or "flats_list" depending on the input.
# The desired value loops around to the opposite end of the list and continues
# depending on the amount of steps inputted by the user.

# Referenced POGILs #16-18
# Referenced Think Python: How to Think Like a Computer Scientist
# 2nd Edition (Ch.5, Ch.6, Ch.10)
# Referenced https://www.youtube.com/watch?v=r526yum0EYQ and other CS Dojo
# Python Tutorials.
# Formatting advice was provided by Professor Vanselow and
# Katarya Johnson-Williams. 

# This is the list used for transposing "sharp" and/or natural user inputs.
chord_list = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
# This is the list used for transposing "flat" and/or natural user inputs.
flats_list = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]


def is_note_valid(chord):
    """function for determining whether the chords that are inputted
    are valid (inside of "chord_list").
    :param chord - user input that is going to be transposed to element in
    chord_list or flats_list.
    :return - validates or denies user input
    """
    if not chord or chord[0] not in chord_list:
        return False

    # The if statement checks for the initial character in the input following
    # the chord name; it returns a false input if this is not included.
    if len(chord) > 1:
        if chord[1] not in ["#", "b", "m", "d", "a", "1", "7"]:
            return False

    # This check ensures that if there are characters trailing a valid
    # note, those characters construct a valid chord type and/or accidental
    # (ex: major or minor, flat "b" or sharp "#").
    if len(chord) > 2:
        if chord[1] in ["#", "b"]:
            accidental = chord[2:]
        else:
            accidental = chord[1:]
        # These are the chord types that will be accepted as input along with
        # the actual note name.
        if accidental not in ["maj", "min", "7", "maj7", "min7", "dim", "aug",
                              "min7b5", "13"]:
            return False
    return True


def transpose(user_notes, tones, direction):
    """This function takes the user input from the main function and shifts
    the input by the desired amount.
    :param user_notes - empty list that stores user input to be transposed
    :param tones - amount of semi-tones (or elements) to transpose by
    :param direction - whether the user wants to shift the chords up or down
    (right or left in the list)
    :return: element(s) in list that represent(s) the requested transposed
    chord name(s).
    """
    # This argument stores previous user input as an argument for calculation.
    transposed = []
    # This loop iterates through all input notes and transposes them the
    # desired number of steps, up or down.
    for x in range(len(user_notes)):
        # This conditional determines whether or not there is a sharp or
        # a flat in order to grab the base note.
        if len(user_notes[x]) > 1 and user_notes[x][1] in ["#", "b"]:
            curr_note = user_notes[x][0:2]
        else:
            curr_note = user_notes[x][0]
        # This argument identifies user input in "chord_list" and sets
        # that as the argument to be transposed.
        if len(user_notes[x]) > 1 and user_notes[x][1] == "#":
            target_index = chord_list.index(curr_note)
            if direction == "up":
                # This conditional takes the number of tones and selects
                # positions in the list from left/right of starting position.
                transposed.append(chord_list[(target_index + int(tones)) % 12])
                # This check determines ensures the addition of the chord type
                # to the end of the transposed chord value.
                if len(user_notes[x]) > 1:
                    if user_notes[x][1] == "#":
                        transposed[-1] += user_notes[x][2:]
                    else:
                        transposed[-1] += user_notes[x][1:]
            # This is the same conditional as "direction == up", but for the
            # "down" direction input.
            elif direction == "down":
                transposed.append(chord_list[target_index - int(tones)])
                if len(user_notes[x]) > 1:
                    if user_notes[x][1] == "#":
                        transposed[-1] += user_notes[x][2:]
                    else:
                        transposed[-1] += user_notes[x][1:]
        # The contents of this else statement complete the same transposition,
        # computation, and checks as above for but for "flat" inputs.
        else:
            target_index = flats_list.index(curr_note)
            if direction == "up":
                transposed.append(flats_list[(target_index + int(tones)) % 12])
                if len(user_notes[x]) > 1:
                    if user_notes[x][1] == "b":
                        transposed[-1] += user_notes[x][2:]
                    else:
                        transposed[-1] += user_notes[x][1:]
            elif direction == "down":
                transposed.append(flats_list[target_index - int(tones)])
                if len(user_notes[x]) > 1:
                    if user_notes[x][1] == "b":
                        transposed[-1] += user_notes[x][2:]
                    else:
                        transposed[-1] += user_notes[x][1:]
    return transposed


def main():
    """This is the main function, where the user is asked for multiple
    inputs to clarify the amount and type of chords they desire to
    transpose, the direction and amount by which they want to transpose the
    inputted chords, whether their inputs appear correct. Finally, the
    result is printed and the user can choose to end the program or
    start again.
    """
    print("Hello Traveler! Welcome to TEG's Chord Transposer", end="...")
    print("\nThis tool will take any chord or chord progression and transpose "
          "it by the degrees of your choosing.\n")
    print("Input the chord names one at a time, for as many chords as you "
          "like.")
    print("You can choose from the following: A, A# or Bb, B, C, C# or Db, D, "
          "D# or Eb, E, F, F# or Gb, G, G# or Ab")
    print("You can also add a chord type at the end if you like (ex: Amaj, "
          "Bmin, etc.)\n")
    print("If you choose to add a chord type, please only select one of the "
          "following: maj, min, 7, maj7, min7, dim, aug, min7b5, 13\n")

    user_notes = []
    while True:
        # This statement takes user input and assigns it to the "chord"
        # argument.
        chord = input("Please enter a note/chord [ex: Amaj, F#min, B, etc.]\n"
                      "Enter 'stop' to finish input and 'clear' "
                      "to empty list and restart: ")
        # Input stop to stop inputting, input clear to empty user input list
        if chord == "stop":
            if not len(user_notes):
                while chord == "stop":
                    chord = input("Please input at least one chord "
                                  "prior to stopping: ")
            break
        # If the user inputs clear, the "user_notes" list will be emptied and
        # new input can be stored in the list.
        elif chord == "clear":
            user_notes = []
            continue
        # This is a call to the function is_note_valid; it checks if the input
        # is valid or not.
        while not is_note_valid(chord):
            chord = input("Input is not valid, please enter a valid note: ")
        # The else statement places chords into empty list "user_notes".
        else:
            user_notes.append(chord)
    print()
    direction_is_valid = False
    direction = ""
    # This check verifies that the user input is up or down, and also rejects
    # invalid inputs.
    while not direction_is_valid:
        direction = input("Would you like to shift the chords up or down?: ")
        if direction == "up" or direction == "down":
            direction_is_valid = True
        else:
            print("Direction is invalid, Please input 'up' or 'down'")
    # Semitones are the smallest interval between notes in music.
    # (ex. A to A#, B to C, etc.)
    # This argument prompts the user to provide the amount of semi-tones by
    # which they want to transpose their initial chord values.
    tones_is_valid = False
    tones = ""
    # This check ensures that the user provides a positive integer value for
    # their input, and rejects non-numerical values.
    while not tones_is_valid:
        tones = input("How many semitones would you like to shift " +
                      direction + "? (Input Positive Integer): ")
        if tones.isnumeric():
            tones_is_valid = True
        else:
            print("Semitone input is invalid, please input a positive integer "
                  "amount")
    # Assuming the input chord(s) start(s) at element 0, the amount of
    # semi-tones it takes to return to the same note-name is 12.
    # This is called an octave in music, it is the same note value occurring 12
    # semitones higher or lower in pitch.
    # The "oct_shift" variable divides tone by an octave to calculate the
    # number of octaves user wants to shift (1 octave = 12 semitones).
    oct_shift = int(int(tones) / 12)
    # "Semi_result" calculates the remainder of the octave calculation
    # (the number of semitones asked for past the octave number).
    semi_result = int(tones) % 12
    print("\nYou want to shift:", *user_notes)
    print(direction, "by", oct_shift, "octaves and", semi_result,
          "semitones\n")
    answer_is_valid = False
    # This is a while loop for checking the user's answer and guiding the user
    # to the next appropriate position. It also detects any invalid input.
    while not answer_is_valid:
        answer = input("Is this correct? (Input yes or no): ")
        if answer == "yes":
            answer_is_valid = True
        elif answer == "no":
            main()
        elif answer != "yes" or "no":
            print("Please input yes or no:")
    result = transpose(user_notes, semi_result, direction)
    # "*result" prints out the result of all of the transposed items in the
    # "user_notes" list.
    print("\n", *result)
    print("")

    # This is the final user input for determining whether to run the program
    # again, or to end running the program.
    final = input("Would you like to transpose again? (Input yes or no): ")
    while final not in ["yes", "no"]:
        final = input("Please input yes or no: ")
        # If the user answers yes, the main function is called and the program
        # runs again.
    if final == "yes":
        main()
    # If the user answers "no", the program ends.
    elif final == "no":
        # These print statements demonstrate unused math operators.
        print()
        print("Here are some math equations!")
        print("\n16 + 3 =", 16 + 3)
        print("16 ** 3 =", 16 ** 3)
        print("16 * 3 =", 16 * 3)
        print("16 // 3 =", 16 // 3)
        print("\nEnd of the Chord Transposer! " * 10)


# Call to main function
main()
