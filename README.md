# Notable Deaths

This project analyzes daily reported deaths of notable individuals as listed on Wikipedia from **1990 to 2024**.

## 🗂️ Project Structure

- `get_wiki_deaths.py`: Script to collect death records using the Wikipedia API. It fetches daily pages and extracts relevant entries.
- `wiki_deaths.json`: JSON file containing the raw data collected from Wikipedia. Each entry includes name, age (when available), date of death, and a short info string.
- `an_deaths.ipynb`: Jupyter Notebook performing data cleaning and statistical analysis on the collected dataset.

## 📊 Dataset Description

Each record includes:
- **Name** of the deceased
- **Age** (when mentioned)
- **Date of death**
- **Info**: Additional context (e.g., profession, achievements, nationality)

The analysis focuses on:
- Age distribution
- Deaths over time
- Potential for future extraction of attributes like cause of death and profession

## 🚀 Future Work

- Named Entity Recognition (NER) to extract structured attributes (profession, nationality, cause of death)
- Trend analysis by decade or region
- Integration with external datasets (e.g., Wikidata)

## 🛠️ Requirements

- Python 3.x
- pandas, requests, matplotlib, seaborn, etc. (see notebook for details)

## 📌 Notes

The dataset is based on publicly available Wikipedia data. Some entries may be incomplete or inconsistently formatted.
