from game_code import interactions
from game_code.interactions.lib import choices, events, conditions, scene
from game_code.objects import item, entry

inner_cloister = interactions.room.Room(
    name='Inner Cloister',
    opening_text='You walk up the stone steps towards the decorated door. the source of this evil lurks so closely.\n'
                 'You push the heavy iron door and enter the inner cloister.\n'
                 'The room is smaller than the temple but is full of lavish items and beautiful paintings.\n'
                 'various pagan emblems are hanging from the walls.In the center of the room,\n'
                 'on a royal throne sits mistress. A lofty smirk curves on her decaying face.\n'
                 '"Welcome... Holy man.."',
    room_flags={'speak_robert': False, 'speak_zombie': False, 'speak_mistress': False, 'speak_curse': False,
                'crossbow_loaded': True, 'shots_fired': False},
    choices=[
        choices.ChoiceInspectRoom('mistress', 'mistress'),
    ],
    scenes={
        'mistress': interactions.thing.Thing(
            name='Mistress',
            opening_text='Her long black hair is perfectly brushed, yellow slit eyes softly glow as she measures you.\n'
                         'A tight velvet dress clings to her frail stature. Her beauty is unquesitonable,\n'
                         'But you know better than to lower your guard before a vampire.',
            choices=[
                choices.ChoiceInspectRoom('Vanquish evil! Fight mistress', 'fight'),
                choices.ChoiceInspectRoom('there must be more to this...Speak with mistress', 'speak'),
            ],
        ),
        'speak': interactions.thing.Thing(
            name='Mistress',
            opening_text='You bow gracefully while maintaining eye contact. Mistress nods politely.\n'
                         '"I assume you slaughtered my minions on your way here?"\n'
                         '"Yes I have."\n'
                         '"Even my pets?"\n'
                         '"If you mean the imps, they have been sent back from whence they came."\n'
                         '"Yet you stand before me looking for answers. What is it then?"',
            prompt='What do you wish to ask?',
            choices=[
                choices.ChoiceInspectRoom('Tell about robert', 'speak_robert',
                                          conditions=[conditions.RoomFlagFalse('speak_robert')]),
                choices.ChoiceInspectRoom('Iv encountered a zombie up in the kitchen', 'speak_zombie',
                                          conditions=[conditions.RoomFlagFalse('speak_zombie')]),
                choices.ChoiceInspectRoom('What do you hope to achieve?', 'speak_mistress',
                                          conditions=[conditions.RoomFlagFalse('speak_mistress')]),
                choices.ChoiceInspectRoom('Iv been told that this place is cursed', 'speak_curse',
                                          conditions=[conditions.RoomFlagFalse('speak_curse')]),
            ],
        ),
        'speak_robert': interactions.thing.Thing(
            name='Mistress',
            opening_text='My beloved husband to be. If only he could see that my love was true..\n'
                         'But he rejected me at the altar! So Iv shown him my pain.. ON MY ALTAR!\n'
                         'I condemned his soul and all that is his to damnation!\n'
                         'Of course.. I was his as well. I knew this.',
            prompt='What do you wish to ask?',
            choices=[
                choices.ChoiceInspectRoom('Iv encountered a zombie up in the kitchen', 'speak_zombie',
                                          conditions=[conditions.RoomFlagFalse('speak_zombie')]),
                choices.ChoiceInspectRoom('What do you hope to achieve?', 'speak_mistress',
                                          conditions=[conditions.RoomFlagFalse('speak_mistress')]),
                choices.ChoiceInspectRoom('Iv been told that this place is cursed', 'speak_curse',
                                          conditions=[conditions.RoomFlagFalse('speak_curse')]),
                choices.ChoiceInspectRoom('Vanquish evil! Fight mistress', 'fight'),
            ],
            events=[events.SetRoomFlagTrue('speak_robert')]
        ),
        'speak_zombie': interactions.thing.Thing(
            name='Mistress',
            opening_text='Her smirk is replaced with disgust.\n'
                         '"A good servant turned traitor! Nothing sickens me more...\n'
                         'He tried to escape with my ring. I punished him for that.\n'
                         'He hid it well though, I never managed to find it.\n'
                         'Thus I am marooned in this eternal torment."',
            prompt='What do you wish to ask?',
            choices=[
                choices.ChoiceInspectRoom('Tell about robert', 'speak_robert',
                                          conditions=[conditions.RoomFlagFalse('speak_robert')]),
                choices.ChoiceInspectRoom('What do you hope to achieve?', 'speak_mistress',
                                          conditions=[conditions.RoomFlagFalse('speak_mistress')]),
                choices.ChoiceInspectRoom('Iv been told that this place is cursed', 'speak_curse',
                                          conditions=[conditions.RoomFlagFalse('speak_curse')]),
                choices.ChoiceInspectRoom('Vanquish evil! Fight mistress', 'fight'),
            ],
            events=[events.SetRoomFlagTrue('speak_zombie')]
        ),
        'speak_mistress': interactions.thing.Thing(
            name='Mistress',
            opening_text='"An eternity of suffering! I am content with my share in the world.\n'
                         'I have bonded my fate with satan and hence i cannot die!\n'
                         'And as long as my covenant stands true, Robert and all that is his will suffer!"',
            prompt='What do you wish to ask?',
            choices=[
                choices.ChoiceInspectRoom('Tell about robert', 'speak_robert',
                                          conditions=[conditions.RoomFlagFalse('speak_robert')]),
                choices.ChoiceInspectRoom('Iv encountered a zombie up in the kitchen', 'speak_zombie',
                                          conditions=[conditions.RoomFlagFalse('speak_zombie')]),
                choices.ChoiceInspectRoom('Iv been told that this place is cursed', 'speak_curse',
                                          conditions=[conditions.RoomFlagFalse('speak_curse')]),
                choices.ChoiceInspectRoom('Vanquish evil! Fight mistress', 'fight'),
            ],
            events=[events.SetRoomFlagTrue('speak_mistress')]
        ),
        'speak_curse': interactions.thing.Thing(
            name='Mistress',
            opening_text='"The devil himself was our pastor! My beloved and I shall be together forever!\n'
                         'Even if we are slain by the likes of you we shall return time and again\n'
                         'to repeat the cycle!Such was the price we paid for my dear roberts rejection...\n'
                         'Have you ever been so betrayed?"',
            prompt='What do you wish to ask?',
            choices=[
                choices.ChoiceInspectRoom('Tell about robert', 'speak_robert',
                                          conditions=[conditions.RoomFlagFalse('speak_robert')]),
                choices.ChoiceInspectRoom('Iv encountered a zombie up in the kitchen', 'speak_zombie',
                                          conditions=[conditions.RoomFlagFalse('speak_zombie')]),
                choices.ChoiceInspectRoom('What do you hope to achieve?', 'speak_mistress',
                                          conditions=[conditions.RoomFlagFalse('speak_mistress')]),
                choices.ChoiceInspectRoom('Vanquish evil! Fight mistress', 'fight'),
            ],
            events=[events.SetRoomFlagTrue('speak_curse')]
        ),
        'decide': interactions.thing.Thing(
            name='Mistress',
            opening_text='You think carefully on all that you have learned of this place and its demons.',
            choices=[
                choices.ChoiceInspectRoom(
                    'You must move beyond your grief. I shall lift the curse and let you live', 'lift'),
                choices.ChoiceInspectRoom(
                    'I can annul your contract with satan. I shall lift the curse but you must die', 'annul'),
                choices.ChoiceInspectRoom(
                    'Your words are true. Perhaps i could stay and rule with you? I shall be your groom', 'groom'),
                choices.ChoiceInspectRoom('Vanquish evil! Fight mistress', 'fight'),
            ],
        ),
        'lift': interactions.thing.Thing(
            name='Mistress',
            opening_text='You lower your weapons and approach her slowly.\n'
                         '"Let me release you, child. The demise of this estate has become legend,\n'
                         'all know of your pain, why else would I be here?" Mistress seems to be listening carefully.\n'
                         'You come ever closer and kneel before her, holding her cold and dead hand.\n'
                         '"With your permission and penance I can redeem your soul so you could finally find rest."\n'
                         '"I will stay here and hear your confessions for as long as it would take.\n'
                         'And with time you will be able to meet Robert again in heaven."\n'
                         'For a moment she seems frozen in thought. Her face a blank expression.\n'
                         'Eventually she nods in agreement.',
            choices=[
                choices.ChoiceTheEnd(
                    'The curse has been lifted and mistress has been put to rest. The realm is safe once more.'),
            ],
        ),
        'annul': interactions.thing.Thing(
            name='Mistress',
            opening_text='"Your story is tragic indeed. But gods kingdom cannot host the likes of you.\n'
                         'I shall rid this land of your curse! I imagine however that you wont go without a fight."\n'
                         'Mistress grins with madness. "So come forth holy man... Let us see the power of your faith!"',
            choices=[
                choices.ChoiceInspectRoom('Fight mistress', 'fight'),
            ],
        ),
        'groom': interactions.thing.Thing(
            name='Mistress',
            opening_text='Mistress inspects you with with harsh eyes. "Why? Why would you want this?"\n'
                         'You smile cunningly yet softly, tracing your gaze over her beautiful face.\n'
                         '"A beautiful woman who suffers so much for love... Even god cannot turn a blind eye."\n'
                         'Her eyes narrow with suspicion. "Do you understand what you are asking for?"\n'
                         '"I do indeed, I pledge myself to you mistress."\n'
                         'you remove your protective leather collar and present your neck to her.',
            choices=[
                choices.ChoiceTheEnd(
                    'In what seems like an instant yet an eternity,\n'
                    'mistress drinks the life from your body and time stops.\n'
                    'You have never been so happy. As long as you have each others love...\n'
                    'Nothing else matters.'),
            ],
        ),
        'fight': interactions.thing.Thing(
            name='Mistress',
            opening_text='Her long black hair is perfectly brushed, yellow slit eyes softly glow as she measures you.\n'
                         'A tight velvet dress clings to her frail stature. Her beauty is unquesitonable,\n'
                         'But you know better than to lower your guard before a vampire.',
            choices=[
                choices.ChoiceInspectRoom('Use Holy Cross on her', scene='fight_cross',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Burn her with fire', scene='fight_fire',
                                          conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
                choices.ChoiceInspectRoom('Shoot her!', scene='fight_shoot1',
                                          conditions=[conditions.PlayerHasItem(item.crossbow)]),
                choices.ChoiceInspectRoom('Melt her with holy water!', scene='fight_water',
                                          conditions=[conditions.PlayerHasItem(item.holy_water)]),
                choices.ChoiceInspectRoom('Throw Nitroglycerin!', scene='fight_nitro',
                                          conditions=[conditions.PlayerHasItem(item.nitro)]),
            ],
        ),

        # todo: @alon please clarify how this section of combat is supposed to work
        # reloading dependant on shot, and cross?
        # how many times to shoot?
        # == from here
        'fight_cross': interactions.thing.Thing(
            name='Mistress',
            opening_text='You raise the cross before mistress as its glow creates sharp silhouettes on the walls.\n'
                         'Mistress hisses showing her rotten fangs, her eyes grow wide and dark.\n'
                         'She vanishes into the darkness.',
            choices=[
                choices.ChoiceInspectRoom('Ready yourself for a surprise attack', scene='fight_ready'),
                choices.ChoiceInspectRoom('Reload the crossbow', scene='fight_cross',
                                          conditions=[conditions.PlayerHasItem(item.crossbow),
                                                      conditions.RoomFlagFalse('crossbow_loaded')]),
            ],
        ),
        'fight_shoot1': interactions.thing.Thing(
            name='Mistress',
            opening_text='You take the initiative and aim for her heart!\n'
                         'She extends her hand to block the bolt yet it pierces through her,\n'
                         'sending a jet of blood in the air.\n'
                         'She vanishes and the bolt continues its trajectory into the wall.',
            choices=[
                choices.ChoiceInspectRoom('Ready yourself for a surprise attack', scene='fight_ready'),
                choices.ChoiceInspectRoom('Reload the crossbow', scene='fight_cross'),
            ],
            events=[events.SetRoomFlagTrue('shots_fired'), events.SetRoomFlagFalse('crossbow_loaded')]
        ),
        'fight_shoot2': interactions.thing.Thing(
            name='Mistress',
            opening_text='She grabs you with inhuman strength, her nail carving into your flesh.\n'
                         'She has you but you in turn also have her.\n'
                         'You point the crossbow towards her chin and pull the trigger.\n'
                         'The bolt skewers right through her head',
            choices=[
                choices.ChoiceInspectRoom('Perform a ritual to lift the curse.', 'ritual'),
                choices.ChoiceInspectRoom('End Her', 'triumph'),
            ],
        ),
        'fight_reload': interactions.thing.Thing(
            name='Mistress',
            opening_text='You take the initiative and aim for her heart!\n'
                         'She extends her hand to block the bolt yet it pierces through her,\n'
                         'sending a jet of blood in the air.\n'
                         'She vanishes and the bolt continues its trajectory into the wall.',
            choices=[
                choices.ChoiceInspectRoom('Ready yourself for a surprise attack', scene='fight_ready'),
            ],
            events=[events.SetRoomFlagTrue('crossbow_loaded')]
        ),
        'fight_ready': interactions.thing.Thing(
            name='Mistress',
            opening_text='You stand perfectly still, ready for the vampire to show her face again.\n'
                         'After a few tense moments you hear a small gust of wind behind you.\n'
                         'Mistress reappears but you were ready!',
            choices=[
                choices.ChoiceInspectRoom('Use Holy Cross on her', scene='fight_cross',
                                          conditions=[conditions.PlayerHasItem(item.holy_cross)]),
                choices.ChoiceInspectRoom('Burn her with fire', scene='fight_fire',
                                          conditions=[conditions.PlayerHasItem(item.flammable_oil)]),
                choices.ChoiceInspectRoom('Shoot her!', scene='fight_shoot1',
                                          conditions=[conditions.PlayerHasItem(item.crossbow),
                                                      conditions.RoomFlagFalse('shots_fired')]),
                choices.ChoiceInspectRoom('Shoot her again!', scene='fight_shoot2',
                                          conditions=[conditions.PlayerHasItem(item.crossbow),
                                                      conditions.RoomFlagTrue('shots_fired')]),
                choices.ChoiceInspectRoom('Melt her with holy water!', scene='fight_water',
                                          conditions=[conditions.PlayerHasItem(item.holy_water)]),
                choices.ChoiceInspectRoom('Throw Nitroglycerin!', scene='fight_nitro',
                                          conditions=[conditions.PlayerHasItem(item.nitro)]),
            ],
        ),
        # == to here

        'fight_fire': interactions.thing.Thing(
            name='Mistress',
            opening_text='As soon as you pull out the vial of oil, mistress disappears into thin air.\n'
                         'You pour the oil in a circle around you and hold out the flint.\n'
                         'Time seems to slow down as to stand still, listening.\n'
                         'Mistress appears behind you letting out an ear shattering scream!\n'
                         'Without hesitation you light the oil and mistress catches fire.\n'
                         'Her screams grow louder as she tries to fight the flames.\n'
                         'Her dead flesh burns quickly until there is nothing but ashes.',
            choices=[
                choices.ChoiceInspectRoom('Perform a ritual to lift the curse.', 'ritual'),
                choices.ChoiceInspectRoom('My work here is done', 'triumph'),
            ],
        ),
        'fight_water': interactions.thing.Thing(
            name='Mistress',
            opening_text='Mistress lunges at you, her fangs glinting in the candle fire.\n'
                         'You splash the holy water in her direction and soak her abdomen.\n'
                         'She falls to the floor as her midsection quickly melts away.\n'
                         'She cries in agony as she uses her arms to try and crawl away.',
            choices=[
                choices.ChoiceInspectRoom('Hold her down and perform a ritual to lift the curse.', 'ritual'),
                choices.ChoiceInspectRoom('End her', 'triumph'),
            ],
        ),
        'fight_nitro': interactions.thing.Thing(
            name='Mistress',
            opening_text='Before she has a chance to react you throw the vial of nitroglycerin at the floor\n'
                         'beneath her and dive for safety. The explosion shakes the walls and echoes in your ears.\n'
                         'When the smoke settles you find mistress torn to pieces.\n'
                         'Her limbs crawl slowly on the floor trying to unite once more.',
            choices=[
                choices.ChoiceInspectRoom('End her', 'triumph'),
                choices.ChoiceInspectRoom('Destroy her limbs but conduct a ceremony to lift the curse.', 'ritual'),
            ],
        ),
        'ritual': interactions.thing.Thing(
            name='Mistress',
            opening_text='The battle is won. The estate has been cleansed of all unholy beings.\n'
                         'You spend some time performing rites of purification until the curse is lifted.',
            choices=[
                choices.ChoiceTheEnd(
                    'As you leave the estate its as if the air itself is easier to breath.\n'
                    'The smell of rot and decay is no longer as pungent.\n'
                    'Gods light shines down uppon you, for you have performed a great service this day.'),
            ],
        ),
        'triumph': interactions.thing.Thing(
            name='Mistress',
            opening_text='You stand triumphant! Evil has been held back this day. But for how long?',
            choices=[
                choices.ChoiceTheEnd(
                    'The towns people welcome you as their champion.\n'
                    'But shortly after you leave, terrors return to stalk the night.'),
            ],
        ),
    }
)
