
# play a wave sound on a Windows Box
# Python23 tested   vegaseat   2/8/2005
import winsound
import time
# pick a wave file supplied by Windows XP or one of your own ...
# soundfile = "c:\\Windows\\Media\\chimes.wav"
# Python also accepts the forward slash
soundfile = "c:/Windows/Media/chimes.wav"
winsound.PlaySound(soundfile, winsound. SND_FILENAME |winsound.SND_ASYNC)
# wait one and a half seconds
time.sleep(1.5)
# play the system exit sound if set
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

