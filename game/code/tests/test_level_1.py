import unittest
import logging
import code


log = logging.getLogger('test.level_1')


class TestAdventureLevelOne(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.game = code.main.start_game(interface='python')

    def test_outside_slowly(self):
        outside = self.game.interface.get_next_screen()
        self.assertEqual(outside.title, 'Outside')
        self.assertEqual(outside.choices[1], 'Open the door slowly')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_outside_kick(self):
        outside = self.game.interface.get_next_screen()
        self.assertEqual(outside.title, 'Outside')
        self.assertEqual(outside.choices[2], 'Kick down the door!')
        ok = self.game.interface.put_choice(2)
        self.assertTrue(ok)

    def test_entrance_hall_left(self):
        entrance_hall = self.game.interface.get_next_screen()
        self.assertEqual(entrance_hall.title, 'Entrance Hall')
        self.assertEqual(entrance_hall.choices[1], 'Left Door')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_entrance_hall_front(self):
        entrance_hall = self.game.interface.get_next_screen()
        self.assertEqual(entrance_hall.title, 'Entrance Hall')
        self.assertEqual(entrance_hall.choices[2], 'Front Door')
        ok = self.game.interface.put_choice(2)
        self.assertTrue(ok)

    def test_entrance_hall_right(self):
        entrance_hall = self.game.interface.get_next_screen()
        self.assertEqual(entrance_hall.title, 'Entrance Hall')
        self.assertEqual(entrance_hall.choices[3], 'Right Door')
        ok = self.game.interface.put_choice(3)
        self.assertTrue(ok)

    def test_closet_room_search(self):
        closet_room = self.game.interface.get_next_screen()
        self.assertEqual(closet_room.title, 'Closet Room')
        self.assertEqual(closet_room.choices[1], 'Search the closet')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_closet_go_back(self):
        closet_room = self.game.interface.get_next_screen()
        self.assertEqual(closet_room.title, 'Closet')
        self.assertEqual(closet_room.choices[1], 'Go back.')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_closet_room_leave(self):
        closet_room = self.game.interface.get_next_screen()
        self.assertEqual(closet_room.title, 'Closet Room')
        self.assertEqual(closet_room.choices[1], 'Leave room')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_kitchen_listen(self):
        kitchen = self.game.interface.get_next_screen()
        self.assertEqual(kitchen.title, 'Kitchen')
        self.assertEqual(kitchen.choices[1], 'Kneel next to the zombie and listen.')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_kitchen_ask(self):
        listening = self.game.interface.get_next_screen()
        self.assertEqual(listening.title, 'Listen To Zombie')
        self.assertEqual(listening.choices[1], 'Ask why he tried to run away')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_kitchen_ask_ring(self):
        listening = self.game.interface.get_next_screen()
        self.assertEqual(listening.title, 'Listen To Zombie')
        self.assertEqual(listening.choices[1], 'Ask for the ring')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_kitchen_leave(self):
        listening = self.game.interface.get_next_screen()
        self.assertEqual(listening.title, 'Listen To Zombie')
        self.assertEqual(listening.choices[1], 'Leave room')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_living_room_hold(self):
        living_room = self.game.interface.get_next_screen()
        self.assertEqual(living_room.title, 'Living Room')
        self.assertEqual(living_room.choices[1],
                         'Hold your holy cross firmly before the ghost and recite a banishment prayer!')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_living_room_move(self):
        living_room = self.game.interface.get_next_screen()
        self.assertEqual(living_room.title, 'Ghast Destroyed')
        self.assertEqual(living_room.choices[1],
                         'Move towards the iron gate at the far end of the room')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_living_room_key(self):
        living_room = self.game.interface.get_next_screen()
        self.assertEqual(living_room.title, 'Iron Gate')
        self.assertEqual(living_room.choices[1], 'Try the key')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_living_room_stairs(self):
        living_room = self.game.interface.get_next_screen()
        self.assertEqual(living_room.title, 'Iron Gate')
        self.assertEqual(living_room.choices[1], 'Advance down the stairs')
        ok = self.game.interface.put_choice(1)
        self.assertTrue(ok)

    def test_arrive_at_grande_hall(self):
        grande_hall = self.game.interface.get_next_screen()
        self.assertEqual(grande_hall.title, 'Grande Hall')
