import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Update:
    def __init__(self):
        pass

    def GET(self, matricula): 
        datos = model_datos.select_matricula(matricula) 
        return render.update(datos)
    
    def POST(self, matricula):
        formulario = web.input() # Almacena los datos del formulario web
        matricula = formulario['matricula'] # almacena el email del imput email
        nombre = formulario['nombre'] # almacena el password del input password
        a_paterno = formulario['a_paterno']
        a_materno = formulario['a_materno']
        calle = formulario['calle']
        numero = formulario['numero']
        colonia = formulario['colonia']
        municipio = formulario['municipio']
        estado = formulario['estado']
        cp = formulario ['cp']
        email = formulario['email']
        password = formulario['password']
       
        model_datos.update_datos(matricula, nombre, a_paterno, a_materno, calle, numero, colonia, municipio, estado, cp, email, password) # Actualiza los valores
        raise web.seeother('/') # redirecciona al index  CALVE REGEX
