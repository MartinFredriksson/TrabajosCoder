from django.http import HttpResponse 
from django.template import Template,Context


def HermanoMayor(request):
    hermano_mayor ={"Nombre": "Martin" ,"Apellido": "Fredriksson" , "Edad": 18} 

    archivo = open("C:/Users/Martin/Desktop/MVT+Martin/virtual/Proyecto1/Plantillas/template1.HTML")
    
    template= Template(archivo.read())
    archivo.close()
    contexto=Context(hermano_mayor)

    documento=template.render(contexto)
    return HttpResponse(documento)

def HermanoMedio(request):
    
    hermano_del_medio= {"Nombre": "Ignacio" , "Apellido": "Fredriksson" , "Edad": 14}
    
    archivo = open("C:/Users/Martin/Desktop/MVT+Martin/virtual/Proyecto1/Plantillas/template2.HTML")
    
    template= Template(archivo.read())
    archivo.close()
    contexto=Context(hermano_del_medio)

    documento=template.render(contexto)
    return HttpResponse(documento)

def HermanoChico(request):
    hermano_mas_chico = {"Nombre": "Santino" , "Apellido": "Fredriksson" , "Edad": 10}
     
    archivo = open("C:/Users/Martin\Desktop/MVT+Martin/virtual/Proyecto1/Plantillas/template3.HTML")
    
    template= Template(archivo.read())
    archivo.close()
    contexto=Context(hermano_mas_chico)

    documento=template.render(contexto)
    return HttpResponse(documento)

   
    


