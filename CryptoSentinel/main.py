import requests
import time

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# --- TUTAJ PYTAMY UŻYTKOWNIKA O CELE ---
print("Ustawienia alertów:")
cel_sprzedazy = float(input("Przy jakiej cenie chcesz SPRZEDAĆ? (np. 70000): "))
cel_kupna = float(input("Przy jakiej cenie chcesz KUPIĆ? (np. 60000): "))

print("\nUruchamiam Crypto Sentinela... (Naciśnij Ctrl+C, aby zatrzymać)")
print("-" * 30)

try:
    while True:
        try:
            odpowiedz = requests.get(url)
            dane = odpowiedz.json()
            
            cena = float(dane['price'])
            teraz = time.strftime("%H:%M:%S")
            
            print(f"[{teraz}] BTC: {cena:.2f} $")

            # --- UŻYWAMY TWOICH WYBRANYCH CELÓW ---
            if cena >= cel_sprzedazy:
                print("ALERT: SPRZEDAWAJ! 🤑")
            
            if cena <= cel_kupna:
                print("ALERT: KUPUJ! 📉")
            
        except Exception as e:
            print(f"Błąd połączenia: {e}")

        time.sleep(5)

except KeyboardInterrupt:
    print("\nZatrzymano program. Do zobaczenia!")