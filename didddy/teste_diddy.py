import speech_recognition as sr
from didddy import diddy
# 428855
# 492506
def executar_comando(texto: str):
    if "vídeo" in texto:
        diddy.youtube()

    elif "código" in texto:
        diddy.github()

    elif "mal" in texto:
        print("Comando de saída recebido. A desligar...")
        return False

    else:
        print("Comando desconhecido. Tenta novamente.")

    return True


def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("A ajustar ao ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Pronto. A ouvir...")

        while True:
            try:
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=4
                )

                texto = recognizer.recognize_google(
                    audio,
                    language="pt-PT"
                ).lower()

                print("Ouvi:", texto)

                continuar = executar_comando(texto)
                if not continuar:
                    break

            except sr.WaitTimeoutError:
                # Silencioso para não poluir consola
                continue

            except sr.UnknownValueError:
                print("Não consegui perceber o que disseste.")

            except sr.RequestError as e:
                print(f"Erro no serviço de reconhecimento: {e}")
                break


if __name__ == "__main__":
    main()

