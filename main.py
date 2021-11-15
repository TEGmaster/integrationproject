# Thomas Gargiulo

# This program is going to be a Musical Chord Progression Transposition Tool.
# The user will input a chord or series of chords, and then input how many "steps" to transpose the chords.

# If you are unfamiliar with this aspect of musical theory, this program essentially takes the user input, identifies
# it as a part of the list in argument "chordlist", and then substitutes it with the desired value to the left or right
# inside of "chordlist". The desired value loops around to the opposite end of the list and continues depending on the
# amount of steps inputted by the user.

# There are still certain technical music features I need or would like to add to this program, however for the purpose
# of this sprint they are unnecessary and I will add them in for the final project submission.
# (For example, Bb = A#, so incorporating a list of equivalent flats instead of sharps and transposing those in the
# same way.)

# Referenced POGILs #16-18
# Referenced Think Python: How to Think Like a Computer Scientist, 2nd Edition (Ch.5, Ch.6, Ch.10)
# Referenced https://www.youtube.com/watch?v=r526yum0EYQ and other CS Dojo Python Tutorials

# Introduction and explanation for the user.
print("Hello Traveler! Welcome to TEG's Chord Transposer", end="...")
print("\nThis tool will take any chord or chord progression and transpose it by the degrees of your choosing.\n")
print("Input the chord names one at a time, for as many chords as you like.")
print("You can choose from A, A#, B, C, D, D#, E, F, F#, G, and G#")
print("You can also add a chord name at the end if you like (ex: Amaj, Bmin, etc.)\n")

chordlist = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


# function definition for determining whether the chord(s) that are inputted are valid (inside of "chordlist")
def is_note_valid(chords):
    is_valid = False
    for x in range(0, 12):
        if chordlist[x] == chords:
            is_valid = True
            return is_valid
    return is_valid


# function definition that takes the user input and shifts the
def transpose(user_notes, tones, direction):
    transposed = []
    for x in range(0, len(user_notes)):
        # Stores previous user input list as an argument for calculation
        curr_note = user_notes[x][0]
        # Identifies user input in "chordlist" and sets that as the argument to be transposed
        target_index = chordlist.index(curr_note)
        if direction == "up":
            # in the event has entered a chord type, chord type needs to be attached to the transposed note.
            # this if/else statement takes the "tones" amount and selects positions in the list from left to right
            # from the starting input position.
            # len allows chord information input after the list value to be carried with the value.
            if len(user_notes[x]) > 1:
                transposed.append(chordlist[target_index + int(tones)] + user_notes[x][1: len(user_notes[x])])
            else:
                transposed.append(chordlist[target_index + int(tones)])
        elif direction == "down":
            # this if/else statement takes the "tones" amount and selects positions in the list from right to left
            # from the starting input position.
            if len(user_notes[x]) > 1:
                transposed.append(chordlist[target_index - int(tones)] + user_notes[x][1: len(user_notes[x])])
            else:
                transposed.append(chordlist[target_index - int(tones)])
    return transposed


def main():
    # empty list to store user input
    user_notes = []
    user_choice = True
    print("Please enter a note/chord [ex: Amaj, F#min, B, etc.]")
    while user_choice:
        # Takes user input and assigns it to "chords" argument
        chords = input("Enter 'stop' to finish input and 'clear' to empty list and restart: ")
        # Input stop to stop inputting, input clear to empty user input list
        if chords == "stop":
            user_choice = False
        elif chords == "clear":
            user_notes = []
        # Call to is_note_valid, checks if input is valid or not
        elif not is_note_valid(chords[0]):
            print(chords, "input is not valid, please enter a valid note")
        # Places chords into empty list "user_notes"
        else:
            user_notes.append(chords)
    print()
    direction_is_valid = False
    direction = ""
    # Verifies that the user input is up or down
    while not direction_is_valid:
        direction = input("Would you like to shift the chords up or down?: ")
        if direction == "up" or direction == "down":
            direction_is_valid = True
        else:
            print("Direction invalid, Please input up or down")
    # Semitones are the smallest interval between notes in music (ex. A, A#, B, C...)
    tones = input("How many semitones would you like to shift" + " " + direction + "? (Input Positive Integer): ")
    # Assuming the input chord(s) start(s) at (0), the amount of semi-tones it takes to return to the same letter is 12.
    # This is called an octave in music, it is the same note name occurring 12 semitones higher or lower in pitch
    octave = 12
    # Stores user input of semitones as a variable
    num1 = int(tones)
    # Divides num1 and octave to calculate the amount of octaves user wants to shift (1 octave = 12 semitones)
    oct_shift = int(num1 / octave)
    # Calculates the remainder of the octave calculation (the number of semitones asked for past the octave number)
    semi_result = num1 % octave
    print("\nYou want to shift", *user_notes, direction)
    print(oct_shift, "octaves and", semi_result, "semitones")
    print()
    answer_is_valid = False
    # while loop for checking answer and guiding user to next appropriate position, also detects invalid input
    while not answer_is_valid:
        answer = input("Is this correct? (Input yes or no):" + " ")
        if answer == "yes":
            answer_is_valid = True
        elif answer == "no":
            main()
        elif answer != "yes" or "no":
            print("Please input yes or no:")
    result = transpose(user_notes, semi_result, direction)
    print()
    # *result prints out all of the items in the user_notes list
    print(*result)
    print()
    final_is_valid = False
    # Final input that asks user to end program or if they want to run the program again
    while not final_is_valid:
        final = input("Would you like to transpose again? (Input yes or no):" + " ")
        print("")
        # yes runs program again
        if final == "yes":
            main()
        # ends loop, and then ends the program
        elif final == "no":
            final_is_valid = True
            # print statements to demonstrate unused math operators
            print("Here are some math equations!")
            print("\n16 + 3 =", 16 + 3)
            print("16 ** 3 =", 16 ** 3)
            print("16 * 3 =", 16 * 3)
            print("16 // 3 =", 16 // 3)
            print("\nEnd of Sprint 2! " * 10)
        else:
            print("Please input yes or no:")
    print()


# Call to main #
main()
