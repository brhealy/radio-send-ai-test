from microbit import *
import radio

radio.on()  # Turn on the radio
radio.config(channel=1)  # Set to a specific channel

while True:
    if button_a.was_pressed():
        # Start sending volume data
        volume_data = microphone.get_level()  # Get volume data from the microphone
        radio.send(str(volume_data))  # Send volume data as a string
    elif button_b.was_pressed():
        # Stop sending data
        radio.send('stop')  # Send a stop signal
        break  # Exit the loop