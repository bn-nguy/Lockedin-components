"""
Oral Presentation Tool
"""

import tkinter as tk
import sounddevice as sd
import numpy as np
import threading
from scipy.io import wavfile

import sdl2
import sdl2.sdlmixer as mixer
from tkextrafont import Font

root = tk.Tk()
root.title("Oral Presentation")
root.geometry("300x360")

# https://python-sounddevice.readthedocs.io/en/latest/examples.html#recording-with-arbitrary-duration

samplerate = 44100

recording = []
is_active = [False]

def callback(indata, frames, time, status):
    """
    Callback called while recording.

    Args:
        indata: Audio data.
        frames | time | status: Passed automatically by sounddevice.
    Returns:
        None
    """
    recording.append(indata.copy())


def record():
    """
    Records audio to recording.wav. Persists until end_recording is called.
    """

    is_active[0] = True
    recording.clear()

    with sd.InputStream(samplerate=samplerate, channels=2, callback=callback):
        while is_active[0]:
            pass

    data = np.concatenate(recording)
    data = np.int16(data * 16384)
    # sd.play(recording)
    wavfile.write("recording.wav", samplerate, data)


def start_recording():
    """
    Triggers record() in a synchronous thread.
    """

    t = threading.Thread(target=record)
    t.start()


def end_recording():
    """
    Ends recording.
    """

    is_active[0] = False


def playback():
    """
    Triggers audio playback from file.
    """

    if mixer.Mix_Playing(-1):
        mixer.Mix_HaltChannel(-1)

    file = mixer.Mix_LoadWAV("./recording.wav".encode("utf-8"))
    mixer.Mix_PlayChannel(-1, file, 0)


def toggle_pause(button):
    """
    Toggles playback.

    Args:
        button: The pause button.
        
    Returns:
        None
        """

    if mixer.Mix_Playing(-1):
        if mixer.Mix_Paused(-1):
            mixer.Mix_Resume(-1)
            button.config(text="Pause")
        else:
            mixer.Mix_Pause(-1)
            button.config(text="Resume")


def stop(pause_button):
    """
    Stops playback.

    Args:
        pause_button: The pause button.
        
    Returns:
        None
    """
    pause_button.config(text="Pause")
    mixer.Mix_FadeOutChannel(-1, 500)

# Main

root.title("Lockedin Presentation Helper")
img = tk.PhotoImage(file='assets/lockedin_mascot.png')
root.iconphoto(False, img)

root.option_add("*Button.Background", "#f68958")
root.option_add("*Label.background", "#f68958")

font = Font(file="fonts/sniglet.ttf", family="Sniglet")
root.option_add("*Font", "Sniglet 10")

bg = tk.PhotoImage(file = "assets/g_oral.png").subsample(2, 2)
bg_label = tk.Label(root, image=bg)
bg_label.place(x = 0, y = 0)
root.resizable(False, False) 


# Initiates audio output
mixer.Mix_OpenAudio(44100, sdl2.AUDIO_S16SYS, 2, 2048)

# Buttons

rec_button = tk.Button(root, text="Record", command=start_recording)
rec_button.grid(row=1, column=0, padx=10, pady=0)

end_button = tk.Button(root, text="End", command=end_recording)
end_button.grid(row=1, column=1, padx=10, pady=0)

play_button = tk.Button(root, text="Play", command=playback)
play_button.grid(row=2, column=0, padx=10, pady=0)

pause_button = tk.Button(root, text="Pause")
pause_button.config(command=lambda: toggle_pause(pause_button))
pause_button.grid(row=2, column=1, padx=10, pady=0)

stop_button = tk.Button(root, text="Stop", command=lambda: stop(pause_button))
stop_button.grid(row=3, column=0, padx=10, pady=0)


root.mainloop()
