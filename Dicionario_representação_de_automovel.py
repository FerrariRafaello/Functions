import pprint

def car_dictionary_demo():
    print('Creating a dictionary to store car data:')
    car = {
        'brand': 'Hyundai',
        'model': 'hb20',
        'year': 2015,
        'engine': 1.6,
        'transmission': 'automatic',
        'accessories': [],
    }
    print('Dictionary created:', car)

    # Update some values
    car['year'] = 2018
    car['model'] = 'hb20 R-spec'
    print('Upgraded to a newer car:', car)

    # Adding accessories
    print('Adding accessories to the car:')
    car['accessories'] = ['alarm']
    print('Installed a new alarm')
    car['accessories'].append('sound system')
    print('Added a new sound system:', car)
    car['accessories'][1] = 'different sound system'
    print('Replaced the sound system model:', car)

    # Removing accessories
    del car['accessories']
    print('Removed accessories key:', car)


def products_dictionary_demo():
    products = {
        1: {
            'description': 'wireless optical mouse',
            'price': 50.0,
            'stock': 130
        },
        2: {
            'description': 'USB keyboard',
            'price': 42.0,
            'stock': 100
        },
        3: {
            'description': '20 inch color monitor',
            'price': 850.0,
            'stock': 20
        },
        4: {
            'description': 'pair of speakers',
            'price': 90.0,
            'stock': 17
        }
    }
    pprint.pprint(products)


# Call demos
car_dictionary_demo()
products_dictionary_demo()
