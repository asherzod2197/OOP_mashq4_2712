class Tejamkorlik:
    def __init__(self, maqsad, kerakli_summa):
        self.maqsad = maqsad                 
        self.kerakli = kerakli_summa
        self.jamg‘arma = 0

    def qo_sh(self, summa):
        if summa > 0:
            self.jamg‘arma += summa
            print(f"+ {summa:,} so'm qo‘shildi")
            self.holat()
        else:
            print("Miqdor musbat bo‘lishi kerak!")

    def holat(self):
        qoldi = self.kerakli - self.jamg‘arma
        foiz = (self.jamg‘arma / self.kerakli) * 100 if self.kerakli > 0 else 0
        
        print(f"Maqsad: {self.maqsad}")
        print(f"Jami jamg‘arma: {self.jamg‘arma:,} so'm")
        print(f"Kerakli summa: {self.kerakli:,} so'm")
        print(f"Qolgan:     {qoldi:,} so'm ({100 - foiz:.1f}%)")
        print("-" * 40)

    def tayyormi(self):
        if self.jamg‘arma >= self.kerakli:
            print(f"Tabriklaymiz! {self.maqsad} uchun yetarli pul to‘plandi! 🎉")
        else:
            print("Hali yetarli emas... Davom eting! 💪")

telefon_uchun = Tejamkorlik("Yangi telefon", 12000000)

telefon_uchun.qo_sh(3000000)
telefon_uchun.qo_sh(4500000)
telefon_uchun.qo_sh(2000000)
telefon_uchun.qo_sh(1500000)

telefon_uchun.tayyormi()
