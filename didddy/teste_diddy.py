import speech_recognition as sr
from didddy import diddy

PALAVRA_CHAVE = "ativar"
Sair = "sair"
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("...")
    while True:
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=3)
            texto = r.recognize_google(audio, language="pt-PT").lower()

            if PALAVRA_CHAVE in texto:
                print(f"{PALAVRA_CHAVE} diddy")
                print("OI Neu soIu DIDDY G1.0 o queE posso ajudarR")
                audio_comando = r.listen(source, timeout=5)
                comando = r.recognize_google(audio_comando, language="pt-PT")

                if comando == "vídeo":
                    diddy.youtube()

                if Sair in comando:
                    print(".")
                    break


        except sr.WaitTimeoutError:
            pass

        except sr.UnknownValueError:
            pass

        except sr.RequestError as e:
            print("Erro no serviço:", e)
