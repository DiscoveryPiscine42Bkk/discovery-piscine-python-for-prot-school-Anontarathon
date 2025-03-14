def greeting(n=None):#(2)นำ 1 มา พิจารณา
    if n is None :#
        print("noble stranger")#3
    elif isinstance(n, str):#
        print(f"Hello, {n}")#3
    else:
        print("Error it not was a name")#3
greeting('Alexandra')#1
greeting('Wil')
greeting()
greeting(42)
    