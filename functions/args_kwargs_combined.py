

#Combined args and kwargs with normal parameters

def info(a, b, *args, **kwargs):
    print("a (parameter):", a)
    print("b (parameter):", b)
    print("args (extra positional):", args)
    print("kwargs (extra keywords):", kwargs)


info(10, 20, 30, 40, name="Kusuma", age=25)