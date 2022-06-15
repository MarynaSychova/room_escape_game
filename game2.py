from os import system
from time import sleep
from sys import stdout
from math import ceil

import images2 as img

def displayText(text):
    for c in text:
        stdout.write(c)
        stdout.flush()
        sleep(0.001)


def displayStamina(timer):
    last_index = ceil(40 * timer + 1)
    img.Stamina = img.Stamina[:-last_index] + (last_index - 1) * "." + "]"
    print("DOOR: " + img.Stamina)


def printText(text, INVENTORY, timer):
    space = "\n" * 2
    print("INVENTORY: " + str(INVENTORY) + "\n")
    displayStamina(timer)
    print("\n" + text)
    print(space)


def showImage(image, text, INVENTORY, timer):
    system('cls')
    print(image)
    printText(text, INVENTORY, timer)


def beginning():
    intro_text = ["It was a bad idea to stay in the woods after dusk.",
                  "Turned out that the legend was true and there IS a moster roaming around at night.",
                  "I managed to run away and hide in the little cabin.",
                  "Fortunately, this thing is too big to get inside through a window.",
                  "But this door will not take it for long.",
                  "I have to come up with something."]
    
    system('cls')
    print(img.Start)
    INPUT = input()
    
    system('cls')
    print(img.Intro)
    
    displayText(intro_text[0])
    INPUT = input("\n--press ENTER to continue--")
    
    for sentence in intro_text[1:]:
        print("\u001b[29;0H\u001b[0J", end="")
        displayText(sentence)
        INPUT = input("\n--press ENTER to continue--")
        
    system('cls')
    print(img.Help)
    INPUT = input("\n--press ENTER to start--")


