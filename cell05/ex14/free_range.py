import sys
argv   = sys.argv[1:]
if len(argv) == 0:
    print("none")
elif len(argv) == 2:
    st = int(argv[0])
    end = int(argv[1])
    result = list(range(st, end+1))
    print(result)
else:
    print("none")
