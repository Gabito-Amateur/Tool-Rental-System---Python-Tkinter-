#Librerias
import tkinter as tk
from tkinter import messagebox
from funciones import HerramientaAlquiler
from login import iniciar_login
from datetime import datetime

#Funcion principal del sistema
def abrir_sistema():
    herramientas = []

    ventana = tk.Tk()
    ventana.title("Tool Rental System")
    ventana.geometry("700x450")
    ventana.resizable(False, False)
    ventana.configure(bg="#f0f4f8")

    # Titulo
    frame_titulo = tk.Frame(ventana, bg="#1a73e8")
    frame_titulo.pack(fill=tk.X)
    tk.Label(frame_titulo, text="TOOL RENTAL SYSTEM", bg="#1a73e8", fg="white",
             font=("Arial", 14, "bold")).pack(pady=12)

    # Frame principal
    frame_main = tk.Frame(ventana, bg="#f0f4f8")
    frame_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # ---- SECCION IZQUIERDA ----
    frame_izq = tk.Frame(frame_main, bg="#f0f4f8")
    frame_izq.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))

    tk.Label(frame_izq, text="Register Tool", bg="#f0f4f8",
             font=("Arial", 11, "bold")).pack(anchor="w")

    tk.Label(frame_izq, text="Tool ID:", bg="#f0f4f8").pack(anchor="w", pady=(10, 0))
    entry_id = tk.Entry(frame_izq, width=25, relief=tk.FLAT, bg="#e8f0fe", font=("Arial", 10))
    entry_id.pack(ipady=5)

    tk.Label(frame_izq, text="Departure Time:", bg="#f0f4f8").pack(anchor="w", pady=(10, 0))
    frame_spin_salida = tk.Frame(frame_izq, bg="#f0f4f8")
    frame_spin_salida.pack(anchor="w")
    spin_hora_salida = tk.Spinbox(frame_spin_salida, from_=0, to=23, width=4, format="%02.0f")
    spin_hora_salida.pack(side=tk.LEFT)
    tk.Label(frame_spin_salida, text=":", bg="#f0f4f8").pack(side=tk.LEFT)
    spin_min_salida = tk.Spinbox(frame_spin_salida, from_=0, to=59, width=4, format="%02.0f")
    spin_min_salida.pack(side=tk.LEFT)

    tk.Label(frame_izq, text="Rate per Hour ($):", bg="#f0f4f8").pack(anchor="w", pady=(10, 0))
    entry_tarifa = tk.Entry(frame_izq, width=25, relief=tk.FLAT, bg="#e8f0fe", font=("Arial", 10))
    entry_tarifa.pack(ipady=5)

    def registrar_herramienta():
        id_tool = entry_id.get().strip()
        hora_s = f"{spin_hora_salida.get()}:{spin_min_salida.get()}"
        tarifa = entry_tarifa.get().strip()

        if not id_tool or not tarifa:
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            tarifa = float(tarifa)
        except ValueError:
            messagebox.showerror("Error", "Rate must be a number")
            return

        herramienta = HerramientaAlquiler(id_tool, hora_s, tarifa)
        herramientas.append(herramienta)
        spin_hora_salida.delete(0, tk.END)
        spin_hora_salida.insert(0, "00")
        spin_min_salida.delete(0, tk.END)
        spin_min_salida.insert(0, "00")
        lista.insert(tk.END, f"{id_tool} - Departure: {hora_s} - Rate: ${tarifa:.2f}/hr")
        entry_id.delete(0, tk.END)
        entry_tarifa.delete(0, tk.END)
        messagebox.showinfo("Success", "Tool registered successfully")

    tk.Button(frame_izq, text="Register Tool", command=registrar_herramienta,
              bg="#1a73e8", fg="white", font=("Arial", 10, "bold"),
              relief=tk.FLAT, cursor="hand2").pack(pady=15, ipady=5, fill=tk.X)

    # ---- SECCION DERECHA ----
    frame_der = tk.Frame(frame_main, bg="#f0f4f8")
    frame_der.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    tk.Label(frame_der, text="Registered Tools", bg="#f0f4f8",
             font=("Arial", 11, "bold")).pack(anchor="w")

    lista = tk.Listbox(frame_der, width=50, height=10, relief=tk.FLAT, bg="#e8f0fe")
    lista.pack(pady=(10, 10))

    tk.Label(frame_der, text="Return Time:", bg="#f0f4f8").pack(anchor="w")
    frame_spin_retorno = tk.Frame(frame_der, bg="#f0f4f8")
    frame_spin_retorno.pack(anchor="w")
    spin_hora_retorno = tk.Spinbox(frame_spin_retorno, from_=0, to=23, width=4, format="%02.0f")
    spin_hora_retorno.pack(side=tk.LEFT)
    tk.Label(frame_spin_retorno, text=":", bg="#f0f4f8").pack(side=tk.LEFT)
    spin_min_retorno = tk.Spinbox(frame_spin_retorno, from_=0, to=59, width=4, format="%02.0f")
    spin_min_retorno.pack(side=tk.LEFT)

    label_costo = tk.Label(frame_der, text="Total Cost: -", bg="#f0f4f8",
                           font=("Arial", 11, "bold"), fg="#1a73e8")
    label_costo.pack(pady=10)

    def registrar_retorno():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Please select a tool from the list")
            return

        indice = seleccion[0]
        herramienta = herramientas[indice]
        hora_r = f"{spin_hora_retorno.get()}:{spin_min_retorno.get()}"

        herramienta.registrar_retorno(hora_r)
        costo = herramienta.calcular_costo(hora_r)


        if costo is None:
            messagebox.showerror("Error", "Return time must be greater than departure time")
            return

        label_costo.config(text=f"Total Cost: ${costo:.2f}")
        messagebox.showinfo("Success", f"Total cost: ${costo:.2f}")
        spin_hora_retorno.delete(0, tk.END)
        spin_hora_retorno.insert(0, "00")
        spin_min_retorno.delete(0, tk.END)
        spin_min_retorno.insert(0, "00")

    tk.Button(frame_der, text="Register Return & Calculate", command=registrar_retorno,
              bg="#1a73e8", fg="white", font=("Arial", 10, "bold"),
              relief=tk.FLAT, cursor="hand2").pack(ipady=5, fill=tk.X)

    ventana.mainloop()


iniciar_login(abrir_sistema)