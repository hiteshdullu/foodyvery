from partner import Agent
class Order:
    orders = {}
    order_id = 1
    def __init__(self, restaurant_id, customer_id):
        self.order_id = Order.order_id
        Order.order_id += 1
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.status = "Pending"
        self.items = []
        self.agent_id = None

    def add_items(self, item):
        self.items.append([item.menu_item, item.quantity])

    def assign_agent(self):
        for agent in Agent.agents:
            if Agent.agents[agent].status == "Available":
                self.agent_id = agent
                Agent.agents[agent].status = "Busy"
                self.status = "Out for Delivery"
                return agent
        return None

    def order_complete(self):
        self.status = "Order Complete"
        Agent.agents[self.agent_id] = "Available"