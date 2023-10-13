# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spend exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar.  Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

expense = {'January': 2200, 'February': 2350, 'March': 2600, 'April': 2130, 'May': 2190}
extra = expense['January'] -  expense['February']
print("In Feb, ",abs(extra)," dollars you spent extra compare to January")
first_quater_expense = expense['January'] + expense['February'] + expense['March']
print("First quater expense is ",first_quater_expense)
for spend in expense:
    if (expense[spend] == 2000):
        print("In ",spend,"You spend exactly 2000 ")
# We can use update function to add the value
expense['June'] = 1980

expense['April'] = 2130 + 200
# expense.update({'April': 2330})

print(expense)
