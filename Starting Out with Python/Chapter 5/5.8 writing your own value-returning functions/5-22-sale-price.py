# This program calculates a retail item's sale price

DISCOUNT_PERCENTAGE = 0.20

def main():
    reg_price = get_regular_price()
    sale_price = reg_price - discount(reg_price)
    print(f'The sale price is ${sale_price:,.2f}.')

def get_regular_price():
    return float(input("Enter the item's regular price: "))

def discount(price):
    return price * DISCOUNT_PERCENTAGE

main()
