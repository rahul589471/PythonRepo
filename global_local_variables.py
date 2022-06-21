x = 45


def func_test():
    global x
    x = x + 10
    print("value of x inside function  is : ", x)

    def test_function():
        global x
        x = 100
        print("value of x inside-2 function  is : ", x)

    test_function()

def func_test2():
    global x
    x = x + 10
    print("value of x inside func_test2 function  is : ", x)


print("value of x is : ", x)

func_test()
func_test2()


print("value of x after function call is : ", x)
