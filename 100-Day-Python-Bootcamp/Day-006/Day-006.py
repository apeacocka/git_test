#Functions

#To make your own function start with keyword def
#Give your function a name()
#Add colon
#Everything in the function is indented
def my_function():
    print("Hello")
    print("Bye")
#To trigger or call the function, type the name
my_function()

#Robot Game
# def turn_around():
#     turn_left()
#     turn_left()

# move()
# move()
# turn_around
# move()
# move()
# turn_around

#Make a box

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

#Hurdle

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for step in range(6):
#     hurdle()


#While loops: Continue going while a particular condition is true

#2 typs of for loops for far

#Run through a list of items
#for item in list_of_items:
#   do something to each item

#Running through a range of numbers
#for number in range(a, b):
#   print(number)

#While loop
#while something_is_true
#   Do something repeatedly

#number_of_hurdles = 6
#while number_of_hurdles > 0:
#   hurdle()
#   number_of_hurdles -= 1


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#    hurdle()

#Why choose one loop over the other?
#For loops are great for iterating over something and you need to do something with each thing that you are iterating over
#for fruit in fruits
#   print(fruits)
#for n in range(1, 6)
#   print(n)

#While loops are for when you don't care what number in a sequence you are in, what item you are iterating through in a list
#You just want to carry some functionality many times until some condition you set
#While loops are dangerous because they can keep looping

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal() == True:
#     if front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         hurdle()

#or
# while not at_goal() == True:
#     if wall_in_front() == True:
#         hurdle()
#     else:
#         move()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def hurdle():
#     turn_right()
#     move()
#     turn_right()
#     move()

# while not at_goal() == True:
#     if wall_in_front() == True and right_is_clear() != True:
#         turn_left()
#     elif wall_on_right() == True:
#         move()
#     elif right_is_clear() == True:
#         hurdle()
#     elif front_is_clear() == True:
#         move()

#Her solution

# def turn_right():
#      turn_left()
#      turn_left()
#      turn_left()
# def jump():
#      turn_left()
#      while wall_on_right():
#          move()
#      turn_right()
#      move()
#      turn_right()
#      while front_is_clear():
#          move()
#      turn_left()
# while not at_goal():
#      if wall_in_front():
#          jump()
#      else:
#          move()

#My solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal() == True:
#     if right_is_clear == True:
#         turn_right()
#         move()
#     elif not wall_in_front() == True:
#         move()
#         turn_right()
#     else:
#         turn_left()

#Her solution

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()


###Final Solution for all Worlds###
# def turn_right():
#      turn_left()
#      turn_left()
#      turn_left()
# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#      if right_is_clear():
#          turn_right()
#          move()
#      elif front_is_clear():
#          move()
#      else:
#          turn_left()