import time
import os

def tamagotchi():
    print(" Telur menetas...")
    time.sleep(2)
    nama = input("Kasih nama monstermu: ")
    
    # Status Awal
    lapar = 50   # 0 = Kenyang, 100 = Mati Kelaparan
    kotor = 0    # 0 = Bersih, 100 = Sakit
    bahagia = 50 # 0 = Depresi, 100 = Sangat Bahagia
    hidup = True
    umur = 0
    
    while hidup:
        # Tampilkan Status (Model Bar Sederhana)
        # os.system('cls') # Kalau mau clear screen (Windows), opsional
        print("\n" + "="*30)
        print(f" NAMA: {nama} | UMUR: {umur} hari")
        print(f" Lapar   : {lapar}/100") 
        print(f" Kotor   : {kotor}/100")
        print(f" Bahagia : {bahagia}/100")
        print("="*30)
        
        # Cek Kondisi Mati
        if lapar >= 100:
            print(f" {nama} mati kelaparan...")
            break
        if kotor >= 100:
            print(f" {nama} mati kena penyakit karena jorok...")
            break
        if bahagia <= 0:
            print(f" {nama} kabur karena depresi...")
            break

        print("Pilih Aksi:")
        print("1.  Makan (Kurangi Lapar)")
        print("2.  Mandi (Kurangi Kotor)")
        print("3.  Main  (Tambah Bahagia, Tapi jadi Lapar)")
        print("4.  Tidur (Skip hari)")
        
        aksi = input(" Pilihanmu: ")
        
        # --- PROSES AKSI USER ---
        if aksi == "1":
            print(f"{nama} makan dengan lahap... nyam nyam.")
            lapar -= 20
            kotor += 5
        elif aksi == "2":
            print(f"{nama} dimandikan... segeer!")
            kotor -= 40
        elif aksi == "3":
            print(f"{nama} bermain bola! Seru banget!")
            bahagia += 20
            lapar += 10 # Main bikin laper
            kotor += 10 # Main bikin kotor
        elif aksi == "4":
            print(f"{nama} tidur nyenyak... zzz...")
            # Tidur memulihkan sedikit kebahagiaan
            bahagia += 5
        else:
            print(f"{nama} bingung melihatmu.. (Turn terlewat)")

        # --- EFEK WAKTU (STATE DECAY) ---
        # Setiap turn, kondisi pasti memburuk sedikit (alami)
        lapar += 5
        kotor += 5
        bahagia -= 5
        umur += 1
        
        # --- BATASAN NILAI (CLAMPING) ---
        # Jangan sampai nilai minus atau lebih dari 100
        if lapar < 0: lapar = 0
        if kotor < 0: kotor = 0
        if bahagia > 100: bahagia = 100
        
        time.sleep(1)

    print("\n--- GAME OVER ---")
    print(f"Kamu berhasil merawat {nama} selama {umur} hari.")

tamagotchi()
