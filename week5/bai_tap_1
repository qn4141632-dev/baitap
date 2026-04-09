from datetime import datetime

class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_san_xuat = nha_san_xuat
        self.gia = gia

    def xuat_thong_tin(self):
        print(f"Mã hàng        : {self.ma_hang}")
        print(f"Tên hàng       : {self.ten_hang}")
        print(f"Nhà sản xuất   : {self.nha_san_xuat}")
        print(f"Giá            : {self.gia:,.0f} VNĐ")


class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, cong_suat, dien_ap, thoi_gian_bao_hanh):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self.cong_suat = cong_suat
        self.dien_ap = dien_ap
        self.thoi_gian_bao_hanh = thoi_gian_bao_hanh

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"Công suất      : {self.cong_suat} W")
        print(f"Điện áp        : {self.dien_ap} V")
        print(f"Bảo hành       : {self.thoi_gian_bao_hanh} tháng")
        print("-" * 50)


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"Loại nguyên liệu: {self.loai_nguyen_lieu}")
        print("-" * 50)


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, ngay_san_xuat, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self.ngay_san_xuat = ngay_san_xuat
        self.ngay_het_han = ngay_het_han

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"Ngày sản xuất  : {self.ngay_san_xuat}")
        print(f"Ngày hết hạn   : {self.ngay_het_han}")
        print("-" * 50)


#  CHƯƠNG TRÌNH CHÍNH 
if __name__ == "__main__":
    print("=== BÀI TẬP 1: QUẢN LÝ HÀNG HÓA ===\n")

    # Tạo 1 mặt hàng Điện máy
    may_giat = HangDienMay(
        ma_hang="DM001",
        ten_hang="Máy giặt LG Inverter 9kg",
        nha_san_xuat="LG Electronics",
        gia=8500000,
        cong_suat=450,
        dien_ap=220,
        thoi_gian_bao_hanh=24
    )

    # Tạo 1 mặt hàng Sành sứ
    bo_bat_dia = HangSanhSu(
        ma_hang="SS001",
        ten_hang="Bộ bát đĩa sứ cao cấp 20 món",
        nha_san_xuat="Minh Long",
        gia=1250000,
        loai_nguyen_lieu="Sứ cao cấp"
    )

    # Tạo 1 mặt hàng Thực phẩm
    sua_tuoi = HangThucPham(
        ma_hang="TP001",
        ten_hang="Sữa tươi Vinamilk 1 lít",
        nha_san_xuat="Vinamilk",
        gia=45000,
        ngay_san_xuat="02/04/2026",
        ngay_het_han="02/07/2026"
    )

    # Xuất thông tin các mặt hàng
    may_giat.xuat_thong_tin()
    bo_bat_dia.xuat_thong_tin()
    sua_tuoi.xuat_thong_tin()

    print("Hoàn thành Bài tập 1!")
