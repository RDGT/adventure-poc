from lib import entity


class Item(entity.MenuItem):
    pass


# starting items
crossbow = Item('Crossbow', 'Your trusty crossbow')
holy_cross = Item('Holy Cross', 'Your Holy Cross')
holy_water = Item('Holy Water', 'A vial of holy water')
flammable_oil = Item('Flammable Oil', 'A vial of flammable oil')

# level 1 items
iron_key = Item('Iron Key', 'Iron Key found in the pocket of a leather coat in a closet')
engagement_ring = Item('Engagement Ring', 'A ring found on a Zombie')

# level 2 items
nitro = Item('Nitroglycerin', 'You made a small vial of nitroglycerin')
