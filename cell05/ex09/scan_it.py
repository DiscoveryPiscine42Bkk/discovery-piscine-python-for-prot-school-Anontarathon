import sys

if len(sys.argv) !=3:
    print("none")
else:
    a = sys.argv[1]
    b = sys.argv[2]
    c = ({a},{b}) 
    count = len(c)
    print(f"{count}$")




    