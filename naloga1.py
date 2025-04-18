import cv2 as cv
import numpy as np
import time

<<<<<<< HEAD

def zmanjsaj_sliko(slika, sirina, visina):
    return cv.resize(slika,(sirina,visina))
=======
def zmanjsaj_sliko(slika, sirina, visina):
    pass
>>>>>>> analiza-koze

def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze) -> list: #preveri kje so polja barve koze
    visina, sirina, _ = slika.shape  # pridobimo višino in širino slike
    rezultat = []       # končni seznam s številom pikslov kože

    for y in range(0, visina, visina_skatle): 
        vrstica = []
        for x in range(0, sirina, sirina_skatle):#premik od leve proti desni v korahih visine
            skatla = slika[y:y+visina_skatle, x:x+sirina_skatle] #izreze del slike
            st_koza = prestej_piklse_z_barvo_koze(skatla, barva_koze) #prestej koliko pikslov ima barvo koze
            vrstica.append(st_koza) #dodaj trenutno stevilo pikslov barve koze
        rezultat.append(vrstica) #celo vrstico daj v rezultat
    return rezultat

<<<<<<< HEAD
=======

>>>>>>> analiza-koze
def prestej_piklse_z_barvo_koze(slika, barva_koze) -> int:
    spodnja, zgornja = barva_koze
    maska = cv.inRange(slika, spodnja, zgornja) #ustvari crno belo masko ki vraca kje na sliki je so piksli koze(0,255)
    return cv.countNonZero(maska) #vrne stevilo pikslov kozne barve v skatli

<<<<<<< HEAD
def doloci_barvo_koze(slika,levo_zgoraj,desno_spodaj) -> tuple: #določi barvo kože glede na povprečno barvo v kvadratu
    x1, y1 = levo_zgoraj 
    x2, y2 = desno_spodaj
    podslika = slika[y1:y2, x1:x2]#izrezek slike kjer naj bi bila koza
    povprecje = np.mean(podslika.reshape(-1, 3), axis=0)#izracuna povprecje barve koze v kvadratu, vsaka vrstica stevilo pikslov x 3 barvne vrednosti
    toleranca = 40  # dodatek da pokrije tudi malo svetlejse in temnejse
    spodnja = np.clip(povprecje - toleranca, 0, 255).astype(np.uint8) #clip uporabljen da vrednosti manjse od min postanejo min/vecje od max postanejo max
    zgornja = np.clip(povprecje + toleranca, 0, 255).astype(np.uint8)
    return (spodnja, zgornja) #vrne spodno pa zgorno mejo barve
=======

def doloci_barvo_koze(slika,levo_zgoraj,desno_spodaj) -> tuple: #določi barvo kože glede na povprečno barvo v kvadratu
    pass
>>>>>>> analiza-koze

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
<<<<<<< HEAD

        slika = zmanjsaj_sliko(slika, SIRINA, VISINA) #zmanjsaj sliko
        cv.rectangle(slika, (100, 100), (160, 160), (0, 255, 0), 2) #narisi kvadrat
        cv.putText(slika, "Pritisni 's' za zajem barve koze", (10, 20), #navodila
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
=======
    

        cv.rectangle(slika, (100, 100), (160, 160), (0, 255, 0), 2) #narisi kvadrat
        cv.putText(slika, "Pritisni 's' za zajem barve koze", (10, 20), #navodila
                cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
>>>>>>> analiza-koze
        cv.imshow("Zajem barve koze", slika) #prikazi sliko z kvadratom

        tipka = cv.waitKey(1) #pocakaj na pritisk gumba
        if tipka == ord('s'):
<<<<<<< HEAD
            barva_koze = doloci_barvo_koze(slika, (100, 100), (160, 160)) #določi barvo kože z zajemom barve v kvadratu
=======

>>>>>>> analiza-koze
            break
        elif tipka == 27:  # ESC
            kamera.release()
            cv.destroyAllWindows()
            exit()

    cv.destroyWindow("Zajem barve koze")
<<<<<<< HEAD

=======
    
>>>>>>> analiza-koze
    # Glavna zanka
    while True:
        start = time.time()

        ret, slika = kamera.read()
        if not ret:
            continue

        slika = zmanjsaj_sliko(slika, SIRINA, VISINA)
        rezultat = obdelaj_sliko_s_skatlami(slika, *VELIKOST_SKATLE, barva_koze) #vrne mrezo rezultatov

        # Poišči škatlo z največ piksli kože
        prag = 500  # prag za odločitev, ali škatla vsebuje dovolj kože

        inset = 6   # koliko manjši naj bo okvir z vseh strani

        for i, vrstica in enumerate(rezultat): #vsaka vrstica
            for j, stevilo in enumerate(vrstica): #vsaka skatla
                if stevilo > prag: #pogoj pikslov
                    x = j * VELIKOST_SKATLE[0]
                    y = i * VELIKOST_SKATLE[1]
            # Manjši okvir znotraj škatle
                    zgoraj_levo = (x + inset, y + inset)
                    spodaj_desno = (x + VELIKOST_SKATLE[0] - inset, y + VELIKOST_SKATLE[1] - inset)
                    cv.rectangle(slika, zgoraj_levo, spodaj_desno, (0, 0, 255), 1) #narise kvadrat, kjer je dosti pikslov pravilne barve

        # FPS
        end = time.time()
        fps = 1 / (end - start)
        cv.putText(slika, f"FPS: {fps:.2f}", (10, 20),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv.imshow("Detekcija obraza", slika)
        if cv.waitKey(1) == 27:  # ESC
            break

    kamera.release()
    cv.destroyAllWindows()
    pass