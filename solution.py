import json

with open("data.json", "r") as inp:
    data_read = inp.read()

all_data = json.loads(data_read)
data = all_data["data"]

# -- REVENUE --
revenue = 0
for d in data:
    account_cat = d["account_category"]
    if (account_cat == "revenue"):
        total_amt = d["total_value"]
        revenue += total_amt

revenue = int(round(revenue))

print("Revenue: ${:,}".format(revenue))
