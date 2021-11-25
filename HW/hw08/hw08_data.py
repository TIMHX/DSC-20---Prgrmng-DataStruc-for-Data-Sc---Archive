### Data for Question 3 is below ###

Arda = ('Arda', 5, 10);        Yuxuan = ('Yuxuan', 6, 5)
Wesley = ('Wesley', 9, 5);     Aaron = ('Aaron', 7, 10)
Chase = ('Chase', 7, 5);       Cecilia = ('Cecilia', 8, 3)
Prem = ('Prem', 8, 2);         Sudiksha = ('Sudiksha', 8, 5)
Jonathan = ('Jonathan', 6, 5); Iman = ('Iman', 6, 7)
Etsu = ('Etsu', 3, 1);         Nabi = ('Nabi', 7, 5)
Aragorn = ('Aragorn', 10, 5);  Sauron = ('Sauron', 10, 6)
Neo = ('Neo', 10, 7);          Morpheus = ('Morpheus', 9, 10)

Pla1 = ('Pla1', 5, 10); Pla2 = ('Pla2', 6, 5)
Pla3 = ('Pla3', 4, 1);  Pla4 = ('Pla4', 4, 2)
Pla5 = ('Pla5', 9, 5);  Pla6 = ('Pla6', 7, 10)
Pla7 = ('Pla7', 8, 5);  Pla8 = ('Pla8', 8, 3)

secret_dict = {}
secret_dict.update({'Pla1': 'Arda', 'Arda': Pla1})
secret_dict.update({'Pla2': 'Yuxuan', 'Yuxuan': Pla2})
secret_dict.update({'Pla3': 'Etsu', 'Etsu': Pla3})
secret_dict.update({'Pla4': 'Nabi', 'Nabi': Pla4})
secret_dict.update({'Pla5': 'Wesley', 'Wesley': Pla5})
secret_dict.update({'Pla6': 'Aaron', 'Aaron': Pla6})
secret_dict.update({'Pla7': 'Sudiksha', 'Sudiksha': Pla7})
secret_dict.update({'Pla8': 'Cecilia', 'Cecilia': Pla8})

### Data for Questions 4-5-6 is below ###

def make_review(place, rating):
    return [place, rating]

def get_place(review):
    return review[0]

def get_rating(review):
    return review[1]

# Some reviews found from Google.
google_reviews = [
    make_review('Canyon Vista', 1),
    make_review('Canyon Vista', 3),
    make_review('Canyon Vista', 4),
    make_review('Canyon Vista', 1),
    make_review('Canyon Vista', 2),
    make_review('Foodworx', 3),
    make_review('Foodworx', 5),
    make_review('Foodworx', 1),
    make_review('Foodworx', 5),
    make_review('Foodworx', 3),
    make_review('Pines', 3),
    make_review('Pines', 2),
    make_review('Pines', 4),
    make_review('Pines', 5),
    make_review('Pines', 4),
    make_review('64 Degrees', 4),
    make_review('64 Degrees', 5),
    make_review('64 Degrees', 4),
    make_review('64 Degrees', 3),
    make_review('64 Degrees', 5),
    make_review('OVT', 5),
    make_review('OVT', 4),
    make_review('OVT', 2),
    make_review('OVT', 5),
    make_review('OVT', 4),
    make_review('Cafe Ventanas', 4),
    make_review('Cafe Ventanas', 1),
    make_review('Cafe Ventanas', 5),
    make_review('Cafe Ventanas', 3),
    make_review('Cafe Ventanas', 4)
]
