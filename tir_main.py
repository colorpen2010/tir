import wrap_py, wrap_py.ru
from wrap_py import world
from wrap_py import sprite

world.create_world(700, 800)
world.set_world_background_image('C:/Users/admin/wrap_py_catalog/backgrounds/fon_gori1_700_800.png')
pushka=sprite.add_sprite('blast_ball',350, 600)


@wrap_py.on_mouse_move
def mouse(pos):
    sprite.move_sprite_to(pushka,pos[0],600)
    leftyshka=sprite.get_left(pushka)
    if leftyshka<0:
        sprite.set_left_to(pushka,0)