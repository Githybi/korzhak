letters={
"a":
'''
 ###
#   #
#   #
#####
#   #
#   #
#   #
''',
"b":
'''
####
#   #
#   #
####
#   #
#   #
#### 
''',
"c":
  '''
###
#   # 
#   
#    
#    
#   #
###
''',
"d":
  '''
####
#   #
#   #
#   #
#   #
#   # 
####
  ''',
"e":
  '''
#####
#
#
#####
#
#
#####
  ''',
"f":
  '''
#####
#
#
###
#
#
#
  ''',
"g":
  '''
### 
#   #
#
#  ##
#   #
#   #
 ###
 ''',
"h":
  '''
#   #
#   #
#   #
#####
#   # 
#   # 
#   #
  ''',
"i":
  '''
###
 #
 #
 # 
 #
 #
###
''',
"j":
  '''
 ###
  #
  #
  #
  #
  #
##
  ''',
"k":
  '''
#   #
#  #
# #
##
# #
#  #
#   #
''',
"l":
  '''
#
#
# 
#
#
#
#####
  ''',
"m":
  '''
#   #
#   #
## ##
# # #
#   #
#   #
#   #
''',
"n":
  '''
#   #
#   #
##  #
# # #
#  ##
#   #
#   #
''',
"o":
  '''
 ###
#   #
#   #
#   #
#   #
#   #
 ###
 ''',
"p":
 ''' 
####
#   #
#   #
####
#
#
#
''',
"q":
''' 
 ###
#   #
#   #
#   #
#   #
#  #
 ## #
''',
"r":
'''
####
#   #
#   #
####
# #
#  #
#   #
''',
"s":
'''  
 ####
#
#
 ###
    #
    #
 ###
''',
"t":
'''
#####
  #
  #
  #
  #
  #
  #
''',
"v":
'''
#   #
#   #
#   #
#   #
#   #
 # #
  #
''',
"w":
'''
#   #
#   # 
#   # 
# # #
## ##
#   #
#   #
''',
"x":
'''
#   #
#   #
 # #
  #
 # #
#   #
#   #
''',
"y":
'''
#   #
#   #
 # #
  #
  #
  #
  #
''',
"z":
'''
 #####
     #
    #
   #
  #
 # 
 ##### 
 ''',
}

user_input = input()
print("output:")
for letter in user_input.lower():
  print(letters[letter])