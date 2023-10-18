import tkinter as tk
from tkinter import scrolledtext
import re
import random
from login_ia import LoginApp
from crud_ia import CrudApp

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

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

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('¡Hola Soy CerBot! ¿En qué puedo ayudarte?', ['hola', 'hi', 'saludos', 'buenas'], single_response=True)
    response('La próxima clase es el Miercoles [7:00 am - 10:00 am].', ['proxima','clase', 'siguiente', 'horario'], single_response=True)
    response('Los documentos o archivos del curso están disponibles en la plataforma de "certus".', ['documentos','archivos', 'donde'], single_response=True)
    response('Puedes encontrar ejemplos de tareas o proyectos anteriores en la plataforma de "Certus".', ['dudas', 'tarea','proyecto','donde'], single_response=True)
    response('Tu desempeño se evaluará a través de tareas, proyectos, exámenes y participación.', ['evaluacion','evaluar', 'calificación', 'calificar', 'como se evalua'], single_response=True)
    response('Tus notas las puedes encontrar ingresando al intranet, en la seccion ver mis notas intranet.', ['ver','calificacion', 'notas', 'donde','puedo'], single_response=True)
    response('Sí, tenemos una comunidad en línea para estudiantes. Únete y participa.', ['grupo',' estudio', 'comunidad','estudiantes', ' unirme','donde'], single_response=True)
    response('Estamos aquí para apoyarte en el aprendizaje de tu Curso de Inteligencia Artificial. ¡Buena suerte en tus estudios!', ['gracias', 'adios', 'despedida'], single_response=True)

    best_match = max(highest_prob, key=highest_prob.get)

    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['no entendí tu consulta', 'No estoy seguro de lo que quieres', 'Disculpa, ¿puedes intentarlo de nuevo?'][random.randrange(3)]
    return response

def send_message():
    user_input = user_entry.get()
    response = get_response(user_input)
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_input}\n")
    chat_display.insert(tk.END, f"Cerbot: {response}\n")
    chat_display.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

def clear_chat():
    chat_display.config(state=tk.NORMAL)
    chat_display.delete(1.0, tk.END)
    chat_display.config(state=tk.DISABLED)

def on_enter(event):
    send_message()

def mostrar_ventana_chat():
    root.title("CERBOT")

    # Ajusta el tamaño del área de chat
    chat_display.config(state=tk.DISABLED)
    chat_display.pack()

    user_entry.pack()

    send_button = tk.Button(root, text="Enviar", command=send_message)
    send_button.pack()

    clear_button = tk.Button(root, text="Reiniciar", command=clear_chat)
    clear_button.pack()

    # Vincula la tecla Enter al evento de enviar el mensaje
    root.bind('<Return>', on_enter)

    root.mainloop()

if __name__ == "__main__":
    crud_app = CrudApp()
    login_app = LoginApp(tk.Tk(), crud_app)
    login_app.root.mainloop()
    
    if login_app.sesion_iniciada:          
        root = tk.Tk()
        chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        user_entry = tk.Entry(root, width=60)
        send_button = tk.Button(root, text="Enviar", command=send_message)
        clear_button = tk.Button(root, text="Reiniciar", command=clear_chat)
        
        mostrar_ventana_chat()
