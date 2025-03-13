import sys
if len(sys.argv) !=2:
    print("none")
else:
    string = sys.argv[1]
    a_n = [a for a in string if a == 'z']
    if len(a_n) == 0:
        print("none")
    else :
        print("".join(a_n) + "$")