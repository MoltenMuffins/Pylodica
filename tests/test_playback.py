#!/usr/bin/env python3

from simpleaudio.functionchecks import run_all

if __name__ == "__main__":
    try:
        run_all()
    except Exception as msg:
        print("Unable to play audio via ALSA library. See error message below for details:")
        print(msg)