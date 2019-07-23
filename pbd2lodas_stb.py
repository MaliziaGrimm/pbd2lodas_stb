from flask import Flask
from flask import request
import os, webbrowser
from flask import render_template
from shutil import copyfile
from fpdf import FPDF


app = Flask(__name__)

#@app.route('/')
#def homepage():
#    return render_template('index.html')
# Block ok !

@app.route('/')
@app.route('/index.html', methods=['POST', 'GET'])
def index():
##############################################################
### Anlage der Stammdaten (Konfiguration) für die Erfassung
### Beraternummer, Mandant und Lohnarten mit Text = 5 für Stunden, 5 für Betrag
##############################################################

    if request.method == 'POST':
        fileziel=open("daten/basisdaten.txt","w")
        # schreiben in Datei für Basisdaten
        fileziel.write(request.form['form_berater']+"|"+request.form['form_mandant']+"|")
        if (request.form['loa_ns1'] != "" and request.form['loa_ts1'] != "") and (request.form['loa_ns1'] != "Nummer") :
            fileziel.write(request.form['loa_ns1']+"|"+request.form['loa_ts1']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_ns2'] != "" and request.form['loa_ts2'] != "") and (request.form['loa_ns2'] != "Nummer"):
            fileziel.write(request.form['loa_ns2']+"|"+request.form['loa_ts2']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_ns3'] != "" and request.form['loa_ts3'] != "" ) and (request.form['loa_ns3'] != "Nummer"):
            fileziel.write(request.form['loa_ns3']+"|"+request.form['loa_ts3']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_ns4'] != "" and request.form['loa_ts4'] != "") and (request.form['loa_ns4'] != "Nummer"):
            fileziel.write(request.form['loa_ns4']+"|"+request.form['loa_ts4']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_ns5'] != "" and request.form['loa_ts5'] != "") and (request.form['loa_ns5'] != "Nummer"):
            fileziel.write(request.form['loa_ns5']+"|"+request.form['loa_ts5']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_nb1'] != "" and request.form['loa_tb1'] != "") and (request.form['loa_nb1'] != "Nummer"):
            fileziel.write(request.form['loa_nb1']+"|"+request.form['loa_tb1']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_nb2'] != "" and request.form['loa_tb2'] != "") and (request.form['loa_nb2'] != "Nummer"):
            fileziel.write(request.form['loa_nb2']+"|"+request.form['loa_tb2']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_nb3'] != "" and request.form['loa_tb3'] != "") and (request.form['loa_nb3'] != "Nummer"):
            fileziel.write(request.form['loa_nb3']+"|"+request.form['loa_tb3']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_nb4'] != "" and request.form['loa_tb4'] != "") and (request.form['loa_nb4'] != "Nummer"):
            fileziel.write(request.form['loa_nb4']+"|"+request.form['loa_tb4']+"|")
        else:
            fileziel.write("nicht|buchen|")
        if (request.form['loa_nb5'] != "" and request.form['loa_tb5'] != "") and (request.form['loa_nb5'] != "Nummer"):
            fileziel.write(request.form['loa_nb5']+"|"+request.form['loa_tb5'])
        else:
            fileziel.write("nicht|buchen")
        fileziel.close()
    else:
        pass
    return render_template('index.html')


webbrowser.open('http://localhost:1701')

if __name__ =='__main__':
    app.run(port=1701, debug=False)