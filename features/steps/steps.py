from behave import given, when, then
import re

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            "quarto":0.25, "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
            "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
            "ochenta": 80, "noventa": 90, "media": 0.5, "medio":0.5, "cien":100, "cientos":100, "ciento":100, "doscientos":200, "trescientos":300, 
            "cuatrocientos":400, "quinientos":500, "seiscientos":600, "setecientos":700, "ochocientos":800, 
            "novecientos":900, "mil":1000
        }
        return numeros.get(palabra.lower(), 0)

@given('que he comido {cukes:d} pepinos')
def step_given_eaten_cukes(context, cukes):
    context.belly.comer(cukes)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.strip()

    if time_description == 'media hora':
        total_time_in_hours = 0.5
    elif time_description == 'una hora':
        total_time_in_hours = 1
    elif time_description == 'una hora y media':
        total_time_in_hours = 1.5
    elif time_description == 'un cuarto de hora':
        total_time_in_hours = 0.25
    elif time_description == 'una hora y cuarto':
        total_time_in_hours = 1.25
    else:
        pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')
        match = pattern.match(time_description)

        if match:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
	    #Verifica el numero de segundos mencionados - misma funcion de antes pero agregando el parametro de segundos
            seconds_word = match.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            #Halla numero de segundos
            seconds = convertir_palabra_a_numero(seconds_word)

            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        else:
            if time_description == 'medio minuto':
                total_time_in_hours = 1 / 120
            elif time_description == 'un minuto':
                total_time_in_hours = 1 / 60
            else:
                pattern_min_seg = re.compile(r'(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')
                match = pattern_min_seg.match(time_description)
                if match:
                    minutes_word = match.group(1) or "0"
                    seconds_word = match.group(2) or "0"
                    minutes = convertir_palabra_a_numero(minutes_word)
                    seconds = convertir_palabra_a_numero(seconds_word)
                    total_time_in_hours = (minutes / 60) + (seconds / 3600)
                else:
                    if time_description == 'medio segundo':
                        total_time_in_hours = 1 / 7200
                    elif time_description == 'un segundo':
                        total_time_in_hours = 1 / 3600
                    else:
                        pattern_seg = re.compile(r'(?:(\w+)\s*segundos?)?')
                        match = pattern_seg.match(time_description)
                        if match:
                            seconds_word = match.group(1) or "0"
                            seconds = convertir_palabra_a_numero(seconds_word)
                            total_time_in_hours = (seconds / 3600)
                        else:
                            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."
