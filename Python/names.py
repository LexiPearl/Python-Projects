#Part 1
# x={
#     'students':[
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# }
# def names(x):
#     for key, data in x.items():
#         for value in data:
#             print value["first_name"], value["last_name"]
# names(x)

#Part 2
users = {
 'Students': [
     {'first_name': 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def namescharacters(users):
    y=0
    print "Students"
    for key, data in users.items():
        for value in data:
            if 'Students' in key:
                y+=1
                print y, "-", value["first_name"], value["last_name"], "-", (len(value["first_name"])+ len(value["last_name"]))
    print "Instructors"
    y=0
    for key, data in users.items():
        for value in data:
            if 'Instructors' in key:
                y+=1
                print y, "-", value["first_name"], value["last_name"], "-", (len(value["first_name"])+ len(value["last_name"]))
namescharacters(users)


# users = {
#  'students': [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
#   ],
#  'instructors': [
#      {'first_name' : 'Michael', 'last_name' : 'Choi'},
#      {'first_name' : 'Trey', 'last_name' : 'Villafane'}
#   ]
#  }
#
# for key, data in users.items():
# 	print "\n%s" %key.title()
# 	counter = 0
#
# 	for value in data:
# 		counter = counter +1
# 		full_name = value["first_name"] + " " + value["last_name"]
# 		full_name_upper = full_name.upper()
# 		name_count = len(value["first_name"]) + len(value["last_name"])
#
# 		print "%d - %s - %d" %(counter, full_name_upper, name_count)
