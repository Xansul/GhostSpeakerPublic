# GhostSpeaker

This project was a gift for a family member. Based on the Destiny franchise, this is a simple smart speaker that can respond with a variety of voice lines from the Ghost character in Destiny 1. The voice lines are sourced from a community-made archive of voice lines for the original voice actor of Ghost. There is currently basic contextual responses, where specific categories of voice lines can be played based on the presence of several select words/phrases in the voice command. Wake word detection and speech-to-text functionality is implemented using PicoVoice (https://picovoice.ai/), an AI powered voice platform. There is also the option to use offline DeepSpeech models for speech-to-text services. The script currently runs on a Raspberry Pi using a mic/speaker addition (Adafruit Voice Bonnet: https://www.adafruit.com/product/4757), and makes use of the extra button input to provide a headless shutdown option.

NOTE: Credit to GitHub user @sloria for their open source WAV recorder (recorder.py).
