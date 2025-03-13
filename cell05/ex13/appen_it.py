import sys
if len(sys.argv) !=4:
   print("none")
else:
   a = sys.argv[1]
   b = sys.argv[2]
   c = sys.argv[3]
   new_w = a+ b[3:]
   new2_w = c+ b[3:]
   print(new_w)
   print(new2_w)