from art import tprint  # importujemy funkcję do ładnych napisów
import datetime

def powitanie():
    # Wielki napis na powitanie
    tprint("WITAJ  PONOWNIE", font="bulbhead")
    
    teraz = datetime.datetime.now()
    data_str = teraz.strftime("%d-%m-%Y %H:%M")
    
    print(f"--- Sesja programowania: {data_str} ---")
    
    # Mała logika: lista celów
    cele = []
    while True:
        cel = input("\nCo chcesz dzisiaj ogarnąć? (lub wpisz 'koniec'): ")
        if cel.lower() == 'koniec':
            break
        cele.append(cel)
    
    print("\nTwoja lista zadań na dzisiaj:")
    for i, c in enumerate(cele, 1):
        print(f"{i}. [ ] {c}")
    
    print("\nPowodzenia! Git Bash i VS Code są gotowe.")

if __name__ == "__main__":
    powitanie()