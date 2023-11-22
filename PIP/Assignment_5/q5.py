a = 4
def f():
    global a
    a = 5
    def g():
        nonlocal a
        a = 10
        print("Inside function g, ", "a=", a)
        def h():
            nonlocal a
            a = 20
            print("Inside function h, ", "a=", a)
        h()
    g()
    print("Inside function f, ", "a=", a)
f()
