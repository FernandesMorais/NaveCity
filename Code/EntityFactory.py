#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint

from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Enemy import Enemy
from Code.Player import Player


class EntityFactory:

    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for i in range(1, 7):
                    list_bg.append(Background(f'Level1BG0{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level1BG0{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Level2BG':
                list_bg = []
                for i in range(1, 7):
                    list_bg.append(Background(f'Level2BG0{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level2BG0{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player(name='Player1', position=(10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player(name='Player2', position=(10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, randint(40, WIN_HEIGHT - 40)))

        return
