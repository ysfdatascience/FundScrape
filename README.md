#  TEFAS Fon Verisi Scraper

Bu proje, **Türkiye Elektronik Fon Dağıtım Platformu (TEFAS)** üzerinden belirli yatırım fonlarının güncel verilerini otomatik olarak çekmek için geliştirilmiş Python betiğidir.  
Fonların güncel fiyat, getiriler, yatırımcı sayısı, fon toplam değeri gibi temel bilgilerini alır ve `pandas.DataFrame` formatında döndürür.

---

##  Özellikler

- Belirtilen fon kodları için TEFAS sayfalarından verileri çeker.
- Güncel fon fiyatı, kategori bilgileri ve son dönem getirilerini listeler.
- Verileri `pandas.DataFrame` olarak düzenler.

##  Gereksinimler

pip install requests beautifulsoup4 pandas
