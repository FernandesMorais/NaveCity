from Code.Const import ENTITY_SPEED
from Code.Entity import Entity


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[name]

    def move(self):
        self.rect.centerx -= self.speed


