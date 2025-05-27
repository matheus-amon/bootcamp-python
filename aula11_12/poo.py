import pandas as pd

class CSVProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.filtered_df = None

    def read_file_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filter_df_by_invoice(self, invoice_id):
        self.filtered_df = self.df[self.df['invoice_id'] == invoice_id]
    
    def show_df(self, is_filtered_df = False):
        if is_filtered_df:
            print(self.filtered_df)
            separate_outputs()
        else:
            print(self.df)
            separate_outputs()

    def filter_notna_rows(self, column, is_filtered_df=False):
        df = self.filtered_df if is_filtered_df else self.df
        try:
            filtered = df[df[column].notna()]
            if is_filtered_df:
                self.filtered_df = filtered
            else:
                self.df = filtered
        except Exception as e:
            raise ValueError(f"Não foi possível filtrar, verifique os argumentos: {e}")

def separate_outputs():
    print(' ')
    print("=====#####=====#####=====#####=====#####=====#####=====#####=====")