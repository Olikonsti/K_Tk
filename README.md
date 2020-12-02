# K_Tk
 Tkinter library to create dark/light mode guis easily and add icons and sounds
 ![alt text](https://raw.githubusercontent.com/Olikonsti/K_Tk/main/Screenshot%202020-11-25%20130254.png)

```python

from K_Tk import *


a = KTk()

b = KLabel(a, text="This is demonstration text\n"
                   "this is the second line of the demonstration text\n"
                   "this is the third")
b.place(x=10, y=10)

c = KButton(a, command=KToggleMode, text="Change Mode(Appearence)")
c.place(x=500, y=50)

c = KButton(a, command=click_sound.play, text="Click")
c.place(x=50, y=90)

KDarkMode()
a.mainloop()
```
