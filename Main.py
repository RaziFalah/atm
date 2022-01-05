print("==============================")
print("| Banking system  with python|")
print("| www.razifalah.com          |")
print("| By Razi Falah              |")
print("|Copyright(C) 2022 Razi falah|")
print("|============================|")



ids = {
    1: {
        "passcode" : 1,
        "sn" : 1,
        "amount" : 20.5,
        "name" : "Razi"
    },
    2: {
        "passcode" : 2,
        "sn" : 2,
        "amount" : 630.5,
        "name" : "Eliot"
    }
}

loop_holder = 0
def login(stopper):
 stopper += 1
 global ask_for_id
 ask_for_id = int(input("Input you id number: "))
 global ask_for_pass
 ask_for_pass = int(input("Input you passcode: "))
 global ask_for_sn
 ask_for_sn = int(input("Input your sn: "))
 def func(id, passcode, sn):
     if(id in ids):
         true_passcode = ids[id]["passcode"]
         true_sn = ids[id]["sn"]
     else:
         print("We wasn't able to authenticate the id you provided")
         exit()
     if (passcode == true_passcode):
         pass
     else:
         print("The passcode you entered is wrong")
         exit()
     if(sn == true_sn):
         pass
     else:
         print("Wrong sn")
         exit()
 func(ask_for_id, ask_for_pass, ask_for_sn)

if loop_holder == 0:
    login(loop_holder)
else:
    pass
loop_holder_pro = 0
def pro(stopper, loop_holder):
 stopper += 1
 while 0 != 1:
  print(f"your balance is: " + str(ids[ask_for_id]["amount"]))
  while 0 != 1:
   ask_for_action = input("Takeout / Send / Exit / new login / balance : ")
   ask_for_action = ask_for_action.strip()
   ask_for_action = ask_for_action.upper()
   if(ask_for_action == "EXIT"):
       print("Bye.")
       exit()
   elif (ask_for_action == "NEW LOGIN"):
       loop_holder -= 1
       login(loop_holder)
       stopper -= 1
       pro(stopper ,loop_holder)
   elif(ask_for_action == "TAKEOUT"):
       ask_for_amount = float(input("Amount: "))
       if(ids[ask_for_id]["amount"] - ask_for_amount < 0):
           print("You don't have enough money")
       else:
         newamount = ids[ask_for_id]["amount"] - ask_for_amount
         ids[ask_for_id]["amount"] = newamount
         print("Your new amount is: " + str(newamount))
   elif(ask_for_action == "SEND"):
       ask_for_account_id = int(input("Enter receiver's account id: "))
       if ask_for_account_id == ask_for_id:
           print("You can't send money to yourself")
       else:
        if ask_for_account_id in ids:
            ask_for_amount_to_send = int(input("Enter the amount: "))
            if ids[ask_for_id]["amount"] - ask_for_amount_to_send > 0:
             ids[ask_for_id]["amount"] -= ask_for_amount_to_send
             ids[ask_for_account_id]["amount"] += ask_for_amount_to_send
             print("Operation completed successfuly sent " + str(ask_for_amount_to_send) + " to mr." + ids[ask_for_account_id]["name"] + "'s account")
            else:
                print("You don't have enough money")
        else:
             print("Invalid account id")
   elif ask_for_action == "BALANCE":
       print(ids[ask_for_id]["amount"])
   else:
       print("Unkown action, check your spell and try again")

if loop_holder_pro == 0:
    pro(loop_holder_pro ,loop_holder)
else:
    pass
