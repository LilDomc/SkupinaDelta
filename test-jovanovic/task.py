import random

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}"

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.health = min(100, self.health + 10)
        print(f"Health is now {self.health}.")

    def fight(self):
        print(f"{self.name} fights a monster!")
        damage = random.randint(1, 10)
        self.health -= damage
        print(f"{self.name} took {damage} damage. Health is now {self.health}.")


def main():
    print("Welcome to the Witcher 3 game!")
    name = input("Enter your character's name: ")
    character = Character(name)

    print(f"Character created: {character}")

    character.sleep()
    character.fight()

if __name__ == "__main__":
    main()