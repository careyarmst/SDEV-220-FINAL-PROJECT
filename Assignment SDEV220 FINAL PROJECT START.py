# Assignment SDEV220 FINAL PROJECT START ONLY
# Author: Carey Armstrong
# Version: 2.0
# Date: 2024-11-09

# Initialize Patron class
class Patron:
    pnumber = 0
    def __init__(self, mPurchase="None"):
        self.mPurchase = mPurchase
        Patron.pnumber += 1
        self.Patron_id = Patron.pnumber

    def __str__(self):
        return f"Patron ID: {self.Patron_id}, Miscellaneous Purchase:  {self.mPurchase}"

Patron1 = Patron("Hat")
Patron2 = Patron("small bucket")

print(Patron1)
print(Patron2)

#class Golfer(Patron):
 #   def __init__(self, pnumber, mPurchase, gPurchase, lname, fname, phone):
  #      super().__init__(pnumber)
   #     self.mPurchase = mPurchase
    #    self.gPurchase = gPurchase
     #   self.lname = lname
      #  self.fname = fname
       # self.phone = phone

