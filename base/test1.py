class A:
    def aa(self):
        print('aa')

    def say(self):
        print('say AAA!')


class B:
    def bb(self):
        print('bb')

    def say(self):
        print('say BBB!')


class C(B, A):
    def __init__(self, nn):
        self.nn = nn

    def cc(self):
        print('CC')


c = C(3)
c.say()
print(dir(c))
print(c.__dict__)
print(c.__class__)
# print(c.__bases__)
# print(c.__base__)
print(C.mro())
