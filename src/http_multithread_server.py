''' Esercitazione 5 - Corso di Programmazione di Reti - Università di Bologna'''

#!/bin/env python
import sys, signal
import http.server
import socketserver
import os

# Legge il numero della porta dalla riga di comando
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080
  
web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir(web_dir)

server = socketserver.ThreadingTCPServer(('',port), http.server.SimpleHTTPRequestHandler )

#Assicura che da tastiera usando la combinazione
#di tasti Ctrl-C termini in modo pulito tutti i thread generati
server.daemon_threads = True  
#il Server acconsente al riutilizzo del socket anche se ancora non è stato
#rilasciato quello precedente, andandolo a sovrascrivere
server.allow_reuse_address = True  

#definiamo una funzione per permetterci di uscire dal processo tramite Ctrl-C
def signal_handler(signal, frame):
    print( 'Exiting http server (Ctrl+C pressed)')
    try:
      if( server ):
        server.server_close()
    finally:
      sys.exit(0)

#interrompe l’esecuzione se da tastiera arriva la sequenza (CTRL + C) 
signal.signal(signal.SIGINT, signal_handler)

# entra nel loop infinito
try:
  while True:
    #sys.stdout.flush()
    server.serve_forever()
except KeyboardInterrupt:
  pass

server.server_close()
