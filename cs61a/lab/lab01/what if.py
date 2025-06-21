def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make
bake(1, "mashed potatoes")
def pressure(v, t, n=6.022e23):
    """计算理想气体的压力，单位为帕斯卡

    使用理想气体定律：http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- 气体体积，单位为立方米
    t -- 绝对温度，单位为开尔文
    n -- 气体粒子，默认为一摩尔
    """
    k = 1.38e-23  # 玻尔兹曼常数
    return n * k * t / v
def f(x):
    f=print(x)
    return print(x)
print("A:"),f(2)
def h(x):
    print(f(x))
    return f(x) 
def g(x):
    y = f(x)
    print(y)
    return y 
print("B:"),h(2)
print("c:"),g(2)
print(print(3))