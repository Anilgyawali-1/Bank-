from oop import bank_info
import time
import random
import importlib
import os

print('\033[1m'+'\033[32m'+"\n\n          WELCOME T0 " + '\033[0m' )
r = '\033[031m'
y = '\033[033m'
c = '\033[036m'
e = '\033[0m'
b = '\033[38;5;4m'
ca = '\033[035m'
def mai():
  colors = [
  '\033[34m',
  '\033[94m',
  '\033[36m',
  '\033[96m',
  '\033[38;5;67m',
  '\033[38;5;63m',
  '\033[38;5;20m',
  '\033[38;5;18m',
  '\033[38;5;69m',
  '\033[38;5;33m',
  '\033[38;5;188m',
  '\033[38;5;153m',
  '\033[38;5;153m',
  '\033[38;5;99m',
  '\033[38;5;105m',
  '\033[38;5;39m',
  '\033[38;5;75m',
  '\033[38;5;87m',
  '\033[38;5;159m',
  '\033[38;5;69m',
  '\033[38;5;159m',
  '\033[38;5;51m',
  '\033[38;5;33m',
  ]

  L = ["N","\n\n   M","A","I","T","I","  N","E","P","A","L","  B","A","N","K","  P","V","T",".","  L","T","D",". \n\n"]
  l = 0
  for l in range(22):
    l += 1
    print('\033[1m'+ colors[l] + L[l], end = "" + '\033[0m')
mai()
time.sleep(2)
print("\n Enter Your Command \n a. 1 for new account \n b. 2 for Login")

x = int(input("\n What's Your Choice :"))

# ============= first part of bank ============ #

