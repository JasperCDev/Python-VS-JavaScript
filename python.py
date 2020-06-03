
# --------------- PYTHON DATA TYPES -------------------
#------------------------------------------------------


# string = "string"
# print(string + ' is ' + str(type(string)))

# number = 1
# print(str(number) + ' is ' + str(type(number)))

# decimal = 1.4
# print(str(decimal) + ' is ' + str(type(decimal)))

# boolean = True
# print(str(boolean) + ' is ' + str(type(boolean)))

# array = []
# print(str(array) + ' is ' + str(type(array)))

# object = {}
# print(str(object) + ' is ' + str(type(object)))

# null = None
# print(str(null) + ' is ' + str(type(null)))


#------------------PYTHON CONDITIONALS --------------------
#----------------------------------------------------------

#------------PART ONE ----------------------------------
# num1 = 1
# num2 = 2


# if num1 == num2: # 'is' also works
#   print(str(num1) + ' is equal to ' + str(num2))

# if num1 != num2: # 'is not' also works
#   print(str(num1) + ' is not equal to ' + str(num2))

# if num1 < num2:
#   print(str(num1) + ' is less than ' + str(num2))

# if num1 > num2:
#   print(str(num1) + ' is greater than ' + str(num2))


# #------------PART TWO ----------------------------------


# variable = 'string'

# if str(type(variable)) == "<class 'int'>":
#   print('variable is type int')
# elif str(type(variable)) == "<class 'str'>":
#   print('variable is type str')
# else:
#   print('variable is not type int or type str')


#---------------INLINE CONDITIONAL----------------------

# bool = True

# inline = 'True' if bool else 'False'
# print(inline)

#--------------- PYTHON LOOPS --------------------------
#-------------------------------------------------------


# list = ['JavaScript', 'Python', 'Jasper', 'Tim', 'Jay']

# ####################
# for string in list:
#   print(string)

#############################
# for n in range(len(list)):
#   print(n)


############################
# i = 0

# while i < 10:
#   print(i)
#   i += 1
# else:
#   print(i >= 10)

#----------------PYTHON FUNCTIONS--------------------------
#----------------------------------------------------------

#declaration
# def add(a, b):
#   return a + b

# print(add(1, 2))

#anonymous
# anonymous = lambda x : x * 2
# print(anonymous(1))


#--------------ROCK PAPER SCISSORS EXAMPLE-----------------
#----------------------------------------------------------

# TO-DO: WRITE ROCK PAPER SCISSORS FUNCTION----------------

# def rockPaperScissors(n):
#   permutations = []
#   plays = ['R', 'P', 'S']
#   def loop(string):
#     if (len(string) == n):
#       permutations.append(string)
#       return
#     for play in plays:
#       loop(string + play)
#   loop('')
#   return permutations


# print(rockPaperScissors(3))


#----------------------SPIRAL TRAVERSAL---------------------
#-----------------------------------------------------------

# def spiralTraversal(matrix):
#   copy = matrix.copy()
#   list = []
#   if copy[0]:
#     list = list + copy[0]
#     copy.pop(0)
#     for row in copy:
#       list.append(row[-1])
#       row.pop()
#     if copy[0]:
#       for i in range(len(copy[0]) - 1, - 1, -1):
#         list.append(copy[-1][i])

#       copy.pop()
#       for i in range((len(copy) - 1), -1, -1):
#         if copy[i][0]:
#           list.append(copy[i][0])
#           copy[i].pop(0)

#   if not len(list) or not list[0]: return []

#   if len(copy) > 1:
#     return list + spiralTraversal(copy)
#   else:
#     if (len(copy)):
#       return list + copy[0]
#     else:
#       return list


# print(spiralTraversal([
#   [ 1, 2, 3, 4],
#   [ 5, 6, 7, 8],
#   [ 9,10,11,12],
#   [13,14,15,16],
# ]));

# print(spiralTraversal([
#   [1],
#   [2],
#   [3],
#   [4],
#   [5],
#   [6],
#   [7],
#   [8],
# ]));


#------------ROTATED MATRIX----------------
#------------------------------------------


# def rotateMatrix(matrix):
#   copy = matrix.copy()
#   list = []
#   if copy[0]:
#     for i in range(0, len(copy)):
#       newRow = []
#       for j in range(len(copy) - 1, -1, -1):
#         newRow.append(copy[j][i])
#       list.append(newRow)
#   return list


# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# print(rotateMatrix(matrix));