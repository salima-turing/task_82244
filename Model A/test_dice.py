# game/dice.py
import random
import pytest

class Dice:
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		return random.randint(1, self.num_sides)

# game/test/test_dice.py
# from ..dice import Dice

@pytest.mark.parametrize("num_sides, expected_outcomes", [
	(6, [1, 2, 3, 4, 5, 6]),
	(4, [1, 2, 3, 4]),
	(20, list(range(1, 21)))
])
def test_dice_roll_outcomes(num_sides, expected_outcomes):
	dice = Dice(num_sides)
	outcomes = set()
	for _ in range(1000):  # Large number of rolls to ensure coverage
		outcomes.add(dice.roll())
	assert outcomes == set(expected_outcomes)

if __name__ == "__main__":
	pytest.main()
