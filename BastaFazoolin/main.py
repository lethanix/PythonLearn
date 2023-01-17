class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        if end_time < 12:
            end_time += 12
        self.end_time = end_time

    def __repr__(self) -> str:
        return "{} menu is available from {} to {}".format(
            self.name, self.start_time, self.end_time
        )

    def calculate_bill(self, purchased_items: list):
        bill = 0
        for item in purchased_items:
            bill += self.items.get(item, 0)

        return bill


brunch = Menu(
    "Brunch",
    {
        "pancakes": 7.50,
        "waffles": 9.00,
        "burger": 11.00,
        "home fries": 4.50,
        "coffee": 1.50,
        "espresso": 3.00,
        "tea": 1.00,
        "mimosa": 10.50,
        "orange juice": 3.50,
    },
    11,
    4,
)

early_bird = Menu(
    "Early-bird",
    {
        "salumeria plate": 8.00,
        "salad and breadsticks (serves 2, no refills)": 14.00,
        "pizza with quattro formaggi": 9.00,
        "duck ragu": 17.50,
        "mushroom ravioli (vegan)": 13.50,
        "coffee": 1.50,
        "espresso": 3.00,
    },
    3,
    6,
)

dinner = Menu(
    "Dinner",
    {
        "crostini with eggplant caponata": 13.00,
        "caesar salad": 16.00,
        "pizza with quattro formaggi": 11.00,
        "duck ragu": 19.50,
        "mushroom ravioli (vegan)": 13.50,
        "coffee": 2.00,
        "espresso": 3.00,
    },
    5,
    11,
)

kids = Menu(
    "Kids",
    {
        "chicken nuggets": 6.50,
        "fusilli with wild mushrooms": 12.00,
        "apple juice": 3.00,
    },
    11,
    9,
)

print(brunch)

print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))


class Franchise:
    def __init__(self, address, menus) -> None:
        self.address = address
        self.menus = menus

    def __repr__(self) -> str:
        return "{} franchise".format(self.address)

    def available_menus(self, time) -> list:
        menu_list = []
        for menu in self.menus:
            if menu.start_time < time and menu.end_time > time:
                menu_list.append(menu.name)
        return menu_list


flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise(
    "12 East Mulberry Street", [brunch, early_bird, dinner, kids]
)

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(5 + 12))


class Business:
    def __init__(self, name, franchises) -> None:
        self.name = name
        self.franchises = franchises


basta_business = Business(
    "Basta Fazoolin' with my Heart", [flagship_store, new_installment]
)

arepas_menu = Menu(
    "Take a' Arepa",
    {
        "arepa pabellon": 7.00,
        "pernil arepa": 8.50,
        "guayanes arepa": 8.00,
        "jamon arepa": 7.50,
    },
    10,
    8,
)

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

arepas_business = Business("Take a' Arepa", arepas_place)
