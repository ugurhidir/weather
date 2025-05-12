import requests
import json # Aslında requests.json() bunu bizim için halledecek

# API Anahtarını buraya yapıştır (Kimseyle paylaşma!)
API_KEY = "99a3a396d24f3cbf1557344b3d713924"
# Temel API URL'si (Current Weather Data için)
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(sehir_adi):
    # API isteği için parametreleri hazırla
    params = {
        'q': sehir_adi,      # Aranacak şehir
        'appid': API_KEY,    # Senin API anahtarın
        'units': 'metric',   # Sıcaklığı Santigrat olarak almak için ('imperial' Fahrenheit için)
        'lang': 'tr'         # Bilgileri Türkçe almak için (destekleniyorsa)
    }

    try:
        print(f"\n{sehir_adi} için hava durumu bilgileri alınıyor...")
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()  # HTTP hata kodu varsa (4xx veya 5xx) hata fırlat

        # Yanıtı JSON olarak işle
        hava_durumu_json = response.json()
        return hava_durumu_json

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Hata: API anahtarı geçersiz veya yetkilendirme sorunu.")
        elif response.status_code == 404:
            print(f"Hata: '{sehir_adi}' şehri bulunamadı.")
        else:
            print(f"HTTP hatası oluştu: {http_err} - {response.text}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Bağlantı hatası oluştu: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"İstek zaman aşımına uğradı: {timeout_err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Bir hata oluştu: {err}")
        return None
    except json.JSONDecodeError:
        print("Hata: API'den gelen yanıt JSON formatında değil.")
        return None

def display_weather_data(data, sehir_adi):
    if not data:
        return # Eğer veri yoksa (hata oluştuysa) bir şey gösterme

    # JSON verisinden istediğimiz bilgileri ayıklayalım
    # OpenWeatherMap API dokümantasyonuna bakarak doğru anahtarları bulmalısın!
    try:
        ana_bilgi = data.get('weather', [{}])[0] # Hava durumu açıklaması ve ikonu list içinde geliyor
        hava_aciklamasi = ana_bilgi.get('description', 'Bilgi yok').capitalize()
        # icon_kodu = ana_bilgi.get('icon') # İkonu da alabilirsin, web uygulamasında gösterilebilir

        temp_bilgisi = data.get('main', {})
        sicaklik = temp_bilgisi.get('temp', 'N/A')
        hissedilen_sicaklik = temp_bilgisi.get('feels_like', 'N/A')
        nem_orani = temp_bilgisi.get('humidity', 'N/A')

        ruzgar_bilgisi = data.get('wind', {})
        ruzgar_hizi = ruzgar_bilgisi.get('speed', 'N/A') # m/s cinsinden

        gorus_mesafesi = data.get('visibility', 'N/A') # Metre cinsinden

        print(f"\n--- {sehir_adi.capitalize()} Hava Durumu ---")
        print(f"Durum: {hava_aciklamasi}")
        print(f"Sıcaklık: {sicaklik}°C")
        print(f"Hissedilen Sıcaklık: {hissedilen_sicaklik}°C")
        print(f"Nem: %{nem_orani}")
        print(f"Rüzgar Hızı: {ruzgar_hizi} m/s")
        if gorus_mesafesi != 'N/A':
            print(f"Görüş Mesafesi: {gorus_mesafesi / 1000} km")
        print("-----------------------------")

    except (IndexError, KeyError, TypeError) as e:
        print(f"Hava durumu verisi parse edilirken bir hata oluştu: {e}")
        print("Alınan veri yapısı beklenenden farklı olabilir.")
        # print("Ham Veri:", data) # Hata ayıklama için ham veriyi yazdırabilirsin

# Ana program akışı
if __name__ == "__main__":
    while True:
        sehir = input("Hava durumunu öğrenmek istediğiniz şehri girin (Çıkmak için 'q'): ").strip()
        if sehir.lower() == 'q':
            print("Uygulamadan çıkılıyor...")
            break
        if not sehir:
            print("Lütfen bir şehir adı girin.")
            continue

        weather_json_data = get_weather_data(sehir)
        display_weather_data(weather_json_data, sehir)