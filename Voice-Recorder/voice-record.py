import sounddevice
from scipy.io.wavfile import write

# Create sample rate 
sr = 44100

# Create custom time to end program 
times = 10

# Print some message to make sure our record work
print('Program start recording....')

recorded_voice = sounddevice.rec(int(times * sr), samplerate=sr, channels=2)

# wait our record to adjust there is no lost
sounddevice.wait()
write('my_voice.wav', sr, recorded_voice)