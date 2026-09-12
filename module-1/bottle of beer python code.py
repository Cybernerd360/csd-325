def countdown(user_bottles):
#main function that takes the user input and counts down the number of bottles of beer on the wall.
    while user_bottles >0:
        current_bottles = user_bottles -1
        print (f"{user_bottles} bottles of beer on the wall, {user_bottles} bottles of beer.")
        print (f"Take one down and pass it around, {current_bottles} bottles of beer on the wall.")
# While the number of bottles is greater than 0, the program will print the current number of bottles and decrement the count by 1.
        user_bottles -= 1
# Whatever the user inputs, the countdown function will continue to run until the number of bottles reaches 0. Each iteration of the loop will print the current number of bottles and decrement the count by 1.
        if user_bottles == 0:
            print ("0 bottles of beer on the wall, no more bottles of beer.")
            print ("Go to the store and buy some more, 99 bottles of beer on the wall.")
# If the user inputs 0 or number reaches 0, the program will print the final lines of the song and end the countdown.
user_bottles = int(input("Enter the number of bottles of beer: "))
# user inputs the number of bottles of beer, and the countdown function is called with that input.
countdown(user_bottles)