# Program ARP Spoofing Detection

## Opis
Ten program jest narzędziem do monitorowania tablicy ARP i wykrywania potencjalnych ataków ARP Spoofing. Działa na systemach operacyjnych Windows oraz Linux, umożliwiając logowanie podejrzanych zdarzeń oraz generowanie pliku logów z informacją o wykrytych atakach.

---

## Funkcjonalności
1. **Ekstrakcja tablicy ARP**
   - Program zbiera informacje z tablicy ARP, wykorzystując polecenie `arp -a`.
   - Obsługa systemów operacyjnych Windows oraz Linux.

2. **Wykrywanie duplikacji adresów MAC**
   - Analiza tablicy ARP w celu wykrycia duplikacji adresów MAC, co może wskazywać na potencjalny atak ARP Spoofing.

3. **Logowanie wyników**
   - W przypadku wykrycia duplikacji adresów MAC generowany jest log z datą, godziną oraz szczegółami podejrzanego zdarzenia.
   - Logi przechowywane są w pliku `log.txt`.

4. **Raportowanie braku zagrożeń**
   - Jeśli podczas analizy nie zostaną wykryte ataki, program odnotowuje to w logach.

---

## Wymagania systemowe
- Python 3.6 lub nowszy
- System operacyjny Windows lub Linux

---

## Instrukcja użycia
1. Uruchom program w terminalu lub wierszu poleceń:
   ```bash
   python nazwa_pliku.py
   ```
2. Program automatycznie wykryje system operacyjny i odpowiednio dostosuje metodę ekstrakcji tablicy ARP.
3. Wyniki analizy zostaną zapisane w pliku `log.txt` w katalogu programu.

---

## Struktura kodu

1. **Funkcja `arp_table_extraction`**
   - Rozpoznaje system operacyjny i wywołuje odpowiednią funkcję ekstrakcji tablicy ARP:
     - `arp_table_extraction_windows()` dla Windows
     - `arp_table_extraction_linux()` dla Linux

2. **Funkcja `arp_table_extraction_windows` i `arp_table_extraction_linux`**
   - Zbiera adresy IP, MAC oraz interfejsy sieciowe z tablicy ARP i zapisuje je w strukturze słownika.

3. **Funkcja `identify_duplication`**
   - Analizuje tablicę ARP w poszukiwaniu duplikacji adresów MAC.
   - Generuje logi, gdy zostanie wykryty potencjalny atak lub gdy tablica ARP jest wolna od zagrożeń.

4. **Funkcja `create_log`**
   - Zapisuje informacje o zdarzeniach do pliku `log.txt` wraz z datą i godziną.

---

## Przykładowy wynik
- **Log w przypadku wykrycia ataku**:
  ```
  12-01-2025 14:35:25 ARP Spoofed! The address is: 192.168.0.101 on interface Ethernet0
  ```

- **Log w przypadku braku zagrożeń**:
  ```
  12-01-2025 14:36:45 ARP Spoofing has not been found
  ```

---

## Uwagi
- Program wymaga odpowiednich uprawnień do uruchomienia polecenia `arp -a`.
- W przypadku wykrycia problemów z kompatybilnością, należy upewnić się, że system operacyjny jest obsługiwany oraz że polecenie `arp -a` działa prawidłowo.

---

## Autor
Program został stworzony jako narzędzie do nauki i monitorowania tablicy ARP w celu wykrywania ataków typu ARP Spoofing - i do testów ("https://github.com/NorbertKowalski80")


