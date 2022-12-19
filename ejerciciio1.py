from ast import main


class Nonogram():

    def _init_(self,clues):
        self.clues=clues
        self.rows=len(clues[0])
        self.columns=len(clues[1])
        self.board=[[0 for i in range(self.rows)] for j in range(self.columns)]
        print(self.board)

    def solve(self):
        pass

#experimentacion
clues1=Nonogram([1,1])

if __name__=='__main__':
   main()