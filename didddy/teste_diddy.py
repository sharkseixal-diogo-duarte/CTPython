import speech_recognition as sr
from didddy import diddy

r = sr.Recognizer()

with sr.Microphone() as source:
    print("A ajustar ao ruído ambiente...")
    r.adjust_for_ambient_noise(source, duration=1)
    print(f"A ouvir")

    while True:
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=3)
            texto = r.recognize_google(audio, language="pt-PT").lower()
            print("Ouvi:", texto)

            if texto == "vídeo":
                diddy.youtube()

            elif texto == "código":
                diddy.github()

            elif texto == "sair":
                print("Comando de saída recebido. A desligar...")
                break
            else:
                print("Comando desconhecido. Tenta novamente.")

        except sr.WaitTimeoutError:
            pass

        except sr.UnknownValueError:
            pass

        except sr.RequestError as e:
            print("Erro no serviço de reconhecimento de voz:", e)