if (x == 1):

  # =========== New Account Formation =========== #

  print("For New Acc You Have To Fill A Form ")
  a2 = input("\n Enter your name: ").strip()
  c1 = input("\n Enter your password: ").strip()
  for n in range(3):
    if len(c1) < 8 :
      print(y+ "password must be 8 Digit Number encluding special , AplphaNumeric , capital and smaller"+ e)
      c1 = input("\n Enter Your Password: ").strip()
          # print(i)
    elif c1 == 8:
        break
    else:
      pass
  if len(c1) < 8:
    raise Exception(r+"password error. You are attempting it too much please Re-Sign Up"+e)
  d1 = int(input("\n Enter your ACC/NO. :"))
  b1 = int(input("\n Enter your deposits: "))
  e1 = int(input("\n Set Up Your Transactio Pin: "))
  for n in range(3):
    if len(str(e1)) < 4 :
            print(y+"TP must be composition of 4 digit"+e)
            e1 = int(input("\n Set up your Transation Pin: "))
                # print(i)
    elif len(str(e1)) == 4:
              break
    else:
            pass
  if len(str(e1)) < 4:
    raise Exception(r+"Transaction-Pin Error. You are attempting it too many times please Re-Sign Up"+e)
  a1 = bank_info()
  lineso = ["Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"]
  with open(f"./Datas/data_{d1}.py", "a") as f:
    lines = [a2, c1, d1, b1, e1]
    polen = ["a1", "b1", "c1", "d1", "e1"]
    f.write(f"Data_format = {lineso}")
    f.write(f"\nData_{d1} = {lines}")
    f.write(f"\n{polen[0]} =  Data_{d1}[0]")
    f.write(f"\n{polen[1]} =  Data_{d1}[1]")
    f.write(f"\n{polen[2]} =  Data_{d1}[2]")
    f.write(f"\n{polen[3]} =  Data_{d1}[3]")
    f.write(f"\n{polen[4]} =  Data_{d1}[4]")

  # ============= logic part_1 =============== #

  time.sleep(3)
  aloa = a2.upper()
  print(f"\n You Have Authenticated as ",b + f"\"{aloa}\""+e)
  mai()
  print("\n PROFILE : ")
  print(ca + f'\n (👤) "{aloa}" \n Acc/No. : {d1}'+e)
  print(ca  + f"Your balance is ${b1}.00"+e)
  acco = "\n What your accomodation sir/mam !"
  print(acco.title())
  print(
      "\n Accomodations: \n a. 1 For Withdraw \n b. 2 For Deposits Balance \n c. 3 for Money transaction \n d. 4 For Other Services.. \n e. 5 For Quit "
  )
  accin = int(input("\n:"))

  # ============== withdraw ============== #
  if accin == 1:
    fstinp = int(input("Enter Your Transaction Pin : "))
    if fstinp == e1:
      if b1 > 1:
        fstin = int(input("\n Withdraw Money Rs. :"))
        nola = b1
        print(f"Current balance is ${nola}.00")
        print(c  + "Procesing..." + e)
        time.sleep(2)
        with open(f"Datas/data_{d1}.py", "w") as mla:
          lineso = ["Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"]
          lines = [a2, c1, d1, nola - fstin, e1]
          polen = ["a1", "b1", "c1", "d1", "e1"]
          mla.write(f"Data_format = {lineso} ")
          mla.write(f"\nData_{d1} = {lines}")
          mla.write(f"\n{polen[0]} =  Data_{d1}[0]")
          mla.write(f"\n{polen[1]} =  Data_{d1}[1]")
          mla.write(f"\n{polen[2]} =  Data_{d1}[2]")
          mla.write(f"\n{polen[3]} =  Data_{d1}[3]")
          mla.write(f"\n{polen[4]} =  Data_{d1}[4]")
          a1.withdraw(fstin, b1)
      else:
        print(r + "Withdrawl Interrupted ! Your balance must be more than $ 1.00 For Withdrawl ")
    else:
      raise Exception("Wrong Transaction Pin" + e)

  # ============== deposits ============== #
  elif accin == 2:
    ndinp = input("Enter Your PassWord : ")
    if ndinp == c1:
      ndin = int(input("\n Deposit Money Rs. :"))
      sola = b1
      print(f"Current balance is ${sola}.00")
      print(c + "Procesing..." + e)
      time.sleep(2)
      with open(f"Datas/data_{a2}.py", "w") as mla:
        lineso = ["Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"]
        lines = [a2, c1, d1, sola + ndin, e1]
        polen = ["a1", "b1", "c1", "d1", "e1"]
        mla.write(f"Data_format = {lineso}")
        mla.write(f"\nData_{d1} = {lines}")
        mla.write(f"\n{polen[0]} =  Data_{d1}[0]")
        mla.write(f"\n{polen[1]} =  Data_{d1}[1]")
        mla.write(f"\n{polen[2]} =  Data_{d1}[2]")
        mla.write(f"\n{polen[3]} =  Data_{d1}[3]")
        mla.write(f"\n{polen[4]} =  Data_{d1}[4]")
      a1.deposit(ndin, b1)
    else:
      raise Exception(r + "Wrong Password" + e)

  elif accin == 3:

    # ============ transactions ============= #

    # ============= Sender ============= #
    rdinp = int(input("Enter Your Transaction Pin : "))
    if rdinp == e1:
      if b1 > 1:
        ftin_1 = int(input("\n Amount to send. :"))
        ndin = input("Recievers Account no. :")
        cola_1 = b1
        sola_1 = cola_1 - ftin_1
        print(f"Current balance is ${cola_1}.00")
        print(c + "Procesing..." + e)
        time.sleep(2)
        lineso = ["Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"]
        with open(f"Datas/data_{d1}.py", "w") as mla:
          mla.write(f"Data_format = {lineso}")
          lines = [a2, c1, d1, sola_1, e1]
          polen = ["a1", "b1", "c1", "d1", "e1"]
          mla.write(f"\nData_{d1} = {lines}")
          mla.write(f"\n{polen[0]} =  Data_{d1}[0]")
          mla.write(f"\n{polen[1]} =  Data_{d1}[1]")
          mla.write(f"\n{polen[2]} =  Data_{d1}[2]")
          mla.write(f"\n{polen[3]} =  Data_{d1}[3]")
          mla.write(f"\n{polen[4]} =  Data_{d1}[4]")
        a1.transactions(ftin_1, sola_1)
        print(f"Amount ${ftin_1}.00 Succesfully Sent To Acc/No. {ndin} ")
  
        # ============= reciever ============ #
        data_module = importlib.import_module(f"Datas.data_{ndin}")
        reciever_set = [
            data_module.a1, data_module.b1, data_module.c1, data_module.d1,
            data_module.e1
        ]
        with open(f"Datas/data_{ndin}.py", "w") as pla:
          lineso = ["Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"]
          lala = reciever_set[3] + ftin_1
          lines = [
              reciever_set[0], reciever_set[1], reciever_set[2], lala,
              reciever_set[4]
          ]
          polen = ["a1", "b1", "c1", "d1", "e1"]
          pla.write(f"Data_format = {lineso} ")
          pla.write(f"\nData_{ndin} = {lines}")
          pla.write(f"\n{polen[0]} =  Data_{ndin}[0]")
          pla.write(f"\n{polen[1]} =  Data_{ndin}[1]")
          pla.write(f"\n{polen[2]} =  Data_{ndin}[2]")
          pla.write(f"\n{polen[3]} =  Data_{ndin}[3]")
          pla.write(f"\n{polen[4]} =  Data_{ndin}[4]")
          print(f"Reciever's Name is {reciever_set[0].upper()}.")
      else:
        print(r + "Transaction Innerupted ! You balance must be more than $ 1.00 for Transaction"+e)
    else:
      raise Exception(r+"Wrong Transaction Pin"+ e)

  elif accin == 4:

    # =========== password/TP Change ========== #
    print("\n a. p for password change \n b. T for Transactions pin change")
    psctpin = input("\n :")

    # ============ password ============= #

    if psctpin == "p":
      pstpndinp = input("\n Enter Your Password :")
      if pstpndinp == c1:
        npp = input(" Enter Your New Password : ")
        npp2 = input(" Re-Type Your Password :")
        if npp == npp2:
          print(c + "Procesing..." + e)
          time.sleep(2)
          with open(f"Datas/data_{d1}.py", "w") as mla:
            lineso = [
                "Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"
            ]
            lines = [a2, npp, d1, b1, e1]
            polen = ["a1", "b1", "c1", "d1", "e1"]
            mla.write(f"Data_format = {lineso}")
            mla.write(f"\nData_{d1} = {lines}")
            mla.write(f"\n{polen[0]} =  Data_{d1}[0]")
            mla.write(f"\n{polen[1]} =  Data_{d1}[1]")
            mla.write(f"\n{polen[2]} =  Data_{d1}[2]")
            mla.write(f"\n{polen[3]} =  Data_{d1}[3]")
            mla.write(f"\n{polen[4]} =  Data_{d1}[4]")
          print(c + 
              f"Successfull Changed !!. Your New Password is {npp}. Dont Share With Others " +e
          )
        else:
          print(r + "Exception Wrong !. You Typed two Different Credentials"+e)
      else:
        raise Exception(r+"Wrong Password" + e)

  # ============ TP ============= #
    else:
      pstpndinp = input("Enter Your Transaction pin :")
      if pstpndinp == e1:
        ntp = input("Enter Your New Transaction pin  : ")
        ntp2 = input("Re-Type Your Transaction pin :")
        if ntp == ntp2:
          print(c + "Procesing..." + e)
          time.sleep(2)
          with open(f"Datas/data_{d1}.py", "w") as mla:
            lineso = [
                "Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"
            ]
            lines = [a2, c1, d1, b1, ntp]
            polen = ["a1", "b1", "c1", "d1", "e1"]
            mla.write(f"Data_format = {lineso}")
            mla.write(f"\nData_{d1} = {lines}")
            mla.write(f"\n{polen[0]} =  Data_{d1}[0]")
            mla.write(f"\n{polen[1]} =  Data_{d1}[1]")
            mla.write(f"\n{polen[2]} =  Data_{d1}[2]")
            mla.write(f"\n{polen[3]} =  Data_{d1}[3]")
            mla.write(f"\n{polen[4]} =  Data_{d1}[4]")
          print(y + 
              f"Successfull Changed !!. Your New Transaction pin is {ntp}. Dont Share With Others " + e
          )
        else:
          print(r + "Exception Wrong !. You Typed two Different Credentials"+e)
      else:
        raise Exception(r+"Wrong Password" + e)

  # ============ Quit process ============= #

  else:
    print("\n INITALIZING....")
    time.sleep(3)
    print(
        "\n      Re-Saved Changes.... \n\n      Thank You For Your Co-operation "
    )
    mai()
    
    # break

