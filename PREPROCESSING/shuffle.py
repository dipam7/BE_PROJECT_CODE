import random
fid = open("generated_fuzzified_access_data2.csv", "r")
li = fid.readlines()
fid.close()
#print(li)

random.shuffle(li)
#print(li)

fid = open("shuffled_example.csv", "w",newline='')
fid.writelines(li)
fid.close()
