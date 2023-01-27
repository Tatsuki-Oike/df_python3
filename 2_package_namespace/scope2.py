global_x = "global_x"

def f():
    global global_x
    global_x = "global_x上書き"
    enclosing_x = "enclosing_x"

    def g():
        nonlocal enclosing_x
        enclosing_x = "enclosing_x上書き"
    g()
    print(enclosing_x)

f()
print(global_x)