def game():
    INVENTORY = []

    wall_index = 0
    walls = [img.Wall1, img.Wall2, img.Wall3, img.Wall4, img.Attic]
    stuff = ["door", "dresser", "closet", "window", "safe", "drawer", "axe", "cupboard", "attic"]
    
    # close_ups[2] = Drawer3
    # close_ups[5] = Safe
    close_ups = [img.Dresser, img.Drawer1, img.Code, img.Book, img.Window, img.Code, img.Drawer, img.Chest, img.Paper, img.Attic_wall]

    Window_seen = False
    Wall_seen = False
    Dresser_Opened = False
    Safe_Opened = False
    Bullets_dipped = False
    Shotgun_taken = False
    Meat_taken = False
    Meat_hanged = False
    Fire_lit = False
    Chest_opened = False
    Trap_taken = False
    Trap_placed = False
    Hidden = False

    dreser_text = "--enter an index of a drawer to open it--"
    dresser3_text = "--enter a password to open the drawer--"
    drawer_text = "Seems like the drawer is locked. I can't open it."
    safe_text = "--enter a password to open the safe--"
    chest_text = "A wooden chest. It's locked."
    b_text = "\n--enter B to go back--"
    help_text = "--enter HELP to check controls--"

    timer = 0

    showImage(walls[0], help_text, INVENTORY, timer)    
    INPUT = input("> ").lower()

    while timer < 1.6:
        if INPUT == "r":
            wall_index += 1
            if wall_index == 4:
                wall_index = 0

            showImage(walls[wall_index], help_text, INVENTORY, timer)
            INPUT = input("> ").lower()


        elif INPUT == "l":
            wall_index -= 1
            if wall_index == -1:
                wall_index = 3

            showImage(walls[wall_index], help_text, INVENTORY, timer)
            INPUT = input("> ").lower()

        elif INPUT == "help":
            showImage(img.Help, b_text, INVENTORY, timer)

            while timer < 1.6:
                INPUT = input("> ").lower()

                if INPUT == "b":
                    showImage(walls[wall_index], help_text, INVENTORY, timer)
                    break


        elif INPUT in stuff:
            if wall_index == 0:
                if INPUT == "door":
                    print("Better not to touch it.")
                    INPUT = input("> ").lower()


                elif INPUT == "dresser":
                    showImage(close_ups[0], dreser_text + b_text, INVENTORY, timer)

                    while timer < 1.6:
                        INPUT = input("> ").lower()

                        if INPUT == "b":
                            showImage(walls[wall_index], help_text, INVENTORY, timer)
                            break

                        elif INPUT == "1":
                            showImage(close_ups[1], "A dirty book." + b_text, INVENTORY, timer)

                            while timer < 1.6:
                                INPUT = input("> ").lower()

                                if INPUT == "b":
                                    showImage(close_ups[0], dreser_text + b_text, INVENTORY, timer)
                                    break

                                elif INPUT == "book":
                                    timer += 0.1 #
                                    showImage(close_ups[3], "Look like it's a dictionary of the owner of the cabin." + b_text, INVENTORY, timer)
                                    
                                    while timer < 1.6:
                                        INPUT = input("> ").lower()

                                        if INPUT == "b":
                                            showImage(close_ups[1], dreser_text + b_text, INVENTORY, timer)
                                            break

                        elif INPUT == "2":
                            if "MATCHES" not in INVENTORY:
                                INVENTORY.append("MATCHES")
                                stuff.append("matches")
                                print("\u001b[28;0H\u001b[0J")
                                printText("I've found a MATCH BOX." + b_text, INVENTORY, timer)

                            else:
                                print("It's empty.")

                        elif INPUT == "3":
                            showImage(close_ups[2], dresser3_text + b_text, INVENTORY, timer)

                            while timer < 1.6:
                                INPUT = input("> ").lower()

                                if INPUT == "b":
                                    showImage(close_ups[0], dreser_text + b_text, INVENTORY, timer)
                                    break

                                elif INPUT == "6481" and Window_seen and not Dresser_Opened:
                                    timer += 0.1 #
                                    Dresser_Opened = True
                                    close_ups[2] = img.Drawer3
                                    dresser3_text = "There are a box with bullets and a piece of paper."
                                    showImage(close_ups[2], dresser3_text + b_text, INVENTORY, timer)

                                elif INPUT == "bullets" and Dresser_Opened:
                                    if "BULLETS" not in INVENTORY:
                                        INVENTORY.append("BULLETS")
                                        print("\u001b[28;0H\u001b[0J")
                                        printText("I think three BULLETS will be enough." + b_text, INVENTORY, timer)

                                    else:
                                        print("I don't think I need more.")

                                elif INPUT == "paper" and Dresser_Opened:
                                    timer += 0.1 #
                                    showImage(close_ups[8], "A piece of paper." + b_text, INVENTORY, timer)
                                    
                                    while timer < 1.6:
                                        INPUT = input("> ").lower()

                                        if INPUT == "b":
                                            showImage(close_ups[2], dresser3_text + b_text, INVENTORY, timer)
                                            break

                                if close_ups[2] == img.Code:
                                    timer += 0.1 #

                else:
                    INPUT = input("> ").lower()


            elif wall_index == 1:
                if INPUT == "closet":
                    print("\u001b[28;0H\u001b[0J")
                    printText("Should I just hide here?\n--enter YES or NO--", INVENTORY, timer)

                    while timer < 1.6:
                        INPUT = input("> ").lower()

                        if INPUT == "yes":
                            Hidden = True
                            return ending(Bullets_dipped, Shotgun_taken, Fire_lit, Trap_placed, Hidden)

                        elif INPUT == "no":
                            showImage(walls[wall_index], help_text, INVENTORY, timer)
                            break
                        
                
                elif INPUT == "window":
                    if not Window_seen:
                        Window_seen = True
                        
                    timer += 0.1 #
                    showImage(close_ups[4], "There are some strange scratches on the window." + b_text, INVENTORY, timer)

                    while timer < 1.6:
                        INPUT = input("> ").lower()

                        if INPUT == "b":
                            showImage(walls[wall_index], help_text, INVENTORY, timer)
                            break
                
                elif INPUT == "safe":
                    showImage(close_ups[5], safe_text + b_text, INVENTORY, timer)

                    while timer < 1.6:
                        INPUT = input("> ").lower()

                        if INPUT == "b":
                            showImage(walls[wall_index], help_text, INVENTORY, timer)
                            break

                        elif INPUT == "9843" and Dresser_Opened and Wall_seen and not Safe_Opened:
                            timer += 0.1 #
                            Safe_Opened = True
                            close_ups[5] = img.Jar
                            safe_text = "There is a big jar with water. A thread with a cross is wrapped around its neck."
                            showImage(close_ups[5], safe_text + b_text, INVENTORY, timer)

                        elif INPUT == "bullets" and "BULLETS" in INVENTORY and Safe_Opened:
                            if not Bullets_dipped:
                                timer += 0.1 #
                                Bullets_dipped = True
                                print("\u001b[28;0H\u001b[0J")
                                printText("I've dipped the bullets into the holy water.\nHope it'll help." + b_text, INVENTORY, timer)
                                
                            else:
                                print("I don't need to do this again.")

                        if close_ups[5] == img.Code:
                            timer += 0.1 #
                    
                elif INPUT == "drawer":
                    showImage(close_ups[6], drawer_text + b_text, INVENTORY, timer)

                    while timer < 1.6:
                        INPUT = input("> ").lower()

                        if INPUT == "b":
                            showImage(walls[wall_index], help_text, INVENTORY, timer)
                            break

                        elif INPUT == "axe" and "AXE" in INVENTORY:
                            timer += 0.2 #
                            close_ups[6] = img.Broken_Drawer
                            INVENTORY.remove("AXE")
                            INVENTORY.append("SHOTGUN")
                            Shotgun_taken = True
                            showImage(close_ups[6], "The axe's broken. At least I've found a SHOTGUN inside the drawer. Looks new." + b_text, INVENTORY, timer)
                            drawer_text = "It's empty."

                else:
                    INPUT = input("> ").lower()


            elif wall_index == 2:
                if INPUT == "axe":
                    stuff.remove("axe")
                    INVENTORY.append("AXE")
                    walls[2] = img.Changed_Wall3
                    showImage(walls[wall_index], "I've taken an AXE. Looks like it'll break at any time.\n" + help_text, INVENTORY, timer)

                elif INPUT == "cupboard":
                    if not Meat_taken:
                        timer += 0.1 #
                        INVENTORY.append("MEAT")
                        stuff.append("meat")
                        Meat_taken = True
                        print("\u001b[28;0H\u001b[0J")
                        printText("There are some herbs and a piece of MEAT inside the cupboard.\nThe meat is rotten but I think I'll figure out something with it.\n" + help_text,
                                  INVENTORY, timer)
                        
                    else:
                        INPUT = input("> ").lower()

                elif INPUT == "attic":
                    showImage(walls[4], "Hope I'll find something useful in this pile of trash." + b_text, INVENTORY, timer)

                    while timer < 1.6:
                        INPUT = input("> ").lower()

                        if INPUT == "b":
                            showImage(walls[wall_index], help_text, INVENTORY, timer)
                            break
                                
                        elif INPUT == "chest":
                            showImage(close_ups[7], chest_text + b_text, INVENTORY, timer)

                            while timer < 1.6:
                                INPUT = input("> ").lower()

                                if INPUT == "b":
                                    showImage(walls[4], help_text, INVENTORY, timer)
                                    break

                                elif INPUT == "axe" and "AXE" in INVENTORY:
                                    timer += 0.2 #
                                    Chest_opened = True
                                    close_ups[7] = img.Opened_Chest
                                    INVENTORY.remove("AXE")
                                    chest_text = "The chest is full of bear traps."
                                    showImage(close_ups[7], chest_text + b_text, INVENTORY, timer)

                                elif INPUT == "trap" and Chest_opened:
                                    if not Trap_taken:
                                        Trap_taken = True
                                        INVENTORY.append("TRAP")
                                        stuff.append("trap")
                                        print("\u001b[28;0H\u001b[0J")
                                        printText("I think I'll take one." + b_text, INVENTORY, timer)

                                    else:
                                        print("I don't need more")

                        elif INPUT == "wall":
                            if not Wall_seen:
                                Wall_seen = True
                                
                            timer += 0.1 #
                            showImage(close_ups[9], "Some strange symbols are painted on the wall." + b_text, INVENTORY, timer)

                            while timer < 1.6:
                                INPUT = input("> ").lower()

                                if INPUT == "b":
                                    showImage(walls[4], help_text, INVENTORY, timer)
                                    break

                else:
                    INPUT = input("> ").lower()

            elif wall_index == 3:
                if INPUT == "meat" and "MEAT" in INVENTORY:
                    timer += 0.1 #
                    Meat_hanged = True
                    walls[3] = img.Wall4_with_meat
                    INVENTORY.remove("MEAT")
                    stuff.remove("meat")
                    showImage(walls[wall_index], "I've hanged the piece of meat on the hook.\n" + help_text, INVENTORY, timer)
                    
                elif INPUT == "matches" and "MATCHES" in INVENTORY:
                    if Meat_hanged:
                        timer += 0.1 #
                        Fire_lit = True
                        walls[3] = img.Wall4_with_fire
                        INVENTORY.remove("MATCHES")
                        stuff.remove("matches")
                        showImage(walls[wall_index], "I've lit a fire in the fireplace.\n" + help_text, INVENTORY, timer)

                    else:
                        print("I can't see why I should do that.")
                        INPUT = input("> ").lower()


                elif INPUT == "trap" and "TRAP" in INVENTORY:
                    if Fire_lit:
                        timer += 0.1 #
                        Trap_placed = True
                        walls[3] = img.Wall4_with_trap
                        INVENTORY.remove("TRAP")
                        stuff.remove("trap")
                        showImage(walls[wall_index], "I've placed the trap near the fireplace.\n" + help_text, INVENTORY, timer)
                
                    else:
                        print("I can't see why I should do that.")
                        INPUT = input("> ").lower()

                else:
                    INPUT = input("> ").lower()
                
            
        else:
            INPUT = input("> ").lower()
            
    ending(Bullets_dipped, Shotgun_taken, Fire_lit, Trap_placed, Hidden)


