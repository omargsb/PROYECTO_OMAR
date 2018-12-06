import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Index:
    def __init__(self):
        pass

    def GET(self):  
        datos = model_datos.select_datos().list() # esta linea toma todos los registros de la base de datos
        return render.index(datos)
