import time
import board
import displayio
from adafruit_display_text import label
import terminalio
import keypad


display = board.DISPLAY
group = displayio.Group()
font = terminalio.FONT
text = label.Label(font,
                   scale=4,
                   text="Hello World!",
                   color=0xFFFFFF)
text.x = 10
text.y = 10
text.scale = 2

text_coords = (text.x, text.y)

info = label.Label(font,
                   scale=2,
                   x=100,
                   y=120,
                   text=str(text_coords),
                   color=0xFFFFFF)


group.append(text)
group.append(info)
display.root_group = group

buttons = keypad.ShiftRegisterKeys(
    clock=board.BUTTON_CLOCK,
    data=board.BUTTON_OUT,
    latch=board.BUTTON_LATCH,
    key_count=8,
    value_when_pressed=True,
)


while True:
    button_events = buttons.events.get()
    if button_events:
        if button_events.pressed:
            if button_events.key_number == 0: #down
                text.y = text.y = + 10
                text_coords = (text.x, text.y)
                info.text = str(text_coords)

            if button_events.key_number == 1: #up
                text.y = text.y = - 10
                text_coords = (text.x, text.y)
                info.text = str(text_coords)

            
            if button_events.key_number == 2: #right
                text.x = text.x = + 10
                text_coords = (text.x, text.y)
                info.text = str(text_coords)

            if button_events.key_number == 3: #right
                text.x = text.x = - 10
                text_coords = (text.x, text.y)
                info.text = str(text_coords)

    pass