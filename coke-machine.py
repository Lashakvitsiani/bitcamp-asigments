coins = [5, 10, 25]


amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    insert = int(input("Insert Coin: "))


    if insert not in coins:
    
        continue


    amount_due -= insert


print(f"Change Owed: {abs(amount_due)}")
