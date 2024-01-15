import npyscreen

class TextEditorForm(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.MultiLineEdit, editable=True, rely=2, relx=2, max_height=10)
        self.add(npyscreen.ButtonPress, name='Fechar', when_pressed_function=self.on_close)

    def on_close(self):
        self.parentApp.switchForm(None)

class TextEditorApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', TextEditorForm, name='Text Editor')

if __name__ == '__main__':
    app = TextEditorApp()
    app.run()
