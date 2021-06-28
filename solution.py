import json

with open("data.json", "r") as inp:
    data_read = inp.read()

all_data = json.loads(data_read)
data = all_data["data"]

# -- REVENUE AND EXPENSES --
revenue = 0
expenses = 0
for d in data:
    account_cat = d["account_category"]
    if account_cat == "revenue":
        total_amt = d["total_value"]
        revenue += total_amt
    elif account_cat == "expense":
        total_amt = d["total_value"]
        expenses += total_amt

revenue_rounded = int(round(revenue))
expenses_rounded = int(round(expenses))

print("Revenue: ${:,}".format(revenue_rounded))
print("Expenses: ${:,}".format(expenses_rounded))
