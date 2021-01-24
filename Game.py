
#Credintials from user input
print("Welcome to the unknown game!")
name = input("what is your name? ")
print("Hello,",name, "lets go and good luck.")

#inside def main(): is the game
def main():

    left_or_right = input("You're at a crossroad, do you want to go left or right (left/right)? ").lower()
    if left_or_right == "left":
        ans = input("Nice, you follow the path and reach a lake...Do you swim across or go around (swim/around)? ").lower()

        if ans == "around":
            print("You went around and reached the other side of the lake.")
            ans = input("You notice a house and a cave, which do you go to (house/cave)? ").lower()
            #
            if ans == "house":
                print("Inside the house you realise no one is home but something is cooking on the stove")
                ans = input(" Do you help yourself to food or wait to the owner to return (eat/wait)? ").lower()
                if ans == "eat":
                    print("You help yourself to food, it smells good, it taste good but something is off, you start to feel dizzy, the room is spinning, the walls are closing in on you, you're struggling to breath, there's a pain your chest, you collasp to the floor, you're dying, the lights go out, you're dead...You lose")
                elif ans == "wait":
                    print("1 hr later the front door opens, a man comes limping, barley able to stand covered in blood and a missing arm. He see's you, confused 'who are...Hhhhelp!")
            
            elif ans == "cave":
                print("You make your way to the cave. ")

                        
                ans = input("As you approach the cave entrance you hear a screen coming from inside. Do you investigate or run to the house (investigate/run)? ").lower()
                if ans == "run":
                        print("You reach the house and enter.")
                        
                        ans = input("Inside the house you realise no one is home but something is cooking on the stove. Do you help yourself to whats cooking or wait for the owner to return (eat/wait)? ").lower()
                        if ans == "wait":
                            print("1 hr later the front door opens, a man comes limping in, barley able to stand covered in blood and missing an arm. He see's you, confused, he stutters 'wh-who are...Hhh-help!")

                            ans = input("You stand, shocked. Do you help or run (help/run)? ").lower()
                            if ans == "help":
                                print("You rush over to help but realsie you haven't got a F****** clue what you're doing, so you watch on in horror as the man bleeds to death... You lose")
                            
                            elif ans == "run":
                                print("You run past the helpless corps, out into the openess and keep on running")

                                ans = input("As you're are running you can see a wooded area ahead and a river to the right. Go to woods or river (woods/river) ").lower()

                                if ans == "river":
                                    print("You're are standing on the river bank looking down into the rocky river, then suddenly a wasps buzzes around your face, panic sets in, you try to shoo the wasp away but it causes you to lose balance and fall down the river bank hitting your head, knocking you unconcious face down in the river, slowly dying...You lose ")
                                
                                elif ans == "woods":
                                    print("You're at the woods.")

                                    ans = input("Do you go through or walk around (through/around) ").lower()

                                    if ans == "around":
                                        print("As you walk around you see road and on the road you see your car what have been looking for this whole time. You get in your car and drive home. You win, The end!!")
                                    
                                    elif ans =="through":
                                        print("5 minutes in you see a mumma bear and her cub, they see you, you flap hard, mumma bears charges, your life flashes before you, you remember something from primary school about playing dead, you drop to the floor, playing dead praying for your life that this to work. Mumma bear is having none of it and rips your apart. You lose!!! ")
                                    
                        

                        elif ans == "eat":
                            print("You help yourself to food, it smells good, it taste good but something is off, you start to feel dizzy, the room is spinning, the walls are closing in on you, you're struggling to breath, there's a pain your chest, you collasp to the floor, you're dying, the lights go out, dead...You lose!!")

                elif ans == "investigate":
                    print("You enter the cave and see a severed arm on the ground, at that point you hear more screams, you push on with the investigation cuz you're brave mother f*****. 10 minutes go by, you're balls deep in the cave and suddenly you see a bear you freeze, the bears sees you, you locks eyes, theres a moment between you then suddenly the bears roars so loud you crap yourself, whilst shit is runnging down your leg the bear charges, blood dripping at the mouth from it's most recent victim, it's eyes a blaze with fury. This is where you begin to think I F***** up.....You lose")

            
            
            
        elif ans == "swim":
            print("You tried to swim across but you was eating by the loch ness monster...you lose!!")

          
    
    else:
        print("You Stepped on a mine. DEAD!! You lose.")

    #Restarts the game
    restart = ""
    while True:
        print("Do you want to play agian (y/n) ")
        restart = input()
        if restart == "y":
            main()

        elif restart == "n":
            exit()
        
        else:
            print("Invaild command")
        
        
# returns to of programme
main()
        
    







