import sys
in_f_name = sys.argv[1]
out_f_name = sys.argv[2]
f = open('cat.bmp', "rb")
d = f.read()
#print d[:16]
#import struct
#print struct.unpack("<ccihhi", d[:14])
#print len(d)
#print struct.unpack("<iiihhiiiiii", d[14:54])
#print len(d)
d2 = d[:54] + (len(d)-54)*'\xff'
open("cat1.bmp", "wb").write(d2)
d2 = d[:54] + (len(d) - 54)*'\x00'
open("cat2.bmp", "wb").write(d2)