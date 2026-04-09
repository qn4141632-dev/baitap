from abc import ABC, abstractmethod
from datetime import datetime

class InvalidHangHoaError(Exception):
    pass

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

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, cong_suat, dien_ap, thoi_gian_bao_hanh):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self.cong_suat = cong_suat
        self.dien_ap = dien_ap
        self.thoi_gian_bao_hanh = thoi_gian_bao_hanh

    def xuat_thong_tin(self):
        print(self)
        print(f"Công suất: {self.cong_suat} W, Điện áp: {self.dien_ap} V, Bảo hành: {self.thoi_gian_bao_hanh} tháng")

# Demo
if __name__ == "__main__":
    try:
        may_giat = HangDienMay("DM001", "Máy giặt LG", "LG", 8500000, 450, 220, 24)
        may_giat.xuat_thong_tin()
    except InvalidHangHoaError as e:
        print("Lỗi:", e)
