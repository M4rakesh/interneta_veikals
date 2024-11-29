
#Uzdevumu var pielikt eksamenam,netiku gala ar prog.,jo vajadzeja atkartot temu
class Gramata:
    def __init__(self,nosaukums,autors,pieejamiba=True):
        self.nosaukums = nosaukums
        self.autors = autors
        self.pieejamiba= pieejamiba

    
    def mainit_piejamibu(self):
        self.pieejamiba = not self.pieejamiba


    def g_info(self):
        print(f"Gramatas nosaukums: {self.nosaukums},gramatas autors: {self.autors},gramatas pieejamiba: {self.pieejamiba}")
garamatej=[]
#def del_g(index):
    #response=input("Vai jūs veleties izdzest gramatu no saraksta (y/n): ")
    #if response=='y':
        



g1=Gramata("Antara","Dainis","Pieejama")
g2=Gramata("Rich dad poor dad","Robert T.Kiyosaki","Pieejama")
g1.g_info()
g2.g_info()


garamatej.append(g1)
garamatej.append(g2)
