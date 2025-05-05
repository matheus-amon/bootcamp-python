from etl import pipeline
from pathlib import Path

if __name__ == "__main__":
    path = Path(r"C:\Users\Finance-SingleSoftwa\OneDrive\studyspace\jornada-de-dados\aula08\db")

    formats = []
    for i in range(3):
        format = input("Escolha o formato de saída (csv, json, parquet): ")
        if format:
            formats.append(format)
    
    pipeline(path, formats)
