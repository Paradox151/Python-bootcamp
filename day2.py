 #tip calculator
print("wlcome to tip calculator")
bill = int(input("enter total bill $:"))
tip = int(input("how much tip do you want to give? 10 ,12 0r 15:"))
split= int(input("how many people dou you want to split the bill"))
final_bill =  (bill*(tip/100*1))/split
print(f"each person should pay {final_bill}")
