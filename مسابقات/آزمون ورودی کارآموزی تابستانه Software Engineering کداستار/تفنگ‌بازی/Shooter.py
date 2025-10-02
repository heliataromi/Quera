class Shooter:
    WEAPONS = {
        "Submachine Gun": {
            "range": 100,
            "power": 10,
            "bullet size": 0.5
        },
        "Assault Rifle": {
            "range": 200,
            "power": 20,
            "bullet size": 1
        },
        "Pistol": {
            "range": 80,
            "power": 8,
            "bullet size": 0.5
        },
        "Shotgun": {
            "range": 50,
            "power": 40,
            "bullet size": 4
        },
        "Sniper Rifle": {
            "range": 1000,
            "power": 30,
            "bullet size": 3
        }
    }

    BULLETS = {
        "A": {
            "size": 0.5,
            "damage": 1
        },
        "B": {
            "size": 1,
            "damage": 1.5
        },
        "C": {
            "size": 3,
            "damage": 3
        },
        "D": {
            "size": 4,
            "damage": 2
        }
    }

    def __init__(self):
        self.weapon = ''
        self.bullet, self.bullet_count = '', 0

    def set_gun_by_name(self, name: str) -> None:
        if name not in Shooter.WEAPONS:
            raise Exception("No such weapon was found.")

        self.weapon = name

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        if not self.weapon:
            raise Exception("No weapon was set.")
        if count < 0:
            raise Exception("Count must be greater than 0.")
        if Shooter.WEAPONS[self.weapon]['bullet size'] != size:
            raise Exception("Size is invalid.")

        for bullet, info in Shooter.BULLETS.items():
            if info['size'] == size:
                self.bullet = bullet
                self.bullet_count += count
                return

        raise Exception("No such bullet was found.")

    def shoot_to_target(self, target_x: int, target_y: int, target_distance: int, aim_x: int, aim_y: int) -> float:
        if not self.weapon:
            raise Exception("No weapon was set.")
        if self.bullet_count == 0 or not self.bullet:
            raise Exception("Out of bullet.")

        if not (target_x <= aim_x <= target_x + 10 and target_y <= aim_y <= target_y + 10):
            return 0

        if Shooter.WEAPONS[self.weapon]['range'] < target_distance:
            return 0

        result = Shooter.WEAPONS[self.weapon]['power'] * Shooter.BULLETS[self.bullet]['damage']

        self.bullet_count -= 1
        if self.bullet_count == 0:
            self.bullet = ''

        return result
