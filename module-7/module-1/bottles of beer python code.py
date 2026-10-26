user_bottles = int(input("Enter number of bottles:"))
# Make sure the user input is a positive integer and greater than 0

while user_bottles > 0:
  current_bottles = user_bottles - 1
  print(
      f"{user_bottles} bottles of beer on the the wall, {user_bottles} of"
      " beer"
  )
  print(
      f"Take one down and pass it around, {current_bottles} bottles of beer on"
      f" the wall. \n"
  )
  # While number is less than 0 bottles will decrease by 1 and print the song message until it reaches 0
  user_bottles -= 1
# user_bottles decreases by 1 and if not 0 then repeats loop.
  if user_bottles == 0:
    print("0 bottles of beer on the wall, 0 bottles of beer.")
    print("Need to get more beer bottles")
    # user_bottles reached 0, so the loop will break and the program will end