# game/engine.py

class GameEngine:
    def __init__(self):
        self.players = []
        self.current_player_index = 0

    def add_player(self, player):
        self.players.append(player)

    def get_current_player(self):
        return self.players[self.current_player_index]

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

# game/player.py

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage

# game/test/test_engine.py

import unittest
# from game import engine, player

class TestGameEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GameEngine()
        self.player1 = Player("Alice")
        self.player2 = Player("Bob")

        self.engine.add_player(self.player1)
        self.engine.add_player(self.player2)

    def test_player_addition(self):
        self.assertIn(self.player1, self.engine.players)
        self.assertIn(self.player2, self.engine.players)

    def test_current_player(self):
        self.assertEqual(self.engine.get_current_player(), self.player1)

    def test_player_turn_switch(self):
        self.engine.next_player()
        self.assertEqual(self.engine.get_current_player(), self.player2)
        self.engine.next_player()
        self.assertEqual(self.engine.get_current_player(), self.player1)

if __name__ == '__main__':
    unittest.main()
