import sys 
if len(sys.argv)   !=2:
    print("none")
else:
    pa = sys.argv[1]
    user = input("what")
    if pa == user:
        print("Good job")
    else :
        print("Nope, sorry")