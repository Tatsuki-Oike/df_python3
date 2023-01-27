global_x = "global_x"

def f():
    enclosing_x = "enclosing_x"

    def g():
        local_x = "local_x"
        print(f"関数gのlocalスコープ : {locals()}")

    print(f"関数fのlocalスコープ : {locals()}")
    g()

f()

print(f"globalスコープ : {globals()}")
print(f"builtinスコープ : {dir(__builtins__)}")