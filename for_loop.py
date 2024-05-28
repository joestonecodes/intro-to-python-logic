#i = 0
#numbers_divisible_by3 = 0
#while numbers_divisible_by3 < 10: # not sure of how many numbers I need
#    i = i +1 
#    if i % 3 == 0:
#        numbers_divisible_by3 = numbers_divisible_by3 +1
#        print(i)
#my_name = "Joe Stone"

#for i in range(len(my_name)): # i know what I need
#    print(my_name[i])
#    i = 1 + 1

#names = ["bob", "janet", "herbert", "satan"]    #an array

#for name in names:
#    print(name + "@themultiverse.school")

guests = "Art,Hal,RZA,Josh,Albert"

names = guests.split(",")

names.append("liz")
names.append("liz")

print(len(names))
print(names[6]) #last is the list
print(names[0]) #First in the list
names[6] = "Roger"
first_person = names.pop(-1) #pops it out of the list. -1 pull the first from the last
for name in names[0:3]: 
    print(name + "@themultiverse.school")

