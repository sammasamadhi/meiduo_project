class demoClass(object):
    instances_created = 0

    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)
        instance = super(demoClass, cls).__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance

    def __init__(self, attribute):
        print("__init__():", self, attribute)
        self.attribute = attribute

test1 = demoClass("abc")
print(test1.__class__.__mro__)
# test2 = demoClass("xyz")
# print(test2.__class__.__mro__)
# print(test1.number, test1.instances_created)
# print(test2.number, test2.instances_created)


# class Root(object):
#     def __init__(self):
#         print("this is Root")
#
#
# class B(Root):
#     def __init__(self):
#         print("enter B")
#         super(B, self).__init__()
#         print("leave B")
#
#
# class C(Root):
#     def __init__(self):
#         print("enter C")
#         super(C, self).__init__()
#         print("leave C")
#
#
# class D(B, C):
#     pass
#
#
# d = D()
# print(d.__class__.__mro__)



