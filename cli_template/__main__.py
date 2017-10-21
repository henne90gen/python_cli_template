from .app import TemplateApp

if __name__ == '__main__':
    with TemplateApp() as app:
        app.run()
