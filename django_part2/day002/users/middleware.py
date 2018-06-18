def my_middleware(view_fun):
    def func1(*args, **kwargs):
        print("----视图执行前处理的代码")
        response = view_fun(*args, **kwargs)
        print("----视图执行后处理的代码")

        return response
    return func1