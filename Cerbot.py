import re
import random
import tkinter as tk
from tkinter import font, scrolledtext
import tkinter
from db.ConsultasCRUD import ConsultasCRUD

class Cerbot:
    def __init__(self):
        self.consultasCRUD = ConsultasCRUD()
        self.consultas = self.consultasCRUD.leer()

    def get_response(self, user_input):
        split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
        response = self.check_all_messages(split_message)
        return response

    def message_probability(self, user_message, recognized_words, single_response=False, required_word=[]):
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

    def check_all_messages(self, message):
        highest_prob = {}
        palabras_clave = []
        codigo = 1
        
        def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob
            highest_prob[bot_response] = self.message_probability(message, list_of_words, single_response, required_words)
        
        for row in self.consultas:
            if (row[1] != 10):            
                if (row[1] != codigo):
                    response(respuesta, palabras_clave, single_response=True)
                    # print(f"\n{respuesta} - {palabras_clave}")
                    palabras_clave = []
                    codigo = row[1]
                
                palabras_clave.append(row[3])
                respuesta = row[2]
        
        best_match = max(highest_prob, key=highest_prob.get)

        return self.unknown() if highest_prob[best_match] < 1 else best_match

    def unknown(self):
        consulta_desconocida = []
        
        for row in self.consultas:
            if row[1] == 10:
                consulta_desconocida.append(row[2])
            
        response = consulta_desconocida[random.randrange(3)]
        return response

# def send_message(user_input, message_type):
#     global user_entry
#     global chat_display
#     response = a.get_response(user_input)
#     chat_display.config(state=tk.NORMAL)

#     if message_type == 'user':
#         chat_display.insert(tk.END, f"You: {user_input}\n", 'user_font')
#     elif message_type == 'bot':
#         chat_display.insert(tk.END, f"Cerbot: {response}\n", 'bot_font')

#     chat_display.config(state=tk.DISABLED)
#     user_entry.delete(0, tk.END)

# def clear_chat():
#     global chat_display
#     chat_display.config(state=tk.NORMAL)
#     chat_display.delete(1.0, tk.END)
#     chat_display.config(state=tkinter.DISABLED)

# def on_enter(event):
#     user_input = user_entry.get()
#     send_message(user_input, 'user')

# def mostrar_ventana_chat():
#     global chat_display

#     def send_message():
#         user_input = user_entry.get()
#         response = a.get_response(user_input)
#         chat_display.config(state=tk.NORMAL)

#         chat_display.insert(tk.END, f"You: {user_input}\n", 'user_font')
#         chat_display.insert(tk.END, f"Cerbot: {response}\n", 'bot_font')

#         chat_display.config(state=tk.DISABLED)
#         user_entry.delete(0, tk.END)

#     root = tk.Tk()
#     root.title("CERBOT")

#     # Configuración de colores
#     fondo_crema = "#d5d5d5"
#     naranja_negrita = "#FF5733"

#     # Configuración de estilos
#     estilo = {
#         'user_font': font.Font(family='Verdana', size=9, weight='bold', underline=False, overstrike=False, slant='roman'),
#         'bot_font': font.Font(family='Impact', size=10, weight='normal', underline=False, overstrike=False, slant='roman')
#     }

#     chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 9), bg=fondo_crema)
#     user_entry = tk.Entry(root, width=60, font=("Arial", 9))

#     send_button = tk.Button(root, text="Enviar", command=send_message, bg=naranja_negrita, fg='white')
#     clear_button = tk.Button(root, text="Limpiar chat", command=clear_chat, bg=naranja_negrita, fg='white')

#     chat_display.tag_configure('user_font', font=estilo['user_font'])
#     chat_display.tag_configure('bot_font', font=estilo['bot_font'])

#     chat_display.config(state=tk.DISABLED)
#     chat_display.pack()

#     user_entry.pack()

#     send_button.pack()
#     clear_button.pack()

#     root.bind('<Return>', lambda event=None: send_message())

#     root.mainloop()

# if __name__ == "__main__":
#     a = Cerbot()
#     mostrar_ventana_chat()