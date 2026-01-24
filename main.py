from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.clock import Clock
import datetime, calendar

class LoginScreen(Screen):
    def do_login(self, user, password):
        if user == "admin" and password == "123":
            self.manager.current = "final"

class FinalLayout(Screen):
    tarefas = ListProperty([])
    calendario = StringProperty("")
    notificacao = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_time, 1)
        self.calendario = calendar.month(
            datetime.date.today().year,
            datetime.date.today().month
        )

    def update_time(self, dt):
        self.ids.relogio.text = datetime.datetime.now().strftime("%H:%M:%S")

    def adicionar_tarefa(self, texto, prioridade, prazo):
        if texto:
            self.tarefas.append({
                "texto": texto,
                "prioridade": prioridade,
                "prazo": prazo
            })
            self.ids.lista_tarefas.adapter.data = [t["texto"] for t in self.tarefas]
            self.verificar_prazos()

    def remover_tarefa(self, index):
        if 0 <= index < len(self.tarefas):
            self.tarefas.pop(index)
            self.ids.lista_tarefas.adapter.data = [t["texto"] for t in self.tarefas]

    def verificar_prazos(self):
        hoje = datetime.date.today()
        for t in self.tarefas:
            if t["prazo"]:
                prazo = datetime.datetime.strptime(t["prazo"], "%Y-%m-%d").date()
                if prazo < hoje:
                    self.notificacao = f"Tarefa atrasada: {t['texto']}"
                    return
        self.notificacao = ""
