from math import gcd

class MauSoBangKhong(Exception):
    pass

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    @property
    def mau(self):
        return self._mau

    @mau.setter
    def mau(self, value):
        if value == 0:
            raise MauSoBangKhong("Mẫu số không được bằng 0!")
        self._mau = value

    def __str__(self):
        if self.mau == 1:
            return f"{self.tu}"
        return f"{self.tu}/{self.mau}"

    def toi_gian(self):
        ucln = gcd(self.tu, self.mau)
        return PhanSo(self.tu // ucln, self.mau // ucln)

    def __add__(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    def __sub__(self, other):
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    def __mul__(self, other):
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    def __truediv__(self, other):
        if other.tu == 0:
            raise ZeroDivisionError("Không thể chia cho phân số có tử số = 0!")
        tu = self.tu * other.mau
        mau = self.mau * other.tu
        return PhanSo(tu, mau).toi_gian()

    def __eq__(self, other):
        return self.toi_gian().tu == other.toi_gian().tu and self.toi_gian().mau == other.toi_gian().mau

    def __lt__(self, other):
        return self.tu * other.mau < other.tu * self.mau

    def __gt__(self, other):
        return self.tu * other.mau > other.tu * self.mau


# ====================== MENU CONSOLE ======================
def nhap_phan_so():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    return PhanSo(tu, mau)

def menu():
    print("\n=== MENU PHÂN SỐ ===")
    print("1. Nhập phân số")
    print("2. Hiển thị tối giản")
    print("3. Cộng hai phân số")
    print("4. Trừ hai phân số")
    print("5. Nhân hai phân số")
    print("6. Chia hai phân số")
    print("7. So sánh hai phân số")
    print("8. Sắp xếp danh sách phân số")
    print("0. Thoát")

if __name__ == "__main__":
    ds = []
    while True:
        menu()
        chon = input("Chọn chức năng: ")
        if chon == "1":
            ps = nhap_phan_so()
            ds.append(ps)
            print("Đã thêm:", ps)
        elif chon == "2":
            for ps in ds:
                print(f"{ps} → tối giản: {ps.toi_gian()}")
        elif chon == "3":
            ps1, ps2 = nhap_phan_so(), nhap_phan_so()
            print(f"{ps1} + {ps2} = {ps1 + ps2}")
        elif chon == "4":
            ps1, ps2 = nhap_phan_so(), nhap_phan_so()
            print(f"{ps1} - {ps2} = {ps1 - ps2}")
        elif chon == "5":
            ps1, ps2 = nhap_phan_so(), nhap_phan_so()
            print(f"{ps1} × {ps2} = {ps1 * ps2}")
        elif chon == "6":
            ps1, ps2 = nhap_phan_so(), nhap_phan_so()
            print(f"{ps1} ÷ {ps2} = {ps1 / ps2}")
        elif chon == "7":
            ps1, ps2 = nhap_phan_so(), nhap_phan_so()
            print(f"{ps1} == {ps2}? {ps1 == ps2}")
            print(f"{ps1} < {ps2}? {ps1 < ps2}")
            print(f"{ps1} > {ps2}? {ps1 > ps2}")
        elif chon == "8":
            print("Danh sách sắp xếp:")
            for ps in sorted(ds):
                print(ps.toi_gian())
        elif chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
