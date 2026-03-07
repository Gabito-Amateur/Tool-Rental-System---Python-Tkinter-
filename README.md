# Tool Rental System
**Author:** Gabriel Alejandro Suarez 
**Course:** Programming - Code 213023  
**University:** Universidad Nacional Abierta y a Distancia (UNAD)  
**Exercise:** 5 - Tool Rental System

---

## Description
A desktop application built with Python and Tkinter that manages tool rentals. The system tracks tool check-out and return times, and automatically calculates the rental cost based on hours used.

---

## Project Structure

```
project/
│
├── credenciales.py   # Usuario class with private credentials and login validation
├── login.py          # Login window (Tkinter GUI)
├── funciones.py      # HerramientaAlquiler class with core business logic
└── main.py           # Entry point - connects login with the main system
```

---

## Files Overview

### `credenciales.py`
Contains the `Usuario` class with:
- Private attributes `_usuario` and `_password`
- Method `validar(usuario_ingresado, password_ingresado)` that returns `True` if credentials match

### `funciones.py`
Contains the `HerramientaAlquiler` class with:
- Private attributes: `_id_herramienta`, `_hora_salida`, `_hora_retorno`, `_tarifa_hora`
- `registrar_salida(horaS)` — stores the departure time
- `registrar_retorno(horaR)` — stores the return time
- `calcular_costo(horaR)` — calculates total rental cost based on hours elapsed
- `obtener_id()` — returns the tool ID

### `login.py`
Tkinter login window that:
- Validates credentials using the `Usuario` class
- Opens the main system on successful login
- Shows an error message on failed login

### `main.py`
Main system window that:
- Displays a registration form (Tool ID, Departure Time, Rate per Hour)
- Lists all registered tools
- Allows selecting a tool and registering its return time
- Automatically calculates and displays the total cost

---

## How to Run

```bash
python main.py
```

---

## Login Credentials

| Field    | Value         |
|----------|---------------|
| Username | programacion  |
| Password | programacion  |

---

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)

---

## Time Format

Times are entered in **HH:MM** (24-hour format) using Spinbox controls.  
The return time must be greater than the departure time, otherwise the system will display an error.
