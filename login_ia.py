import tkinter as tk
from tkinter import messagebox
from crud_ia import CrudApp

class LoginApp:
    def __init__(self, root, crud_instance):
        self.root = root
        self.root.title("Inicio de Sesión")

        self.crud_instance = crud_instance

        tk.Label(root, text="Correo:").grid(row=0, column=0)
        tk.Label(root, text="Contraseña:").grid(row=1, column=0)

        self.correo_entry = tk.Entry(root)
        self.contrasena_entry = tk.Entry(root, show='*')
        self.correo_entry.grid(row=0, column=1)
        self.contrasena_entry.grid(row=1, column=1)

        tk.Button(root, text="Iniciar Sesión", command=self.iniciar_sesion).grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Registrarse", command=self.mostrar_registro).grid(row=3, column=0, columnspan=2)

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

        # Crear etiquetas y campos de entrada para el registro
        tk.Label(registro_window, text="Nombres:").grid(row=0, column=0)
        tk.Label(registro_window, text="Apellidos:").grid(row=1, column=0)
        tk.Label(registro_window, text="Correo:").grid(row=2, column=0)
        tk.Label(registro_window, text="Contraseña:").grid(row=3, column=0)

        nombres_entry = tk.Entry(registro_window)
        apellidos_entry = tk.Entry(registro_window)
        correo_entry = tk.Entry(registro_window)
        contrasena_entry = tk.Entry(registro_window, show='*')

        nombres_entry.grid(row=0, column=1)
        apellidos_entry.grid(row=1, column=1)
        correo_entry.grid(row=2, column=1)
        contrasena_entry.grid(row=3, column=1)

        tk.Button(registro_window, text="Registrar", command=lambda: self.registrarse(nombres_entry, apellidos_entry, correo_entry, contrasena_entry)).grid(row=4, column=0, columnspan=2, pady=5)

    def registrarse(self, nombres_entry, apellidos_entry, correo_entry, contrasena_entry):
        nombres = nombres_entry.get()
        apellidos = apellidos_entry.get()
        correo = correo_entry.get()
        contrasena = contrasena_entry.get()

        self.crud_instance.insertar(nombres, apellidos, correo, contrasena)
        messagebox.showinfo("Registro Exitoso", "¡Usuario registrado con éxito!")

if __name__ == "__main__":
    menu = tk.Tk()
    crud_app = CrudApp()
    login_app = LoginApp(menu, crud_app)
    menu.mainloop()