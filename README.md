# TUI Dashboard 

An application to complement your everyday life, displaying useful information around the clock.
Video demonstrating the project:
[Dashboard TUI app](https://youtu.be/le_tm3CKcSY)

## Installation Instructions
1) Install asciimatics. 
```
pip install asciimatics
```

2) `button.py` in your local `asciimatics` source must be modified to accept an extra parameter, called retVal,
which is stored in an instance variable:
```
__slots__ = ["_text", "_text_raw", "_add_box", "_on_click", "_label", "_retVal"]

def __init__(self, text, on_click,retVal, label=None, add_box=True, name=None, **kwargs):
    self._retVal = retVal
```
and the following method must be added:
```
def doClick(self):
        if self._retVal is not None:
            self._on_click(self._retVal)
        else:
            self._on_click()
```
You can find a correctly modified version of `button.py` [here](https://gist.github.com/twenty-twenty/1ff768fbd87800fbab5a3e9fd34c6166)

3) To run the application, use python to execute `main.py` within the terminal of your choice.

## Overview
Within this application you are able to:
- add and remove widgets 
- save and create and load layouts of widgets
- configure widgets to your desire
