# Elaborato Programmazione di reti - Zammarchi

## Informazioni personali

* Cognome e nome -> Zammarchi Andrea
* Email -> andrea.zammarchi3@studio.unibo.it
* Matricola -> 914652

## Descrizione: traccia n.2

Si immagini di dover realizzare un Web Server in Python per una azienda ospedaliera.
I requisiti del Web Server sono i seguenti:

* Il web server deve consentire l’accesso a più utenti in contemporanea.
* La pagina iniziale deve consentire di visualizzare la lista dei servizi erogati dall’azienda ospedaliera. Per ogni servizio avere un link di riferimento ad una pagina dedicata.
* L’interruzione da tastiera (o da console) dell’esecuzione del web server deve essere opportunamente gestita in modo da liberare la risorsa socket.
* Nella pagina principale dovrà anche essere presente un link per il download di un file pdf da parte del browser
* Come requisito facoltativo si chiede di autenticare gli utenti nella fase iniziale della connessione.

## Specifiche progetto

Questo progetto ha l'obiettivo di creare un Web Server http multithread in Python con login tramite credenziali.
Questo Web Server è di proprietà di una clinica ospedaliera immaginaria: Clinica Zammarchi.\
\
Per poter avviare il server è necessario innanzitutto effettuare l'autenticazione tramite la finestra di accesso che apparirà all'avvio del programma. Se si è nuovi basta digitare un username e una password a piacere e si verrà aggiunti all'archivio degli utenti registrati. Altrimenti si può semplicemente effettuare il login tramite username e password utilizzati in precedenza.\
\
Nella Homepage sono elencati tutti i servizi offerti dalla clinica, ovvero:

* Fisioterapia
* Riabilitazione
* Palestra

Ogni servizio ha inoltre una pagina dedicata con ulteriori informazioni a riguardo.
Nella Homepage in aggiunta è possibile scaricare un file pdf, in questo caso è il manuale dei server http per Python.

## Librerie esterne necessarie

Per poter eseguire l'applicazione è necessario aver installate, oltre alle librerie incluse nel pacchetto Python base, la libreria PIL. Per installare tale libreria si consiglia di utilizzare il package manager [pip](https://pip.pypa.io/en/stable/). 

```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

## Utilizzo

Per avviare il programma aprire la console, spostarsi all'interno della directory 'src' ed eseguire il comando:

```bash
python http_multithread_server.py PORT
```

Il parametro PORT specifica la porta su cui aprire il web server, ma questa è opzionale (default 8080).

Si aprirà quindi una finestra di login dove bisognerà registrarsi/accedere. Una volta eseguito l'accesso il server sarà attivo, quindi aprire il browser e fare la richiesta al seguente link: [http://127.0.0.1:PORT](http://127.0.0.1:8080). Ci si ritroverà nella Homepage e sarà possibile navigare tra le varie pagine.

Per terminare il server basta selezionare la console e digitare Ctrl-C.

## License

[MIT](https://choosealicense.com/licenses/mit/)

```text
MIT License

Copyright (c) 2020 Gianluca Pasolini

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```