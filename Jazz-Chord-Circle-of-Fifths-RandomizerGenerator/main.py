#to-do:
#  (1) more proper time signature?
#  (2) debug try-excepts

import random
import time

while True:
    try:
        print("\nWelcome to Random Jazz Chord (Circle of Fifths) Generator! To stop or exit the program, press Ctrl + C.\n")
        mode = input("\nTo begin with, select mode:\n'C' = complete mode\n'1' = M7(9) open voicing\n'M' = manual mode\n")

        # base keys from the Circle of Fifths. I intentionally include both "Gb" and "F#" (despite both being the same key) just to familiarize myself with both notation.
        cof = ["C", "G", "D", "A", "E", "B", "Gb", "F#", "Db", "Ab", "Eb", "Bb", "F"]

        # manual mode
        if mode == "M":
            # if want to remove certain keys from the Circle of Fifths
            mode_cof = input("\nDo you want to remove certain key(s) from the Circle of Fifths?\n    Yes (Y)\n    No (press any other key) ")
            if mode_cof == "Y":
                cof_removed = []
                n_cof_input = int(input("Enter number of key(s) you want to remove: "))
                for i in range (0, n_cof_input):
                    ele_cof = str(input())
                    cof.remove(ele_cof)
                    cof_removed.append(ele_cof)
                print("You have removed the following key(s):")
                print(cof_removed)
            else:
                print("You will be playing all the keys within the Circle of Fifths.")
            # manually inputting chord(s)
            chord = []
            n_chord_input = int(input("\nEnter number of base chord(s) to be played: "))
            for i in range (0, n_chord_input):
                ele_chord = str(input())
                chord.append(ele_chord)
            print("You will be playing in the following chord(s):")
            print(chord)
            # manually inputting extension(s)
            extension = []
            n_ext_input = int(input("\nEnter number of extension(s) to be played:\nnote #1: use 'b' for flat and '#' for sharp\nnote #2: type each extension in parentheses\n"))
            for i in range (0, n_ext_input):
                ele_ext = str(input())
                extension.append(ele_ext)
            print("You will be playing the following extension(s):")
            print(extension)
            # manually selecting voicing(s)
            voicing = []
            n_voi_input = int(input("\nEnter number of voicing(s) to be played (you're free to type anything for this): "))
            for i in range (0, n_voi_input):
                ele_voi = str(input())
                voicing.append(ele_voi)
            print("You will be playing the following voicing(s):")
            print(voicing)

        # complete mode
        elif mode == "C":
            cof = cof
            chord = ["M7", "m7", "7"]
            extension = ["(9)", "(b9)", "(#9)", "(#11)", "(13)", "(b13)", "(#13)", ""]
            voicing = ["open voicing", "closed voicing"]

        # mode 1 (M7(9), open voicing only)
        elif mode == "1":
            cof = cof
            chord = ["M7"]
            extension = ["(9)"]
            voicing = ["open voicing"]

        else:
            print("Command can't be comprehended.")
            continue

        tempo = float(input("\nEnter tempo (BPM) = "))
        #timesig = input("time signature (.../...) = ")
        # spb = second per beat
        spb = 60.0 / tempo
        # bpb = beat per bar
        bpb = float(input("Enter beat per bar = "))
        starttime = time.time()

        def metronome():
            metronome = bpb - 1.0
            while metronome > 0.0:
                metronome -= 1.0
                time.sleep((spb - ((time.time() - starttime) % spb)))
                print(".")
            else: time.sleep((spb - ((time.time() - starttime) % spb)))

        def generator():
            print(random.choice(cof) + random.choice(chord) + random.choice(extension) + " " + random.choice(voicing))
            metronome()

        def pickup_measure():
            pickup_beat = bpb - 1.0
            while pickup_beat > 0.0:
                pickup_beat -= 1.0
                time.sleep((spb - ((time.time() - starttime) % spb)))
                print(str(int(pickup_beat) + 1) + "...")
            else: time.sleep((spb - ((time.time() - starttime) % spb)))

        target_confirm = input("\nDo you want to assign a target number of chords/bars played (the program will automatically stop once the target is reached)? (Y/N) ")
        if target_confirm == "Y":
            target = int(input("Input target: "))

        while True:
            try:
                #print("\n")
                pickup_measure()
                bar_count = 1
                if target_confirm == "Y":
                    target_count = target
                    while target_count > 0:
                        generator()
                        bar_count += 1
                        target_count -= 1
                    else:
                        print("You've reached your target (" + str(bar_count - 1) + " chords/bars played)!")
                elif target_confirm == "N":
                    while True:
                        generator()
                        bar_count += 1
            except:
                print("\nStopped. You've played " + str(bar_count) + " chords/bars!")
            pause = input("Type:\n  - 'restart' (with the same setting)\n  - 'change tempo'\n  - 'change bpb' (beat per bar)\n  - 'exit' or Ctrl + C (back to main menu)\n")
            if pause == "change tempo":
                tempo = float(input("Input new tempo (BPM) = "))
                spb = 60.0 / tempo
            elif pause == "change bpb":
                bpb = float(input("Input new beat per bar = "))
            elif pause == "restart": continue
            elif pause == "exit": break
    except:
        pause = input("\n### Developer's note: Either you intentionally press the Ctrl + C button, or something went wrong (I'm working on this, but to avoid it in the meantime, make sure you've entered valid inputs!)\n\nOptions:\n    1 = back to main menu\n    2 = exit the program\n")
        if pause == "2":
            end_message = ["Have a good day!", "Don't forget to practice 40 hours a day!"]
            print("\n" + random.choice(end_message))
            break
        elif pause == "1":
            continue
        else:
            print("Command cannot be comprehended.")
            continue
