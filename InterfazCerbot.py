from datetime import datetime
from tkinter import font, scrolledtext, ttk
import tkinter as tk
from Cerbot import Cerbot
from db.HistorialCRUD import HistorialCRUD

class InterfazCerbot:
    def __init__(self):
        self.cerbot = Cerbot()
        self.historial = HistorialCRUD()
        self.consultas = self.cerbot.consultas

    def clear_chat(self, tree_chat):
        for item in tree_chat.get_children():
            tree_chat.delete(item)

    def logout(self, root, login_window):
        login_window.deiconify()
        root.destroy()
    
    def mostrar_ventana_chat(self, usuario, login_window):
        def send_message():
            user_input = user_entry.get()
            consulta = []
            
            if user_input == "": return
            response = self.cerbot.get_response(user_input)
            # chat_display.config(state=ttk.NORMAL)
            
            # Agregar historial
            fecha_temp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for row in self.consultas:
                if row[2] == response: consulta = row
            
            print(f"\nResponse: {response}, Consulta: {consulta}")
            
            # self.historial.agregarHistorial(user_input, fecha_temp, 1, consulta[0])
            if consulta:
                self.historial.agregarHistorial(user_input, fecha_temp, usuario[0], consulta[0])
            else:
                print("\nNo se encontró una consulta correspondiente a la respuesta.")            
            
            hora_minuto = fecha_temp.split()[1][:5]
            # Mensaje con la hora y minuto al extremo derecho
            user_message = f"Usted: {user_input}\n"
            bot_message = f"Cerbot: {response}\n"
            
            # chat_display.insert(tk.END, f"Usted: {user_input}\t")
            # chat_display.insert(tk.END, f"Hora: {hora_minuto}\n")
            tree_chat.insert("", tk.END, values=(user_message, hora_minuto))
            tree_chat.insert("", tk.END, values=(bot_message, hora_minuto))
            # Insertar mensaje en el Treeview
            # tree_chat.insert("Mensaje", tk.END, values=(user_message, hora_minuto))
            # tree_chat.insert("Hora", tk.END, values=(bot_message, hora_minuto))
            
            # combined_message = f"{user_message:<60}{hora_minuto}\n{bot_message:<60}"        
            # chat_display.insert(tk.END, combined_message, "bot_font")

    
            # print(hora_minuto)
            # chat_display.config(state=ttk.DISABLED)
            user_entry.delete(0, tk.END) # Limpiar user_entry
        
        ############################ VENTANA ##########################
        root = tk.Tk()
        root.title("CERBOT")
        
        # Fila 1: Nombre de usuario, espacio vacío, Salir de sesión
        frame_user = ttk.Frame(root, padding=(5, 5, 5, 5))
        label_username = ttk.Label(frame_user, text=f"{usuario[1]} {usuario[2]}")
        btn_logout = ttk.Button(frame_user, text="Salir de la Sesión", command=lambda: self.logout(root, login_window))
        
        label_username.grid(row=0, column=0)
        frame_user.grid_columnconfigure(1, weight=1) # Espacio vacío
        btn_logout.grid(row=0, column=2)

        frame_user.pack(fill="x") # Expandir esta fila de forma horizontal

        # Fila 2: Conversación y hora asociada
        frame_chat = ttk.Frame(root)
        chat_display = ttk.Scrollbar(frame_chat)

        # Treeview para mostrar la conversación
        tree_chat = ttk.Treeview(frame_chat, columns=("Mensajes", "Hora"), show="headings", height=10, yscrollcommand=chat_display.set)
        tree_chat.column("Mensajes", width=400)
        tree_chat.column("Hora", width=50)

        # Configuración de encabezados
        tree_chat.heading("Mensajes", text="Mensaje")
        tree_chat.heading("Hora", text="Hora")

        # Configuración de scrollbar
        chat_display.config(command=tree_chat.yview)
        chat_display.pack(side="right", fill="y")

        # Empacar el Treeview
        tree_chat.pack(expand=True, fill="both")
        frame_chat.pack(expand=True, fill="both")

        # Fila 3: Entrada del usuario
        frame_input = ttk.Frame(root, padding=(5, 5, 5, 5))
        user_entry = ttk.Entry(frame_input, width=50)
        btn_send = ttk.Button(frame_input, text="Enviar", command=lambda: send_message())

        user_entry.grid(row=0, column=0)
        btn_send.grid(row=0, column=1)

        frame_input.pack(fill="x")

        # Fila 4: Botones Ver historial, Limpiar chat, y Enviar
        frame_buttons = ttk.Frame(root, padding=(5, 5, 5, 5))
        
        btn_history = ttk.Button(frame_buttons, text="Ver Historial", command=lambda: self.verHistorial(usuario))
        btn_clear = ttk.Button(frame_buttons, text="Limpiar Chat", command=lambda: self.clear_chat(tree_chat))

        btn_history.grid(row=0, column=0)
        frame_buttons.grid_columnconfigure(2, weight=1)
        btn_clear.grid(row=0, column=1)
        
        frame_buttons.pack(fill="x")
        
        root.mainloop()
        
    def verHistorial(self, usuario):
        usuarioHistorial = []
        
        root = tk.Tk()
        root.title("Mi historial de consultas")
        
        # Fila 1: Nombre de usuario, espacio vacío, Salir de sesión
        frame_user = ttk.Frame(root, padding=(5, 5, 5, 5))
        label_username = ttk.Label(frame_user, text=f"{usuario[1]} {usuario[2]}")
        btn_logout = ttk.Button(frame_user, text="Regresar", command= root.destroy)
        
        label_username.grid(row=0, column=0)
        frame_user.grid_columnconfigure(1, weight=1) # Espacio vacío
        btn_logout.grid(row=0, column=2)

        frame_user.pack(fill="x") # Expandir esta fila de forma horizontal

        # Fila 2: Conversación y hora asociada
        frame_chat = ttk.Frame(root)
        historial_display = ttk.Scrollbar(frame_chat)

        # Treeview para mostrar la conversación
        tree_chat = ttk.Treeview(frame_chat, columns=("Consultas", "Respuestas de Cerbot", "Fechas"), show="headings", height=20, yscrollcommand=historial_display.set)
        tree_chat.column("Consultas", width=200)
        tree_chat.column("Respuestas de Cerbot", width=500)
        tree_chat.column("Fechas", width=130)

        # Configuración de encabezados
        tree_chat.heading("Consultas", text="Consultas")
        tree_chat.heading("Respuestas de Cerbot", text="Respuestas de Cerbot")
        tree_chat.heading("Fechas", text="Fechas")

        # Configuración de scrollbar
        historial_display.config(command=tree_chat.yview)
        historial_display.pack(side="right", fill="y")

        # Empacar el Treeview
        tree_chat.pack(expand=True, fill="both")
        frame_chat.pack(expand=True, fill="both")

        for row in self.historial.leerHistorial():
            if usuario[0] == row[3]:
                usuarioHistorial.insert(0, row)
        
        if usuarioHistorial == []:
            print(f"El usuario {usuario[1]} {usuario[2]}, no tiene mensajes previos.")
        else:
            for historial in usuarioHistorial:
                respuesta = self.cerbot.consultasCRUD.getConsultaByID(historial[4])
                
                tree_chat.insert("", tk.END, values=(historial[1], respuesta[2], historial[2]))
                
                # print(f"Consulta: {historial[1]} - Respuesta: {respuesta[2]} - Fecha: {historial[2]}")
                
        root.mainloop()

