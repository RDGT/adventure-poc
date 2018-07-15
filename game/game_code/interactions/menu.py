from lib import scene, choices


class MenuItem(scene.Screen):

    def __init__(self, menu_item):
        super(MenuItem, self).__init__(title=menu_item.name, text=menu_item.description, add_menu_choices=False)


class Menu(scene.Scene):

    def __init__(self, name, menu_items):
        menu_choices = []  # [choices.ChoiceExitMenu('Exit {}'.format(name))]
        for menu_item in menu_items:
            menu_choice = choices.ChoiceMenuItem(MenuItem(menu_item))
            menu_choices.append(menu_choice)
        super(Menu, self).__init__(
            name=name,
            opening_text='select a menu item to learn more',
            prompt='Select a number',
            choices=menu_choices,
            add_menu_choices=False,
            add_menu_exit=choices.ChoiceExitMenu('Exit {} [X]'.format(name)),
        )
