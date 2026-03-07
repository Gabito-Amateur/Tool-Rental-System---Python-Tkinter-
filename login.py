import tkinter as tk
from tkinter import messagebox
from credenciales import Usuario

def iniciar_login(callback_exito):
    usuario = Usuario()
    
    ventana = tk.Tk()
    ventana.title("User Login")
    ventana.geometry("300x400")
    ventana.resizable(False, False)
    ventana.configure(bg="#f0f4f8")

    # Titulo
    frame_titulo = tk.Frame(ventana, bg="#1a73e8", width=300, height=50)
    frame_titulo.pack(fill=tk.X)
    tk.Label(frame_titulo, text="USER LOGIN", bg="#1a73e8", fg="white",
             font=("Arial", 14, "bold")).pack(pady=12)

    # Icono usuario
    tk.Label(ventana, text="👤", font=("Arial", 40), bg="#f0f4f8").pack(pady=15)

    # Campo username
    tk.Label(ventana, text="Username", bg="#f0f4f8", fg="#555",
             font=("Arial", 9)).pack(anchor="w", padx=50)
    entry_usuario = tk.Entry(ventana, width=25, font=("Arial", 11),
                             relief=tk.FLAT, bg="#e8f0fe")
    entry_usuario.pack(ipady=6, padx=50, pady=(0, 10))

    # Campo password
    tk.Label(ventana, text="Password", bg="#f0f4f8", fg="#555",
             font=("Arial", 9)).pack(anchor="w", padx=50)
    entry_password = tk.Entry(ventana, width=25, font=("Arial", 11),
                              relief=tk.FLAT, bg="#e8f0fe", show="*")
    entry_password.pack(ipady=6, padx=50, pady=(0, 20))

    # Funcion login
    def intentar_login():
        user = entry_usuario.get()
        pwd = entry_password.get()
        if usuario.validar(user, pwd):
            ventana.destroy()
            callback_exito()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    # Boton login
    tk.Button(ventana, text="LOG IN", command=intentar_login,
              bg="#1a73e8", fg="white", font=("Arial", 11, "bold"),
              width=20, relief=tk.FLAT, cursor="hand2").pack(ipady=6)

    ventana.mainloop()