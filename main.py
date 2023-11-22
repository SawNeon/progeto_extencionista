from translate import Translator
import pyttsx3
import speech_recognition as sr
from colorama import init, Fore

init(autoreset=True)

class ProfessorTradutor:
    def __init__(self):
        self.robo = pyttsx3.init()
        self.robo.setProperty('voice', self.robo.getProperty('voices')[1].id)
        self.reconhecedor = sr.Recognizer()

    def carregar_professor_art(self):
        return """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠀
⠀⠀⠀⠀⢀⣤⣀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⣿⣿⣿⡆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⢻⣿⡿⠃⣸⣿⣿⠿⠿⠟⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⣀⣠⣤⣈⣠⣤⣠⣤⣤⡴⠶⠶⠛⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⣾⡿⣿⣿⣿⣿⣿⡏⢠⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⣿⡇⢸⣿⣿⣿⣿⠇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⣿⡇⢸⣿⣿⣿⣿⠀⣈⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⠉⠀
⠀⣿⡇⢸⣿⠟⣿⡏⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀
⠀⠀⠀⢸⣿⠀⣿⡇⠀⠀⢀⣾⣷⣆⠀⠀⠀⣰⣾⣶⡀⠀⠀⢀⣶⣿⣆⠀⠀⠀
⠀⠀⠀⢸⣿⠀⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀
⠀⠀⠀⢸⣿⠀⣿⡇⠀⠀⠀⠙⠛⠁⠀⠀⠀⠈⠛⠋⠀⠀⠀⠀⠙⠛⠋⠀⠀⠀
⠀⠀⠀⢸⣿⠀⣿⡇⠀⠀⢀⣾⣿⣦⠀⠀⠀⣰⣿⣷⣄⠀⠀⢀⣾⣿⣦⡀⠀⠀
⠀⠀⠀⠘⠛⠀⠛⠃⠀⠀⠚⠛⠛⠛⠓⠀⠐⠛⠛⠛⠛⠂⠀⠚⠛⠛⠛⠓⠀⠀"""

    def falar(self, texto):
        self.robo.say(texto)
        print(Fore.CYAN + f"📢 Professor: {texto}")
        self.robo.runAndWait()

    def ouvir_comando(self):
        escolha = input(Fore.YELLOW + "Escolha uma opção (1 - Digitar / 2 - Falar): ")
        if escolha == "1":
            return input(Fore.CYAN + "Digite a frase: ")
        elif escolha == "2":
            with sr.Microphone() as source:
                try:
                    print(Fore.CYAN + "🎤 Diga algo...")
                    print(Fore.YELLOW + "Comece a falar agora.")
                    self.reconhecedor.adjust_for_ambient_noise(source)
                    audio = self.reconhecedor.listen(source, timeout=10)
                    texto = self.reconhecedor.recognize_google(audio, language="pt-BR")
                    print(Fore.GREEN + f"👂 Você disse: {texto}")
                    return texto
                except sr.UnknownValueError:
                    print(Fore.RED + "❌ Não foi possível entender o áudio. Digite a frase.")
                    return input(Fore.CYAN + "Digite a frase: ")
                except sr.RequestError as e:
                    print(Fore.RED + f"❌ Erro ao chamar Google API: {e}")
                    return ""
                except sr.WaitTimeoutError:
                    print(Fore.RED + "❌ Tempo expirado. Tente novamente.")
                    return ""

def traduzir_e_falar():
    professor = ProfessorTradutor()
    professor.falar(professor.carregar_professor_art())

    # Adicionando a lista de idiomas suportados
    idiomas = ['pt-br', 'en-us', 'de', 'es', 'fr', 'it', 'ja', 'ko', 'nl', 'pl',
               'ru', 'sv', 'tr', 'zh-cn', 'zh-tw', 'ar', 'bg', 'cs', 'da',
               'el', 'et', 'fi', 'hu', 'id', 'ms', 'no', 'ro', 'sr', 'sk',
               'sl']

    print('Lista de idiomas suportados:')
    print('-=' * 30)
    for i, idioma in enumerate(idiomas, start=1):
        print(f"{i}-{idioma.capitalize()}", end='    ' if i % 5 != 0 else '\n')
    print('\n' + '-=' * 30)

    idioma_origem = idiomas[int(input('Digite o número do idioma que você deseja traduzir: ')) - 1]
    idioma_destino = idiomas[int(input('Digite o número do idioma que você quer: ')) - 1]

    tradutor = Translator(from_lang=idioma_origem, to_lang=idioma_destino)

    professor.falar("Agora, me diga o que você quer traduzir.")
    frase = professor.ouvir_comando()

    if frase:
        frase_traduzida = tradutor.translate(frase)
        professor.falar(f"Frase Original: {frase}")
        professor.falar(f"Frase Traduzida: {frase_traduzida}")

if __name__ == "__main__":
    traduzir_e_falar()
