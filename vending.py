# Author    : Kelvin Bacelli
# Email     : kbacelli@umass.edu
# Spire ID  : 34596797

class VendingMachine:

    def __init__(self):
        self.items = {}
        self.balance = 0.0
        self.total_sales = 0.0
        self.change = 0.0
        self.sales_history = []
    
    def add_item(self,item_name,price,quantity):
        if item_name not in self.items:
            self.items[item_name] = {'price':price,'quantity':quantity}
            print(f"{quantity} {item_name}(s) added to inventory")        
        else:
            self.items[item_name]['quantity'] += quantity
            self.items[item_name]['price'] = price
            print(f"{quantity} {item_name}(s) added to inventory")
    
    def get_item_price(self,item_name):
        if item_name not in self.items:
            print("Invalid item")
            return None
        else:
            return self.items[item_name]['price']

    def get_item_quantity(self,item_name):
        if item_name not in self.items:
            print("Invalid item")
            return None
        else:
            return self.items[item_name]['quantity']

    def list_items(self):
        sorted_items = sorted(self.items)
        if len(self.items) == 0:
            print("No items in the vending machine")
        else:
            print("Available items:")
            for key in sorted_items:
                print(f"{key} (${self.items[key]['price']}): {self.items[key]['quantity']} available")

    def insert_money(self,dollar_amount):
        if dollar_amount == 1.0 or dollar_amount == 2.0 or dollar_amount == 5.0:
            self.balance += round(dollar_amount,2)
            print(f"Balance: {self.balance}")
        else:
            print("Invalid amount")

    def purchase(self,item_name):
        if item_name not in self.items:
            print("Invalid item")
        elif self.items[item_name]['quantity'] == 0:
            print(f"Sorry {item_name} is out of stock")
        elif self.balance < self.items[item_name]['price']:
            print(f"Insufficient balance. Price of {item_name} is {self.items[item_name]['price']}")
        else:
            self.items[item_name]['quantity'] -= 1
            self.balance -= self.items[item_name]['price']
            print(f"Purchased {item_name}\nBalance: {self.balance}")
            self.total_sales += round(self.items[item_name]['price'],2)
            self.sales_history.append((item_name,self.items[item_name]['price']))

    def output_change(self):
        if self.balance > 0:
            self.change += self.balance
            print(f"Change: {self.change}")
            self.balance = 0.0
        else:
            print("No change")

    def remove_item(self,item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} removed from inventory")
        else:
            print("Invalid item")

    def empty_inventory(self):
        self.items.clear()
        print("Inventory cleared")

    def get_total_sales(self):
        return round(self.total_sales,2)

    def stats(self, N):
        if len(self.sales_history) == 0:
            print("No sale history in the vending machine")
            return

    # Get the N most recent sales
        recent_sales = self.sales_history[-N:]

    # Build the statistics dictionary
        stats_dict = {}
        for item_name, price in recent_sales:
            if item_name in stats_dict:
                stats_dict[item_name]['total_sales'] += price
                stats_dict[item_name]['count'] += 1
            else:
                stats_dict[item_name] = {'total_sales': price, 'count': 1}

    # Sort by item name
        sorted_stats = sorted(stats_dict.items())

    # Print results
        print(f"Sale history for the most recent {len(recent_sales)} purchase(s):")
        for item_name, data in sorted_stats:
            print(f"{item_name}: ${round(data['total_sales'], 2)} for {data['count']} purchase(s)")
