# Bài tập 1 - Quản lý hàng hóa
# Họ tên: Nguyễn Thị Quỳnh Anh
# MSSV: 25112009

from abc import ABC, abstractmethod
from datetime import datetime

# ====================== CUSTOM EXCEPTION ======================
class InvalidHangHoaError(Exception):
    """Ngoại lệ cho dữ liệu hàng hóa không hợp lệ"""
    pass

# ====================== ABSTRACT CLASS ======================
class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_san_xuat = nha_san_xuat
        self.gia = gia

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise InvalidHangHoaError("Giá không được âm!")
        self._gia = value

    @abstractmethod
    def xuat_thong_tin(self):
        pass

    def __str__(self):
        return f"{self.ten_hang} ({self.ma_hang}) - {self.gia:,.0f} VNĐ"

    def __repr__(self):
        return f"HangHoa(ma_hang={self.ma_hang}, ten_hang={self.ten_hang})"

    def __eq__(self, other):
        return self.ma_hang == other.ma_hang

    def __lt__(self, other):
        return self.gia < other.gia

    def __hash__(self):
        return hash(self.ma_hang)

# ====================== SUBCLASSES ======================
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, cong_suat, dien_ap, thoi_gian_bao_hanh):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self.cong_suat = cong_suat
        self.dien_ap = dien_ap
        self.thoi_gian_bao_hanh = thoi_gian_bao_hanh

    def xuat_thong_tin(self):
        print(self)
        print(f"Công suất: {self.cong_suat} W")
        print(f"Điện áp: {self.dien_ap} V")
        print(f"Bảo hành: {self.thoi_gian_bao_hanh} tháng")
        print("-" * 50)

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu

    def xuat_thong_tin(self):
        print(self)
        print(f"Loại nguyên liệu: {self.loai_nguyen_lieu}")
        print("-" * 50)

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, ngay_san_xuat, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self.ngay_san_xuat = datetime.strptime(ngay_san_xuat, "%d/%m/%Y")
        self.ngay_het_han = datetime.strptime(ngay_het_han, "%d/%m/%Y")

    def xuat_thong_tin(self):
        print(self)
        print(f"Ngày sản xuất: {self.ngay_san_xuat.strftime('%d/%m/%Y')}")
        print(f"Ngày hết hạn: {self.ngay_het_han.strftime('%d/%m/%Y')}")
        print("-" * 50)

# ====================== CONTEXT MANAGER ======================
class QuanLyHangHoa:
    """Quản lý danh sách hàng hóa bằng context manager"""
    def __init__(self):
        self.danh_sach = []

    def __enter__(self):
        return self

    def them_hang(self, hanghoa):
        if not isinstance(hanghoa, HangHoa):
            raise InvalidHangHoaError("Đối tượng không phải là hàng hóa!")
        self.danh_sach.append(hanghoa)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("\n=== DANH SÁCH HÀNG HÓA ===")
        for h in self.danh_sach:
            h.xuat_thong_tin()
        print("Kết thúc quản lý hàng hóa.")

# ====================== DEMO ======================
if __name__ == "__main__":
    print("=== BÀI TẬP 1: QUẢN LÝ HÀNG HÓA ===\n")
    try:
        with QuanLyHangHoa() as ql:
            may_giat = HangDienMay("DM001", "Máy giặt LG Inverter 9kg", "LG Electronics", 8500000, 450, 220, 24)
            bo_bat_dia = HangSanhSu("SS001", "Bộ bát đĩa sứ cao cấp 20 món", "Minh Long", 1250000, "Sứ cao cấp")
            sua_tuoi = HangThucPham("TP001", "Sữa tươi Vinamilk 1 lít", "Vinamilk", 45000, "02/04/2026", "02/07/2026")

            ql.them_hang(may_giat)
            ql.them_hang(bo_bat_dia)
            ql.them_hang(sua_tuoi)

    except InvalidHangHoaError as e:
        print("Lỗi:", e)
