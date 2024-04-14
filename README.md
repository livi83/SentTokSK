# SentTokSK

## Úvod
SentTokSK je knižnica jazyku Python navrhnutá na tokenizáciu vstupného textu na vety pomocou regulárnych výrazov. Poskytuje flexibilný a prispôsobiteľný spôsob rozdelenia textu na jednotlivé vety, pričom zvláda rôznu interpunkciu a skratky.

## Použitie
1. Importujte triedu SentTokSK do vášho skriptu v jazyku Python.
2. Vytvorte inštanciu triedy SentTokSK.
3. Zavolajte metódu `tokenize()` tejto inštancie a ako argument jej predajte text, ktorý chcete tokenizovať.
4. Metóda vráti zoznam viet extrahovaných z vstupného textu.

Príklad:
```python
from sent_tok_sk import SentTokSK

tokenizer = SentTokSK()
text = "To je veta. Toto je druhá veta.“"
sentences = tokenizer.tokenize(text)
print(sentences)
