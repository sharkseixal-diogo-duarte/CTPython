from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock
import datetime
import calendar
import json
import os


# -------------------------
#   REGISTO DE UTILIZADOR
# -------------------------
class RegisterScreen(Screen):
    def register(self):
        user = self.ids.reg_user.text
        password = self.ids.reg_pass.text

        if not user or not password:
            self.ids.reg_msg.text = "Preencha todos os campos"
            return

        data = {"user": user, "password": password}

        with open("utilizador.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        self.ids.reg_msg.text = "Registo concluído!"
        self.manager.current = "login"


# -------------------------
#         LOGIN
# -------------------------
class LoginScreen(Screen):
    def do_login(self):
        user = self.ids.user_input.text
        password = self.ids.pass_input.text

        if not os.path.exists("utilizador.json"):
            self.ids.login_msg.text = "Nenhum utilizador registado"
            return

        with open("utilizador.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        if user == data["user"] and password == data["password"]:
            self.manager.current = "final"
        else:
            self.ids.login_msg.text = "User ou password incorretos"


# -------------------------
#      ITEM DA TAREFA
# -------------------------
class TaskItem(RecycleDataViewBehavior, BoxLayout):
    texto = StringProperty()
    prioridade = StringProperty()
    prazo = StringProperty()

    def remove_task(self, instance):
        app = App.get_running_app()
        final = app.root.get_screen("final")

        for i, t in enumerate(final.tarefas):
            if t["texto"] == self.texto and t["prioridade"] == self.prioridade and t["prazo"] == self.prazo:
                final.remover_tarefa(i)
                break


# -------------------------
#      ECRÃ FINAL
# -------------------------
class FinalLayout(Screen):
    tarefas = ListProperty([])
    calendario = StringProperty("")
    notificacao = StringProperty("")

    def on_enter(self):
        hoje = datetime.date.today()
        self.calendario = calendar.month(hoje.year, hoje.month)

        self.load_tasks()
        self.update_task_list()

        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, dt):
        self.ids.relogio.text = datetime.datetime.now().strftime("%H:%M:%S")

    # Guardar tarefas
    def save_tasks(self):
        with open("tarefas.json", "w", encoding="utf-8") as f:
            json.dump(self.tarefas, f, ensure_ascii=False, indent=4)

    # Carregar tarefas
    def load_tasks(self):
        if os.path.exists("tarefas.json"):
            with open("tarefas.json", "r", encoding="utf-8") as f:
                self.tarefas = json.load(f)
        else:
            self.tarefas = []

    def adicionar_tarefa(self, texto, prioridade, prazo):
        if texto:
            self.tarefas.append({
                "texto": texto,
                "prioridade": prioridade,
                "prazo": prazo
            })
            self.update_task_list()
            self.save_tasks()
            self.verificar_prazos()

    def remover_tarefa(self, index):
        if 0 <= index < len(self.tarefas):
            self.tarefas.pop(index)
            self.update_task_list()
            self.save_tasks()
            self.verificar_prazos()

    def update_task_list(self):
        self.ids.lista_tarefas.data = [
            {"texto": t["texto"], "prioridade": t["prioridade"], "prazo": t["prazo"]}
            for t in self.tarefas
        ]

    def verificar_prazos(self):
        hoje = datetime.date.today()
        self.notificacao = ""

        for t in self.tarefas:
            prazo_str = t.get("prazo", "")
            if not prazo_str:
                continue

            try:
                prazo = datetime.datetime.strptime(prazo_str, "%Y-%m-%d").date()
                dias_restantes = (prazo - hoje).days

                if dias_restantes < 0:
                    self.notificacao = f"Tarefa atrasada: {t['texto']}"
                    return

                if 0 <= dias_restantes <= 3:
                    self.notificacao = f"Tarefa quase no prazo: {t['texto']} (faltam {dias_restantes} dias)"
                    return

            except ValueError:
                continue


# -------------------------
#      APLICAÇÃO
# -------------------------
class FinalApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(FinalLayout(name="final"))
        return sm


if __name__ == "__main__":
    FinalApp().run()