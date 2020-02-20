import web
import app
import csv
import json
render = web.template.render('application/views/')
class Action:
    def GET(self):
        try:
            data = web.input()
            if data['token'] =="1234":
                if data['action'] == "get":
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        na = []
                        caja = []
                        text = {}
                        text ['status'] = "200 ok"
                        text ['app_version'] = "0.0.1"
                        caja.append(text)
                        result={}
                        for row in reader:
                            na.append(result)
                            result ['matricula'] = str(row['matricula'])
                            result ['nombre'] =  str(row['nombre'])
                            result ['primer_apellido'] = str(row['primer_apellido'])
                            result ['segundo_apellido'] = str(row['segundo_apellido'])
                            result ['carrera'] = str(row['carrera'])
                            text ['Alumno'] = na
                    return json.dumps(caja)
                elif data["action"] == "put":
                    data["matricula"]
                    data["nombre"]
                    data["primer_apellido"]
                    data["segundo_apellido"]
                    data["carrera"]
                    with open ('static/csv/datos.csv','a+', newline = '') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(result)
                else:
                    result={}
                    text= "Comand not found"
                    result  ['status'] = text 
                    return json.dumps(result)

                
            else:
                result={}
                text= "Token no valido"
                result  ['status'] = text 
                return json.dumps(result)
        except Exception as e:
            result={}
            text= "ups algo paso{}".format(e.args)
            result  ['status'] = text 
            return json.dumps(result)
            