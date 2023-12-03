from tkinter import font, scrolledtext
import tkinter as tk
from crud_ia import CrudApp
from Cerbot import Cerbot;

# if __name__ == "__main__":
#     app = CrudApp()

#     while True:
#         print("\nMenu:")
#         print("1. Insertar")
#         print("2. Seleccionar")
#         print("3. Actualizar")
#         print("4. Eliminar")
#         print("5. Salir")

#         choice = input("Ingrese el número de la opción que desea: ")

#         if choice == "1":
#             nombres = input("Ingrese nombres: ")
#             apellidos = input("Ingrese apellidos: ")
#             correo = input("Ingrese correo: ")
#             contrasena = input("Ingrese contraseña: ")
            
#             app.insertar(nombres, apellidos, correo, contrasena)
#         elif choice == "2":
#             app.seleccionar()
#         elif choice == "3":
#             app.actualizar()
#         elif choice == "4":
#             app.eliminar()
#         elif choice == "5":
#             app.db.close_connection()
#             print("Saliendo del programa. ¡Hasta luego!")
#             break
#         else:
#             print("Opción no válida.")
            

def send_message(user_input, message_type):
    global user_entry
    global chat_display
    response = cerbot.get_response(user_input)
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
        response = cerbot.get_response(user_input)
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
    cerbot = Cerbot()
    mostrar_ventana_chat()