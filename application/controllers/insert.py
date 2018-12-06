import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return render.insert()
    
    def POST(self):
        formulario = web.input() # Almacena datos al formulario
        matricula = formulario ['matricula']
        nombre = formulario['nombre']
        a_paterno = formulario['a_paterno']
        a_materno = formulario['a_materno']
        calle = formulario['calle']
        numero = formulario['numero']
        colonia = formulario['colonia']
        municipio = formulario['municipio']
        estado = formulario['estado']
        cp = formulario['cp']
        email = formulario['email'] # almacena el email escrito en input
        password = formulario['password'] # almacena el password escrto en input
        model_datos.insert_datos(matricula, nombre, a_paterno, a_materno, calle, numero, colonia, municipio, estado, cp, email, password) # llama al metodo insert_datos y lo pasa a los datos guardados
        raise web.seeother('/') # redirecciona al index.html
