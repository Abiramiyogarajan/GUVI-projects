def register():
    db = open("loginvalid.txt", "r")
    un = input("create username")
    pw = input("create password")
    pw1 = input("confirm password")
    d = []
    f = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    print(data)

    if pw != pw1:
        print("password don't match, restart")
        register()
    else:
        if len(pw) <= 6:
            print("password too short")
            register()
        elif un in db:
            print("username exists")
            register()
        else:
            db = open("loginvalid.txt", "a")
            db.write(un + ", " + pw + "\n")
            print("Success")


register()


def access():
    un = input("enter username")
    pw = input("enter password")
    if not len(un or pw) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
          if data[un]:
             try:
                if pw == data[un]:
                  print("Login success")
                  print("Hi,", un)
                else:
                  print("Password or usename incorrect")
             except:
                 print("incorrect password or username")

          else:
            print("username doesn't exist")
        except:
            print("login error")
    else:
        print("please enter a value")


def home(option=None):
    option = input("Login|Signup:")
    if option == "login":
        access()
    elif option == "signup":
        register()
    else:
        print("pls enter an option")
home()
