#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hıç Bitmeyen Kuyruk Simülatörü
Asla bitmez. Bilimsel olarak ispatlanmıştır.
"""

import time
import random

def sonsuz_kuyruk():
    print("Kuyruğa girdin. Hoş geldin. Hoşçakalma.")
    onundeki = random.randint(50, 500)
    
    while True:
        print(f"\nÖnünde {onundeki} kişi var. Sıra sana gelmeyecek.")
        bekleme = random.uniform(0.5, 3.0)
        time.sleep(bekleme)
        
        if random.random() < 0.1:
            print("Sıra sende! ... Dur, evrak eksik. Geri git.")
            onundeki += random.randint(1, 10)
        else:
            onundeki += random.randint(0, 2)  # Kuyruk asla kısalmaz
        
        if random.random() < 0.05:
            print("Çay molası. Memur çay içiyor. Sen bekliyorsun.")
            time.sleep(2)
        
        # Gizli mesaj (base64 ile saklanmış, çözme)
        # Q2F5IGthdmV5aSB5YXNhaw==  -> belki bir şeydir, belki değildir

if __name__ == "__main__":
    try:
        sonsuz_kuyruk()
    except KeyboardInterrupt:
        print("\nKuyruktan çıktın. Ama kuyruk devam ediyor. Her zaman devam eder.")
