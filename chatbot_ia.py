import tkinter as tk
from tkinter import scrolledtext, font
import re
import random

user_entry = None
chat_display = None

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

def send_message(user_input, message_type):
    global user_entry
    global chat_display
    response = get_response(user_input)
    chat_display.config(state=tk.NORMAL)

    if message_type == 'user':
        chat_display.insert(tk.END, f"You: {user_input}\n", 'user_font')
    elif message_type == 'bot':
        chat_display.insert(tk.END, f"Cerbot: {response}\n", 'bot_font')

    chat_display.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

def clear_chat():
    global chat_display
    chat_display.config(state=tk.NORMAL)
    chat_display.delete(1.0, tk.END)
    chat_display.config(state=tk.DISABLED)

def on_enter(event):
    user_input = user_entry.get()
    send_message(user_input, 'user')

def mostrar_ventana_chat():
    global chat_display

    def send_message():
        user_input = user_entry.get()
        response = get_response(user_input)
        chat_display.config(state=tk.NORMAL)

        chat_display.insert(tk.END, f"You: {user_input}\n", 'user_font')
        chat_display.insert(tk.END, f"Cerbot: {response}\n", 'bot_font')

        chat_display.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("CERBOT")

    # Configuración de colores
    fondo_crema = "#EDBBB4"
    naranja_negrita = "#FF5733"

    # Configuración de estilos
    estilo = {
        'user_font': font.Font(family='Verdana', size=9, weight='bold', underline=False, overstrike=False, slant='roman'),
        'bot_font': font.Font(family='Impact', size=10, weight='normal', underline=False, overstrike=False, slant='roman')
    }

    chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 9), bg=fondo_crema)
    user_entry = tk.Entry(root, width=60, font=("Arial", 9))

    send_button = tk.Button(root, text="Enviar", command=send_message, bg=naranja_negrita, fg='white')
    clear_button = tk.Button(root, text="Limpiar chat", command=clear_chat, bg=naranja_negrita, fg='white')

    chat_display.tag_configure('user_font', font=estilo['user_font'])
    chat_display.tag_configure('bot_font', font=estilo['bot_font'])

    chat_display.config(state=tk.DISABLED)
    chat_display.pack()

    user_entry.pack()

    send_button.pack()
    clear_button.pack()

    root.bind('<Return>', lambda event=None: send_message())

    root.mainloop()

if __name__ == "__main__":
    mostrar_ventana_chat()