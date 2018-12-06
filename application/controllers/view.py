import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class View:
    def __init__(self):
        pass

    def GET(self, matricula):  
        datos = model_datos.select_matricula(matricula) #es cuando se muestra la pagina view cuando le damos clic en el email
        return render.view(datos)
