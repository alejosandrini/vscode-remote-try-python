#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

opciones = ["piedra", "papel", "tijera"]
puntaje = {"rondas": 0, "ganadas": 0, "perdidas": 0, "empates": 0}

print("Bienvenido al juego de piedra, papel o tijera")
print("Elija una opcion: piedra, papel o tijera")

def jugar():

    input_usuario = input("Ingrese su opcion: ").lower()
    input_usuario = input_usuario
    if input_usuario in opciones:
        opcion_computadora = random.choice(opciones)
        print("La computadora eligio: ", opcion_computadora)
        if input_usuario == opcion_computadora:
            print("Empate")
            puntaje["empates"] += 1
        elif input_usuario == "piedra":
            if opcion_computadora == "papel":
                print("Perdiste")
                puntaje["perdidas"] += 1
            else:
                print("Ganaste")
                puntaje["ganadas"] += 1
        elif input_usuario == "papel":
            if opcion_computadora == "tijera":
                print("Perdiste")
                puntaje["perdidas"] += 1
            else:
                print("Ganaste")
                puntaje["ganadas"] += 1
        elif input_usuario == "tijera":
            if opcion_computadora == "piedra":
                print("Perdiste")
                puntaje["perdidas"] += 1
            else:
                print("Ganaste")
                puntaje["ganadas"] += 1

        puntaje["rondas"] += 1
    else:
        print("Opcion invalida")

    


seguir_jugando = "si"
while seguir_jugando == "si":
    jugar()
    seguir_jugando = input("Desea seguir jugando? [si/no]: ")

print("Rondas jugadas: ", puntaje["rondas"])
print("Rondas ganadas: ", puntaje["ganadas"])
print("Rondas perdidas: ", puntaje["perdidas"])
