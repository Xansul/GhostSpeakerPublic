import pygame
import Config
import GhostTest as GS

#setup objects
Ghost = GS.GhostTest()

#play startup file
pygame.mixer.init()
pygame.mixer.music.load(Config.startup_path)
pygame.mixer.music.play()

#cleanup on keyboard interrupt
try:
    Ghost.run()
except KeyboardInterrupt:
    print("Shutting down")
    Ghost.pv_recorder.delete()
    Ghost.pv_leopard.delete()
    Ghost.porcupine.delete()