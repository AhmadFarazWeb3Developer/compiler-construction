class SymbolTable:
    def __init__(self):

        self.size = 10
        self.table = [[] for _ in range(self.size)]
        self.memory = 1000


    def add(self,name,symbol): # self must always be the first parameter
    
            index = self.hash(name)
            self.table[index].append([name, symbol, self.memory])
            self.memory+=1

    def hash(self,name):
         return sum(ord(c) for c in name) % self.size

   
    def display(self):
        print("Index\tName\tSymbol\tMemory")
        print("----------------------------------")
        for i in range(self.size):
            for name, symbol, memory in self.table[i]:
                print(i, "\t", name, "\t", symbol, "\t", memory)

table= SymbolTable()


table.add("a", "int"),
table.add("b", "float"),
table.add("c", "char"),
table.add("d", "bool"),
table.add("e", "int"),
table.add("f", "float"),
table.add("g", "char"),
table.add("h", "bool"),
table.add("i", "int"),
table.add("j", "float"),
table.add("k", "char")
table.display()



# self = the current object, so you can access its variables and functions.
# just like this pointer we have in other langauges


# self is needed in every function which know which object to refer