from engine.modules.main_class import Main

username = input("Digite o usuário: ")

app = Main(username)
app.execute_all()