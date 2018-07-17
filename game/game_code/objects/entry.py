from lib import entity


class Entry(entity.MenuItem):
    pass


# == Starting Entry ==
equipped = Entry(
    name='I am equipped and ready',
    description='I am equipped and ready to enter the cursed dungeon, I wonder what evil lurks within.'
)

# == level 1 ==
# level 1 | Entrance Hall
cursed_dungeon = Entry(
    name='I have entered the Cursed Dungeon',
    description='I have entered this cursed dungeon, I wonder what evil lurks within.'
)
# level 1 | Closet Room
found_a_key = Entry(
    name='An Iron Key',
    description='I have found a key. Now where is the lock?'
)
# level 1 | Kitchen
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
# level 1 | Living Room
stand_ground = Entry(
    name='An Illusion',
    description='Iv encountered an illusion in the living room. Probably meant to ward off the simple folk.'
)
destroy_ghast = Entry(
    name='A Ghast',
    description='Iv destroyed the ghast in the living room. I should anticipate encountering more minions.'
)
use_key = Entry(
    name='Used Iron Key',
    description='The key fit the locked gate. I sense negligence. I can now go down the stairs to the next level.'
)

# == level 2 ==
# level 2 | Grande hall
ask_about_servants_no_ring = Entry(
    name='Who is Robert?',
    description='The ghoul told me about a certain "Robert". Perhaps he could tell me more.'
)
ask_about_servants_with_ring = Entry(
    name='Who is Robert?',
    description='The ghoul told me about a certain "Robert". Perhaps he could tell me more.\n'
                'Also the ring iv found seems to be important to this man.'
)
ghoul_mistress = Entry(
    name='The Mistress is in',
    description='The ghoul has told me that mistress is currently present and in her chamber below.'
)
examine_clock = Entry(
    name='Old Clock',
    description='The old clock in the Grande Hall has stopped working many years ago.'
)
clock_hands = Entry(
    name='Clock Hands Moved',
    description='Iv moved the clock hand to 3:15. A noise came from the dining room. I should investigate.'
)
ghoul_defeated = Entry(
    name='Destroyed the Ghoul',
    description='Iv destroyed the ghoul "butler".\n'
                'It would seem that mistress fancies herself as the owner of the estate.'
)
# level 2 | Library
clock_scribble = Entry(
    name='Clock Scribble',
    description='Iv found a scribble of a clock in the writing desk.\n'
                'In the scribble the clock hand point at 3:15. Perhaps this is will reveal some secrets.'
)
# level 2 | Dining Room
examine_table = Entry(
    name='Carved Inscription',
    description='Iv found an inscription carved into the table.\n'
                'It reads "Fortunes close. Masked by time." Perhaps this is worth investigating.'
)
# level 2 | Treasure room
robert_mistress = Entry(
    name='The Unholy Mistress',
    description='Robert claims to have been the rightful owner of the estate.\n'
                'He referred to mistress as "it". She seems to have unholy powers. I should not underestimate her.'
)
robert_ring = Entry(
    name='Gave Robert the Ring',
    description='Iv released robert from his torment.'
)
destroy_shadow_no_nitro = Entry(
    name='Destroyed Shadow',
    description='I have banished the evil shadow who was guarding the treasure.'
)
destroy_shadow_nitro = Entry(
    name='Destroyed Shadow',
    description='I have destroyed the shadow but the explosion destroyed the treasure chest and its contents.'
)
injured_vs_shadow = Entry(
    name='Injured by a Shadow',
    description='The fight with the shadow took its toll. Iv been injured. But I must press on.'
)
found_treasure = Entry(
    name='Found a Treasure',
    description='Iv found some gold and what seems to be Roberts head. I wonder where is the rest of him.'
)
# level 2 | Laboratory
make_nitro = Entry(
    name='Made Nitroglycerin',
    description='Iv used the apparatus in the laboratory to make a vial of nitroglycerin.\n'
                'This is a very potent chemical. I should be careful when using it.'
)
little_lock_box = Entry(
    name='Valuable Gem',
    description='Iv found a valuable gem in a little lock box, a ruby the size of my fist'
)
