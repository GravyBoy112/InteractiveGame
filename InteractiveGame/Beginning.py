#Just a framework for the game's dialogue

def beginning():
    choice_value = 0
    while (choice_value <= 100):
        print("You wake up in cold cell. You have no idea how you got there, but you can hear voices coming toward you. ")

        choice_value = 0

        print("Before you lies a hammer, a sword, and an apple. Which do you take? ")
        print("1) Hammer ")
        print("2) Sword ")
        print("3) Apple ")

        choice = input("What is your choice? ")

        if choice == "1" or choice == "Hammer" or choice == "hammer" or choice == "One" or choice == "one":
            choice_value = (choice_value + 1)  

            print("You hastily grab the hammer and start banging away at the lock.")
            print("Down the dark hallway you can hear the voices again, and they seem to have been alerted by the sudden noise.")
    
            print("1) Keep hammering")
            print("2) Stop hammering and hide")
            print("3) drop the hammer and retreat back into your cell")
            hammer1 = input("What do you do? ")
    
            if hammer1 == "1":
                choice_value = (choice_value + 1)        

                print("You keep hammering at the door's lock.")
                print("The lock finally breaks, but you hear the footsteps are very close and you can see the light from your captors' torch")
                print("You spot a clever hiding spot. You could use it to hide from your captors. You also spot a stairwell going downward. You aren't quite sure where you are, but this culd lead you out. You could also try to tfight your way throught your unknown captors to freedom.")
                
                print("1) Hide")
                print("2) Go down the stairwell")
                print("3) Fight")
                hammer2 = input("What will you do? ")
                
                if hammer2 == "1":
                    choice_value = (choice_value + 1)


                    print("You decide to hide in the clever spot nearby. The spot in question is a pile of hay conveniently located across the hall.")
                    print("It seems to work well enough, though it seems as well that your captors have taken notice of your escape.")
                    print("You wait a moment, until your captors leave, though they will be back soon in greater numbers. Free from prying eyes for now, you scan your surroundings and look for where to go from here.")
                    print("You can follow them to see where they go, check out a suspicios looking light down the hallway, or go down that stairwell you saw earlier.")
                   
                    print("1) Follow captors")
                    print("2) Investigate light")
                    print("3) Go down the staris")
                    hammer3 = input("which will you choose? ")
                    

                if hammer2 == ("2", "Two", "two"):
                    print("You hastily go down the stairwell")
                    print("")
                
                    

            elif hammer1 == "2":
                choice_value = (choice_value + 2)        

                print("You stop hammering and hide behind a pile of hay, which you assume is meant to act as a bed.")
                print("The guards come up to your cell and begin conversing about the ruckus.")
                exit
        
            elif hammer1 == "3":
                choice_value = (choice_value + 0.5)        

                print("You drop the hammer and retreat into your cell.")
                print("Your captors come to your cell door and see the hammer lying next to it.")
                exit
            else:
                print("That's not an option.")
                print("Due to your lack of judgement skills, you fail to acknowledge the present danger posed to you.")
                print("You stand there with the hammer in your hand staring at the locked door.")
                print("Your captors reach the cell and take you to the courtyard to carry out your sentence.")
                print("You died!")
                exit

        elif choice == "2":
            choice_value = (choice_value + 2)    

            print("You grab the sword and begin tryin to pry open the rusty, old door.")
            print("Just as you feel the door begin to loosen from its hold, you hear footseps. They're coming toward you.")
            print("Ahead of you resides a cabinet, a dark area you might be able to hide in, and a light seemingly coming from the other side of the hallway. ")
    
            print("What do you do?")
            print("1) Hide in the cabinet")
            print("2) Blend in with the shadows")
            print("3) Begin running toward the light")
            sword1 = input("What do you do? ")
    
            if sword1 == "1":
                choice_value = (choice_value + 1)        

                print("You run to the cabinet and hide inside, making it just in time, as your captors have reached the cell")
                print("They immediately raise the alarm and hoards of the creatures, masked by the cabinet door rush by you.")
                exit
            elif sword1 == "2":
                choice_value = (choice_value + 2)
        
                print("You attempt to blend in with your environment, adopting the shadows as if they were your home.")
                print("Your attempt is in vain, and your captors immediately find you")
                exit
            elif sword1 == "3":
                choice_value = (choice_value + 0.5)
                print("You begin running toward the light.")
                print("You are mortified to find that what you once thought was sunlight was in fact the fire of a camp.")
                print("You find yourself surrounded by creatures in cloaks.")
                exit
            else:
                print("You stand dumbfounded by the thought of capture.")
                print("You immediately find out that this does you no favors and suddenly find yourself in a courtyard.")
                print("Due to your inaction, your captors have taken you to the courtayrd to carry out your sentence.")
                print("You died!")
                exit
    
        elif choice == "3":
            choice_value = (choice_value + 3)

            print("While you now have no need to worry about an untimely visit from the doctor, this provide you with no help at the moment.")
            print("Just as you begin pondering your next decision, a rabid rat jumps at you from the darkness. No doubt he is after the apple.")
    
            print("1) Use the apple as a shield")
            print("2) Protect the apple at all costs")
            apple1 = input("What do you do? ")
    
            if apple1 == "1":
                choice_value = (choice_value + 0)   

                print("You sacrifice the apple to save yourself")
                print("The regret immediately fills you")
                print("What are you gonnna do now that there is no deterrent to against the doctors")
                print("As you ponder this, the rat scurries away leaving you with no defense against such invaders")
                exit
            elif apple1 == "2":
                choice_value = (choice_value + 10) 

                print("You sacrifice everything in defense of the apple. After all, who else will protect you from those dastardly health proffesionals?")
                exit
    
    
        else:
            print("Thats not an option")
            print("Try again!")
            continue