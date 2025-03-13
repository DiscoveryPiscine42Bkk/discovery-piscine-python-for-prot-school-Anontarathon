import sys
if len(sys.argv) !=4:
    print("none")
else:
    a = sys.argv[0:3]
    b = sys.argv[1]
    c = sys.argv[2]
    d = sys.argv[3]
    count1 = len(a)
    count2 = len(b)
    count3 = len(c)
    count4 = len(d)
    
    
    
    print(f"parameter: {count1}$") 
    print(f"{sys.argv[1]}: {count2}$")
    print(f"{sys.argv[2]}: {count3}$")
    print(f"{sys.argv[3]}: {count4}$" )