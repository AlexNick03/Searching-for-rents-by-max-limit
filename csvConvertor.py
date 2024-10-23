import pandas as pd


class Convertor:
    def __init__(self, my_dict, file_name):
        self.my_dict = my_dict
        self.file_name = file_name
        self.df=pd.DataFrame(my_dict)
        self.df.to_csv(f'./Liste_csv/{self.file_name}.csv',sep=';', encoding='utf8', index=True)
