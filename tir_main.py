import wrap_py, wrap_py.ru, random
from wrap_py import world
from wrap_py import sprite

world.create_world(700, 700)
world.set_world_background_image('wrap_py_catalog/backgrounds/fon_gori1_700_800.png')
pushka = sprite.add_sprite('blast_ball', 350, 600)
ball = sprite.add_sprite('misc',350,350,costume='ny_ball')
bullet = None
all_bullet = []
all_ball=[]


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
    bullet = sprite.add_sprite('bullet', sprite.get_sprite_x(pushka), sprite.get_sprite_y(pushka))
    all_bullet.append(bullet)

@wrap_py.on_key_down(wrap_py.K_b)
def add_ball():
    ball= sprite.add_sprite('misc',0,0)
    all_ball.append(ball)

@wrap_py.always
def move_ball():
    for b in all_ball:
        x=sprite.get_sprite_x(b)
        y=sprite.get_sprite_y(b)
        sprite.move_sprite_to(b,x+10,y+10)

@wrap_py.always
def shof_bullet():
    for a in all_bullet:
        x = sprite.get_sprite_x(a)
        y = sprite.get_sprite_y(a) - 10
        sprite.move_sprite_to(a, x, y)
