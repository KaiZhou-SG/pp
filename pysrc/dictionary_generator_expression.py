prices = {'apple': 0.40, 'banana': 0.50, 'orange': 0.60}
my_purchase = {
    'apple': 1,
    'orange': 10,
    'banana': 6
    }

grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print 'I owe the grocer $%.2f' %grocery_bill