def ending(Bullets_dipped, Shotgun_taken, Fire_lit, Trap_placed, Hidden):
    if Bullets_dipped and Shotgun_taken and Fire_lit and Hidden:
        ending1_text = ["This creature finally broke into the cabin.",
                        "It immediately forgot about me when it smelled a burning piece of meat.",
                        "The thing stopped by the fireplace, I stayed in my hideout and aimed for the head.",
                        "One shot was enough for it's head to start \"melting.\"",
                        "Soon there was nothing but a pile of flesh and a ringing in my ears after its screams.",
                        "I came closer to its remains and saw a small key in them.",
                        "I don't want to think whose key it was and how it got into the monster's stomach.",
                        "ENDING 1: Survivor"]
        system('cls')
        print(img.Ending1_1)

        displayText(ending1_text[0])
        INPUT = input("\n--press ENTER to continue--")
    
        for sentence in ending1_text[1:5]:
            print("\u001b[29;0H\u001b[0J", end="")
            displayText(sentence)
            INPUT = input("\n--press ENTER to continue--")

        system('cls')
        print(img.Ending1_2)
        
        displayText(ending1_text[5])

        for sentence in ending1_text[6:]:
            INPUT = input("\n--press ENTER to continue--")
            print("\u001b[29;0H\u001b[0J", end="")
            displayText(sentence)

    elif Fire_lit and Trap_placed and Hidden:
        ending2_text = ["This creature finally broke into the cabin.",
                        "It stopped by the fireplace, I stayed in my hideout.",
                        "Fortunately, the thing was dumb enough to step on the bear trap.",
                        "The monster ran away into the woods, screaming in agony and dragging its injured leg.",
                        "I left the cabin and headed back to the village.",
                        "It was my last day there, I couldn't be sure that this thing wouldn't look for me.",
                        "ENDING 2: Another Nail In The Coffin"]

        system('cls')
        print(img.Ending2_1)

        displayText(ending2_text[0])
        INPUT = input("\n--press ENTER to continue--")
    
        for sentence in ending2_text[1:3]:
            print("\u001b[28;0H\u001b[0J", end="")
            displayText(sentence)
            INPUT = input("\n--press ENTER to continue--")

        system('cls')
        print(img.Ending2_2)
        
        displayText(ending2_text[3])

        for sentence in ending2_text[4:]:
            INPUT = input("\n--press ENTER to continue--")
            print("\u001b[29;0H\u001b[0J", end="")
            displayText(sentence)

    else:
        ending3_text = ["This creature finally broke into the cabin and ran straight to me.",
                        "It was so fast that I didn't even notice how its jaws crushed my head.",
                        "I couldn't do anything.",
                        "ENDING 3: Death"]
        system('cls')
        print(img.Ending3)

        displayText(ending3_text[0])
        
        for sentence in ending3_text[1:]:
            INPUT = input("\n--press ENTER to continue--")
            print("\u001b[29;0H\u001b[0J", end="")
            displayText(sentence)


def main():
    beginning()

    game()


if __name__ == '__main__':
    main()
