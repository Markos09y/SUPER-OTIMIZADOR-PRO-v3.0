import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Função para executar comandos
def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Funções principais

def limpar_temp():
    run_cmd("del /s /f /q %temp%\\*.*")
    run_cmd("del /s /f /q C:\\Windows\\Temp\\*.*")
    messagebox.showinfo("OK", "Arquivos temporários removidos")


def flush_dns():
    run_cmd("ipconfig /flushdns")
    messagebox.showinfo("OK", "DNS limpo")


def reparar_sistema():
    run_cmd("sfc /scannow")


def dism_repair():
    run_cmd("dism /online /cleanup-image /restorehealth")


def otimizar_disco():
    run_cmd("defrag C: /O")
    messagebox.showinfo("OK", "Disco otimizado")


def modo_automatico():
    limpar_temp()
    flush_dns()
    reparar_sistema()
    otimizar_disco()
    messagebox.showinfo("FINALIZADO", "Manutenção completa concluída")

# Interface
root = tk.Tk()
root.title("SUPER OTIMIZADOR PRO v3.0")
root.geometry("500x400")
root.configure(bg="#111")

# Título
label = tk.Label(root, text="SUPER OTIMIZADOR PRO", fg="lime", bg="#111", font=("Arial", 16, "bold"))
label.pack(pady=20)

# Botões
btn1 = tk.Button(root, text="Limpar Temporários", width=30, command=limpar_temp)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Limpar DNS", width=30, command=flush_dns)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Reparar Sistema (SFC)", width=30, command=reparar_sistema)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Reparo Avançado (DISM)", width=30, command=dism_repair)
btn4.pack(pady=5)

btn5 = tk.Button(root, text="Otimizar Disco", width=30, command=otimizar_disco)
btn5.pack(pady=5)

btn6 = tk.Button(root, text="Modo Automático", width=30, command=modo_automatico, bg="green", fg="white")
btn6.pack(pady=20)

# Rodar
root.mainloop()
