import web #permite hacer conecciones
'''
Parametros de configuracion para conectarse a una base de datos
MySQL o MariaDB
'''
db_host = 'localhost' # Servidor colocamos la URL
db_name = 'base_alumnos' # Nombre de la base de datos
db_user = 'omar' # Usuario
db_pw = 'omar.2018' # contrasena
db_port = 3306 # puerto de mariadb 
# en el model se coloca todo lo que tiene que ver con las bases de datos
# db lo que hace es conectarse con la base de datos
db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw,
    port = db_port
    )

'''
Metodo para seleccionar todos los registros de la tabla datos
'''
def select_datos():
    try:
        return db.select('datos')
    except Exception as e:
        print "Model select_datos Error {}".format(e.args)
        print "Model select_datos Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el email dato
'''
def select_matricula(matricula):
    try:
        return db.select('datos',where='matricula=$matricula', vars=locals())[0]
    except Exception as e:
        print "Model select_matricula Error {}".format(e.args)
        print "Model select_matricula Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando email y password
'''
def insert_datos(matricula, nombre, a_paterno, a_materno, calle, numero, colonia, municipio, estado, cp, email, password):
    try:
        return db.insert('datos', matricula=matricula, nombre=nombre, a_paterno=a_paterno, a_materno=a_materno, calle=calle, numero=numero, colonia=colonia, municipio=municipio, estado=estado, cp=cp, email=email, password=password)
    except Exception as e:
        print "Model insert_datos Error {}".format(e.args)
        print "Model insert_datos Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el email dato
'''
def delete_datos(matricula):
    try:
        return db.delete('datos', where='matricula=$matricula',vars=locals())
    except Exception as e:
        print "Model delete_datos Error {}".format(e.args)
        print "Model delete_datos Message {}".format(e.message)
        return None

'''
Metodo para actualizar el email y el password
'''
def update_datos(matricula, nombre, a_paterno, a_materno, calle, numero, colonia, municipio, estado, cp, email, password):
    try:
        return db.update('datos', 
            matricula=matricula,
            nombre=nombre, 
            a_paterno=a_paterno, 
            a_materno=a_materno, 
            calle=calle, 
            numero=numero, 
            colonia=colonia, 
            municipio=municipio, 
            estado=estado,
            cp=cp, 
            email=email,
            password=password,
             
            where='matricula=$matricula',
            vars=locals())
    except Exception as e:
        print "Model update_datos Error {}".format(e.args)
        print "Model update_datos Message {}".format(e.message)
        return None
