
import beepy
beepy.beep(sound="ping")

import winsound
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

def beep():
    winsound.Beep(440, 500)
    print('\a')