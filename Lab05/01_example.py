class SymbolTable:
    def __init__(self):
        self.table = []
        self.memory = 1000
    def add(self,name,symbol): # self must always be the first parameter
        self.table.append([name,symbol,self.memory])
        self.memory+=1

    def display(self):
        print("Name\tSymbol\tMemory")
        print("-----------------------")
        for name,symbol,self.memory in self.table:
                print(name, "\t", symbol,'\t',self.memory)


table= SymbolTable()

table.add("w","int")
table.add('x','float')
table.add('y','char')
table.add('z','bool')

table.display()



# self = the current object, so you can access its variables and functions.
# just like this pointer we have in other langauges