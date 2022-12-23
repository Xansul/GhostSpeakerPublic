import pvporcupine
#import wave
import recorder
#import numpy
#import deepspeech
import time
import pygame
import os, random
import re
from pvrecorder import PvRecorder
import pvleopard
import Config

class GhostTest():

    #initial variables
    porcupine = None
    model = None
    result_text = None
    result_text_leopard = None
    recorder = None
    pv_recorder = None
    pv_leopard = None

    #delay time
    delay = 4

    #WAV file path variables
    output_path = "recording.wav"

    def __init__(self):
        #porcupine setup
        self.porcupine = pvporcupine.create(access_key=Config.AccessKey, keyword_paths=[Config.P_keyword_path])

        #PvRecorder setup
        self.pv_recorder = PvRecorder(device_index=-1, frame_length=self.porcupine.frame_length)

        #Leopard setup
        self.pv_leopard = pvleopard.create(access_key=Config.AccessKey, model_path=Config.L_model_path)

        #deepspeech setup
        #self.model = deepspeech.Model(Config.DS_model_file_path)
        #self.model.enableExternalScorer(Config.DS_scorer_file_path)

        #lm_alpha = 0.75
        #lm_beta = 1.85
        #self.model.setScorerAlphaBeta(lm_alpha, lm_beta)

        #beam_width = 500
        #self.model.setBeamWidth(beam_width)

        #deepspeech hotword boosting
        #self.model.addHotWord("Ghost", 20)
        #self.model.addHotWord("Fallen", 20)
        #self.model.addHotWord("Cabal", 20)
        #self.model.addHotWord("Backs", 20)
        #self.model.addHotWord("High", 20)

    #Processes recording with DeepSpeech
    #def process_recording(self):
        #wave file setup
        #w = wave.open(self.output_path, "r")
        #rames = w.getnframes()
        #buffer = w.readframes(frames)

        #convert buffer to 16 bit array
        #data16 = numpy.frombuffer(buffer, dtype=numpy.int16)

        #process text
        #self.result_text = self.model.stt(data16)
        #w.close()

    #Processes recording with Leopard
    def process_recording_leopard(self):
        #process audio
        self.result_text_leopard, words = self.pv_leopard.process_file(self.output_path)

    def run(self):
        #recording loop
        while True:
            #begin recording
            self.pv_recorder.start()
            pcm = self.pv_recorder.read()

            #process and look for wake word
            result = self.porcupine.process(pcm)

            if result >= 0:
                print("Keyword detected!")
                self.pv_recorder.stop()

                #record to wav
                #recorder setup
                self.recorder = recorder.RecordingFile(self.output_path, "wb", 1, 16000, 1024)

                #record
                self.recorder.start_recording()
                time.sleep(self.delay)
                self.recorder.stop_recording()
                self.recorder.close()

                #cleanup
                del self.recorder

                #process
                #choose either DeepSpeech or Leopard processing function
                self.process_recording_leopard()
                print(self.result_text_leopard)

                #search and play audio file
                #setup pygame
                pygame.mixer.init()

                #search for character type references
                if re.search(r"[fF]allen", self.result_text_leopard):
                    #play random file from appropriate folder
                    file_to_play = random.choice(os.listdir(Config.fallen_path))
                    file_to_play = os.path.join(r"Resources/Dialogue/Fallen", file_to_play)
                    pygame.mixer.music.load(file_to_play)
                    pygame.mixer.music.play()

                elif re.search(r"[hH]ive", self.result_text_leopard):
                    #play random file from appropriate folder
                    file_to_play = random.choice(os.listdir(Config.hive_path))
                    file_to_play = os.path.join(r"Resources/Dialogue/Hive", file_to_play)
                    pygame.mixer.music.load(file_to_play)
                    pygame.mixer.music.play()

                elif re.search(r"[cC]abal", self.result_text_leopard):
                    #play random file from appropriate folder
                    file_to_play = random.choice(os.listdir(Config.cabal_path))
                    file_to_play = os.path.join(r"Resources/Dialogue/Cabal", file_to_play)
                    pygame.mixer.music.load(file_to_play)
                    pygame.mixer.music.play()

                elif re.search(r"[vV]ex", self.result_text_leopard):
                    #play random file from appropriate folder
                    file_to_play = random.choice(os.listdir(Config.vex_path))
                    file_to_play = os.path.join(r"Resources/Dialogue/Vex", file_to_play)
                    pygame.mixer.music.load(file_to_play)
                    pygame.mixer.music.play()
        
                elif re.search(r"[sS]ay", self.result_text_leopard):
                    #play random file from appropriate folder
                    file_to_play = random.choice(os.listdir(Config.misc_path))
                    file_to_play = os.path.join(r"Resources/Dialogue/Misc", file_to_play)
                    pygame.mixer.music.load(file_to_play)
                    pygame.mixer.music.play()

                elif re.search(r"[gG]o", self.result_text_leopard):
                    #play random file from appropriate folder
                    file_to_play = random.choice(os.listdir(Config.going_path))
                    file_to_play = os.path.join(r"Resources/Dialogue/GoingPlaces", file_to_play)
                    pygame.mixer.music.load(file_to_play)
                    pygame.mixer.music.play()

                #default to random file in "Responses"
                else:
                    file_to_play = random.choice(os.listdir(Config.responses_path))
                    file_to_play = os.path.join(r"Resources/Dialogue/Responses", file_to_play)
                    pygame.mixer.music.load(file_to_play)
                    pygame.mixer.music.play()