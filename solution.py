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

# -- GROSS PROFIT MARGIN --
total = 0
for d in data:
    account_type = d["account_type"]
    value_type = d["value_type"]
    if account_type == "sales" and value_type == "debit":
        total_amt = d["total_value"]
        total += total_amt

gross_prof = int(round((total / revenue) * 100))
print("Gross Profit Margin: {}%".format(gross_prof))

# -- NET PROFIT MARGIN --
net_prof = ((revenue - expenses) / revenue) * 100
net_prof_rounded = int(round(net_prof))
print("Net Profit Margin: {}%".format(net_prof_rounded))
