import random
import math
import pandas as pd
#pip install pyarrow

def genera_configurazione():
    """Genera casualmente e calcola i parametri di produzione per il processo."""
    def conf_dipendenti():
        """Genera i parametri per il personale"""
        percentuale_staff_totale = 100                                              # Percentuale dei dipendenti totali.
        staff_totale = random.randint(18000, 22000)                                 # Generazione casuale del numero totale dei dipendenti assunti dell'azienda nel range tra 251 e 500.
        
        percentuale_malattia = random.randint(0, 10)                                # Generazione casuale della percentuale di assenti per malattia nel range tra 0 e 10.
        staff_malattia = math.floor(staff_totale * (percentuale_malattia / 100))    # Calcolo effettivo degli assenti per malattia.
                                                                                    # Il valore, se decimale, è arrotondato per difetto.
        
        percentuale_formazione = random.randint(0, 5)                                   # Generazione casuale della percentuale di assenti per frequentazione corsi di formazione, nel range tra 0 e 5.
        staff_formazione = math.floor(staff_totale * (percentuale_formazione / 100))    # Calcolo effettivo degli assenti per frequentazione corsi,
                                                                                        # il valore, se decimale, è arrotondato per difetto.
                                                                                        
        percentuale_staff_ferie = random.randint(0, 20)                             # Generazione casuale della percentuale di assenti per ferie nel range tra 0 e 20.
        staff_ferie = math.floor(staff_totale * (percentuale_staff_ferie / 100))    # Calcolo effettivo degli assenti per ferie,
                                                                                    # il valore, se decimale, è arrotondato per difetto.

        staff_disponibile = staff_totale - (staff_malattia + staff_formazione + staff_ferie)                # Calcolo dei dipendenti impiegati effettivamente nel processo di produzione.
        percentuale_disponibili = math.floor((staff_disponibile * percentuale_staff_totale) / staff_totale) # Calcolo della percentuale dei dipendenti impiegati effettivamente nel processo di produzione,
                                                                                                            # il valore, se decimale, è arrotondato per difetto.

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
        
        '''generare dei tempi delle diverse fasi di fabbricazione di ogni prodotto: lavorazione, assemblaggio, controllo qualità e confezionamento.
           Questi tempi saranno successivamente sommati e comporranno i tempi unitari di produzione per ogni prodotto'''
              
        fasi_produzione = {
            "Produzione componenti": {"Smartphone": random.uniform(17, 21), "Ebook": random.uniform(8, 10), "Tablet": random.uniform(15, 17)},
            "Assemblaggio": {"Smartphone": random.uniform(6, 8), "Ebook": random.uniform(4, 5), "Tablet": random.uniform(6, 7)},
            "Controllo qualità": {"Smartphone": random.uniform(3.5, 4.5), "Ebook": random.uniform(2, 2.5), "Tablet": random.uniform(2.5, 3.5)},
            "Confezionamento": {"Smartphone": random.uniform(1.5, 2.5), "Ebook": random.uniform(1.5, 2), "Tablet": random.uniform(1, 1.5)}
        }
          
        # Dizionario che racchiude tutte le informazioni riguardo i prodotti.
        prodotti = {                                                          # Generazione casuale delle quantità
            "Smartphone": {"quantità": random.randint(60000, 80000)},   # e dei tempi di produzione per prodotto.             40000000, 55000000
            "Ebook": {"quantità": random.randint(20000, 50000)},        # I tempi, quando generati, verranno arrotondati,     10000000, 15000000
            "Tablet": {"quantità": random.randint(50000, 70000)}        # per praticità, all'intero più vicino fino alla prima cifra decimale,
        }                                                                     # per rendere più semplice la successiva conversione in termini di tempo.     15000000, 30000000
        
        return prodotti, fasi_produzione # Esportazione del dizionario prodotti alla funzione generale di configurazione.
    
    def conf_macchinari(dipendenti):
        """Genera i parametri per i macchinari"""
        percentuale_macchinari_totale = 100                 # Percentuale dei macchinari totali.
        macchinari_totale = math.floor(dipendenti['Totale dipendenti'] / 3)         # Generazione casuale del numero totale dei macchinari posseduti dall'azienda nel range tra 70 e 170.
    
        percentuale_macchinari_manutenzione = random.randint(0, 5)                      # Generazione casuale della percentuale dei macchinari in manutenzione nel range tra 0 e 10.
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
    
'''Codice principale'''
if __name__ == "__main__":                                          
    dipendenti, prodotti, fasi_produzione, macchinari= genera_configurazione()       # Generazione dei dati di configurazione per prodotti, dipendenti e macchianri
    # cap_g_totale, temp_tot = calcolo_tempo_produzione(dipendenti, prodotti, fasi_produzione, macchinari) # Calcolo della capacità giornaliera complessiva e del tempo totale di produzione.
    # stampa_risultati(dipendenti, prodotti, macchinari, cap_g_totale, temp_tot)  # Output dei risultati.
    dipendenti_data = {
        "Descrizione": [
            "Totale dipendenti",
            "Tasso di dipendenti in malattia",
            "Tasso di dipendenti in formazione",
            "Tasso di dipendenti in ferie",
            "Dipendenti impiegabili"
        ],
        "Tasso": [
            "",
            f"{dipendenti['Tasso malattia']}%",
            f"{dipendenti['Tasso formazione']}%",
            f"{dipendenti['Tasso ferie']}%",
            f"{dipendenti['Tasso disponibili']}%"
        ],
        "Unità":[
            dipendenti['Totale dipendenti'],
            dipendenti['Malattia'],
            dipendenti['Formazione'],
            dipendenti['Ferie'],
            dipendenti['Dipendenti disponibili']
        ]
    }
    
    dipendenti_df = pd.DataFrame(dipendenti_data)
    
    print(dipendenti_df.to_string(index=False))    
    
    
    input("\nPremi Invio per uscire!")
