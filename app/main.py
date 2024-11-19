class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f" Health: {self.health}, "
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def __init__(self, name: str, health: int = 100) -> None:
        super().__init__(name)
