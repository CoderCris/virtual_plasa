import board
import displayio
from adafruit_display_text import label
import terminalio
import neopixel

display = board.DISPLAY
group = displayio.Group()
text = label.Label(terminalio.FONT, text="Hello World!", color=0xFFFFFF)
text.x = 10
text.y = 10
text.scale = 4
group.append(text)
display.root_group = group


while True:
    pass