import wrap_py, wrap_py.ru, random
from wrap_py import world
from wrap_py import sprite

world.create_world(700, 700)
world.set_world_background_image('wrap_py_catalog/backgrounds/fon_gori1_700_800.png')
pushka = sprite.add_sprite('blast_ball', 350, 600)


@wrap_py.on_mouse_move
def mouse(pos):
    sprite.move_sprite_to(pushka, pos[0], 600)
    leftyshka = sprite.get_left(pushka)
    rightyshka = sprite.get_right(pushka)
    if leftyshka < 0:
        sprite.set_left_to(pushka, 0)
    elif rightyshka > 700:
        sprite.set_right_to(pushka, 700)


@wrap_py.on_mouse_down()
def add_bullet():
    global bullet
    bullet = sprite.add_sprite('bullet', sprite.get_sprite_x(pushka), sprite.get_sprite_y(pushka))
    @wrap_py.always
    def shof_bullet():
        sprite.move_sprite_to(bullet,sprite.get_sprite_x(bullet),sprite.get_sprite_y(bullet)-10)