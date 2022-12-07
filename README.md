# EksploracjaProjekt
## Potrzebne Narzędzia
Do uruchomenia poniższych programów będą potrzebne następujące narządzia:
*Google Chrome
*chromedriver

## Pobieranie narządzi:
Narzędzia można pobrać z poniższych stron zachowując zgodność wersji
https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_linux64.zip

Na systemach operacyjnych typu debian można użyć poniższych komend:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
wget https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_linux64.zip
sudo dpkg -i google-chrome-stable_current_amd64.deb
google-chrome --version
unzip chromedriver_linux64.zip
realpath chromedriver_linux64.zip
```
Wyswietlona sciezke do pliku chromedriver należy edytowac w pliku bidfax.py i carinfo.py przypisujac do zmiennej PATH

```python

PATH = "/twoja_sciezka/do_pliku/chromedriver"

```

## Uruchomienie
Należy uruchomiec po kolei nastepujace pliki
```bash
./bidfax.py
./carinfo.py
./format_data.py
```
Rezultatem powinno byc wygenerowanie pliku .csv

## Napotkane problemy
Strona bidfax wykrywa scrapowanie dlatego zostało dodane randomow generowane oóźnienie. (bez tego zcrapowanie jest blokowane z danego addresu IP)
