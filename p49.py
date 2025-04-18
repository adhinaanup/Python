class bank_account:
    def __init__(self,deposit,owner):
        self.__deposit=deposit
        self.owner=owner
    def check(self,o):
        print(o.__deposit)
    def update(self,e,amt):
        if self.owner=='owner':
            e.__deposit+=amt
            print(e.__deposit)
        else:
            print('Unauthorized')
    def debit(self,e,amt):
        if self.owner=='owner':
            e.__deposit-=amt
            print(e.__deposit)
        else:
            print('Invalid')

obj1=bank_account(3000,'banker')
obj2=bank_account(9000,'owner')
obj2.debit(obj2,900)

