from game_code import interactions
from game_code.interactions.lib import choices, events, conditions, scene
from game_code.objects import item, entry

temple_room = interactions.room.Room(
    name='Temple Room',
    opening_text='The stairs open to a large hall. In the center is a dark altar, a headless body rots on top.\n'
                 'Several pillars sorround the altar and at the far end are large stone steps\n'
                 'leading up to a decorated door, a few burning brassiers light the room.\n'
                 'Scattered on the steps are several demonic imps, biding their time. Probably "guard dogs".',
    # todo: @alon should there be sort of extra "room" for the steps,
    # todo: where you can go to the steps to interact with the imps later?
    choices=[
        # todo: @alon if not approach the imps, go back?
        choices.ChoiceInspectRoom('Approach the imps.', 'imps'),
        # choices.ChoiceInspectRoom('Attack Ghoul', 'attack'),
    ],
    scenes={
        'imps': interactions.thing.Thing(
            name='Temple Room',
            opening_text='As you come closer the imps all band together to face you.\n'
                         'They are cowardly creatures, full of greed and sin.',
            # todo: @alon can we only haggle if we got the coins from the treasure before?
            choices=[
                choices.ChoiceInspectRoom('Offer a gold coin', 'haggle'),
                choices.ChoiceInspectRoom('Destroy the foul beasts!', 'fight_imps'),
            ],
        ),
        'haggle': interactions.thing.Thing(
            name='Temple Room',
            opening_text='You pull out a gold coin. You have caught their attention.\n'
                         'Their eyes follow the coin as you throw it at their feet.\n'
                         'They cautiously come closer and examine the coin together as they huddle behind a pillar.\n'
                         'Passage seems safe.',
            choices=[
                choices.ChoiceInspectRoom('Have a look around', 'examine'),
                choices.ChoiceNavigate('Advance through the decorated door.', level='level_3', room='inner_cloister'),
                choices.ChoiceInspectRoom('Perhaps they know something about the headless corpse', 'ask_corpse',
                                          conditions=[conditions.OnlyOnce()]),
                choices.ChoiceInspectRoom('Destroy the foul beasts!', 'fight_imps'),
            ],
        ),
        'examine': interactions.thing.Thing(
            name='Temple Room',
            opening_text='The burning brassieres cast flickering shadows on the walls.\n'
                         'Above the door is an upside down cross. This is definitely an evil temple.',
            choices=[
                # todo: @alon once we examine, we can't go back to the imps to ask them questions
                choices.ChoiceInspectRoom('Examine altar', 'altar'),
                choices.ChoiceInspectRoom('Examine upside down cross', 'upside_down_cross'),
                choices.ChoiceNavigate('Advance to the Inner Cloister.', level='level_3', room='inner_cloister'),
                choices.ChoiceNavigate('Go back to the statue room.', level='level_2', room='statue_room'),
            ],
        ),
        'ask_corpse': interactions.thing.Thing(
            name='Temple Room',
            opening_text='You play with a few more coins in your hand. The sound attracts the imps.\n'
                         'You point at the altar and ask: "who is that?".One imp steps forward.\n'
                         '"Is master! Lord of place! IS CURSED! LIKE PLACE!" You toss the coin to the imp.\n'
                         'He catches it and skitters away.',
            choices=[
                # . Offer more gold
                choices.ChoiceInspectRoom('Ask about mistress', 'ask_mistress'),
                choices.ChoiceInspectRoom('Have a look around', 'examine'),
                choices.ChoiceInspectRoom('Destroy the foul beasts!', 'fight_imps'),
            ],
        ),
        'ask_mistress': interactions.thing.Thing(
            name='Temple Room',
            opening_text='You toss another coin to one of the imps: "Is your mistress behind this door?"\n'
                         '"Yes!" They all squeal. Enviously oggling the imp who caught the coin.',
            choices=[
                choices.ChoiceInspectRoom('Ask about the curse', 'ask_curse'),
                choices.ChoiceInspectRoom('Have a look around', 'examine'),
                choices.ChoiceInspectRoom('Destroy the foul beasts!', 'fight_imps'),
            ],
        ),
        'ask_curse': interactions.thing.Thing(
            name='Temple Room',
            opening_text='You come closer and hand an imp a coin: "You said something about a curse?"\n'
                         '"YES! Mistress put curse on master! Put on she self! Put on whole place!"\n'
                         'You pocket the remaining coins as the imps fight amongst themselves for the gold.',
            choices=[
                choices.ChoiceInspectRoom('Have a look around', 'examine'),
                choices.ChoiceInspectRoom('Destroy the fiends!', 'fight_imps'),
            ],
        ),
        'altar': interactions.thing.Thing(
            name='Temple Room',
            opening_text='The bricks around the altar are darkened with old blood.\n'
                         'The headless corpse is shriveled and dry. Judging by the cut of the neck,\n'
                         'this body seems to belong to the head you have found. This is what happened to robert!',
            # todo: @alon should we only make the note about robert if we know about him?
            choices=[
                choices.ChoiceInspectRoom('Examine upside down cross', 'upside_down_cross'),
                choices.ChoiceNavigate('Advance to the Inner Cloister.', level='level_3', room='inner_cloister'),
            ],
        ),
        'upside_down_cross': interactions.thing.Thing(
            name='Temple Room',
            opening_text='Such an unholy symbol! You destroy this affront to your lord without hesitation!',
            future_text='The unholy symbol has been destroyed',
            choices=[
                choices.ChoiceInspectRoom('Examine altar', 'altar'),
                choices.ChoiceNavigate('Advance to the Inner Cloister.', level='level_3', room='inner_cloister'),
            ],
        ),
        'fight_imps': interactions.thing.Thing(
            name='Temple Room',
            opening_text='As you come closer the imps all band together to face you.\n'
                         'They are cowardly creatures, full of greed and sin.',
            choices=[
                choices.ChoiceInspectRoom('Use cross on them', scene='fight_cross',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Shoot them', scene='fight_shoot',
                                          conditions=[conditions.PlayerHasItem(item.crossbow)]),
                choices.ChoiceInspectRoom('Use holy water on them', scene='fight_water',
                                          conditions=[conditions.PlayerHasItem(item.holy_water)]),
                choices.ChoiceInspectRoom('Burn them with fire', scene='fight_fire',
                                          conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
                choices.ChoiceInspectRoom('Blow them up with nitro!', scene='fight_nitro',
                                          conditions=[conditions.PlayerHasItem(item.nitro)]),
            ],
        ),
        'fight_cross': interactions.thing.Thing(
            name='Temple Room',
            opening_text='The moment your cross begins to shine with holy light,\n'
                         'the imps all start screaming with pain as they burst into flames.\n'
                         'Within seconds they vanish back into the pits of hell!',
            choices=[
                choices.ChoiceInspectRoom('Have a look around', 'examine'),
                choices.ChoiceNavigate('Advance to the Inner Cloister.', level='level_3', room='inner_cloister'),
            ],
        ),
        'fight_shoot': interactions.thing.Thing(
            name='Temple Room',
            opening_text='The imps run around cowering as time and time again you reload the crossbow\n'
                         'and shoot the damn vermin one by one until they are all vanquished.',
            choices=[
                choices.ChoiceInspectRoom('Have a look around', 'examine'),
                choices.ChoiceNavigate('Advance to the Inner Cloister.', level='level_3', room='inner_cloister'),
            ],
        ),
        'fight_water': interactions.thing.Thing(
            name='Temple Room',
            opening_text='You pour the contents of the vial in a puddle on the floor then proceed to\n'
                         'grab the struggling imps one by one, then throw them at the puddle.\n'
                         'The evil imps melt in agony.',
            choices=[
                choices.ChoiceInspectRoom('Have a look around', 'examine'),
                choices.ChoiceNavigate('Advance to the Inner Cloister.', level='level_3', room='inner_cloister'),
            ],
        ),
        'fight_fire': interactions.thing.Thing(
            name='Temple Room',
            opening_text='You aproach the imps menacingly and they huddle together in fear.\n'
                         'You pour the oil in a circle around them and ingite it.\n'
                         'Quickly enough the flames drown out the shrieks of pain. The path is cleared.',
            choices=[
                choices.ChoiceInspectRoom('Have a look around', 'examine'),
                choices.ChoiceNavigate('Advance to the Inner Cloister.', level='level_3', room='inner_cloister'),
            ],
        ),
        'fight_nitro': interactions.thing.Thing(
            name='Temple Room',
            opening_text='You place yourself saftely behind a pillar and then toss the vial of nitroglycerin\n'
                         'at the imps. A loud explosion fills the temple up with smoke.\n'
                         'As the view clears the imps are "everywhere".\n'
                         'Two of the pillars have collapsed. The path is cleared.',
            choices=[
                choices.ChoiceInspectRoom('Have a look around', 'examine'),
                choices.ChoiceNavigate('Advance to the Inner Cloister.', level='level_3', room='inner_cloister'),
            ],
        ),
    }
)
