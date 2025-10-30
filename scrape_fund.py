from bs4 import BeautifulSoup
import pandas as pd
import requests

data_columns = [
    "Son Fiyat (TL)",
    "Günlük Getiri (%)",
    "Pay (Adet)",
    "Fon Toplam Değer (TL)",
    "Kategorisi",
    "Kategori Derecesi",
    "Yatırımcı Sayısı",
    "Pazar Payı",
    "Son 1 Ay Getirisi",
    "Son 3 Ay Getirisi",
    "Son 6 Ay Getirisi",
    "Son 1 Yıl Getirisi",
]
def scrape_fund(*args):

    final_list = []
    fon_adı_final = []

    for fund in args:

        try:
            page = requests.get(fr"https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod={fund.upper()}", verify = False, timeout = 10)
        except requests.exceptions.RequestException as e:
            print(f"Hata {e}")
            page = None

        soup = BeautifulSoup(markup = page.content, features="html.parser")

        fon_adı = soup.find(class_ = "main-indicators").find("h2").text.strip()
        fon_adı_final.append(fund.upper() + "-" + fon_adı) #  fon kodu + fon adı

        try:
            # son güncel bilgiler
            top_list =list(
                 item.text\
                .strip()\
                .split("\n\n")[1] for item in soup.find(class_ = "main-indicators").find_all("li"))
        except IndexError as e:
            print(f"Hata: fon listesinde fiyat bilgileri açıklanmayan fonlar bulunmaktadır - {fund.upper()} - {e}")

        # getiriler
        price_indicators = list(
             item.text\
            .strip()\
            .split("\n")[1] for item in soup.find(class_ = "price-indicators").find_all("li"))

        final_list.append(list(top_list) + list(price_indicators))

    # dataframe dönüşümü
    df_final = pd.DataFrame(data = final_list, index = fon_adı_final, columns = data_columns)


    return df_final
