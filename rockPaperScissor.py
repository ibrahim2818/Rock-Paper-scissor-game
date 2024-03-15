while True:
    import random
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    #Write your code below this line 👇
    x=int(input('what do you choose? enter 0 for rock ,1 for paper or 0 for scissors\n'))

    if x==0:
        print(rock)

    elif x==1:
        print(paper)

    elif x==2:
        print(scissors)

    com= random.randint(0,2)


    if com==0:
        print(rock)
    elif com==1:
        print(paper)
    elif com==2:
        print(scissors)

    if x==com:
        print("Its a tie")
    elif x==0 and com==1:
        print('computer win')
    elif x==0 and com== 2: 
        print('you win')
    elif x==1 and com==0:
        print('you win')
    elif x==1 and com==2:
        print('computer win')
    elif x==2 and com == 0:
        print ('computer win')
    elif x==2 and com== 1:
        print ('you win')
    
    y= int(input('Do you want to play again? enter 1 to play again\n'))
    if y==1:
        continue
    else:
        break


