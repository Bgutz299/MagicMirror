from guizero import App
#import spotify_module

def app_init():
	app = App(title="Mira", layout="grid",bg="black",height=1024,width=600)
	#app.full_screen = True
	#app.set_full_screen('Esc')
	#app.tk.protocol( "WM_DELETE_WINDOW", spotify_module.close(app))
	return app
