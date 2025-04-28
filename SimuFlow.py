import random
import math
import pandas as pd
from tabulate import tabulate
import pyfiglet

def genera_configurazione():
    """Genera casualmente e calcola i parametri di produzione per il processo."""
    def conf_dipendenti():
        """Genera i parametri per il personale"""
        # Percentuale e generazione casuale del numero totale dei dipendenti, nel range tra 18000 e 50000.
        percentuale_staff_totale = 100
        staff_totale = random.randint(45000, 50000)
        # Generazione casuale della percentuale di assenti per malattia, nel range tra 0 e 20 e calcolo effettivo degli assenti, arrotondato per difetto.        
        percentuale_malattia = random.randint(0, 20)
        staff_malattia = math.floor(staff_totale * (percentuale_malattia / 100))
        # Generazione casuale della percentuale di assenti per corsi di formazione, nel range tra 0 e 5 e calcolo effettivo degli assenti, arrotondato per difetto.
        percentuale_formazione = random.randint(0, 5)
        staff_formazione = math.floor(staff_totale * (percentuale_formazione / 100))
        # Generazione casuale della percentuale di assenti per ferie, nel range tra 0 e 15 e calcolo effettivo degli assenti, arrotondato per difetto.
        percentuale_staff_ferie = random.randint(0, 15)
        staff_ferie = math.floor(staff_totale * (percentuale_staff_ferie / 100))
        # Calcolo dei dipendenti effettivamente impiegabili e relativa percentuale, arrotondato per difetto.
        staff_disponibile = staff_totale - (staff_malattia + staff_formazione + staff_ferie)
        percentuale_disponibili = math.floor((staff_disponibile * percentuale_staff_totale) / staff_totale)
        # Dizionario che contiene tutte le informazioni riguardo al personale.
        dipendenti = {
            "Totale dipendenti": staff_totale,
            "Tasso totale": percentuale_staff_totale,
            "Malattia": staff_malattia,
            "Tasso malattia": percentuale_malattia,
            "Formazione": staff_formazione,
            "Tasso formazione": percentuale_formazione,
            "Ferie": staff_ferie,
            "Tasso ferie": percentuale_staff_ferie,
            "Dipendenti disponibili": staff_disponibile,
            "Tasso disponibili": percentuale_disponibili
        }
        return dipendenti   # Esportazione del dizionario dipendenti alla funzione generale di configurazione.

    def conf_prodotti():
        '''Genera i parametri per i prodotti'''
        # Generazione dei tempi, in secondi, per le varie fasi di fabbricazione di un prodotto: Produzione componenti, Assemblaggio, Controllo qualità e Confezionamento.
        # Questi tempi saranno successivamente sommati e andranno a comporre il tempo unitario di produzione per ogni prodotto.      
        fasi_produzione = {
            "Produzione componenti": {"Smartphone": random.uniform(17, 21), "Ebook": random.uniform(8, 10), "Tablet": random.uniform(15, 17)},
            "Assemblaggio": {"Smartphone": random.uniform(6, 8), "Ebook": random.uniform(4, 5), "Tablet": random.uniform(6, 7)},
            "Controllo qualità": {"Smartphone": random.uniform(3.5, 4.5), "Ebook": random.uniform(2, 2.5), "Tablet": random.uniform(2.5, 3.5)},
            "Confezionamento": {"Smartphone": random.uniform(1.5, 2.5), "Ebook": random.uniform(1.5, 2), "Tablet": random.uniform(1, 1.5)}
        }      
        # Dizionario che racchiude tutte le informazioni riguardo i prodotti.
        prodotti = {
            "Smartphone": {"Quantità": random.randint(100000, 126000)},
            "Ebook": {"Quantità": random.randint(40000, 64000)},
            "Tablet": {"Quantità": random.randint(70000, 83000)}
        }
        return prodotti, fasi_produzione # Esportazione del dizionario alla funzione generale di configurazione.
    
    def conf_macchinari(dipendenti):
        """Genera i parametri per i macchinari"""
        # Percentuale e generazione casuale del numero totale dei macchinari posseduti dall'azienda, nella misura di un terzo rispetto ai dipendenti totali.
        percentuale_macchinari_totale = 100                 # Percentuale dei macchinari totali.
        macchinari_totale = math.floor(dipendenti['Totale dipendenti'] / 3)
        # Generazione casuale della percentuale e calcolo effettivo dei macchinari in manutenzione, nel range tra 0 e 15.
        percentuale_macchinari_manutenzione = random.randint(0, 15)
        macchinari_manutenzione = math.floor(macchinari_totale * (percentuale_macchinari_manutenzione / 100))
        # Calcolo dei macchinari effettivamente impiegabili e relativa percentuale, arrotondata per difetto.
        macchinari_disponibili = macchinari_totale - macchinari_manutenzione
        percentuale_macchinari_disponibili = math.floor((macchinari_disponibili * percentuale_macchinari_totale) / macchinari_totale)
        # Dizionario che racchiude tutte le informazioni riguardo i macchinari.
        macchinari = {
            "Totale macchinari": macchinari_totale,
            "Tasso macchinari totale": percentuale_macchinari_totale,
            "Macchinari in manutenzione": macchinari_manutenzione,
            "Tasso manutenzione":  percentuale_macchinari_manutenzione,
            "Macchinari disponibili": macchinari_disponibili,
            "Tasso disponibili": percentuale_macchinari_disponibili
        }
    
        return macchinari   # Esportazione del dizionario alla funzione generale di configurazione.
    
    # Assegnazione dei dizionari, provenienti dalle sotto funzioni, alle rispettive variabili.
    dipendenti = conf_dipendenti()
    prodotti, fasi_produzione = conf_prodotti()
    macchinari = conf_macchinari(dipendenti)
    # Restituzione delle informazioni al flusso principale del programma.
    return  dipendenti, prodotti, fasi_produzione, macchinari

