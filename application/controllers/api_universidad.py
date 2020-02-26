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
                        text ['app_version'] = "0.5.0"
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
                elif data['action'] == "update":
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        lo = []
                        
                        validator = 0
                        for row in reader:
                            result = []
                            if  str(row['matricula']) == data['matricula']:
                                """
                                row['matricula'] = data["matricula"]
                                row['nombre'] = data["nombre"]
                                row['primer_apellido'] = data["primer_apellido"]
                                row['segundo_apellido'] = data["segundo_apellido"]
                                row['carrera'] = data["carrera"]
                                v1 = row["matricula"]
                                v2 = row["nombre"]
                                v3 = row["primer_apellido"]
                                v4 = row["segundo_apellido"]
                                v5 = row["carrera"]
                                """
                                with open ('static/csv/alumnos.csv','w') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow(row)
                                    v1 = data["matricula"]
                                    v2 = data["nombre"]
                                    v3 = data["primer_apellido"]
                                    v4 = data["segundo_apellido"]
                                    v5 = data["carrera"]
                                    result.append(v1)
                                    result.append(v2)
                                    result.append(v3)
                                    result.append(v4)
                                    result.append(v5)
                                    lo.append(result)
                            else:
                                fila1 = row['matricula'] 
                                fila2 = row['nombre']
                                fila3 = row['primer_apellido']
                                fila4 = row['segundo_apellido']
                                fila5 = row['carrera']
                                result.append(fila1)
                                result.append(fila2)
                                result.append(fila3)
                                result.append(fila4)
                                result.append(fila5)
                                lo.append(result)
                        with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                            writer = csv.writer(csvfiles)
                            for x in lo:
                                writer.writerow(x)
                        if validator == 0:
                            result.append("No existe el valor")
                    return json.dumps("hecho")
                elif data['action'] == "delete":
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        lo = []
                        validator = 0
                        for row in reader:
                            result = []
                            if  str(row['matricula']) == data['matricula']:
                                with open ('static/csv/alumnos.csv','w') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow(row)
                                    print("ok")
                            else:
                                fila1 = row['matricula'] 
                                fila2 = row['nombre']
                                fila3 = row['primer_apellido']
                                fila4 = row['segundo_apellido']
                                fila5 = row['carrera']
                                result.append(fila1)
                                result.append(fila2)
                                result.append(fila3)
                                result.append(fila4)
                                result.append(fila5)
                                lo.append(result)
                        with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                            writer = csv.writer(csvfiles)
                            writer.writerow(result)
                        if validator == 0:
                            result.append("No existe el valor")
                    return json.dumps("hecho")
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
            
