from guizero import App

def app_init():
	app = App(title="Mira", layout="grid",bg="black",height=1024,width=600)
	#app.full_screen = True
	#app.set_full_screen('Esc')
	return app