# if __name__ == "__main__":
#     interfaz = InterfazCerbot()
#     usuario = [1, "Rodrigo", "Sihues Yanqui", "74663928@certus.edu.pe", "1234"]
#     interfaz.mostrar_ventana_chat(usuario)

## modo beta :v
class InterfazHistorial(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Historial de Consultas")
        self.geometry("500x400")

        # Configuración de colores
        fondo_crema = "#EDBBB4"  # Color crema
        azul_mate = "#3399CC"    # Azul claro
        blanco = "#FFFFFF"       # Blanco
        black = "#000000"        #negro
        azure = "#F0FFFF"        #sky
        red = "#A52A2A"            #red
        

        self.configure(bg=azul_mate)  # Fondo de la ventana

        self.style = ttk.Style(self)
        self.style.configure("TLabel", font=("Verdana", 12), background=azul_mate, foreground='black')
        self.style.configure("TButton", font=("Verdana", 12), background=black, foreground=black)
        self.style.configure("TEntry", font=("Verdana", 12), background=azul_mate)

        self.label = ttk.Label(self, text="Ingrese el usuario:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(self)
        self.entry.pack(pady=10)

        self.button = ttk.Button(self, text="Ver Historial", command=self.mostrar_historial)
        self.button.pack(pady=10)

        self.text_area = tk.Text(self, height=10, width=50, bg=azure, font=("Arial", 9))
        self.text_area.pack(pady=10)

    def mostrar_historial(self):
        usuario = self.entry.get()
        usuarioHistorial = []

        # Aquí iría tu lógica actual para obtener el historial
        # Puedes adaptar tu función verHistorial para trabajar con la lista usuarioHistorial

        # Simulación de datos para probar la interfaz
        usuarioHistorial = [
            ("Consulta1", "Respuesta1", "Fecha1"),
            ("Consulta2", "Respuesta2", "Fecha2"),
        ]

        self.text_area.delete(1.0, tk.END)  # Limpiar el área de texto antes de mostrar nuevo historial

        if usuarioHistorial == []:
            self.text_area.insert(tk.END, f"El usuario {usuario} no tiene mensajes previos.", "warning")
        else:
            for historial in usuarioHistorial:
                self.text_area.insert(tk.END, f"Consulta: {historial[0]}\n", "consulta")
                self.text_area.insert(tk.END, f"Respuesta: {historial[1]}\n", "respuesta")
                self.text_area.insert(tk.END, f"Fecha: {historial[2]}\n\n", "fecha")

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = InterfazHistorial()
    app.run()