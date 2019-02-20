import random

class Zombie:

  max_speed = 5
  horde = []
  plague_level = 10
  default_speed = 1
  max_strength = 8
  default_strength = 3

  def __init__(self, speed, strength):
    """Initializes zombie's speed and strength"""
    if speed > Zombie.max_speed:
      self.speed = Zombie.default_speed
    else:
      self.speed = speed

    if strength > Zombie.max_strength:
      self.strength = Zombie.default_strength
    else:
      self.strength = strength

  def __str__(self):
      return "Zombie has speed {}".format(self.speed)

  @classmethod
  def spawn(cls):
    """Spawns a random number of new zombies, based on the plague level,
    adding each one to the horde.  Each zombie gets a random speed."""
    new_zombies = random.randint(1, Zombie.plague_level)
    count = 0

    while count < new_zombies:
      speed = random.randint(1, Zombie.max_speed)
      Zombie.horde.append(Zombie(speed))
      count += 1

  @classmethod
  def new_day(cls):
    """Represents the events of yet another day of the zombie apocalypse.
    Every day some zombies die off (phew!), some new ones show up,
    and sometimes the zombie plague level increases."""
    Zombie.spawn()
    Zombie.some_die_off()

  @classmethod
  def some_die_off(cls):
    """Removes a random number (between 0 and 10) of zombies from the horde."""
    how_many_die = random.randint(0, 10)
    counter = 0
    while counter < how_many_die and len(Zombie.horde) > 0:
      random_zombie = random.randint(0,len(Zombie.horde) - 1)
      Zombie.horde.pop(random_zombie)
      counter += 1

  def encounter(self):
    """This instance method represents you coming across a zombie! This can end in three possible outcomes:
    1. You outrun the zombie and escape unscathed!
    2. You don't out run the zombie you fight and win, you become a zombie.
    3. You don't outrun the zombie, you fight, you lose and it eats your brains and you die. :(
    Returns a summary of what happened."""
    outrun = self.chase()
    win_fight = self.fight()

    if not outrun:
        win_fight = self.fight()
        if  win_fight:
            Zombie.horde.append(Zombie())
            return 'You are now a zombie. Raawwwwrghh!'
        else:
            return 'You died.'
    else:
        return 'Escaped!'

  def chase(self):
    """Represents you trying to outrun this particular zombie.
    Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run."""
    your_speed = random.randint(1, Zombie.max_speed)
    return your_speed > self.speed


  def fight(self):
    """Represents you trying to fight this particular zombie. Uses 'Zombie.max_strength' to generate a random number that represents how well you are able to fight it off."""

    your_strength = random.randint(1, Zombie.max_strength)
    return your_strength > self.strength


# Testing
zombie = Zombie(3,4)
# print(zombie.speed)
# print(zombie.strength
# print(zombie.fight())
# print(zombie.encounter())
