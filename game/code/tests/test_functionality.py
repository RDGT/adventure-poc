import unittest
import logging
import code


log = logging.getLogger('test.functionality')


class TestAdventureFunctionality(unittest.TestCase):

    def setUp(self):
        self.game = code.main.start_game(interface='python')
        self.go_inside()

    def go_inside(self):
        outside = self.game.interface.get_next_screen()
        self.assertEqual(outside.title, 'Outside')
        self.assertEqual(outside.choices[1], 'Open the door slowly')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_starting_inventory_items(self):
        entrance_hall = self.game.interface.get_next_screen()
        inventory_items = self.open_inventory_and_get_item_list(entrance_hall)
        self.assertListEqual(inventory_items, ['Crossbow', 'Flammable Oil', 'Holy Cross', 'Holy Water'])

    @unittest.expectedFailure
    def test_starting_journal_items(self):
        entrance_hall = self.game.interface.get_next_screen()
        journal_items = self.open_journal_and_get_item_list(entrance_hall)
        self.assertListEqual(journal_items, ['I am equipped and ready', 'I have entered the Cursed Dungeon'])

    # == menu function ==

    def open_inventory_and_get_item_list(self, entrance_hall):
        return self.get_menu_items(self.open_inventory(entrance_hall))

    def open_journal_and_get_item_list(self, entrance_hall):
        return self.get_menu_items(self.open_journal(entrance_hall))

    def open_inventory(self, screen):
        return self.open_menu(screen, 'Inventory', 'I')

    def open_journal(self, screen):
        return self.open_menu(screen, 'Journal', 'J')

    def open_menu(self, screen, menu_name, manu_key):
        self.assertEqual(screen.choices[manu_key], menu_name)
        ok = self.game.interface.put_choice(manu_key)
        self.assertTrue(ok)
        menu = self.game.interface.get_next_screen()
        self.assertEqual(menu.title, menu_name)
        return menu

    def get_menu_items(self, menu):
        menu_items = sorted(i for k, i in menu.choices.items() if isinstance(k, int))
        return menu_items
