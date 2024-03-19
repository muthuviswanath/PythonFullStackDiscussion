
def red():
    a = 10
    def green():
        b = 20
        nonlocal a
        print(a)
        print(b)
        a = 45
        print(a)
    green()
red()