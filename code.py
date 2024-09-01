import board
import displayio
from adafruit_display_text import label
import terminalio
import neopixel

display = board.DISPLAY
#num_pixels = display.width * display.height
num_pixels = 12
pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=0.3, auto_write=False)
pixels.fill(0x0000ff)
pixels.show()

group = displayio.Group()
text = label.Label(terminalio.FONT, text="Hello World!", color=0xFFFFFF)
text.x = 10
text.y = 10
text.scale = 4
group.append(text)
display.root_group = group


while True:
    pass