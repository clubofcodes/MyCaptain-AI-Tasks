class MyClass:

    def method(self):
        return 'instance method called'

    @classmethod
    def classmethod(cls):
        return 'class method called'

    @staticmethod
    def staticmethod():
        return 'static method called'

#instance
obj = MyClass()
print(obj.method())

#classmethod
print(MyClass.classmethod())

#staticmethod
print(MyClass.staticmethod())
