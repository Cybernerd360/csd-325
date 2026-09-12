def countdown(user_bottles):
    while user_bottles >0:
        current_bottles = user_bottles -1
        print (f"{user_bottles} bottles of beer on the wall, {user_bottles} bottles of beer.")
        print (f"Take one down and pass it around, {current_bottles} bottles of beer on the wall.")

        user_bottles -= 1

        if user_bottles == 0:
            print ("0 bottles of beer on the wall, no more bottles of beer.")
            print ("Go to the store and buy some more, 99 bottles of beer on the wall.")

user_bottles = int(input("Enter the number of bottles of beer: "))

countdown(user_bottles)