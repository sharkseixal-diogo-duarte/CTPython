from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,NumericProperty,ListProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup

PERGUNTAS = [
    {
        "perguntas": "Qual é o total de QI dos alunos?",
        "respostas": ["0","5","498"],
        "correta":"-1"
    },
    {
        "perguntas": "Quanto tempo é que os alunos vão demorar a copiar isto?",
        "respostas": ["30min","20min","A aula toda"],
        "correta":"A aula toda"
    },
    {
        "perguntas": "Qual é o melhor país da Europa?",
        "respostas": ["USA","Barreiro","Finlandia"],
        "correta":"Barreiro"
    },
    {
        "perguntas": "Quantas pontes há no rio tejo?",
        "respostas": ["2","16","13"],
        "correta":"16"
    }
]

class QuizLayout(BoxLayout):
    pergunta_text = StringProperty("")
    opcoes = ListProperty([])
    pontuacao = NumericProperty(0)
    index = NumericProperty(0)

    def on_kv_post(self,base_widget):
        self.carregar_proxima()

    def carregar_proxima(self):
        if self.index <len(PERGUNTAS):
            perguntas_atual = PERGUNTAS[self.index]
            self.pergunta_text = perguntas_atual["perguntas"]
            self.opcoes = perguntas_atual["respostas"]

        else:
            self.pergunta_text = "Fim do Quizz!"
            self.opcoes = []
            self.ids.resposta1.disabled = True
            self.ids.resposta2.disabled = True
            self.ids.resposta3.disabled = True

    def responder(self,resposta_escolhida):
        correta = PERGUNTAS[self.index]["correta"]
        if resposta_escolhida == correta:
            self.pontuacao= self.pontuacao +1
            self.mostrar_popup("Certo!","Resposta Correta")
        else:
            self.mostrar_popup("Enrrado",f"A resposta correta era:{correta}")

        self.index =self.index+1
        self.carregar_proxima()

    def mostrar_popup(self,titulo,mensagem):
        popup = Popup(title=titulo, content=Label(text=mensagem),
                      size_hint=(None, None),size=(300,200))

class QuizApp(App):
    def build(self):
        return QuizLayout()

QuizApp().run()