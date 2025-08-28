budget = 1000

expenses = [120, 250, 80, 300, 150, 200, 90]

total_spent = 0

log = []
for i in range(len(expenses)):
    
    budget -= expenses[i]
    total_spent += expenses[i]

    log.append({
        "Expense #":i+1,
        "Amount": expenses[i],
        "Remaining Budget": budget
    })

    if budget < 0:
        print(f"Expense #{i+1}: {expenses[i]} |  Budget Exceeded by {abs(budget)}")
        print(f"\n\nTotal spent before overshoot: {total_spent - expenses[i]}")
        break
    else:
        print(f"Expense #{i+1}: {expenses[i]} | Remaining Budget: {budget}")
        
else:
    print("All expenses were covered!")
    print(f"Final leftover: {budget}")

print("\n Expense log:")

for entry in log:
    print(entry)

