print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

health = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health.")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a beach where you see a beautiful island... Do you swim across or stay on the beach (across/stay on beach)? ")

            if ans == "stay on beach":
                print("You stayed on the beach and tanned your cheeks.")
            elif ans == "across":
                print("You managed to get across, but were bit by killer dolphins and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to the (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by the owner... LeatherFace!!! He almost gets you with his chainsaw lose 5 health for pooping your shorts.")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived... You win!")

            else:
                print("You were eaten by piranhas in the river and lost.")

        else:
            print("A piano fell on your head...you lost")

    else:
        print("Goodbye...")