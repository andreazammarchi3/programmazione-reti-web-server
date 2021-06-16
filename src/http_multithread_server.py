'''
    Elaborato Programmazione di Reti:
            a.a. 2020/2021
            Zammarchi Andrea
            Matricola: 914652
            Traccia 2
            Web Server per clinica con login
'''

#!/bin/env python
import sys, signal
import http.server
import socketserver
import os

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json


# Funzione che viene richiamata quando viene eseguito il login con successo
# Avvia il web server
def UserAuthenticated():
    # Legge il numero della porta specificata da riga di comando
    # Se non viene specificata, di default è 8080
    if sys.argv[1:]:
      port = int(sys.argv[1])
    else:
      port = 8080
    
    # Specifica il percorso del file index.html, in particolare si trova dentro la directory 'web'
    web_dir = os.path.join(os.path.dirname(__file__), 'web')
    os.chdir(web_dir)
    
    # Specifica il tipo di server, ovvero http multithread
    server = socketserver.ThreadingTCPServer(('',port), http.server.SimpleHTTPRequestHandler )
    
    # Assicura che da tastiera usando la combinazione
    # di tasti Ctrl-C termini in modo pulito tutti i thread generati
    server.daemon_threads = True  
    
    # Acconsente al riutilizzo del socket anche se ancora non è stato
    # rilasciato quello precedente, andandolo a sovrascrivere
    server.allow_reuse_address = True  
    
    # Funzione che arresta il server alla pressione dei tasti Ctrl-C
    def signal_handler(signal, frame):
        print( 'Exiting http server (Ctrl+C pressed)')
        try:
          if( server ):
            server.server_close()
        finally:
          sys.exit(0)
        
    # Interrompe l’esecuzione se da tastiera arriva la sequenza Ctrl-C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Loop infinito di funzione del server
    try:
        while True:
            server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    # Se per qualche motivo si interrompe il ciclo, chiudo il server
    server.server_close()

# Stringhe contenenti i codici di alcuni colori
blue = '#259bca'
red = '#bf404c'
light_red = '#f2b5bb'

# Design e layout della finestra di login
w = Tk()
w.geometry('350x500')
w.title('Clinica Zammarchi Login')
w.iconbitmap('web/images/logo.ico')
w.resizable(0,0)
Frame(w, width = 350, height = 500, bg = blue).place(x = 0, y = 0)
Frame(w, width = 250, height = 400, bg = 'white').place(x = 50, y = 50)

# Label e Textbox per username
l1 = Label(w, text = 'Username', bg = 'white')
l = ('consolas', 13)
l1.config(font = 1)
l1.place(x = 80, y = 200)
e1 = Entry(w, width = 20, border = 1)
e1.config(font = l)
e1.place(x = 80, y = 230)

# Label e Textbox per password
l2 = Label(w, text = 'Password', bg = 'white')
l = ('consolas', 13)
l2.config(font = 1)
l2.place(x = 80, y = 280)
e2 = Entry(w, width = 20, border = 1, show = '*')
e2.config(font = l)
e2.place(x = 80, y = 310)

# Immagine dell'user
imagea=Image.open("web/images/log.png")
imageb= ImageTk.PhotoImage(imagea)
label1 = Label(image=imageb,
               border=0,
               
               justify=CENTER)
label1.place(x=115, y=50)

# Funzione per il login dell'utente:
#   - se username e password sono nuovi -> registrato il nuovo utente ed effettuato l'accesso
#   - se username riconosciuto ma password diversa -> concede un nuovo tentativo
#   - se username e password sono riconosciuti -> accesso effettuato
def login(usr):
    uN = e1.get()
    pW = e2.get()

    if uN in usr.keys():
        if pW == usr[uN]:
            answer = messagebox.askyesno("LOGIN RIUSCITO", "BENTORNATO/A. Vuoi avviare il web server? ")
            if answer:
                w.destroy()
                UserAuthenticated()
        else:
            messagebox.showwarning("LOGIN FAILED","        PASSWORD ERRATA        ")
            return
    else:
        usr[uN] = pW
        answer = messagebox.askyesno("ACCOUNT CREATO", "BENVENUTO/A. Vuoi avviare il web server? ")
        if answer:
            w.destroy()
            UserAuthenticated()
    writeUsers(usr)
    return

# Tenta di leggere il dizionario degli utenti memorizzato in un file json
def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Scrive le modifiche effettuate al dizionario degli utenti sul file json
# Se tale file non esiste, viene creato
def writeUsers(usr):
    with open("users.json", "w") as f:
            json.dump(usr, f)

# Funzione eseguita alla pressione del pulsante di login
def cmd():
    users = readUsers()
    login(users)
    
# Funzione che crea il pulsante di login, specificando il suo style e il suo comando
def btn(x, y, text, ecolor, lcolor):
    # Funzioni che definisco l'animazione del pulsante
    def on_entera(e):
        myButton1['background'] = ecolor
        myButton1['foreground'] = lcolor
    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground'] = ecolor
    
    # Specifica le dimensioni, colore, forma e comando del pulsante
    myButton1 = Button(w, text = text,
                width = 20,
                height = 2,
                fg = ecolor,
                border = 0,
                bg = lcolor,
                activeforeground = lcolor,
                activebackground = ecolor,
                command = cmd)
    
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)
    
# Richiama la funzione per creare il pulsante di login
btn(100,375,'LOGIN',light_red,red)
    
# Entro nel loop della GUI
w.mainloop()