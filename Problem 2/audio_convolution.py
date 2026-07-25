from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve
from scipy.fft import fft, ifft

# Load audio
audio = AudioSegment.from_mp3("ringtone.mp3")

audio = audio.set_channels(1)

samples = np.array(audio.get_array_of_samples()).astype(np.float32)

samples = samples / np.max(np.abs(samples))

# Two impulse responses
IR = [
    np.array([1,0,1,0,1]),
    np.array([1,-0.5,0.25])
]

for i, kernel in enumerate(IR):

    # Convolution
    output = convolve(samples, kernel, mode="same")
    output = output / np.max(np.abs(output))
    # Inverse filtering
    N = len(output)
    H = fft(kernel, N)
    Y = fft(output)

    recovered = np.real(ifft(Y/(H+0.000001)))

    recovered = recovered / np.max(np.abs(recovered))

    # Save recovered audio
    data = (recovered*32767).astype(np.int16)

    result = AudioSegment(
        data.tobytes(),
        frame_rate=audio.frame_rate,
        sample_width=2,
        channels=1
    )

    result.export("Recovered_IR"+str(i+1)+".wav",
                  format="wav")

    # Plot
    plt.figure(figsize=(10,5))

    plt.subplot(3,1,1)
    plt.plot(samples)
    plt.title("Original Audio")
    plt.subplot(3,1,2)
    plt.plot(output)
    plt.title("Convolution IR "+str(i+1))
    plt.subplot(3,1,3)
    plt.plot(recovered)
    plt.title("Inverse Filtering IR "+str(i+1))

    plt.tight_layout()
    plt.show()

print("Completed")
