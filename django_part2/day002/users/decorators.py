def register(f):
    def fun(*args, **kwargs):
        print("-----自定义装饰器被调用")
        return f(*args, **kwargs)

    return fun