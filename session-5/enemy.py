import random


# class Enemy:
class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(f"I took {damage} points damage and have {self._hit_points} left")
        else:
            self._lives -= 1
            if self._lives > 0:
                print(f"{self._name} lost a life")
            else:
                print(f"{self._name} is dead")
                self._alive = False

    def __str__(self):
        return f"Name: {self._name}, Lives: {self._lives}, Hit points: {self._hit_points}"