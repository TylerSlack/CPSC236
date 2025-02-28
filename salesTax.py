SALES_TAX = .06
def sales_tax(total):
    return total * SALES_TAX
def after_sales_tax(total):
    return total + sales_tax(total)