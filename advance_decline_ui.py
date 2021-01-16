from tkinter import *
import numpy as np
import requests



class advance_decline_ui(Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.root.title("NSE Advances/Declines")

        self.root.geometry('374x523')
        self.root.resizable(width=FALSE, height=FALSE)


        self.root.iconbitmap('icon.ico')
        self.indices = np.array(['NIFTY 50','NIFTY BANK','NIFTY AUTO','NIFTY FIN SERVICE','NIFTY FMCG','NIFTY IT','NIFTY MEDIA','NIFTY METAL','NIFTY PHARMA',
                   'NIFTY PSU BANK','NIFTY PVT BANK','NIFTY REALTY'])

        self.label_title = Label(self.root, text="Indices Names", padx=10, pady=10, borderwidth=1, relief="solid").grid(row=0, column=0, sticky='EW')
        self.label_title1 = Label(self.root, text="Advances",padx=10, pady=10, borderwidth=1, relief="solid").grid(row=0, column=1, sticky='EW')
        self.label_title2 = Label(self.root, text="Declines",padx=10, pady=10, borderwidth=1, relief="solid").grid(row=0, column=2, sticky='EW')
        self.label_title3 = Label(self.root, text="Unchanged",padx=10, pady=10, borderwidth=1, relief="solid").grid(row=0, column=3, sticky='EW')
        self.exit_button = Button(self.root, text="EXIT", padx=174, pady=10, command=self.root.quit, borderwidth=1, relief="solid")
        self.exit_button.grid(row=13, columnspan=4)



    def buid_tables(self,):
        adv_dec_data = self.get_indices_data()
        for i in range(self.indices.size):
            # print(adv_dec_data[self.indices[i]])
            self.lab = "{}{}".format('label', i)
            self.adv_label = "{}{}".format('advanced', i)
            self.dec_label = "{}{}".format('declined', i)
            self.unchanged_label = "{}{}".format('unchanged', i)

            self.bg = 'green' if int(adv_dec_data[self.indices[i]][0]) > int(adv_dec_data[self.indices[i]][1]) else "red"


            self.lab = Label(self.root, text=self.indices[i], padx=10, pady=10, width=18, borderwidth=1, relief="solid")
            self.adv_label = Label(self.root, text=adv_dec_data[self.indices[i]][0], padx=10, pady=10,  borderwidth=1, bg=self.bg, relief="solid")
            self.dec_label = Label(self.root, text=adv_dec_data[self.indices[i]][1], padx=10, pady=10, borderwidth=1, bg=self.bg, relief="solid")
            self.unchanged_label = Label(self.root, text=adv_dec_data[self.indices[i]][2], padx=10, pady=10, borderwidth=1, relief="solid")

            self.lab.grid(row=i+1, column=0, sticky='EW')
            self.adv_label.grid(row=i + 1, column=1, sticky='EW')
            self.dec_label.grid(row=i + 1, column=2, sticky='EW')
            self.unchanged_label.grid(row=i + 1, column=3, sticky='EW')

            self.root.after(120000, self.buid_tables)

    def get_indices_data(self):
        self.ad_dec_data = {}
        self.adv_dec_url = 'http://www1.nseindia.com/common/json/indicesAdvanceDeclines.json'
        self.headers = {'Accept': '*/*',
                   'Accept-Language': 'en-US,en;q=0.5',
                   'Host': 'www1.nseindia.com',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
                   'X-Requested-With': 'XMLHttpRequest'
                   }
        with requests.session() as session:
            data = session.get(self.adv_dec_url, headers=self.headers)
            indice_data = data.json()
            # print(indice_data)
            for i in indice_data['data']:
                # print(i['indice'])
                if i['indice'] in self.indices:
                    advance = i['advances']
                    declines = i['declines']
                    unchanged = i['unchanged']
                    indice = i['indice']
                    self.ad_dec_data[indice] = [advance,declines,unchanged]
            return self.ad_dec_data


if __name__ == '__main__':
    root = Tk()
    ui = advance_decline_ui(root=root)
    ui.buid_tables()
    ui.mainloop()


