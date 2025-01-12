class Restaurant:
    restaurants = {}
    restaurant_id = 1
    def __init__(self, name, city, menu, status):
        self.restaurant_id = Restaurant.restaurant_id
        Restaurant.restaurant_id+=1
        self.name = name
        self.city = city
        self.menu = menu
        self.status = status