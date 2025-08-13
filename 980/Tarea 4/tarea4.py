import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write, read
from scipy.signal import welch, get_window

# Menú principal
opcion = 0

while opcion != 5:
    print("Seleccione una opción")
    print("1. Grabar")
    print("2. Reproducir")
    print("3. Graficar")
    print("4. Graficar densidad")
    print("5. Salir")

    opcion = int(input("Ingrese su elección: "))

    if opcion == 1:
        # Grabación de audio
        try:
            duracion = int(input("Ingrese la duración de la grabación en segundos: "))
            fs = 44100  
            print("Comenzando la grabación...")
            audio = sd.rec(int(duracion * fs), samplerate=fs, channels=1)
            sd.wait()  # Esperar hasta que termine la grabación
            write("audio.wav", fs, audio)  # Guardar el archivo
            print("Grabación finalizada. Archivo de audio grabado correctamente.")
        except Exception as e:
            print(f"Error al grabar el audio: {e}")

    elif opcion == 2:
        # Reproducción de audio
        try:
            fs, data = read("audio.wav")
            sd.play(data, fs)
            sd.wait()  
            print("Reproducción finalizada.")
        except Exception as e:
            print(f"Error al reproducir el audio: {e}")

    elif opcion == 3:
        # Gráfico de audio
        try:
            fs, data = read("audio.wav")
            tiempo = np.linspace(0, len(data) / fs, num=len(data))
            plt.plot(tiempo, data)
            plt.xlabel('Tiempo (s)')
            plt.ylabel('Amplitud')
            plt.title('Audio')
            plt.show()
        except Exception as e:
            print(f"Error al graficar el audio: {e}")

    elif opcion == 4:
        # Graficar espectro de frecuencia
        try:
            fs, data = read("audio.wav")
            

            if len(data.shape) > 1: 
                data = data[:, 0]

            N = len(data)  
            window = get_window('hamming', N // 8)  
            f, Sxx = welch(data, fs, window=window, nperseg=len(window))  


            plt.plot(f, 10 * np.log10(Sxx))
            plt.xlabel('Frecuencia (Hz)')
            plt.ylabel('Densidad espectral de potencia (dB/Hz)')
            plt.title('Espectro de frecuencia de la señal grabada')
            plt.show()
        except Exception as e:
            print(f"Error al graficar el espectro de frecuencia: {e}")

    elif opcion == 5:
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida.")
