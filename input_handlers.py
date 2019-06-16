import tcod as libtcod

def handle_keys(key):
    #Movement Keys
    if key.vk == libtcod.KEY_UP:
        return {'move': (0, -1)}