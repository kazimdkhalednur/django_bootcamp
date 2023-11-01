class Animal:
    name = "Tiger"


    def __init__(self, name):
        self.name = name
        self.height = 34
    

    def __str__(self):
        return "This is Animal Class"


    def display(self):
        # self.asdf = "greg"
        # print(self.asdf)
        print(self.name)
        print(self.height)

#     # def display2(self):
#     #     print(self.asdf)



# obj = Animal("Tiger")
# # print(obj)
# # print(obj.name)
# # # print(obj.height)
# # obj.display()
# # obj.display2()
# obj.name="aetert"
# obj.height=67
# obj.display()


# inheritance

class Ahgfh:
    def display(self):
        print("This is class A")

class adff:
    def sdff(self):
        print("THis is sdff")
    
    def display(self):
        print("This is class adff")


class Bgrertewyh(Ahgfh, adff):
    def asdf(self):
        print("This is class B")
    
    def display(self):
        print("This is class Bgrertewyh")
        # super(Bgrertewyh, self).display()
        # super(adff, self).display()
        adff().display()
        Ahgfh().display()


obj = Bgrertewyh()
obj.display()
# obj.super().display()
# obj.asdf()
# obj.sdff()



# # polymorphism

# class A:
#     def display(self):
#         print("This is A")

# class B:
#     def display(self):
#         print("This is B")

# class C:
#     def display(self):
#         print("This is C")

# obja = A()
# objb = B()
# objc = C()
# obja.display()
# objb.display()
# objc.display()


# encaptulation

# class A:
#     __a = "grs"

#     def change(self, a):
#         self.__a = a

#     def display(self):
#         print(self.__a)


# obj = A()
# obj.__a = "wqer"
# obj.display()

# obj.change("qwe")
# obj.display()