import mysql.connector
from tkinter import Tk, Label, Button, StringVar, Entry, messagebox, simpledialog

class CrudApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IA-App")

        self.connection = mysql.connector.connect(
            host='localhost',
            database='app_ia',
            user='root',
            password=''
        )

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.root, text="LOGIN - CRUD", font=("Tahoma", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.nombres_var = StringVar()
        self.apellidos_var = StringVar()
        self.correo_var = StringVar()
        self.contrasena_var = StringVar()

        Label(self.root, text="Nombres:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        Entry(self.root, textvariable=self.nombres_var).grid(row=1, column=1, padx=10, pady=5)

        Label(self.root, text="Apellidos:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        Entry(self.root, textvariable=self.apellidos_var).grid(row=2, column=1, padx=10, pady=5)
        
        Label(self.root, text="Correo:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        Entry(self.root, textvariable=self.correo_var).grid(row=3, column=1, padx=10, pady=5)

        Label(self.root, text="Contraseña:").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        Entry(self.root, textvariable=self.contrasena_var, show="*").grid(row=4, column=1, padx=10, pady=5)

        Button(self.root, text="Insertar", command=self.insertar).grid(row=5, column=0, columnspan=2, pady=10)
        Button(self.root, text="Seleccionar", command=self.seleccionar).grid(row=6, column=0, columnspan=2, pady=10)
        Button(self.root, text="Actualizar", command=self.actualizar).grid(row=7, column=0, columnspan=2, pady=10)
        Button(self.root, text="Eliminar", command=self.eliminar).grid(row=8, column=0, columnspan=2, pady=10)

    def validar_letras(self, input_text):
        return input_text.isalpha()

    #CRUD => Create Read Update Delete

    def insertar(self):
        nombres = self.nombres_var.get()
        apellidos = self.apellidos_var.get()
        correo = self.correo_var.get()
        contrasena = self.contrasena_var.get()

        if self.validar_letras(nombres) and self.validar_letras(apellidos):
            cursor = self.connection.cursor()
            sql_insert = "INSERT INTO usuarios (nombres, apellidos,correo, contraseña) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_insert, (nombres, apellidos, correo, contrasena))
            self.connection.commit()
            messagebox.showinfo("Éxito", "Registro insertado!")
        else:
            messagebox.showwarning("Advertencia", "Los campos de Nombres y Apellidos deben contener solo letras.")

    def seleccionar(self):
        cursor = self.connection.cursor()
        sql_select = "SELECT * FROM usuarios"
        cursor.execute(sql_select)
        records = cursor.fetchall()

        result = ""
        for row in records:
            result += f"ID = {row[0]}, Nombres = {row[1]}, Apellidos = {row[2]}, Correo = {row[3]}, Contraseña = {row[4]}\n\n"

        messagebox.showinfo("Usuarios", result)

    def actualizar(self):
        idusuario = simpledialog.askinteger("Actualizar Usuario", "Ingrese el ID del usuario a actualizar:", parent=self.root)
        if idusuario is not None:
            nuevos_nombres = simpledialog.askstring("Actualizar Usuario", "Nuevos Nombres:", parent=self.root)
            nuevos_apellidos = simpledialog.askstring("Actualizar Usuario", "Nuevos Apellidos:", parent=self.root)
            if self.validar_letras(nuevos_nombres) and self.validar_letras(nuevos_apellidos):
                cursor = self.connection.cursor()
                sql_update = "UPDATE usuarios SET nombres = %s, apellidos = %s WHERE idusuarios = %s"
                cursor.execute(sql_update, (nuevos_nombres, nuevos_apellidos, idusuario))
                self.connection.commit()
                messagebox.showinfo("Éxito", "Registro actualizado!")
            else:
                messagebox.showwarning("Advertencia", "Los campos de Nombres y Apellidos deben contener solo letras.")

    def eliminar(self):
        id_usuario = simpledialog.askinteger("Eliminar Usuario", "Ingrese el ID del usuario que desea eliminar:")
        if id_usuario is not None:
            cursor = self.connection.cursor()
            sql_delete = "DELETE FROM usuarios WHERE idusuarios = %s"
            cursor.execute(sql_delete, (id_usuario,))
            self.connection.commit()
            messagebox.showinfo("Éxito", "Registro eliminado!")

if __name__ == "__main__":
    root = Tk()
    app = CrudApp(root)

    # Centrar la ventana y establecer su tamaño
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    root.mainloop()