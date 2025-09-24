print ("Welcome to 'Choose Your Own Adventure'!")
print ("*To make a decision, type 1, 2 (or 3) according to how many choices you have.*")
print ("Your next decision might change your destiny...")
Q1 = input(f"Do you decide to 1; sleep in or 2: get up?:")


# decision path #1
# if question 1 = decision 1
if (Q1 == '1'):
    print("You decide to sleep in...")
    Q1_2 = input(f"Do you decide to 1; make an iced coffee or 2: make a hot coffee?:")


    # if question 2 = decision 1
    if (Q1_2 == '1'):
        print("You decide to get iced coffee...")
        print("Your coffee machine is out of coffee beans!")
        Q1_2_1 = input(f"Do you decide to 1; go to the store and get more coffee beans or 2: skip coffee:")


    # if question 2 = decision 2
    if (Q1_2 == '2'):
        print("You decide to get hot coffee...")
        print("You ended up burning your tongue, and then started to feel sick.")
        Q1_3 = input(f"Do you take 1; the pink medicine or 2: the yellow medicine?:")


        # if question 3 = decisioin 1
        if (Q1_3 == '1'):
            print("You decide to take the pink medicine...")
            print("This medicine causes you to randomly pick a blue hat or red shirt, no questions asked.")
            Q1_3_1 = input(f"Do you decide to 1; take the blue hat or 2: take the red shirt:")


            # if question 4 = decision 1 or 2
            if (Q1_3_1 == '1' or '2'):
                print("Your choice gave you another choice...")
                Q1_3_1_1 = input(f"Do you decide to have the permanent ability to 1; see the past or 2: see the future:")


                # if question 5 = decision 1
                if (Q1_3_1_1 == '1'):
                    print("You know have the permanent ability to see the past.")


                # if question 5 = decision 2
                if (Q1_3_1_1 == '2'):
                    print("You know have the permanent ability to see the future.")


        # if question 3 = decision 2
        if (Q1_3 == '2'):
            print("You decide to take the yellow medicine...")
            Q1_4 = input(f"You now have the permanent ability to 1; time travel or 2: shapeshift:")


            # if question 4 = decision 2
            if (Q1_4 == '2'):
                print("You decide to have the permanent ability to shapeshift...")
                print("CATCH! you only have the ability to shapeshift into two categories.")                
                Q1_5 = input(f"Do you decide to have the ability to 1; shapeshift into a cartoon character OR 2: shapeshift into an animated disney character:")

            if (Q1_4 == '1'):
                print("You now have the permanent ability to time travel!")

                # if question 5 = decision 1
            if (Q1_5 == '1'):
                    print("You now have a burnt tongue and the strange permanent ability to shapeshift into any cartoon character of your choosing!")
                # if question 5 = decision 2
            if (Q1_5 == '2'):
                    print("You now have a burnt tongue and the strange permanent ability to shapeshift into any animated disney character of your choosing!")


