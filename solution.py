import json


# -- REVENUE --
def calc_rev(data):
    revenue = 0

    for d in data:
        account_cat = d["account_category"]
        if account_cat == "revenue":
            total_amt = d["total_value"]
            revenue += total_amt

    revenue_rounded = int(round(revenue))
    print("Revenue: ${:,}".format(revenue_rounded))

    return revenue


# -- EXPENSES --
def calc_exp(data):
    expenses = 0
    for d in data:
        account_cat = d["account_category"]
        if account_cat == "expense":
            total_amt = d["total_value"]
            expenses += total_amt

    expenses_rounded = int(round(expenses))

    print("Expenses: ${:,}".format(expenses_rounded))

    return expenses


# -- GROSS PROFIT MARGIN --
def calc_gpm(data, revenue):
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
def calc_net_prof(revenue, expenses):
    net_prof = ((revenue - expenses) / revenue) * 100
    net_prof_rounded = int(round(net_prof))
    print("Net Profit Margin: {}%".format(net_prof_rounded))


# -- WORKING CAPITAL RATIO --
def calc_wcr(data):
    assets = 0
    liabilities = 0
    for d in data:
        account_cat = d["account_category"]
        account_type = d["account_type"]
        value_type = d["value_type"]
        account_types_assets = ["current",
                                "bank", "current_accounts_receivable"]
        account_types_liab = ["current", "current_accounts_payable"]
        if account_cat == "assets" and account_type in account_types_assets:
            total_amt = d["total_value"]
            if value_type == "debit":
                assets += total_amt
            elif value_type == "credit":
                assets -= total_amt
        if account_cat == "liability" and account_type in account_types_liab:
            total_amt = d["total_value"]
            if value_type == "credit":
                liabilities += total_amt
            elif value_type == "debit":
                liabilities -= total_amt

    wcr = int(round((assets / liabilities) * 100))
    print("Working Captial Ratio: {}%".format(wcr))


def main():
    with open("data.json", "r") as inp:
        data_read = inp.read()

    all_data = json.loads(data_read)
    data = all_data["data"]

    revenue = calc_rev(data)
    expenses = calc_exp(data)
    calc_gpm(data, revenue)
    calc_net_prof(revenue, expenses)
    calc_wcr(data)


main()
