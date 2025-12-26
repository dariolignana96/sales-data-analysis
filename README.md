# 📊 Sales Data Analysis Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

Progetto di analisi dati end-to-end che simula un dataset di vendite retail, esegue operazioni di pulizia e aggregazione, e produce insight visivi sulle performance dei prodotti.

Il progetto dimostra competenze in **Data Generation**, **Exploratory Data Analysis (EDA)** e **Business Intelligence reporting**.

---

## 🚀 Caratteristiche Principali

- **Synthetic Data Generation**: Modulo per la creazione procedurale di dataset di vendita realistici (utile per testare pipeline senza dati sensibili).
- **Data Processing**: Manipolazione dati con **Pandas** (raggruppamenti, calcoli statistici, gestione tipi).
- **Visualization**: Creazione di grafici pronti per la reportistica con **Matplotlib** e **Seaborn**.
- **Automazione**: Script unico per generare dati, analizzarli ed esportare i grafici.

## 📂 Struttura del Repository

```
├── data/               # Cartella di output per il dataset CSV generato
├── notebooks/          # Jupyter Notebook per esplorazione interattiva
├── scripts/            # Script Python di produzione (ETL + Visualizzazione)
├── visualizations/     # Output grafici (report .png/.jpg)
└── README.md           # Documentazione
```

## 📊 Esempio di Output

Lo script genera report visivi per identificare i prodotti top-seller e la distribuzione geografica delle vendite.

![Sales Analysis Output](visualizations/sales_by_product.jpg)
*(Esempio di grafico generato: Vendite medie per categoria di prodotto con barre di errore)*

## 🛠️ Installazione e Utilizzo

1. **Clona il repository:**
   ```
   git clone https://github.com/YOUR_USERNAME/sales-data-analysis.git
   cd sales-data-analysis
   ```

2. **Installa le dipendenze:**
   ```
   pip install pandas numpy matplotlib seaborn
   ```

3. **Esegui la pipeline:**
   Poiché il dataset non è incluso nel repo (per best practice), esegui lo script per **generare i dati** e **creare l'analisi** in un colpo solo:
   ```
   python scripts/analysis.py
   ```
   *Questo comando creerà il file `data/sales_data.csv` e salverà i grafici in `visualizations/`.*

## 📈 Possibili sviluppi futuri

- [ ] Aggiunta di analisi temporale (Time Series Forecasting).
- [ ] Creazione di una dashboard interattiva con Streamlit.
- [ ] Containerizzazione con Docker.

---

### 📬 Contatti

Per domande o collaborazioni, apri una Issue o una Pull Request in questo repository.
---