# decision path #2
# question 1 = decision 2
if (Q1 == '2'):
    print("You decide to get up...")
    Q2 = input(f"Do you decide to start your day by 1; making cinnamon waffles or 2: making blueberry pancakes:")
    # if question 2 = decision 2
    if (Q2 == '2'):
        print("You decide to make blueberry pancakes...")
        print("Oh no! You dont have the proper ingredients to make blueberry pancakes. ")
        Q2_1 = input(f"Do you decide to 1; make waffles instead or 2: go to the store to ge the right ingredients to make your pancakes:")

        # WONT let me 
        #i if question 3 = decision 1
        if (Q2_1 == '1' or Q2 == '1'):
            print("You decide to make waffles...")
            print("While eating your waffles, you see an ad for a once in a lifetime sky dive adventure for 50%... off!")
            Q2_1_1 = input(f"Do you decide to 1; skip out on the offer or 2: take your chances at this adventure:")


            # if question 4 = decision 1
            if (Q2_1_1 == '1'):
                print("You decide to skip out on this adventure...")
                print("After eating, you do your morning tasks and check the mail. A letter in the mail is directed to you from Hogwarts.")
                Q2_1_1_1 = input(f"Do you decide to open the letter by 1; ripping it open, or 2: gently unfolding it:")


                # if question 5 = decision 1
                if (Q2_1_1_1 == '1'):
                    print("You decide to rip open the letter...")
                    print("Your letter contains your official invite to join Hogwarts. After a few months you start your first day at Hogwarts. When the hat is picking your house it chooses based on the way you opened your letter. You are in the Slytherin.")


                # if question 5 = decision 2
                if (Q2_1_1_1 == '2'):
                    print("You decide to gently open your letter...")
                    print("Your letter contains your official invite to join Hogwarts. After a few months you start your first day at Hogwarts. When the hat is picking your house it chooses based on the way you opened your letter. You are in the Ravenclaw.")


            # if question 4 = decision 1
            if (Q2_1_1 == '2'):
                print("You decide to take your chances at this adventure...")
                print("You sign up for a sky dive time, and you start driving to the sky dive start location.")
                Q2_1_1_2 = input(f"Do you decide to 1; speed so you can get there faster or 2: drive the speed limit:")


                # if question 5 = decision 1
                if (Q2_1_1_2 == '1'):
                    print("You decide to drive the speed limit...")
                    print("You make it to your sky dive destination only to realize it does'nt exist. You go around searching for answers and fall into a mysterious pond. The pond transports you to another dimension. Upon exploring this dimension you found a community of baby unicorns. The baby unicorns elect you as their ruler. You live out your life as the ruler of baby unicorns.")


                # if question 5 = decision 1
                if (Q2_1_1_2 == '2'):
                    print("You decide to speed...")
                    print("A cop pulls you over for speeding. You tell her about the instagram ad you saw this morning for sky diving. She doesnt believe you and asks you to show her where this location is. The ad, sign up info, and adress to the location mysteriously dissapeared. The cop arrests you on suspicison of drunk driving and you now have an updates permanent record, along with  no sky diving memories.")


        # if question 3 = decision 2
        # WONT let the path 1 - question 2 - decision 1 come to here
        if (Q2_1 == '2' or Q1_2_1 == '1'):
            print("You decide to go to the store...")
            print("On your way to the store, a lamborghini hits your car. The driver of the lamborghini is a famous celebrity, he wants to avoid backlash and criticism from the public. He offers you 2 options...")
            Q2_2 = input(f"Do you decide to 1; take the lamborghini or 2 take $200k:")


            # if question 4 = decision 1
            if (Q2_2 == '1'):
                print("You decide to take the lamborghini...")
                print("The celebrity compliments your calm manner, and invites you to a celebrity party. You end up getting along very well with the members of the party. Your face and name becomes known through your new celebrity friends. You now have a positive and rich reputation, you quit your job to live on a yacht in the mediterranean.")


            # if question 4 = decision 2
            if (Q2_2 == '2'):
                    print("You decide to take the 200k...")
                    Q2_3 = input(f"You have the opportunity to 1: save the money or 2;invest the money:")


                    # if question 5 = decision 1
                    if (Q2_3 == '1'):
                        print("You decided to save your money...")
                        print("That was a smart and safe financial decision. You end exposing the celebrity, the celebrity then sues you, and you are now in debt with no car, house, or job... and a bad reputation that will haunt you forever.")


                    # if question 5 = decision 2
                    if (Q2_3 == '2'):
                        print("You decided to invest your money...")
                        Q2_4 = input(f"Do you decide to invest in 1; plant.co or 2: puppylovers.inc:")


                        # if question 6 = decision 1
                        if (Q2_4 == '1'):
                            print("You decide to invest in plant.co...")
                            print("That was not a wise decision... you ended up losing all your money, and now have a big dent in your car that your are unable to fix given your current financial situation.")
                        # if question 6 = decision 2
                        if (Q2_4 == '2'):
                            print("You decide to invest in puppylovers.inc...")
                            print("That was a smart choice... puppylovers.inc ended up going worldwide thanks to your contribution, and you are now a growing millionare.")

