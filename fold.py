Sum = lambda x, y: x + y
Dif = lambda x, y: x - y
Mul = lambda x, y: x * y
Div = lambda x, y: x / y
Square = lambda x: x*x


def Foldl(function, a):
    it = iter(a)
    res = next(it)
    for x in it:
        res = function(res, x)
    return res

def Foldr(function, a):
    a = reversed(a)
    it = iter(a)
    res = next(it)
    for x in it:
        res = function(x, res)
    return res

def Map(function, *args):
    if len(args) == 1:
        a = list(args[0])
        for i in range(len(a)):
            a[i] = function(a[i])
        return a
    else:
        it = iter(args)
        res = list(next(it))
        for x in it:
            for i in range(len(x)):
                res[i] = function(res[i],x[i])
        return res

def Fold_r(function, a):
    res = a[-1]
    for i in range(-2, -len(a) - 1, -1):
        res = function(a[i], res)
    return res

def Fold_l(function, a):
    res = a[0]
    for i in range(1, len(a)):
        res = function(res, a[i])
    return res

def Fold_r2(function, a):
    if len(a) == 2:
        return Fold_l(function, a)
    else:
        return Fold_l(function, [a[0], Fold_r2(function, a[1:])])

def Fold_l2(function, a):
    if len(a) == 2:
        return Fold_r(function, a)
    else:
        return Fold_r(function, [Fold_l2(function, a[:-1]), a[-1]])

ar = [16, 4, 2, 1]
print(Foldl(Sum, ar), Foldl(Dif, ar), Foldl(Mul, ar), Foldl(Div, ar))
print(Foldr(Sum, ar), Foldr(Dif, ar), Foldr(Mul, ar), Foldr(Div, ar))
print(Fold_l(Sum, ar), Fold_l(Dif, ar), Fold_l(Mul, ar), Fold_l(Div, ar))
print(Fold_r(Sum, ar), Fold_r(Dif, ar), Fold_r(Mul, ar), Fold_r(Div, ar))
print(Fold_l2(Sum, ar), Fold_l2(Dif, ar), Fold_l2(Mul, ar), Fold_l2(Div, ar))
print(Fold_r2(Sum, ar), Fold_r2(Dif, ar), Fold_r2(Mul, ar), Fold_r2(Div, ar))
#print(Map(Square, ar))
#a = [1, 2, 3]
#b = [4, 5, 6]
#c = [7, 8, 9]
#print(Map(Sum, a, b, c))

a = ['a', 'b', 'c', 'd']
print(reduce(lambda x, y: y + x, reversed(a)))
print(Fold_r(Sum, a))
print(__name__)


