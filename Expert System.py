print("-----Welcome to RAJ BHAVAN-----\n")
print("--------MEALS MENU--------")
print("1.South Indian Thali\n2.North Indian Thali\n3.Chettinadu Combo\n4.Chinese Silk\n")
a=int(input("Choose a meal (Note:Enter the respective meal number): "))
if a==1:
    print("Starter:Papad\nMain course:Rice with curd, sambar, rasam, vatha kozhambu\nSide dish:Ladysfinger fry,Potato fry\nSweet:Laddoo\nPrice:130")
    Total=130
elif a==2:
    print("Starter:Paneer Tikka\nMain course:Chapathi, Paratha, Jeera Rice\nSide dish:Vegetable curry, Dhal\nSweet:Rasmalai\nPrice:150")
    Total=150
elif a==3:
    print("Starter:Chettinadu masala paneer tikka\nMain course:Rice with curd, two varieties of chettinadu gravy\nSide dish:Cabbage poriyal, Potato Roast\nSweet:Paal payasam\nPrice:140")
    Total=140
elif a==4:
    print("Starter:Chilli gobi\nMain course:Fried rice, Noodles\nSide dish:Paneer Manchurian\nSweet:Ice cream\nPrice:160")
    Total=160
else:
    print("Kindly enter the respective number of the dish")
b=input("Do you want to place the order(Yes/No): ")
Bill_amount=Total
if b=="Yes":
    print("Bill amount")
    if a==1:
        print(Bill_amount)
    elif a==2:
        print(Bill_amount)
    elif a==3:
        print(Bill_amount)
    elif a==4:
        print(Bill_amount)
    else:
        print("Invalid Entry")
    
else:
    c=input("Do you want to continue ordering(Note:Type Yes): ")
    if c=="Yes":
        d=int(input("Choose a meal (Note:Enter the respective meal number): "))
        if d==1:
            print("Starter:Papad\nMain course:Rice with curd, sambar, rasam, vatha kozhambu\nSide dish:Ladysfinger fry,Potato fry\nSweet:Laddoo\nPrice:130")
            Total=130
        elif d==2:
            print("Starter:Paneer Tikka\nMain course:Chapathi, Paratha, Jeera Rice\nSide dish:Vegetable curry, Dhal\nSweet:Rasmalai\nPrice:150")
            Total=150
        elif d==3:
            print("Starter:Chettinadu masala paneer tikka\nMain course:Rice with curd, two varieties of chettinadu gravy\nSide dish:Cabbage poriyal, Potato Roast\nSweet:Paal payasam\nPrice:140")
            Total=140
        elif d==4:
            print("Starter:Chilli gobi\nMain course:Fried rice, Noodles\nSide dish:Paneer Manchurian\nSweet:Ice cream\nPrice:160")
            Total=160
        else:
            print("Kindly enter the respective number of the dish")
        Bill_amount+=Total
        print("Bill amount")
        print(Bill_amount)
print("\nTHANK YOU!")
        
        
