import pandas as pd
from pathlib import Path

def extract_sales(csv_path: Path) -> list:
    df = pd.read_csv(csv_path)
    df["Faturamento"] = df["Quantidade"] * df["Venda"]
    dicts = df.to_dict(orient="records")
    return dicts

def transform_df(dicts: list) -> dict:
    dicts_by_category = {}
    for d in dicts:
        category = d["Categoria"]
        if category not in dicts_by_category:
            dicts_by_category[category] = []
        dicts_by_category[category].append(d)
    
    return dicts_by_category

def calculate_sales_category(dicts_by_category: dict) -> dict:
    sales_by_category = {}
    for category, items in dicts_by_category.items():
        total_sales = sum(item["Faturamento"] for item in items)
        sales_by_category[category] = total_sales
    return sales_by_category

def save_to_csv(sales_by_category: dict, output_path: Path) -> None:
    df = pd.DataFrame(list(sales_by_category.items()), columns=["Categoria", "Faturamento"])
    df.to_csv(output_path, index=False)

def main(input_path: Path, output_path: Path) -> None:
    dicts = extract_sales(input_path)
    dicts_by_category = transform_df(dicts)
    sales_by_category = calculate_sales_category(dicts_by_category)
    save_to_csv(sales_by_category, output_path)

if __name__ == "__main__":
    input_path = Path(r"C:\Users\Finance-SingleSoftwa\OneDrive\studyspace\jornada-de-dados\aula07\db\sales.csv")
    output_path = Path(r"C:\Users\Finance-SingleSoftwa\OneDrive\studyspace\jornada-de-dados\aula07\db\report.csv")
    main(input_path, output_path)
