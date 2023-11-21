import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from crud_ia import CrudApp
from chatbot_ia import mostrar_ventana_chat
from ttkthemes import ThemedStyle

class LoginApp:
    def __init__(self, root, crud_instance):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("500x450")
        self.crud_instance = crud_instance

        original_bg_image = Image.open("F:/Desarrollo_IA/images/ANOTHER.jpg")
        resized_bg_image = original_bg_image.resize((500, 450), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_bg_image)

        frame = ttk.Frame(root)
        frame.pack(expand=True, fill='both')

        bg_label = tk.Label(frame, image=self.bg_photo)
        bg_label.place(relwidth=1, relheight=1)

        self.logo_image = tk.PhotoImage(file="F:/Desarrollo_IA/images/bot3.png")

        self.logo_label = tk.Label(frame, image=self.logo_image)
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(frame, text="Correo:", font=('Arial', 10, 'bold')).grid(row=1, column=0, pady=5, padx=5, sticky='e')
        tk.Label(frame, text="Contraseña:", font=('Arial', 10, 'bold')).grid(row=2, column=0, pady=5, padx=5, sticky='e')

        style = ThemedStyle(frame)
        style.configure('TEntry', padding=5, relief="flat", fieldbackground="#d3d3d3")  # Ajusta el color de fondo según tu diseño

        self.correo_entry = ttk.Entry(frame, width=25, style="TEntry")  
        self.contrasena_entry = ttk.Entry(frame, show='*', width=25, style="TEntry")  
        self.correo_entry.grid(row=1, column=1, pady=5, padx=5, sticky='w')
        self.contrasena_entry.grid(row=2, column=1, pady=5, padx=5, sticky='w')

        tk.Button(frame, text="Iniciar Sesión", command=self.iniciar_sesion, bg='lightblue', font=('Arial', 12, 'bold')).grid(row=3, column=0, columnspan=2, pady=10)  
        tk.Button(frame, text="Registrarse", command=self.mostrar_registro, bg='lightblue', font=('Arial', 12, 'bold')).grid(row=4, column=0, columnspan=2, pady=5)

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)
        frame.rowconfigure(4, weight=1)

    def iniciar_sesion(self):
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()

        usuario = self.crud_instance.obtener_usuario_por_correo(correo)

        if usuario and usuario[4] == contrasena:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso. ¡Bienvenido!")
            self.root.destroy()
            mostrar_ventana_chat()
        else:
            messagebox.showerror("Inicio de Sesión", "Inicio de sesión fallido. Verifica tu correo y contraseña.")

    def mostrar_registro(self):
        registro_window = tk.Toplevel(self.root)
        registro_window.title("Registro de Usuario")
        RegistroApp(registro_window, self)

class RegistroApp:
    def __init__(self, root, login_instance):
        self.root = root
        self.root.title("Registro de Usuario")
        self.root.geometry("600x650")
        self.login_instance = login_instance

        frame = ttk.Frame(root)
        frame.pack(expand=True, fill='both')

        original_bg_image = Image.open("F:/Desarrollo_IA/images/ANOTHER.jpg")
        resized_bg_image = original_bg_image.resize((600, 650), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_bg_image)
        
        bg_label = tk.Label(frame, image=self.bg_photo)
        bg_label.place(relwidth=1, relheight=1)

        try:
            self.logo_image = tk.PhotoImage(file="F:/Desarrollo_IA/images/login2.png")
            logo_label = tk.Label(frame, image=self.logo_image)
            logo_label.grid(row=0, column=0, columnspan=2, pady=2)
        except Exception as e:
            print(f"Error al cargar la imagen del logo en la ventana de registro: {e}")

        tk.Label(frame, text="Nombres:", font=('Arial', 10, 'bold')).grid(row=1, column=0, pady=5, padx=5, sticky='e')
        tk.Label(frame, text="Apellidos:", font=('Arial', 10, 'bold')).grid(row=2, column=0, pady=5, padx=5, sticky='e')
        tk.Label(frame, text="Correo:", font=('Arial', 10, 'bold')).grid(row=3, column=0, pady=5, padx=5, sticky='e')
        tk.Label(frame, text="Contraseña:", font=('Arial', 10, 'bold')).grid(row=4, column=0, pady=5, padx=5, sticky='e')

        style = ThemedStyle(frame)
        style.configure('TEntry', padding=5, relief="flat", fieldbackground="#d3d3d3")  # Ajusta el color de fondo según tu diseño

        nombres_entry = ttk.Entry(frame, width=25, style="TEntry")  
        apellidos_entry = ttk.Entry(frame, width=25, style="TEntry")  
        correo_entry = ttk.Entry(frame, width=25, style="TEntry")  
        contrasena_entry = ttk.Entry(frame, show='*', width=25, style="TEntry")  

        nombres_entry.grid(row=1, column=1, pady=5, padx=5, sticky='w')
        apellidos_entry.grid(row=2, column=1, pady=5, padx=5, sticky='w')
        correo_entry.grid(row=3, column=1, pady=5, padx=5, sticky='w')
        contrasena_entry.grid(row=4, column=1, pady=5, padx=5, sticky='w')

        tk.Button(frame, text="Registrar", command=lambda: self.registrarse(nombres_entry, apellidos_entry, correo_entry, contrasena_entry), bg='lightblue', font=('Arial', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=10)  

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)
        frame.rowconfigure(4, weight=1)
        frame.rowconfigure(5, weight=1)

    def registrarse(self, nombres_entry, apellidos_entry, correo_entry, contrasena_entry):
        nombres = nombres_entry.get()
        apellidos = apellidos_entry.get()
        correo = correo_entry.get()
        contrasena = contrasena_entry.get()

        if not nombres or not apellidos or not correo or not contrasena:
            messagebox.showerror("Error de Registro", "Todos los campos deben ser llenados.")
            return

        self.login_instance.crud_instance.insertar(nombres, apellidos, correo, contrasena)
        messagebox.showinfo("Registro Exitoso", "¡Usuario registrado con éxito!")

if __name__ == "__main__":
    menu = tk.Tk()
    crud_app = CrudApp()
    login_app = LoginApp(menu, crud_app)

    style = ThemedStyle(menu)
    style.set_theme("radiance")

    menu.mainloop()