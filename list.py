my_momos = ['chiken']
my_friends_momo = my_momos[:]

my_friends_momo.append("buff")
my_momos.append('veg')

print(my_momos)
print(my_friends_momo)

print("My momos are ")
for momo in my_momos:
    print(momo)

print("My friends momos are ")
for momo in my_friends_momo:
    print(momo)