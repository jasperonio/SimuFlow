import random
import math
import pandas as pd
from tabulate import tabulate
import pyfiglet
#pip install pandas, pyarrow, tabulate, pyfiglet

def genera_configurazione():
    """Genera casualmente e calcola i parametri di produzione per il processo."""
    def conf_dipendenti():
        """Genera i parametri per il personale"""
        percentuale_staff_totale = 100                                              # Percentuale dei dipendenti totali.
        staff_totale = random.randint(18000, 50000)                               # Generazione casuale del numero totale dei dipendenti 
                                                                                    # assunti dell'azienda nel range tra 180000 e 200000.
        
        percentuale_malattia = random.randint(0, 20)                                # Generazione casuale della percentuale di assenti per malattia nel range tra 0 e 20.
        staff_malattia = math.floor(staff_totale * (percentuale_malattia / 100))    # Calcolo effettivo degli assenti per malattia.
                                                                                    # Il valore, se decimale, è arrotondato per difetto.
        
        percentuale_formazione = random.randint(0, 5)                                   # Generazione casuale della percentuale di assenti per frequentazione corsi di formazione, nel range tra 0 e 5.
        staff_formazione = math.floor(staff_totale * (percentuale_formazione / 100))    # Calcolo effettivo degli assenti per frequentazione corsi.
                                                                                        # Il valore, se decimale, è arrotondato per difetto.
                                                                                        
        percentuale_staff_ferie = random.randint(0, 15)                             # Generazione casuale della percentuale di assenti per ferie nel range tra 0 e 15.
        staff_ferie = math.floor(staff_totale * (percentuale_staff_ferie / 100))    # Calcolo effettivo degli assenti per ferie.
                                                                                    # Il valore, se decimale, è arrotondato per difetto.

        staff_disponibile = staff_totale - (staff_malattia + staff_formazione + staff_ferie)                # Calcolo dei dipendenti effettivamente impiegabili.
        percentuale_disponibili = math.floor((staff_disponibile * percentuale_staff_totale) / staff_totale) # Calcolo della percentuale dei dipendenti effettivamente impiegabili.
                                                                                                            # Il valore, se decimale, è arrotondato per difetto.

        # Dizionario che racchiude tutte le informazioni riguardo il personale.
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
        
        '''generazione dei tempi per le diverse fasi di fabbricazione di ogni prodotto.
           Questi tempi saranno successivamente sommati e andranno a comporre il tempo unitaro di produzione per ogni prodotto'''
              
        fasi_produzione = {
            "Produzione componenti": {"Smartphone": random.uniform(17, 21), "Ebook": random.uniform(8, 10), "Tablet": random.uniform(15, 17)},
            "Assemblaggio": {"Smartphone": random.uniform(6, 8), "Ebook": random.uniform(4, 5), "Tablet": random.uniform(6, 7)},
            "Controllo qualità": {"Smartphone": random.uniform(3.5, 4.5), "Ebook": random.uniform(2, 2.5), "Tablet": random.uniform(2.5, 3.5)},
            "Confezionamento": {"Smartphone": random.uniform(1.5, 2.5), "Ebook": random.uniform(1.5, 2), "Tablet": random.uniform(1, 1.5)}
        }
          
        # Dizionario che racchiude tutte le informazioni riguardo i prodotti.
        prodotti = {                                                          # Generazione casuale delle quantità
            "Smartphone": {"Quantità": random.randint(60000, 80000)},   # e dei tempi di produzione per prodotto.             60000, 80000
            "Ebook": {"Quantità": random.randint(20000, 50000)},        # I tempi, quando generati, verranno arrotondati,     20000, 50000
            "Tablet": {"Quantità": random.randint(50000, 70000)}        # per praticità, all'intero più vicino fino alla prima cifra decimale,          50000, 70000
        }                                                                     # per rendere più semplice la successiva conversione in termini di tempo.
        
        return prodotti, fasi_produzione # Esportazione del dizionario prodotti alla funzione generale di configurazione.
    
    def conf_macchinari(dipendenti):
        """Genera i parametri per i macchinari"""
        percentuale_macchinari_totale = 100                 # Percentuale dei macchinari totali.
        macchinari_totale = math.floor(dipendenti['Totale dipendenti'] / 3)         # Generazione casuale del numero totale dei macchinari posseduti dall'azienda nel range tra 70 e 170.
    
        percentuale_macchinari_manutenzione = random.randint(0, 15)                      # Generazione casuale della percentuale dei macchinari in manutenzione nel range tra 0 e 10.
        macchinari_manutenzione = math.floor(macchinari_totale * (percentuale_macchinari_manutenzione / 100))   # Calcolo effettivo dei macchinari in manutenzione.
        
        macchinari_disponibili = macchinari_totale - macchinari_manutenzione            # Calcolo dei macchinari impiegati effettivamente nel processo di produzione.
        percentuale_macchinari_disponibili = math.floor((macchinari_disponibili * percentuale_macchinari_totale) / macchinari_totale) # Calcolo della percentuale totale dei macchinari impiegati effettivamente 
                                                                                                                                      # nel processo di produzione, il valore, se decimale, è arrotondato per difetto.
        # Dizionario che racchiude tutte le informazioni riguardo i macchinari.
        macchinari = {
            "Totale macchinari": macchinari_totale,
            "Tasso macchinari totale": percentuale_macchinari_totale,
            "Macchinari in manutenzione": macchinari_manutenzione,
            "Tasso manutenzione":  percentuale_macchinari_manutenzione,
            "Macchinari disponibili": macchinari_disponibili,
            "Tasso disponibili": percentuale_macchinari_disponibili
        }
    
        return macchinari   # Esportazione del dizionario macchinari alla funzione generale di configurazione.
    
    dipendenti = conf_dipendenti()
    prodotti, fasi_produzione = conf_prodotti()
    macchinari = conf_macchinari(dipendenti)
    
    return  dipendenti, prodotti, fasi_produzione, macchinari     # Vengono richiamate le sotto funzioni specifiche, ritornando le informazioni 
                                                                  # di dipendenti, prodotti e macchinari per le successive elaborazioni.
    
