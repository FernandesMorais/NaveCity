#C
import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0,128,128)


#E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_DAMAGE = {
    'Level1BG01': 0,
    'Level1BG02': 0,
    'Level1BG03': 0,
    'Level1BG04': 0,
    'Level1BG05': 0,
    'Level1BG06': 0,
    'Level1BG07': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}



ENTITY_SPEED = {
   'Level1BG01': 0,
   'Level1BG02': 1,
   'Level1BG03': 2,
   'Level1BG04': 3,
   'Level1BG05': 4,
   'Level1BG06': 5,
   'Level1BG07': 6,
   'Level2BG01': 0,
   'Level2BG02': 1,
   'Level2BG03': 2,
   'Level2BG04': 3,
   'Level2BG05': 4,
   'Level2BG06': 5,
   'Level2BG07': 6,
   'Player1': 3,
   'Player1Shot': 1,
   'Player2': 3,
   'Player2Shot': 3,
   'Enemy1': 1,
   'Enemy1Shot': 5,
   'Enemy2': 1,
   'Enemy2Shot': 2,
}

ENTITY_HEALTH = {
    'Level1BG01': 999,
    'Level1BG02': 999,
    'Level1BG03': 999,
    'Level1BG04': 999,
    'Level1BG05': 999,
    'Level1BG06': 999,
    'Level1BG07': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SCORE = {
    'Level1BG01': 0,
    'Level1BG02': 0,
    'Level1BG03': 0,
    'Level1BG04': 0,
    'Level1BG05': 0,
    'Level1BG06': 0,
    'Level1BG07': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,


}



ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
}


#M
MENU_OPTION = ('NEW GAME 1P',
                'NEW GAME 2P - COOPERATIVE',
                'NEW GAME 2 - COMPETITIVE',
                'SCORE',
                'EXIT')

#P
PLAYER_KEY_UP = {'Player1':pygame.K_UP,
                 'Player2':pygame.K_w}
PLAYER_KEY_DOWN = {'Player1':pygame.K_DOWN,
                   'Player2':pygame.K_s}
PLAYER_KEY_LEFT = {'Player1':pygame.K_LEFT,
                   'Player2':pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1':pygame.K_RIGHT,
                    'Player2':pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1':pygame.K_RCTRL,
                    'Player2':pygame.K_LCTRL}

# S
SPAWN_TIME = 4000



#W
WIN_WIDTH = 576
WIN_HEIGHT = 324


