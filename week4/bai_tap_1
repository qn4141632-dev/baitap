class NhanVien:
    # Hằng số lương tối đa
    LUONG_MAX = 20000  

    def __init__(self, tenNhanVien: str, luongCoBan: float, heSoLuong: float):
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = luongCoBan
        self.heSoLuong = heSoLuong

    # Getter & Setter cho tenNhanVien
    def getTenNhanVien(self):
        return self.tenNhanVien

    def setTenNhanVien(self, tenNhanVien: str):
        self.tenNhanVien = tenNhanVien

    # Getter & Setter cho luongCoBan
    def getLuongCoBan(self):
        return self.luongCoBan

    def setLuongCoBan(self, luongCoBan: float):
        self.luongCoBan = luongCoBan

    # Getter & Setter cho heSoLuong
    def getHeSoLuong(self):
        return self.heSoLuong

    def setHeSoLuong(self, heSoLuong: float):
        self.heSoLuong = heSoLuong

    # 1. Phương thức tính lương
    def tinhLuong(self):
        return self.luongCoBan * self.heSoLuong

    # 2. Phương thức in thông tin nhân viên
    def inTTin(self):
        print(f"Tên nhân viên: {self.tenNhanVien}")
        print(f"Lương cơ bản: {self.luongCoBan}")
        print(f"Hệ số lương: {self.heSoLuong}")
        print(f"Lương hiện tại: {self.tinhLuong()}")

    # 3. Phương thức tăng lương (tăng hệ số lương)
    def tangLuong(self, delta: float):
        heSoLuong_moi = self.heSoLuong + delta
        luong_moi = self.luongCoBan * heSoLuong_moi
        if luong_moi > NhanVien.LUONG_MAX:
            print("Lương mới vượt quá mức tối đa cho phép!")
            return False
        else:
            self.heSoLuong = heSoLuong_moi
            print("Tăng hệ số lương thành công.")
            return True


# ------------------ Ví dụ chạy thử ------------------
if __name__ == "__main__":
    nv = NhanVien("Quỳnh", 5000, 2.5)

    print("Thông tin ban đầu:")
    nv.inTTin()

    print("\nThử tăng hệ số lương thêm 0.5:")
    nv.tangLuong(0.5)
    nv.inTTin()

    print("\nThử tăng hệ số lương thêm 5.0 (vượt mức):")
    nv.tangLuong(5.0)
    nv.inTTin()
