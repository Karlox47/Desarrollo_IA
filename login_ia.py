import tkinter as tk
from tkinter import messagebox
from crud_ia import CrudApp

class LoginApp:
    def __init__(self, root, crud_instance):
        self.root = root
        self.root.title("Inicio de Sesión")

        # Establecer el tamaño de la ventana principal
        self.root.geometry("300x350")

        self.crud_instance = crud_instance

        # Crear un marco para centrar los elementos y agregar espacio
        frame = tk.Frame(root, padx=20, pady=10)
        frame.pack(expand=True, fill='both')

        tk.Label(frame, text="Correo:").grid(row=0, column=0, pady=5, padx=5, sticky='e')
        tk.Label(frame, text="Contraseña:").grid(row=1, column=0, pady=5, padx=5, sticky='e')

        self.correo_entry = tk.Entry(frame)
        self.contrasena_entry = tk.Entry(frame, show='*')
        self.correo_entry.grid(row=0, column=1, pady=5, padx=5, sticky='w')
        self.contrasena_entry.grid(row=1, column=1, pady=5, padx=5, sticky='w')
        
        #Botones para Iniciar sesión y Registrarse
        tk.Button(frame, text="Iniciar Sesión", command=self.iniciar_sesion).grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Registrarse", command=self.mostrar_registro).grid(row=3, column=0, columnspan=2, pady=5)

        # Ajustar las columnas y filas para que el contenido se expanda
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)

    def iniciar_sesion(self):
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()

        usuario = self.crud_instance.obtener_usuario_por_correo(correo)

        if usuario and usuario[4] == contrasena:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso. ¡Bienvenido!")
        else:
            messagebox.showerror("Inicio de Sesión", "Inicio de sesión fallido. Verifica tu correo y contraseña.")

    def mostrar_registro(self):
        # Crear una nueva ventana para el registro
        registro_window = tk.Toplevel(self.root)
        registro_window.title("Registrarse")

        # Establecer el tamaño de la ventana de registro
        registro_window.geometry("300x350")

        # Crear un marco para centrar los elementos y agregar espacio
        frame = tk.Frame(registro_window, padx=20, pady=10)
        frame.pack(expand=True, fill='both')

        tk.Label(frame, text="Nombres:").grid(row=0, column=0, pady=5, padx=5, sticky='e')
        tk.Label(frame, text="Apellidos:").grid(row=1, column=0, pady=5, padx=5, sticky='e')
        tk.Label(frame, text="Correo:").grid(row=2, column=0, pady=5, padx=5, sticky='e')
        tk.Label(frame, text="Contraseña:").grid(row=3, column=0, pady=5, padx=5, sticky='e')

        nombres_entry = tk.Entry(frame)
        apellidos_entry = tk.Entry(frame)
        correo_entry = tk.Entry(frame)
        contrasena_entry = tk.Entry(frame, show='*')

        nombres_entry.grid(row=0, column=1, pady=5, padx=5, sticky='w')
        apellidos_entry.grid(row=1, column=1, pady=5, padx=5, sticky='w')
        correo_entry.grid(row=2, column=1, pady=5, padx=5, sticky='w')
        contrasena_entry.grid(row=3, column=1, pady=5, padx=5, sticky='w')

        tk.Button(frame, text="Registrar", command=lambda: self.registrarse(nombres_entry, apellidos_entry, correo_entry, contrasena_entry)).grid(row=4, column=0, columnspan=2, pady=5)

        # Ajustar las columnas y filas para que el contenido se expanda
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)
        frame.rowconfigure(4, weight=1)

    def registrarse(self, nombres_entry, apellidos_entry, correo_entry, contrasena_entry):
        nombres = nombres_entry.get()
        apellidos = apellidos_entry.get()
        correo = correo_entry.get()
        contrasena = contrasena_entry.get()

        if not nombres or not apellidos or not correo or not contrasena:
            messagebox.showerror("Error de Registro", "Todos los campos deben ser llenados.")
            return

        self.crud_instance.insertar(nombres, apellidos, correo, contrasena)
        messagebox.showinfo("Registro Exitoso", "¡Usuario registrado con éxito!")



#===============================================================================================================
                                        #EJECUCIÓN DEL PROGRAMA
#===============================================================================================================

if __name__ == "__main__":
    menu = tk.Tk()
    crud_app = CrudApp()
    login_app = LoginApp(menu, crud_app)
    menu.mainloop()