import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola soy Cerbot, ¿En que puedo ayudarte?', ['hola', 'hi', 'saludos', 'buenas', 'hey', 'hol', 'ola'], single_response=True)
        
        response('Claro, a continuación te muestro los cursos en los que estas inscrito.', ['curso', 'cursos', 'información', 'informacion', 'info'], single_response=True)
        
        response('Espero haberte ayudado, nos vemos.', ['salir', 'exit', 'adios'], single_response=True)
        # response('Siempre a la orden', 'A la orden chamo', ['gracias', 'te lo agradezco', 'thanks', 'ty', 'grax'], single_response=True)
        
        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['No entendi tu consulta', 'No estoy seguro de lo quieres', 'Disculpa, puedes intentarlo de nuevo?'][random.randrange(3)]
    return response

####################################################################################################################
iniciar_bot = True
curso_interaccion = False
bot = "CERBOT"
curso_dudas = {
    1: 'Horario',
    2: 'Información del docente',
    3: 'Contenido del curso',
    4: 'Evidencias',
}
list_info_cursos = ['cursos', 'curso', 'información', 'informacion', 'info']
list_terminar = ['salir', 'exit', 'adios']

while iniciar_bot:
    usuario_entrada = input('Usted: ')
    print(f'{bot}: ' + get_response(usuario_entrada))
    
    # Obteniendo palabras clave
    usuario_palabras = usuario_entrada.lower().split()
    
    for palabra in usuario_palabras:
        if palabra in list_info_cursos:
            curso_interaccion = True
            
        if palabra in list_terminar:            
            iniciar_bot = False
            print(f'{bot}: {get_response(usuario_entrada)}')
        
    while curso_interaccion:
        cursos_usuario = {}
        
        # Obteniendo los cursos del estudiante
        for i in range(0, 6):
            cursos_usuario[i+1] = f'Curso_{i+1}'
                            
        # Mostrando los cursos del estudiante
        for curso in cursos_usuario:
            print(f'{curso} > {cursos_usuario[curso]}')
        print(f'{len(cursos_usuario)+1} > Volver')  
        print(f'{len(cursos_usuario)+2} > Salir')                    
        
        # Esperando opcion escogida del usuario
        print(f'\n{bot}: Ingresa el número del curso en el que tengas dudas: ')
        opcion = int(input("Usted: "))
        
        while (opcion<1) or (opcion>len(cursos_usuario)+2):
            print(f'\n{bot}: Numero incorrecto, vuelve a intentarlo: ')
            opcion = int(input("Usted: "))
        
        if opcion in cursos_usuario:
            # Almacenando el curso elegido
            curso_elegido = cursos_usuario[opcion-1]
            
            # Entrando a la seccion de dudas
            for duda in curso_dudas:
                print(f'{duda} > {curso_dudas[duda]}')
            print(f'{len(cursos_usuario)+1} > Volver')  
            print(f'{len(cursos_usuario)+2} > Salir')  
            
            print(f'\n{bot}: Ingresa el número de la duda que tengas: ')
            opcion = int(input("Usted: "))
            while (opcion<1) or (opcion>len(curso_dudas)+2):
                print(f'\n{bot}: Numero incorrecto, vuelve a intentarlo: ')
                opcion = int(input("Usted: "))
            
            # Casos
            match opcion:
                case 1: print(f'{bot}: Estas son las horas de clase en este curso: \n{curso_elegido}\nMiercoles: 7am - 10am')
                
                case 2: print(f'{bot}: Esta es la información del docente de este curso: \n{curso_elegido}\nNombre completo: ***\nCorreo: ***')
                
                case 3: print(f'{bot}: En este documento tienes el contenido del curso: \nUD_{curso_elegido}.pdf')
                
                case 4: print(f'{bot}: En estos documentos tienes las rubricas de cada evidencia del curso: \nRubrica_aa1_{curso_elegido}.pdf\nRubrica_aa2_{curso_elegido}.pdf\nRubrica_aa3_{curso_elegido}.pdf\nRubrica_aa4_{curso_elegido}.pdf')
                
                case 5: 
                    print(f'{bot}: Regresando al punto anterior...')
                
                case 6:
                    curso_interaccion = False
                    iniciar_bot = False
                    print(f'{bot}: {get_response("salir")}')
                    
        elif opcion == 7:
            curso_interaccion = False
            print(f'{bot}: Regresando al inicio...\n')
        
        else:
            curso_interaccion = False
            iniciar_bot = False
            print(f'{bot}: {get_response("salir")}')