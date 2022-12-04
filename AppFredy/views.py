from django.shortcuts import render
from .models import hermanos
from django.http import HttpResponse
from django.template import Template,Context


def hermanos(self):
    familia = {"Nombre" : "Martin" , "Apellido": "Fredriksson" , "Edad" :18}
    familia.save()
    documentodetexto = f"------>Familia: {hermanos.Nombre} Apellido: {hermanos.Apellido}"

    return HttpResponse(documentodetexto)




