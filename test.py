for i in range(1,100):
    if i==10:
        print("eurek")
    elif i==15:
        print("ppp")
    else:
        print(f"da li radi {i}")

for i in range(1,100):
    try:
        a=100/i
        print(a)
    except ZeroDivisionError as pp:
        print(pp)
        raise
    except:
        print("minja")
        print("jj")
print("pera")
print("zdera")
a=1
