# language: es

Característica: Comportamiento del Estómago

  Escenario: Comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: Comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir
  
  Escenario: Comer pepinos y esperar horas minutos y segundos
    Dado que he comido 40 pepinos
    Cuando espero "1 hora, 30 minutos y 45 segundos"
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar en segundos
    Dado que he comido 20 pepinos
    Cuando espero 3600 segundos
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar en horas y minutos
    Dado que he comido 30 pepinos
    Cuando espero "1 hora y 30 minutos"
    Entonces mi estómago no debería gruñir

  Escenario: Comer una cantidad fraccionaria de pepinos y esperar horas enteras
    Dado que he comido 24.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer una cantidad fraccionaria de pepinos y esperar fracciones de hora
    Dado que he comido 40.5 pepinos
    Cuando espero 2.75 horas
    Entonces mi estómago no debería gruñir

  Escenario: Esperar usando horas en inglés
    Dado que he comido 30 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir

  Escenario: Esperar usando solo minutos en inglés
    Dado que he comido 20 pepinos
    Cuando espero 3600 seconds
    Entonces mi estómago no debería gruñir