def calcolo_tempo_produzione(dipendenti, prodotti, fasi_produzione, macchinari):
    '''Calcola i tempi di produzione per unità e tipologia. La generazione del tempo unitario è calcolato anche in base alla disponibilità dei dipendenti e dei macchinari
       e le quantità da produrre sono considerate in base al tempo giornaliero disponibile, concentrando la produzione vero i prodotti più complessi e richiesti'''
    # Calcolo del tempo unitario per prodotto, sommando i tempi delle singole fasi di produzione.
    for prodotto in prodotti:
        prodotti[prodotto]["Tempo Unitario"] = round(sum(fasi_produzione[fase][prodotto] for fase in fasi_produzione), 1)
    # SE NON è DISPONBILE IL 100% DEI DIPENDENTI O DEI MACCHINARI, CALCOLA IL FATTORE DI RIDUZIONE DEL TEMPO UNITARIO DI PRODUZIONE DI OGNI PRODOTTO.
    if dipendenti['Tasso disponibili'] != dipendenti['Tasso totale'] or macchinari['Tasso disponibili'] != macchinari['Tasso macchinari totale']:
        fattore_riduzione= (dipendenti['Dipendenti disponibili'] / dipendenti['Totale dipendenti']) * (macchinari['Macchinari disponibili'] / macchinari['Totale macchinari'])
        # Aggiornamento del tempo unitario di produzione di un prodotto.
        for prodotto, dati in prodotti.items():     
            dati['Tempo Unitario'] = round(dati['Tempo Unitario'] / fattore_riduzione ,1)
    else:
        fattore_riduzione = 0
    # Tempo di una giorata lavorativa (16h) in secondi (57.600).    
    tempo_lavorativo_giornaliero = 16 * 3600
    # Linee di produzione che lavorano contemporaneamente.
    linee_produttive = 38
    # Calcolo del tempo totale di produzione per tipologia, considerando le 38 linee di produzione parallele, arrotondato all'intero più vicino.
    for articolo, dati in prodotti.items():
        dati["Tempo Produzione Prodotto"] = round((dati["Quantità"] * dati["Tempo Unitario"]) / linee_produttive, 2)
    # Calcolo del tempo totale di produzione complessivo.
    temp_tot = sum(p["Tempo Produzione Prodotto"] for p in prodotti.values())
    # CALCOLO IN PROPORZIONE DEL TEMPO DISPONIBILE DA DEDICARE AI PRODOTTI PIù COMPLESSI.
    # Calcolo del tempo giornaliero disponibile in base anche alla capacità delle linee produttive.
    tempo_disponibile_totale = tempo_lavorativo_giornaliero * linee_produttive
    for articolo, dati in prodotti.items():
        # Calcolo del tempo in proporzione.
        tempo_in_proporzione = round((dati['Tempo Produzione Prodotto'] / temp_tot), 3)
        # Calcolo del tempo da dedicare a ciascuna tipologia di prodotto.
        tempo_disponibile_prodotto = tempo_disponibile_totale * tempo_in_proporzione
        # Calcolo della capacità massima giornaliera per tipologia, arrotondata per difetto.
        dati["Capacità Massima Giornaliera"] = math.floor((tempo_disponibile_prodotto) / dati["Tempo Unitario"])
    # Calcolo della capacitò massima giornaliera complessiva.
    cap_g_totale = sum(p["Capacità Massima Giornaliera"] for p in prodotti.values())
    # Esportazione dei risultati.
    return cap_g_totale, temp_tot, tempo_lavorativo_giornaliero, fattore_riduzione, linee_produttive

