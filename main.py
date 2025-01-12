from user import User
from restaurant import Restaurant
from partner import Agent
from order_items import OrderItem
from order import Order
from menu import MenuItem

def add_customer(name, email, phone, location):
    user = User(name, email, phone, location)
    User.users[user.user_id] = user
    return user

def add_restaurant(name, city, menu, status):
    restaurant = Restaurant(name, city, menu, status)
    Restaurant.restaurants[restaurant.restaurant_id] = restaurant
    return restaurant

def add_agent(name, phone):
    agent = Agent(name, phone)
    Agent.agents[agent.agent_id] = agent
    return agent

def place_order(user, restaurant, items):
    order = Order(user.user_id, restaurant.restaurant_id)
    Order.orders[order.order_id] = order
    for item in items:
        order.add_items(item)
    return order

def out_for_delivery(order_id):
    order = Order.orders[order_id]
    order.assign_agent()
    return order

def complete_order(order_id):
    order = Order.orders[order_id]
    order.order_complete()
    return order


user1 = add_customer(name="Hitesh", email="hd@gmail.com", phone="002", location="blore")
user2 = add_customer(name="Brad", email="bp@gmail.com", phone="001", location="blore")
user3 = add_customer(name="George", email="gc@gmail.com", phone="003", location="blore")


menu1 = [MenuItem("Biriyani", 100), MenuItem("Pepper Chicken", 200), MenuItem("Mutton", 200)]
menu2 = [MenuItem("pasta", 100), MenuItem("Chicken pizza", 200), MenuItem("Mutton pizza", 200)]


res1 = add_restaurant(name="Meghana Foods", city= "blore", menu = menu1, status="Open")
res2 = add_restaurant(name="Pizza Bakery", city= "blore", menu = menu2, status="Open")

agent1 = add_agent(name = "Santosh", phone="22")
agent2 = add_agent(name = "Ramesh", phone="13")
agent3 = add_agent(name = "Suresh", phone="17")

cart1 = [OrderItem(menu1[0].name, 1), OrderItem(menu1[1].name, 2)]
cart2 = [OrderItem(menu1[0].name, 3), OrderItem(menu1[1].name, 4)]

order1 = place_order(user1, res1, cart1)
print(order1.__dict__)

order2 = place_order(user2, res1, cart2)
print(order2.__dict__)

order1 = out_for_delivery(order1.order_id)
print(order1.__dict__)

order2 = out_for_delivery(order2.order_id)
print(order2.__dict__)

order1 = complete_order(order1.order_id)
print(order1.__dict__)

order2 = complete_order(order2.order_id)
print(order2.__dict__)

cart3 = [OrderItem(menu2[1].name, 2), OrderItem(menu2[0].name, 1)]
order3 = place_order(user3, res2, cart3)
print(order3.__dict__)

order3 = out_for_delivery(order3.order_id)
print(order3.__dict__)



