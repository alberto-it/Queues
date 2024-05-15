class Order:
  def __init__(self, id, items, prep_time):
    self.id = id
    self.items = items
    self.prep_time = prep_time
    self.customer_notified = False

kitchen_queue = []
customer_queue = []

def add_order_to_customer(order):
    inserted = False
    for i, queue_order in enumerate(customer_queue):
        if order.prep_time < queue_order.prep_time:
            customer_queue.insert(i, order)
            inserted = True
            break
    if not inserted: customer_queue.append(order)

def process_next_order():
    if kitchen_queue:
        order = kitchen_queue.pop(0)
        order.customer_notified = True
        return order

print( '=' * 50)

order1 = Order(1, ["Burger", "Fries"], 10)
print("Adding first order...")
add_order_to_customer(order1)

order2 = Order(2, ["Pizza"], 15)
print("Adding second order...")
add_order_to_customer(order2)

print("Sending second order to the kitchen...")
kitchen_queue.append(order2)

order3 = Order(3, ["Salad"], 5)
print("Adding third order...")
add_order_to_customer(order3)

print("Sending first order to the kitchen...")
kitchen_queue.append(order1)

print("Sending third order to the kitchen...")
kitchen_queue.append(order3)

while kitchen_queue:
    completed_order = process_next_order()
    if completed_order:  print(f"Customer for order {completed_order.id}, your order is ready!")

print( '=' * 50)