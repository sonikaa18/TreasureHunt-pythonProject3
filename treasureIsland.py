print('''Welcome to Treasure Island 
your Mission is to find the treasure''')

while True:
     choice=input("left or right").lower()
     if choice=="left":
         choice = input("Wait or Swim").lower()
         if choice=="Wait":
             choice = input("red 0r blue or yellow").lower()
             if choice == "yellow":
                 print("you Win")
             else:
                 break
         else:
             break
     else:
         break
print("Game over")
