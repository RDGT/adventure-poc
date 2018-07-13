from lib import entity


class Entry(entity.MenuItem):
    pass


# starting entry
equipped = Entry(
    name='I am equipped and ready',
    description='I am equipped and ready to enter the cursed dungeon, I wonder what evil lurks within.'
)


# level 1 entries
cursed_dungeon = Entry(
    name='I have entered the Cursed Dungeon',
    description='I have entered this cursed dungeon, I wonder what evil lurks within.'
)

kitchen_zombie_mistress = Entry(
    name='The Mistress',
    description='The zombie told me about a "mistress". Seems like there are dark forces at play here.'
)
acquired_ring = Entry(
    name='A Ring',
    description='I have acquired a ring. It seems to be of some importance.'
)
destroyed_zombie = Entry(
    name='Vanquished a Zombie',
    description='I have destroyed the zombie.'
)
found_a_key = Entry(
    name='An Iron Key',
    description='I have found a key. Now where is the lock?'
)