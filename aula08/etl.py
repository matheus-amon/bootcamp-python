from pathlib import Path
from schema import SalesSchema
from decorators import log_execution, measure_time
from pandera import check_output

import pandas as pd
import glob
import os

@log_execution
@measure_time
@check_output(schema=SalesSchema)
def extract_data(path: Path) -> pd.DataFrame:
    json_files: list = glob.glob(os.path.join(path, "*.json"))

    if not json_files:
        raise FileNotFoundError(f"Nenhum arquivo JSON encontrado no diretório: {path}")

    dfs: list = []
    for file in json_files:
        df = pd.read_json(file)
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)
    return df

@log_execution
@measure_time
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df['Receita'] = df['Quantidade'] * df['Venda']
    df['Receita'] = df['Receita'].astype(float)
    df['Produto'] = df['Produto'].astype(str)
    df['Categoria'] = df['Categoria'].astype(str)
    df['Quantidade'] = df['Quantidade'].astype(int)
    df['Venda'] = df['Venda'].astype(float)
    df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')
    return df

@log_execution
@measure_time
def load_data(df: pd.DataFrame, formats: list) -> None:
    results_path = Path("aula08/db/results")
    results_path.mkdir(parents=True, exist_ok=True)  # Garante que o diretório existe

    for format in formats:
        if format == 'csv':
            df.to_csv(results_path / "output.csv", index=False)
        elif format == 'json':
            df.to_json(results_path / "output.json", 
                       orient='records', lines=True, force_ascii=False,
                       date_format='iso', default_handler=str)
        elif format == 'parquet':
            df.to_parquet(results_path / "output.parquet", index=False)
        elif format == '':
            print("Formato vazio, não será salvo.")
        else:
            print(f"Formato {format} não suportado.")

@log_execution
@measure_time
def pipeline(path: Path, formats: list) -> None:
    df = extract_data(path)
    df = transform_data(df)
    load_data(df, formats)
