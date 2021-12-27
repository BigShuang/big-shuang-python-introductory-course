class A:
    pass


class B(A):
    pass


a = A()
b = B()

# r1 = isinstance(a, A)
# r2 = isinstance(a, B)
# r3 = isinstance(b, A)
# r4 = isinstance(b, B)
# print(r1)
# print(r2)
# print(r3)
# print(r4)


ta = type(a)
tb = type(b)

print(ta)
print(tb)
print(ta==tb)
print(ta==A)
print(ta==B)
print(tb==A)
print(tb==B)