import web
# import app
# comando de virtualenv
# virtualenv -p c:/python36/python.exe venv
# cd ./env/

urls = ('/actions/?', 'application.controllers.api_universidad.Action')
app = web.application(urls, globals())
if __name__ == "__main__":
    web.config.debug = False
    app.run()
