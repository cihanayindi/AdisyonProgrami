from PyQt5 import uic

with open('OnayKutusu.py', 'w', encoding='utf-8') as fout:

    uic.compileUi('OnayKutusuUI.ui',fout)