def conv_tempo(tempo_totale, conv_giorni=True):
        '''Converte i valori dei tempi in ore/minuti e giorni/ore/minuti'''
        if conv_giorni == True:
            '''Conversione in giorni lavorativi'''
            # Il tempo totale in secondi viene diviso per i secondi di una giornata lavorativa di 16 ore, prendendo solo la parte intera.
            giorni = tempo_totale // 57600
            # Calcolo delle ore rimanenti.
            ore_std = (tempo_totale % 57600) // 3600
            # Calcolo dei minuti rimanenti.
            minuti = ((tempo_totale % 3600) // 60)
            # Assegnazione dei risultati ad una stringa da esportare.
            t2 = f"{int(giorni)} giorni lavorativi, {int(ore_std)} ore e {int(minuti)} minuti"
            '''Conversione in ore'''
            # Il tempo in secondi viene nelle ore totali, prendendo solo la parte intera.
            ore_totali = tempo_totale // 3600
            # Calcolo dei minuti rimanenti.
            minuti = (tempo_totale % 3600) // 60
            # Assegnazione dei risultati ad una stringa da esportare.
            t1 = f"{int(ore_totali)} ore e {int(minuti)} minuti"
            tempo = f"{t1} = {t2}"
        else:
            '''Conversione in sole ore'''
            # Il tempo in secondi viene nelle ore totali, prendendo solo la parte intera.
            ore_totali = tempo_totale // 3600
            # Calcolo dei minuti rimanenti.
            minuti = (tempo_totale % 3600) // 60
            # Assegnazione dei risultati ad una stringa da esportare.
            tempo = f"{int(ore_totali)} ore e {int(minuti)} minuti"
        return tempo   # Esporta il valore che contiene la stringa di tempo convertito.

def output_risultati(dipendenti, macchinari, prodotti, cap_g_totale, temp_tot, tempo_lavorativo_giornaliero, fattore_riduzione, linee_produttive):
    # Stampa di ASCII Art, con font style speed, per la stampa del titolo.
    text = "SimuFlow"
    font_style = "speed"
    ascii_art = pyfiglet.figlet_format(text, font=font_style)
    print(ascii_art)
    # Stampa del messaggio dell'inizio dei dati della configurazione e delle ore lavorative.
    print(f"Configurazione Scenario:")
    print(f"\nOre lavorative giornaliere: {conv_tempo(tempo_lavorativo_giornaliero, conv_giorni=False)}\n")
    dipendenti_macchinari_data = {
        "PERSONALE": [
            "Totale dipendenti",
            "Dipendenti in malattia",
            "Dipendenti in formazione",
            "Dipendenti in ferie",
            "Dipendenti impiegabili",
            "MACCHINARI",
            "Totale macchianari",
            "Macchinari in manutenzione",
            "Macchinari impiegabili"
        ],
        "Tasso": [
            f"{dipendenti['Tasso totale']}%",
            f"{dipendenti['Tasso malattia']}%",
            f"{dipendenti['Tasso formazione']}%",
            f"{dipendenti['Tasso ferie']}%",
            f"{dipendenti['Tasso disponibili']}%",
            "",
            f"{macchinari['Tasso macchinari totale']}%",
            f"{macchinari['Tasso manutenzione']}%",
            f"{macchinari['Tasso disponibili']}%"
        ],
        "Unità":[
            dipendenti['Totale dipendenti'],
            dipendenti['Malattia'],
            dipendenti['Formazione'],
            dipendenti['Ferie'],
            dipendenti['Dipendenti disponibili'],
            "",
            macchinari['Totale macchinari'],
            macchinari['Macchinari in manutenzione'],
            macchinari['Macchinari disponibili']
        ]
    }
    # DataFrame dei dati di dipendenti e macchinari.
    dipendenti_macchinari_df = pd.DataFrame(dipendenti_macchinari_data)
    # Stampa dei dati di dipendenti e macchinari, con l'utilizzo del modulo Tabulate definendo lo stile delle tabella, l'allineamento del testo,
    # nascondendo gli indici che stampa pandas e mostrando le intestazioni della tabella.
    print(tabulate(dipendenti_macchinari_df, headers="keys", tablefmt="fancy_grid", colalign=("left", "center", "center"), showindex=False))
    print()
    # Stampa del fattore di riduzione e delle linee di produzione, insieme ad al messaggio che introduce i risultati finali.
    print(f"Fattore di riduzione calcolato: {round(fattore_riduzione, 2)}")
    print(f"Linee di produzione contemporanee: {linee_produttive}")
    print(f"\nIn base ai parametri configurati, i tempi e le quantità del processo produttivo risultano:\n")
    # Preparazione dei risultati alla stampa.
    # Creazione del DataFrame basato sul dizionario prodotti, che è stato trasposto in base all'indice. Le chiavi del dizionario diventano righe e i valori, colonne.
    prodotti_df = pd.DataFrame.from_dict(prodotti, orient="index")
    # Il parametro "Tempo Produzione Prodotto" viene elaborato per la conversione in ore/minuti tramite la funzione conv_temp con flag conv_giorni a False.
    prodotti_df['Tempo Produzione Prodotto'] = prodotti_df['Tempo Produzione Prodotto'].apply(conv_tempo, conv_giorni=False) 
    # Aggiunta della parola "secondi", per mostrare l'output "Tempo Unitario" più verboso. 
    prodotti_df["Tempo Unitario"] = prodotti_df["Tempo Unitario"].apply(lambda x: f"{x} secondi")
    # Aggiunta della parola "unità", per mostrare l'output "Capacità Massima Giornaliera" più verboso. 
    prodotti_df["Capacità Massima Giornaliera"] = prodotti_df["Capacità Massima Giornaliera"].apply(lambda x: f"{x} unità")
    # Stampa dei dati di prodotti, con l'utilizzo del modulo Tabulate definendo lo stile delle tabella, l'allineamento del testo,
    # nascondendo gli indici che stampa pandas e mostrando le intestazioni della tabella.
    print(tabulate(prodotti_df, headers="keys", tablefmt="fancy_grid", colalign=("left", "center", "right", "right", "right")))
    # Stampa di capacità giornaliera complessiva e tempo totale di produzione complessivo, convertito in gg/h/m tramite la funzione conv_tempo, con flag conv_giorni a True.
    print(f"\nCapacità giornaliera complessiva: {cap_g_totale} unità")
    print(f"\nTempo di produzione complessivo: {conv_tempo(temp_tot, conv_giorni=True)}")
    
    '''Codice principale'''
if __name__ == "__main__":                                          
    # Generazione dei dati di coinfigurazione per prodotti, dipendenti e macchinari.
    dipendenti, prodotti, fasi_produzione, macchinari= genera_configurazione()
    # Calcolo della capacità giornaliera complessiva e del tempo totale di produzione
    cap_g_totale, temp_tot, tempo_lavorativo_giornaliero, fattore_riduzione, linee_produttive = calcolo_tempo_produzione(dipendenti, prodotti, fasi_produzione, macchinari)
    # Stampa_risultati.
    output_risultati(dipendenti, macchinari, prodotti, cap_g_totale, temp_tot, tempo_lavorativo_giornaliero, fattore_riduzione, linee_produttive)
    # Input dell'utente, richiesto per uscire dalla sessione.
    input("\nPremi Invio per uscire!")
