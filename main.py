import cocos
import pyglet
import sys
from cocos.actions import *
from pyglet.input import *


class Player(cocos.layer.Layer):

    def __init__(self):
        super(Player, self).__init__()

        self.sprite = cocos.sprite.Sprite('images/white_square.png')
        self.sprite.position = 320, 240
        self.sprite.scale = 0.32
        self.add(self.sprite, z=1)

        self.xv = 0
        self.yv = 0

    def on_joyaxis_motion(self, joystick, axis, value):
        if(value >= -0.05 and value <= 0.05):
            value = 0
        if(axis is 'x'):
            self.xv = 10 * value
        if(axis is 'y'):
            self.yv = -10 * value
        self.sprite.do((MoveBy((self.xv, self.yv), duration=0.1)))

# Main game code
cocos.director.director.init()
player_layer=Player()

# Initialize controller
controllers=get_joysticks()
controller1=controllers[0]
if(controller1 is None):
    print("Error! No controllers connected!")
    sys.exit()
controller1.open()
controller1.register_event_type('on_joyaxis_motion')
controller1.register_event_type('on_joybutton_press')
controller1.register_event_type('on_joybutton_release')
controller1.push_handlers(player_layer)

main_scene=cocos.scene.Scene(player_layer)

cocos.director.director.run(main_scene)
