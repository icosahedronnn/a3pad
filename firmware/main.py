import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D3, board.D4, board.D2, board.D1)
keyboard.row_pins = (board.D0,) # Dummy row for direct wiring
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# super primitive but I think it's fine
keyboard.keymap = [
    [KC.A, KC.S, KC.D, KC.W]
]

# volume. had to think of something!
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D27, board.D26, board.D0, False)
)

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),)
)
i2c_bus = board.I2C()

display_driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display_setup = Display(
    display_handler=display_driver,
    width=128,
    height=32,
    flip=False,
)

# yooo some text is peak
display_setup.entries = [
    TextEntry(text='KMK Keyboard', x=0, y=0),
    TextEntry(text='Layer: 0', x=0, y=12),
    TextEntry(text='ASDW Mode', x=0, y=24),
]

keyboard.extensions.append(display_setup)

if __name__ == '__main__':
    keyboard.go()
