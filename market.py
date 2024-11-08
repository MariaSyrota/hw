class Market2:
    location = ("location: Ukraine")
    purchase = ("purchase: Ukraine")
    size = ("size: big")
    prices = ("prices: normal")

class ATB(Market2):
    size = ("size: normall")
    def milk(self, how_much_milk):
        print(f"milk costs {how_much_milk}grn")

class Avrora(Market2):
    purchase = ("purchase: China")
    size = ("size: small")
    prices = ("prices: small")

    def milk2(self, how_much_milk2):
        print(f"milk costs {how_much_milk2}grn")

class Aliexpress(Market2):
    location = ("location: online")
    purchase = ("purchase: China")
    size = ("size:-")
    prices = ("prices:realy small")

    def milk3(self, how_much_milk3):
        print(f"milk costs {how_much_milk3}grn")

class Market(ATB, Avrora , Aliexpress):
    pass

print("ATB:")
magasin = ATB()
print(magasin.location)
print(magasin.purchase)
print(magasin.size)
print(magasin.prices)
magasin.milk("45")
print("Avrora:")
magasin2 = Avrora()
print(magasin2.location)
print(magasin2.purchase)
print(magasin2.size)
print(magasin2.prices)
magasin2.milk2("32")
print("Aliexpress:")
magasin3 = Aliexpress()
print(magasin3.location)
print(magasin3.purchase)
print(magasin3.size)
print(magasin3.prices)
magasin3.milk3("10")