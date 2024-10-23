import tkinter as tk
from tkinter import ttk
from scraper import Scrapper
BACKGROUND_COLOR = 'SlateGray2'
FONT= ('Arial', 15, "bold")
from csvConvertor import Convertor
class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.scraped_data={}
        self.window.title('Rent finder Romania')
        self.window.geometry()
        self.window.configure(bg=BACKGROUND_COLOR, padx=10, pady=25)
        self.create_labels()
        self.create_entry()
        self.create_buttons()
        self.window.mainloop()

    def create_labels(self):
        self.city_name = ttk.Label(self.window, text='Numele orasului', background=BACKGROUND_COLOR,
                                       foreground="black", font=FONT, justify='center')
        self.city_name.grid(row=0, column=0)
        self.maximum_rent=ttk.Label(self.window, text='Chiria maxima', background=BACKGROUND_COLOR,foreground="black",
                                    font=FONT, justify='center')
        self.maximum_rent.grid(row=0, column=2,padx=10)
        self.csv_name=ttk.Label(self.window, text='Numele fisierului', background=BACKGROUND_COLOR, foreground="black",
                                font=FONT, justify='center')
        self.csv_name.grid(row=3, column=0)
    def create_entry(self):
        self.city_name_ent = ttk.Entry(self.window)
        self.city_name_ent.grid(row=1, column=0)
        self.maximum_rent_ent = ttk.Entry(self.window)
        self.maximum_rent_ent.grid(row=1, column=2)
        self.csv_name_ent = ttk.Entry(self.window, state='disabled')
        self.csv_name_ent.grid(row=4, column=0)

    def create_buttons(self):
        self.cauta=ttk.Button(text='Cauta', command= lambda: self.get_data())
        self.cauta.grid(row=2, column=1, pady=10)
        self.save_button=ttk.Button(text="Save Csv",state='disabled' ,command=lambda: self.save_as_csv(), width=20)
        self.save_button.grid(row=3, column=2, pady=10, rowspan=2)

    def get_data(self):
        self.scraped_data=Scrapper(city_name=self.city_name_ent.get(), max_rent=self.maximum_rent_ent.get()).data_dict
        self.save_button.configure(state='active')
        self.csv_name_ent.configure(state='active')

    def save_as_csv(self):
        Convertor(self.scraped_data,self.csv_name_ent.get())
        self.save_button.configure(state='disabled')
        self.csv_name_ent.configure(state='disabled')

