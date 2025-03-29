import cv2 as cv
import numpy as np
import time

def zmanjsaj_sliko(slika, sirina, visina):
    pass

def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze) -> list: #preveri kje so polja barve koze
    pass


def prestej_piklse_z_barvo_koze(slika, barva_koze) -> int:
    pass

def doloci_barvo_koze(slika,levo_zgoraj,desno_spodaj) -> tuple: #določi barvo kože glede na povprečno barvo v kvadratu
    pass

if __name__ == '__main__':
    kamera = cv.VideoCapture(0)

    SIRINA = 260
    VISINA = 300
    VELIKOST_SKATLE = (int(SIRINA * 0.2), int(VISINA * 0.2)) #skatla za iskanje nastavljena na 20% velikosti

    barva_koze = None

    # Zajemi prvo sliko
    while True:
        ret, slika = kamera.read() #zajemi sliko iz kamere
        if not ret:
            continue
    

        cv.rectangle(slika, (100, 100), (160, 160), (0, 255, 0), 2) #narisi kvadrat
        cv.putText(slika, "Pritisni 's' za zajem barve koze", (10, 20), #navodila
        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv.imshow("Zajem barve koze", slika) #prikazi sliko z kvadratom

        tipka = cv.waitKey(1) #pocakaj na pritisk gumba
        if tipka == ord('s'):

            break
        elif tipka == 27:  # ESC
            kamera.release()
            cv.destroyAllWindows()
            exit()

    cv.destroyWindow("Zajem barve koze")
