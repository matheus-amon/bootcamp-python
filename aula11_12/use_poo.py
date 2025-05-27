from poo import CSVProcessor 

file_path1 = "./aula11_12/example.csv"
csv1 = CSVProcessor(file_path=file_path1)
csv1.read_file_csv()
csv1.show_df()

file_path2 = "./aula11_12/example.csv"
csv2 = CSVProcessor(file_path=file_path2)
csv2.read_file_csv()
csv2.filter_df_by_invoice(1005)
csv2.show_df(is_filtered_df=True)

file_path3 = "./aula11_12/example.csv"
csv3 = CSVProcessor(file_path=file_path3)
csv3.read_file_csv()

