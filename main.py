
# 4
from dataclasses import dataclass

@dataclass
class Foydalanuvchi:
    username: str
    email: str
    parol: int
    oxirgi_kirish_vaqti: str


    def parol_uzunligi(self):
        return self.parol >= 8


p = Foydalanuvchi("......", "sbc@gmail.com", 472193734, "oxirhi marta kecha 7 da kirilgan")

print(p.parol_uzunligi())




# 5
from dataclasses import dataclass

@dataclass
class Mahsulot:
    nom: str
    soni: int
    narx: float


    def umumiy_narx(self):
        return self.soni * self.narx

n = Mahsulot('non', 5, 6.000)
print(n.umumiy_narx())




# 6
from dataclasses import dataclass

@dataclass
class Shaxs:
    ism: str
    familiya: str
    tugilgan_yil: int

    def yosh(self):
        return 2026 - self.tugilgan_yil

y = Shaxs('Ali', "Aliyev", 2000)
print(y.yosh)

