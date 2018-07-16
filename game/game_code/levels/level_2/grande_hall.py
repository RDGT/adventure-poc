from game_code import interactions
from game_code.interactions.lib import choices, events, conditions
from game_code.objects import item, entry

grande_hall = interactions.room.Room(
    name='Grande Hall',
    opening_text='You descend down the stairs into a grande hall. Before you stands a well dressed ghoul.\n'
                 'He is busy sweeping the floor when he lifts his gaze and notices you.\n'
                 'His croaking voice mutters: "ah, a visitor."',
    choices=[
        choices.ChoiceInspectRoom('Speak with the Ghoul', 'speak'),
        choices.ChoiceInspectRoom('Attack Ghoul', 'attack'),
    ],
    scenes={
        'attack': interactions.combat.Combat(
            name='Combat with Ghoul',
            # todo: @inbar complete the combat
            opening_text='Combat - work in progress',
            choices=[
            ],
        ),
        'speak': interactions.thing.Thing(
            name='Ghoul',
            opening_text='You bow gracefully before the ghoul and he bows back.\n'
                         'The ghoul speaks again: "good evening sir. How may i be of service?"',
            prompt='what do you say?',
            choices=[
                choices.ChoiceInspectRoom('I am looking for the mistress. Is she present?', 'speak_mistress1'),
                choices.ChoiceInspectRoom(
                    'Good evening to you as well. Are there other servants in this place?', 'speak_robert'),
            ],
        ),
        'speak_robert': interactions.thing.Thing(
            name='Ghoul',
            opening_text='Other servants? Well lets see...I guess the only "servant"\n'
                         'other than me would be Robert, but he is currently... Indisposed.\n'
                         'He has been searching for that ring of his for what seems like.. an eternity.',
            choices=[
                choices.ChoiceInspectRoom('Ask to meet mistress', 'speak_mistress2'),
                choices.ChoiceInspectRoom('Attack Ghoul', 'attack'),
            ],
            events=[]  # todo: @inbar unlock journal robert conditional with ring or without ring
        ),
        'speak_mistress1': interactions.thing.Thing(
            name='Ghoul',
            opening_text='Ah yes. My mistress is in her chambers below. What would be your business with her?',
            prompt='what do you say?',
            choices=[
                choices.ChoiceInspectRoom('I only wish to meet her', 'speak_mistress2'),
            ],
            events=[events.UnlockJournal(entry.ghoul_mistress)]
        ),
        'speak_mistress2': interactions.thing.Thing(
            name='Ghoul',
            opening_text='"Ah, If you are to meet mistress you must be presentable."\n'
                         'The ghoul exposes his rotten fangs. "And by that i mean dead!".',
            choices=[
                choices.ChoiceInspectRoom('Attack Ghoul', 'attack'),
            ],
        ),

    }
)
