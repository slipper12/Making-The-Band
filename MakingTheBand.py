import sys
import random


class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end="")
        print()

print("Give us a count Mark!.")


class Drummer(Musician):
    def __init__(self):
        super().__init__(["Crash", "Clack", "Ding"])

    def four_count(self):
        print("   Alright guys, here we go.")
        print("One.   Two.   Three!    Four!!")

    def combust(self):
        print("Help! I've combusted again!! Someone grab the extinguisher! ")

class Bassist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thromb", "Thrumb"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("I'm still tuning my guitar guys! Be there in a moment!...")

class Band(object):
    def __init__(self, musicians = []):
        self.musicians = musicians

    def hire(self, musician):
        self.musicians.append(musician)
        print(self.musicians)
            
    def fire(self, musician):
        self.musicians.remove(musician)



Juno = Band()

while len(Juno.musicians) <= 4:
    print("We are hiring")
    print(" ")
    instrument=input("What instrument do you play? ").lower()

    if instrument.lower() in ["guitar", "the guitar", "acoustic guitar", "electric guitar"]:
        new_hire = Guitarist()
        Juno.hire(new_hire)
    elif instrument.lower() in ["drums","the drums","snare drum"]:
        new_hire = Drummer()
        Juno.hire(new_hire)
    elif instrument.lower() == "bass":
        new_hire = Bassist()
        Juno.hire(new_hire)
    else:
        print("Sorry, we don't need that type of instrument.")

print ("We now have {} band members".format(len(Juno.musicians)))