def conv_tempo(tempo_totale, conv_giorni=True):
        '''Converte i valori dei tempi in ore/minuti e giorni/ore/minuti'''
                  
        if conv_giorni == True:
            '''Conversione in giorni lavorativi'''
            giorni = int(tempo_totale // 57600)
            ore_std = int(tempo_totale % 57600) // 3600
            minuti = int((tempo_totale % 3600) // 60)
            t2 = f"{int(giorni)} giorni lavorativi, {int(ore_std)} ore e {int(minuti)} minuti"
            
            '''Conversione in ore'''
            ore_totali = tempo_totale // 3600
            minuti = (tempo_totale % 3600) // 60
            t1 = f"{int(ore_totali)} ore e {int(minuti)} minuti"
            
            # tempo = f"{t1} = {t2} = {t3}"
            tempo = f"{t1} = {t2}"
        
        else:
            ore_totali = tempo_totale // 3600
            minuti = (tempo_totale % 3600) // 60
            tempo = f"{int(ore_totali)} ore e {int(minuti)} minuti"
                    
        return tempo   # Esporta il valore che contiene la stringa di tempo convertito in ore/minuti.

def calcolo_tempo_produzione(dipendenti, prodotti, fasi_produzione, macchinari):
    '''Calcola i tempi di produzione per unità e tipologia. La generazione del tempo unitario è calcolato anche in base alla disponibilità dei dipendenti e dei macchinari'''
    
    for prodotto in prodotti:                                                                                                  # Calcolo del tempo unitario per prodotto,
        prodotti[prodotto]["Tempo Unitario"] = round(sum(fasi_produzione[fase][prodotto] for fase in fasi_produzione), 1)      # sommando i tempi delle singole fasi di produzione
    
    # SE NON è DISPONBILE IL 100% DEI DIPENDENTI O DEI MACCHINARI, CALCOLA IL FATTORE DI RIDUZIONE DEL TEMPO UNITARIO DI PRODUZIONE DI OGNI PRODOTTO.
    
    if dipendenti['Tasso disponibili'] != dipendenti['Tasso totale'] or macchinari['Tasso disponibili'] != macchinari['Tasso macchinari totale']:
        fattore_riduzione= (dipendenti['Dipendenti disponibili'] / dipendenti['Totale dipendenti']) * (macchinari['Macchinari disponibili'] / macchinari['Totale macchinari'])
        for prodotto, dati in prodotti.items():     
            dati['Tempo Unitario'] = round(dati['Tempo Unitario'] / fattore_riduzione ,1) # Aggiornamento del tempo unitario di produzione di un prodotto
        
    tempo_lavorativo_giornaliero = 16 * 3600                                                                # tempo di una gionrata lavorativa (16h) in secondi (57.600).
    linee_produttive = 38
    for articolo, dati in prodotti.items():                                                         # Calcola il tempo totale di produzione per prodotto,
        dati["Tempo Produzione Prodotto"] = round((dati["Quantità"] * dati["Tempo Unitario"]) / linee_produttive, 1)     # considerando le 38 linee di produzione parallele,
                                                                                                    # arrotondato all'intero più vicino.
 
    # calcolare la capacità giornaliera massima in base al tempo totale 
    for articolo, dati in prodotti.items():                                                                             # Calcolo della capacità massima giornaliera per prodotto,
        dati["Capacità Massima Giornaliera"] = math.floor(((tempo_lavorativo_giornaliero) / dati["Tempo Unitario"]) * linee_produttive) # considerando le 38 linee di produzione parallele,
                                                                                                                        # arrotondato per difetto all'intero più vicino.
           
    cap_g_totale = sum(p["Capacità Massima Giornaliera"] for p in prodotti.values())                                # Calcolo della capacità giornaliera totale.
    
    temp_tot = sum(p["Tempo Produzione Prodotto"] for p in prodotti.values())                                                 # Calcolo del tempo totale di produzione e conversione in giorni/ore/minuti.
    
    return cap_g_totale, temp_tot, tempo_lavorativo_giornaliero, fattore_riduzione, linee_produttive   # Esportazione della capacità giornaliera totale e del tempo totale di produzione.

def stampa_risultati(dipendenti, prodotti, macchinari, cap_g_totale, temp_tot, tempo_lavorativo_giornaliero, fattore_riduzione, linee_produttive):
    print(f"\nConfigurazione Scenario:")
    print(f"Ore lavorative giornaliere: {conv_tempo(tempo_lavorativo_giornaliero, conv_giorni=False)}")
    print(f"\nPERSONALE:")
    print(f"Totale dipendenti: {dipendenti['Totale dipendenti']}")
    print(f"Tasso di dipendenti in malattia: {dipendenti['Tasso malattia']}% = {dipendenti['Malattia']} unità")
    print(f"Tasso di dipendenti in formazione: {dipendenti['Tasso formazione']}% = {dipendenti['Formazione']} unità")
    print(f"Tasso di dipendenti in ferie: {dipendenti['Tasso ferie']}% = {dipendenti['Ferie']} unità")
    print(f"Dipendenti effettivamente impiegati: {dipendenti['Tasso disponibili']}% = {dipendenti['Dipendenti disponibili']} unità")
    print(f"\nMACCHINARI:")
    print(f"Totale macchinari: {macchinari['Totale macchinari']}")
    print(f"Tasso macchinari in manutenzione: {macchinari['Tasso manutenzione']}% = {macchinari['Macchinari in manutenzione']}")
    print(f"Macchinari impiegati: {macchinari['Tasso disponibili']}% = {macchinari['Macchinari disponibili']} unità")
    print(f"\nFattore di riduzione calcolato: {round(fattore_riduzione, 2)}")
    print(f"Linee di produzione contemporanee = {linee_produttive}")
    print(f"\nIn base ai parametri configurati, i tempi e le quantità dei prodotti risultano:")
    print(f"\nPRODOTTI:")
    for prodotto, dati in prodotti.items():
        print(f"{prodotto} - Quantità da produrre: {dati['Quantità']} unità - Tempo per unità: {dati['Tempo Unitario']} secondi - Capacità giornaliera: {dati['Capacità Massima Giornaliera']} unità - Tempo totale: {conv_tempo(dati['Tempo Produzione Prodotto'], conv_giorni=False)}")
        
    print(f"\nCapacità giornaliera complessiva: {cap_g_totale} unità")
    print(f"\nTempo complessivo di produzione: {temp_tot}")

def output_risultati(dipendenti, macchinari, prodotti, cap_g_totale, temp_tot, tempo_lavorativo_giornaliero, fattore_riduzione, linee_produttive):
    
    # Stampa di ASCII Art, con font style speed, per la stampa del titolo dell'applicazione.
    text = "SimuFlow"
    font_style = "speed"
    ascii_art = pyfiglet.figlet_format(text, font=font_style)
    print(ascii_art)
    # 
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
    
    dipendenti_macchinari_df = pd.DataFrame(dipendenti_macchinari_data)
    print(tabulate(dipendenti_macchinari_df, headers="keys", tablefmt="fancy_grid", colalign=("left", "center", "center"), showindex=False))
    print()
    
    print(f"Fattore di riduzione calcolato: {round(fattore_riduzione, 2)}")
    print(f"Linee di produzione contemporanee: {linee_produttive}")
    print(f"\nIn base ai parametri configurati, i tempi e le quantità del processo produttivo risultano:\n")
    
    prodotti_df = pd.DataFrame.from_dict(prodotti, orient="index") 
    prodotti_df['Tempo Produzione Prodotto'] = prodotti_df['Tempo Produzione Prodotto'].apply(conv_tempo, conv_giorni=False) 
    prodotti_df["Tempo Unitario"] = prodotti_df["Tempo Unitario"].apply(lambda x: f"{x} secondi")
    prodotti_df["Capacità Massima Giornaliera"] = prodotti_df["Capacità Massima Giornaliera"].apply(lambda x: f"{x} unità")
    print(tabulate(prodotti_df, headers="keys", tablefmt="fancy_grid", colalign=("left", "center", "right", "right", "right")))
    
    print(f"\nCapacità giornaliera complessiva: {cap_g_totale} unità")
    print(f"\nTempo di produzione complessivo: {conv_tempo(temp_tot, conv_giorni=True)}")
    

'''Codice principale'''
if __name__ == "__main__":                                          
    dipendenti, prodotti, fasi_produzione, macchinari= genera_configurazione()       # Generazione dei dati di configurazione per prodotti, dipendenti e macchianri
    cap_g_totale, temp_tot, tempo_lavorativo_giornaliero, fattore_riduzione, linee_produttive = calcolo_tempo_produzione(dipendenti, prodotti, fasi_produzione, macchinari) # Calcolo della capacità giornaliera complessiva e del tempo totale di produzione.
    # stampa_risultati(dipendenti, prodotti, macchinari, cap_g_totale, temp_tot, tempo_lavorativo_giornaliero, fattore_riduzione, linee_produttive)  # Output dei risultati.
    output_risultati(dipendenti, macchinari, prodotti, cap_g_totale, temp_tot, tempo_lavorativo_giornaliero, fattore_riduzione, linee_produttive)
    input("\nPremi Invio per uscire!")
