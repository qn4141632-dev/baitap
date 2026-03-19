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

    # 1. Hàm tính lương
    def tinhLuong(self):
        return self.luongCoBan * self.heSoLuong

    # 2. Hàm in thông tin nhân viên
    def inTTin(self):
        print(f"Tên nhân viên: {self.tenNhanVien}")
        print(f"Lương cơ bản: {self.luongCoBan}")
        print(f"Hệ số lương: {self.heSoLuong}")
        print(f"Lương hiện tại: {self.tinhLuong()}")

    # 3. Hàm tăng lương
    def tangLuong(self, delta: float):
        luong_moi = (self.luongCoBan + delta) * self.heSoLuong
        if luong_moi > NhanVien.LUONG_MAX:
            print("Lương mới vượt quá mức tối đa cho phép!")
            return False
        else:
            self.luongCoBan += delta
            print("Tăng lương thành công.")
            return True


# Class quản lý danh sách nhân viên 
class DanhSachNhanVien:
    def __init__(self):
        self.dsNhanVien = []

    def themNhanVien(self, nv: NhanVien):
        self.dsNhanVien.append(nv)

    def xoaNhanVien(self, ten: str):
        for nv in self.dsNhanVien:
            if nv.getTenNhanVien() == ten:
                self.dsNhanVien.remove(nv)
                print(f"Đã xóa nhân viên: {ten}")
                return True
        print("Không tìm thấy nhân viên cần xóa.")
        return False

    def timNhanVien(self, ten: str):
        for nv in self.dsNhanVien:
            if nv.getTenNhanVien() == ten:
                return nv
        return None

    def inDanhSach(self):
        if not self.dsNhanVien:
            print("Danh sách nhân viên trống.")
        else:
            for nv in self.dsNhanVien:
                nv.inTTin()
                print("-" * 30)

    def tangLuongNhanVien(self, ten: str, delta: float):
        nv = self.timNhanVien(ten)
        if nv:
            return nv.tangLuong(delta)
        else:
            print("Không tìm thấy nhân viên để tăng lương.")
            return False


# Ví dụ chạy thử 
if __name__ == "__main__":
    ds = DanhSachNhanVien()

    # Thêm nhân viên
    nv1 = NhanVien("Quỳnh", 5000, 2.5)
    nv2 = NhanVien("An", 6000, 2.0)
    ds.themNhanVien(nv1)
    ds.themNhanVien(nv2)

    print("Danh sách nhân viên ban đầu:")
    ds.inDanhSach()

    # Tăng lương cho Quỳnh
    print("\nTăng lương cho Quỳnh:")
    ds.tangLuongNhanVien("Quỳnh", 2000)
    ds.inDanhSach()

    # Xóa nhân viên An
    print("\nXóa nhân viên An:")
