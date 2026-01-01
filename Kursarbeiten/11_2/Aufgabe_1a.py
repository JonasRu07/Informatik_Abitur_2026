class A:
    def __init__(self) -> None:
        self.__a = 100
        print(12)
        
class B(A):
    def __init__(self) -> None:
        super(A).__init__()
        
    def get_a(self):
        return self.__a
       
# i
var1 = A()
var2 = var1

print(f"{id(var1)} = {id(var2)}")
del var1
print(f"Var2: {id(var2)}")

# ii
var3 = B()
print(var3.get_a())