import pygame
import ConfigRaspi as cr
import GhostTest as GS

#Run except for runtime error
#setup objects
Ghost = GS.GhostTest()

#play startup file
#USES RASPBERRY PI SOUNDCARD -- DELETE DEVICENAME IF ON WINDOWS
pygame.mixer.init(devicename = cr.card)
pygame.mixer.music.load(cr.startup_path)
pygame.mixer.music.play()

#cleanup on keyboard interrupt
try:
    Ghost.run()
except KeyboardInterrupt:
    print("Shutting down")
    Ghost.pv_recorder.delete()
    Ghost.pv_leopard.delete()
    Ghost.porcupine.delete()