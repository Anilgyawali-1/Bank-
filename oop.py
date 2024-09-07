class bank_info:
  def chyeck_balance(self,depo):
        print(f"Your Current Balance is ${depo}.00")
    
  def withdraw(self, wamount,depo):
    if wamount <= depo:
        try:
          depo -= wamount
          print(f"WITHDRAWL SUCCESSFULLY . Your Balance is ${depo}.00  ")
        except Exception as e:
          print(f"WITHDRAWL INTERRUPTED ...{e} ")
    else:
      print("WITHYDRAWL INTERRUPTED ... .Withdrawl Amount is more than Your Total Balance  ") 
  def deposit(self, amount,depo):
        amount += depo
        print(f"DEPOSITED SUCCESSFULLY . Your New Balance is ${amount}.00 🏧")
    
  def transactions(self,amts, camount):
        camount -= amts
        print(f"\n Transaction SuccessFul . Your Balance is ${camount}.00. 🏧")