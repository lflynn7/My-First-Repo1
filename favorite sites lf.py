import webbrowser
import pyautogui as pg

videos=["https://www.youtube.com/watch?v=_IuEg3xbDA0","https://www.youtube.com/watch?v=H34qrTkhFz0"]
music=["https://www.youtube.com/watch?v=Jf09UAoRG5o"]


answer = pg.prompt (
"""
What would you like to do?
a) Watch videos
b) Listen to music

"""
    )


if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in music:
        webbrowser.open(i)
 
