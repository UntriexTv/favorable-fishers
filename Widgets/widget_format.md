# Critertia
- Each widget must take in an `width` and `height` when called.
- Each widget must have a variable `self.needs_update` which is a boolean for if the application that needs to be updated

Each widget is a 'layout' in the example below so it should conform as seen below.
```
+------------------------------------------------------------------------+
|Screen..................................................................|
|........................................................................|
|...+----------------------------------------------------------------+...|
|...|Frame                                                           |...|
|...|+--------------------------------------------------------------+|...|
|...||Layout 1                                                      ||...|
|...|+--------------------------------------------------------------+|...|
|...|+------------------------------+-------------------------------+|...|
|...||Layout 2                      |                               ||...|
|...|| - Column 1                   | - Column 2                    ||...|
|...|+------------------------------+-------------------------------+|...|
|...|+-------------+---------------------------------+--------------+|...|
|...||Layout 3     | < Widget 1 >                    |              ||...|
|...||             | ...                             |              ||...|
|...||             | < Widget N >                    |              ||...|
|...|+-------------+---------------------------------+--------------+|...|
|...+----------------------------------------------------------------+...|
|........................................................................|
+------------------------------------------------------------------------+
```

# This is the code to test a widget

```python
def demo(screen, scene):
    # define the size of each frame
    height = 15
    width = 50

    # make all the scenes
    scenes = [
        Scene([
            covidView(screen, height, width, 0, 0), 
            covidView(screen, height, width, 0, 1), 
            covidView(screen, height, width, 1, 0),
            covidView(screen, height, width, 1, 1)
            ], -1, name='Main'),
    ]

    # running all the scenes
    screen.play(scenes, stop_on_resize=True, start_scene=scenes[0], allow_int=True)


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
```
