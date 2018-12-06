import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Delete:
    def __init__(self):
        pass

    def GET(self, matricula): 
        datos = model_datos.select_matricula(matricula) 
        return render.delete(datos)
    
    def POST(self, matricula):
        formulario = web.input()
        matricula = formulario['matricula']
        model_datos.delete_datos(matricula)
        raise web.seeother('/')
