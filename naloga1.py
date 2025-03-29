import cv2 as cv
import numpy as np
import time

def zmanjsaj_sliko(slika, sirina, visina):
    return cv.resize(slika,(sirina,visina))

def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze) -> list: #preveri kje so polja barve koze
    pass


def prestej_piklse_z_barvo_koze(slika, barva_koze) -> int:
    pass

def doloci_barvo_koze(slika,levo_zgoraj,desno_spodaj) -> tuple: #določi barvo kože glede na povprečno barvo v kvadratu
    x1, y1 = levo_zgoraj 
    x2, y2 = desno_spodaj
    podslika = slika[y1:y2, x1:x2]#izrezek slike kjer naj bi bila koza
    povprecje = np.mean(podslika.reshape(-1, 3), axis=0)#izracuna povprecje barve koze v kvadratu, vsaka vrstica stevilo pikslov x 3 barvne vrednosti
    toleranca = 40  # dodatek da pokrije tudi malo svetlejse in temnejse
    spodnja = np.clip(povprecje - toleranca, 0, 255).astype(np.uint8) #clip uporabljen da vrednosti manjse od min postanejo min/vecje od max postanejo max
    zgornja = np.clip(povprecje + toleranca, 0, 255).astype(np.uint8)
    return (spodnja, zgornja) #vrne spodno pa zgorno mejo barve

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
    
        slika = (slika, SIRINA, VISINA) #zmanjsaj sliko
        cv.rectangle(slika, (100, 100), (160, 160), (0, 255, 0), 2) #narisi kvadrat
        cv.putText(slika, "Pritisni 's' za zajem barve koze", (10, 20), #navodila
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv.imshow("Zajem barve koze", slika) #prikazi sliko z kvadratom

        tipka = cv.waitKey(1) #pocakaj na pritisk gumba
        if tipka == ord('s'):
            barva_koze = doloci_barvo_koze(slika, (100, 100), (160, 160)) #določi barvo kože z zajemom barve v kvadratu
            break
        elif tipka == 27:  # ESC
            kamera.release()
            cv.destroyAllWindows()
            exit()

    cv.destroyWindow("Zajem barve koze")

     # Glavna zanka
    while True:
        start = time.time()

        ret, slika = kamera.read()
        if not ret:
            continue

        slika = zmanjsaj_sliko(slika, SIRINA, VISINA)