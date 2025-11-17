print("Welcome to 'Choose Your Own Adventure'!\n*To make a decision, type 1, 2 (or 3) according to how many choices you have.*\nYour next decision might change your destiny...")
dy="Do you decide to";yd="You decide to";nh="You now have";u=input
Q1=u(f"{dy} 1; sleep in or 2: get up?:")
if(Q1 =='1'):
    print(f"{yd} sleep in...")
    Q1_2=u(f"{dy} 1; make an iced coffee or 2: make a hot coffee?:")
    if(Q1_2=='1'):
        print(f"{yd} get iced coffee...\nYour coffee machine is out of coffee beans!")
        Q1_2_1=u(f"{dy} 1; go to the store & get more coffee beans or 2: skip coffee:")
    if (Q1_2=='2'):
        print(f"{yd} get hot coffee...\nYou ended up burning your tongue, & then started to feel sick.")
        Q1_3=u(f"{dy} take 1; the pink medicine or 2: the yellow medicine?:")
        if(Q1_3=='1'):
            print(f"{yd} take the pink medicine...\nThis medicine causes you to r&omly pick a blue hat or red shirt, no questions asked.")
            Q1_3_1=u(f"{dy} 1; take the blue hat or 2: take the red shirt:")
            if(Q1_3_1=='1'or'2'):
                print("Your choice gave you another choice...")
                Q1_3_1_1=u(f"{dy} have the permanent ability to 1; see the past or 2: see the future:")
                if(Q1_3_1_1=='1'):
                    print("You know have the permanent ability to see the past.")
                if(Q1_3_1_1=='2'):
                    print("You know have the permanent ability to see the future.")
        if(Q1_3=='2'):
            print(f"{yd} take the yellow medicine...")
            Q1_4=u(f"{nh}  the permanent ability to 1; time travel or 2: shapeshift:")
            if(Q1_4=='2'):
                print(f"{yd} have the permanent ability to shapeshift...\nCATCH! you only have the ability to shapeshift into two categories.")
                Q1_5=u(f"{dy} have the ability to 1; shapeshift into a cartoon character OR 2: shapeshift into an animated disney character:")
            if(Q1_4=='1'):
                print(f"{nh} the permanent ability to time travel!")
            if(Q1_5=='1'):
                    print(f"{nh} a burnt tongue & the strange permanent ability to shapeshift into any cartoon character of your choosing!")
            if(Q1_5=='2'):
                    print(f"{nh} a burnt tongue & the strange permanent ability to shapeshift into any animated disney character of your choosing!")
if(Q1=='2'):
    print(f"{yd} get up...")
    Q2=u(f"{dy} start your day by 1; making cinnamon waffles or 2: making blueberry pancakes:")
    if(Q2=='2'):
        print(f"{yd} make blueberry pancakes...\nOh no! You dont have the proper ingredients to make blueberry pancakes.")
        Q2_1=u(f"{dy} 1; make waffles instead or 2: go to the store to ge the right ingredients to make your pancakes:")
        if(Q2_1=='1'or Q2=='1'):
            print(f"{yd} make waffles...\nWhile eating your waffles, you see an ad for a once in a lifetime sky dive adventure for 50%... off!")
            Q2_1_1=u(f"{dy} 1; skip out on the offer or 2: take your chances at this adventure:")
            if(Q2_1_1=='1'):
                print(f"{yd} skip out on this adventure...\nAfter eating, you do your morning tasks & check the mail. A letter in the mail is directed to you from Hogwarts.")
                Q2_1_1_1=u(f"{dy} open the letter by 1; ripping it open, or 2: gently unfolding it:")
                if(Q2_1_1_1=='1'):
                    print(f"{yd} rip open the letter...\nYour letter contains your official invite to join Hogwarts. After a few months you start your first day at Hogwarts. When the hat is picking your house it chooses based on the way you opened your letter. You are in the Slytherin.")
                if(Q2_1_1_1=='2'):
                    print(f"{yd} gently open your letter...\nour letter contains your official invite to join Hogwarts. After a few months you start your first day at Hogwarts. When the hat is picking your house it chooses based on the way you opened your letter. You are in the Ravenclaw.")
            if(Q2_1_1=='2'):
                print(f"{yd} take your chances at this adventure...\nYou sign up for a sky dive time, & you start driving to the sky dive start location.")
                Q2_1_1_2=u(f"{dy} 1; speed so you can get there faster or 2: drive the speed limit:")
                if(Q2_1_1_2=='1'):
                    print(f"{yd} drive the speed limit...\nYou make it to your sky dive destination only to realize it does'nt exist. You go around searching for answers & fall into a mysterious pond. The pond transports you to another dimension. Upon exploring this dimension you found a community of baby unicorns. The baby unicorns elect you as their ruler. You live out your life as the ruler of baby unicorns.")
                if(Q2_1_1_2=='2'):
                    print(f"{yd} speed...\nA cop pulls you over for speeding. You tell her about the instagram ad you saw this morning for sky diving. She doesnt believe you & asks you to show her where this location is. The ad, sign up info, & adress to the location mysteriously dissapeared. The cop arrests you on suspicison of drunk driving. {nh} an updates permanent record, along with no sky diving memories.")
        if(Q2_1=='2'or Q1_2_1=='1'):
            print(f"{yd} go to the store...\nOn your way to the store, a lamborghini hits your car. The driver of the lamborghini is a famous celebrity, he wants to avoid backlash & criticism from the public. He offers you 2 options..")
            Q2_2=u(f"{dy} 1; take the lamborghini or 2 take $200k:")
            if(Q2_2=='1'):
                print(f"{yd} take the lamborghini...\nThe celebrity compliments your calm manner, & invites you to a celebrity party. You end up getting along very well with the members of the party. Your face & name becomes known through your new celebrity friends. {nh} a positive & rich reputation, you quit your job to live on a yacht in the mediterranean.")
            if(Q2_2=='2'):
                    print(f"{yd} take the 200k...")
                    Q2_3=u(f"You have the opportunity to 1: save the money or 2;invest the money:")
                    if(Q2_3=='1'):
                        print(f"{yd} save your money...\nThat was a smart & safe financial decision. You end exposing the celebrity, the celebrity then sues you, & you are now in debt with no car, house, or job... & a bad reputation that will haunt you forever.")
                    if(Q2_3=='2'):
                        print(f"{yd} invest your money...")
                        Q2_4=u(f"{dy} invest in 1; plant.co or 2: puppylovers.inc:")
                        if(Q2_4=='1'):
                            print(f"{yd} invest in plant.co...\nThat was not a wise decision... you ended up losing all your money, & now have a big dent in your car that your are unable to fix given your current financial situation.")
                        if(Q2_4=='2'):
                            print(f"{yd}invest in puppylovers.inc...\nThat was a smart choice... puppylovers.inc ended up going worldwide thanks to your contribution, & you are now a growing millionare.")