# ============= second_part of bank =========== #
else:
 
  uinp1 = input("\n Enter your Name : ")
  unip = input("\n Enter your password : ")
  for i in range(3):
    if len(unip) < 8 :
      print(y+ "password must be 8 Digit Number"+ e)
      unip = input("\n Enter Your Password: ")
          # print(i)
    elif unip == 8:
        break
    else:
      pass
  if len(unip) < 8:
    raise Exception(r+"password error. You are attempting it too much please Re-Sign Up"+e)
  else:
    pass
  uinp2 = input("\n Enter your Acc/no. : ")
  data_module = importlib.import_module(f"Datas.data_{uinp2}")
  dola = [
      data_module.a1, data_module.b1, data_module.c1, data_module.d1,
      data_module.e1
  ]
  p1 = bank_info()
  if (os.path.exists(f"./Datas/data_{uinp2}.py") and dola[1] == unip
      and dola[0] == uinp1):
    mai()
    aloa = uinp1.upper()
    print("\n PROFILE :")
    print(ca + f'\n (👤) "{aloa}" \n Acc/No. : {uinp2}'+e)
    print(ca + f"Your Balance is ${dola[3]}.00" + e)
    acco = "\n What your accomodation sir/mam !"
    print(acco.title())
    print(
        "\n Accomodations: \n a. 1 For Withdraw \n b. 2 For Deposits Balance \n c. 3 for Money transaction  \n d. 4 For Other Services.. \n e. 5 For Quit "
    )

    # ============== logic part ============== #

    accin = int(input("\n:"))
    # ============== withdraw ============== #
    if accin == 1:
      fstinp = int(input("Enter Your Transaction Pin : "))
      if fstinp == dola[4]:
        fstin = int(input("\n Withdraw Money Rs. :"))
        nola = dola[3]
        print(f"Current balance is ${nola}.00")
        print(c + "Procesing..." + e)
        time.sleep(2)
        with open(f"Datas/data_{uinp2}.py", "w") as mla:
          lineso = [
              "Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"
          ]
          lines = [dola[0], dola[1], dola[2], nola - fstin, dola[4]]
          polen = ["a1", "b1", "c1", "d1", "e1"]
          mla.write(f"Data_format = {lineso} ")
          mla.write(f"\nData_{dola[2]} = {lines}")
          mla.write(f"\n{polen[0]} =  Data_{dola[2]}[0]")
          mla.write(f"\n{polen[1]} =  Data_{dola[2]}[1]")
          mla.write(f"\n{polen[2]} =  Data_{dola[2]}[2]")
          mla.write(f"\n{polen[3]} =  Data_{dola[2]}[3]")
          mla.write(f"\n{polen[4]} =  Data_{dola[2]}[4]")
        p1.withdraw(fstin, dola[3])
      else:
        raise Exception(r + "Wrong Transaction Pin" + e)

    # ============== deposits ============== #
    elif accin == 2:
      ndinp = input("Enter Your PassWord : ")
      if ndinp == dola[1]:
        ndin = int(input("\n Deposit Money Rs. :"))
        tola = dola[3]
        pola = tola + ndin
        print(f"Current balance is ${tola}.00")
        print(c + "Procesing..." + e)
        time.sleep(2)
        with open(f"Datas/data_{uinp2}.py", "w") as mla:
          lineso = [
              "Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"
          ]
          lines = [dola[0], dola[1], dola[2], pola, dola[4]]
          polen = ["a1", "b1", "c1", "d1", "e1"]
          mla.write(f"Data_format = {lineso}")
          mla.write(f"\nData_{dola[2]} = {lines}")
          mla.write(f"\n{polen[0]} =  Data_{dola[2]}[0]")
          mla.write(f"\n{polen[1]} =  Data_{dola[2]}[1]")
          mla.write(f"\n{polen[2]} =  Data_{dola[2]}[2]")
          mla.write(f"\n{polen[3]} =  Data_{dola[2]}[3]")
          mla.write(f"\n{polen[4]} =  Data_{dola[2]}[4]")
        p1.deposit(ndin, dola[3])
      else:
        raise Exception(r + "Wrong Password" + e)

      # ============ transactions ============= #
    elif accin == 3:

      # ============= Sender ============= #
      rdinp = int(input("Enter Your Transaction Pin : "))
      if rdinp == dola[4]:
        ftin_1 = int(input("\n Amount to send. :"))
        ndin = input("Recievers Account no. :")
        cola_1 = dola[3]
        sola_1 = cola_1 - ftin_1
        print(f"Current balance is ${cola_1}.00")
        print(c + "Procesing..." + e)
        time.sleep(2)
        lineso = ["Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"]
        with open(f"Datas/data_{dola[2]}.py", "w") as mla:
          mla.write(f"Data_format = {lineso}")
          lines = [dola[0], dola[1], dola[2], sola_1, dola[4]]
          polen = ["a1", "b1", "c1", "d1", "e1"]
          mla.write(f"\nData_{dola[2]} = {lines}")
          mla.write(f"\n{polen[0]} =  Data_{dola[2]}[0]")
          mla.write(f"\n{polen[1]} =  Data_{dola[2]}[1]")
          mla.write(f"\n{polen[2]} =  Data_{dola[2]}[2]")
          mla.write(f"\n{polen[3]} =  Data_{dola[2]}[3]")
          mla.write(f"\n{polen[4]} =  Data_{dola[2]}[4]")
        p1.transactions(ftin_1, cola_1)
        print(y + f"Amount ${ftin_1}.00 Succesfully Sent To Acc/No. {ndin} " + e)


        # ============= reciever ============ #
        data_module = importlib.import_module(f"Datas.data_{ndin}")
        reciever_set = [
            data_module.a1, data_module.b1, data_module.c1, data_module.d1,
            data_module.e1
        ]
        print(f"Reciever's Name is {reciever_set[0].upper()}.")
        with open(f"Datas/data_{ndin}.py", "w") as pla:
          lineso = [
              "Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"
          ]
          lala = reciever_set[3] + ftin_1
          lines = [
              reciever_set[0], reciever_set[1], reciever_set[2], lala,
              reciever_set[4]
          ]
          polen = ["a1", "b1", "c1", "d1", "e1"]
          pla.write(f"Data_format = {lineso} ")
          pla.write(f"\nData_{ndin} = {lines}")
          pla.write(f"\n{polen[0]} =  Data_{ndin}[0]")
          pla.write(f"\n{polen[1]} =  Data_{ndin}[1]")
          pla.write(f"\n{polen[2]} =  Data_{ndin}[2]")
          pla.write(f"\n{polen[3]} =  Data_{ndin}[3]")
          pla.write(f"\n{polen[4]} =  Data_{ndin}[4]")
      else:
        raise Exception(r + "Wrong Transaction Pin" + e)

    elif accin == 4:

      # =========== password/TP Change ========== #
      print("\n a. p for password change \n b. T for Transactions pin change")
      psctpin = input("\n :")

      # ============ password ============= #

      if psctpin == "p":
        pstpndinp = input("\n Enter Your Password :")
        if pstpndinp == dola[1]:
          npp = input(" Enter Your New Password : ")
          npp2 = input(" Re-Type Your Password :")
          if npp == npp2:
            print(c + "Procesing..." + e)
            time.sleep(2)
            with open(f"Datas/data_{uinp2}.py", "w") as mla:
              lineso = [
                  "Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"
              ]
              lines = [dola[0], npp, dola[2], dola[3], dola[4]]
              polen = ["a1", "b1", "c1", "d1", "e1"]
              mla.write(f"Data_format = {lineso}")
              mla.write(f"\nData_{dola[2]} = {lines}")
              mla.write(f"\n{polen[0]} =  Data_{dola[2]}[0]")
              mla.write(f"\n{polen[1]} =  Data_{dola[2]}[1]")
              mla.write(f"\n{polen[2]} =  Data_{dola[2]}[2]")
              mla.write(f"\n{polen[3]} =  Data_{dola[2]}[3]")
              mla.write(f"\n{polen[4]} =  Data_{dola[2]}[4]")
            print(y + 
                f"Successfull Changed !!. Your New Password is {npp}. Dont Share With Others " + e
            )
          else:
            print(r + "Exception Wrong !. You Typed two Different Credentials" + e)
        else:
          raise Exception(r + "Wrong Password" + e)

    # ============ TP ============= #
      else:
        pstpndinp = int(input("Enter Your Transaction Pin :"))
        if pstpndinp == dola[4]:
          ntp = int(input("Enter Your New Transaction pin  : "))
          ntp2 = int(input("Re-Type Your Transaction pin :"))
          if ntp == ntp2:
            print(c + "Procesing..." + e)
            time.sleep(2)
            with open(f"Datas/data_{uinp2}.py", "w") as mla:
              lineso = [
                  "Name", "Password", "ACC/NO.", "Balance", "Transaction Pin"
              ]
              lines = [dola[0], dola[1], dola[2], dola[3], ntp]
              polen = ["a1", "b1", "c1", "d1", "e1"]
              mla.write(f"Data_format = {lineso}")
              mla.write(f"\nData_{dola[2]} = {lines}")
              mla.write(f"\n{polen[0]} =  Data_{dola[2]}[0]")
              mla.write(f"\n{polen[1]} =  Data_{dola[2]}[1]")
              mla.write(f"\n{polen[2]} =  Data_{dola[2]}[2]")
              mla.write(f"\n{polen[3]} =  Data_{dola[2]}[3]")
              mla.write(f"\n{polen[4]} =  Data_{dola[2]}[4]")
            print( y + 
                f"Successfull Changed !!. Your New Transaction pin is {ntp}. Dont Share With Others " + e
            )
          else:
            print(r + "Exception Wrong !. You Typed two Different Credentials" + e)
        else:
          print(r + "Wrong Transaction pin. Please enter the correct transaction pin." + e)
          


    # ============ Quit process ============= #

    else:
      print("\n INITALIZING....")
      time.sleep(3)
      print(
          "\n     Re-Saved Changes.... \n    Thank You For Your Co-operation "
      )
      mai()
      # break
  else:
    print(r + "\n SORRY FAILED TO LOGIN !!.." + e,  ca + " \n (\_/)", "\n (@.@)", "\n (>⚠️ )> Err " +e, r +"\n Name or password or Acc/no. Might be Wrong check it out !! ⚠️ " +e )
