class Try:
    var = "Dekha"
    var2 = "Dhyan se dekho..."
    var3 = var+", "+var2
    def fun1(abc):
        print(abc.var)
        print(abc.var2)

class Try2(Try):
    # print(Try.var) --Ask var without prenthisis in try
    # print(Try().fun1()) -- try with ()
    # print(Try.var3)
    @classmethod
    def cmet(cls):
        print(Try().var2)

    # def __init__(abc2):
    #     Try().fun1()
        