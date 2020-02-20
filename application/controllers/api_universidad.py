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
                        result=[]
                        caja = []
                        text = {}
                        text ['status'] = "200 ok"
                        text ['app_version'] = "0.0.1"
                        # text ['Alumno'] = na
                        caja.append(text)
                        for row in reader:
                            result.append(row)
                            text ['Alumno'] = result
                    return json.dumps(text)
                elif data['action'] == "search":
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        result = []
                        validator = 0
                        for row in reader:
                            if  str(row['matricula']) == data['matricula']:
                                validator = 1
                                result.append(row)
                        if validator == 0:
                            result.append("No existe el valor")
                    return json.dumps(result)
                elif data["action"] == "put":
                    v1 = data["matricula"]
                    v2 = data["nombre"]
                    v3 = data["primer_apellido"]
                    v4 = data["segundo_apellido"]
                    v5 = data["carrera"]
                    result = []
                    result.append(v1)
                    result.append(v2)
                    result.append(v3)
                    result.append(v4)
                    result.append(v5)
                    with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                        writer = csv.writer(csvfiles)
                        writer.writerow(result)
                    return("Hecho")
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
            