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
                        result={}
                        for row in reader:
                            na.append(result)
                            result ['matricula'] = str(row['matricula'])
                            result ['nombre'] =  str(row['nombre'])
                            result ['primer_apellido'] = str(row['primer_apellido'])
                            result ['segundo_apellido'] = str(row['segundo_apellido'])
                            result ['carrera'] = str(row['carrera'])
                    return json.dumps(na)
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
            