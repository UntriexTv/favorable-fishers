
from __future__ import division

import sys

from asciimatics.effects import Clock, Print
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def demo(screen):
    effects = [
        Print(screen, Rainbow(screen, FigletText("256 colours")),
              y=screen.height//2 - 8),
        Print(screen, Rainbow(screen, FigletText("for xterm users")),
              y=screen.height//2 + 3),
        Clock(screen, screen.width//2, screen.height//2, screen.height//2),
    ]
    log = open("log.log.log", "r+")
    log.write("frame\n")
    log.close()
    screen.play([Scene(effects, -1, clear=True)], stop_on_resize=True, allow_int=True)


while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)

    except ResizeScreenError:
        pass
