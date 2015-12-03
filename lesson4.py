f = open('hosts', "w")
#type(f)
#data = f.readlines()
#print data
#print data[0], data[4]
#Traceback (most recent call last):
#   File ""
f.write("127.0.0.1, vk.com")
f.close()

f = open('hosts', "a")
f.write("127.0.0.1, vk.com \n")