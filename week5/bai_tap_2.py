class NhanVien:
    def __init__(self, ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.ma_nhan_vien = ma_nhan_vien
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_so_luong = he_so_luong
        self.luong_toi_da = luong_toi_da

    def tinh_luong(self):
        """Tính lương cơ bản = hệ số lương * lương tối đa"""
        return self.he_so_luong * self.luong_toi_da

    def xuat_thong_tin(self):
        print(f"Mã NV       : {self.ma_nhan_vien}")
        print(f"Họ tên      : {self.ho_ten}")
        print(f"Năm sinh    : {self.nam_sinh}")
        print(f"Giới tính   : {self.gioi_tinh}")
        print(f"Địa chỉ     : {self.dia_chi}")
        print(f"Hệ số lương : {self.he_so_luong}")
        print(f"Lương tối đa: {self.luong_toi_da:,.0f} VNĐ")


class CongTacVien(NhanVien):
    def __init__(self, ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh, dia_chi, 
                 he_so_luong, luong_toi_da, thoi_han_hop_dong, khoan_phu_cap):
        super().__init__(ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.thoi_han_hop_dong = thoi_han_hop_dong
        self.khoan_phu_cap = khoan_phu_cap

    def tinh_luong(self):
        luong_co_ban = super().tinh_luong()
        return luong_co_ban + self.khoan_phu_cap

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"Thời hạn HĐ : {self.thoi_han_hop_dong}")
        print(f"Phụ cấp     : {self.khoan_phu_cap:,.0f} VNĐ")
        print(f"Lương thực nhận: {self.tinh_luong():,.0f} VNĐ")
        print("-" * 60)


class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh, dia_chi, 
                 he_so_luong, luong_toi_da, vi_tri_cong_viec):
        super().__init__(ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri_cong_viec = vi_tri_cong_viec

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"Vị trí công việc: {self.vi_tri_cong_viec}")
        print("-" * 60)


class TruongPhong(NhanVienChinhThuc):
    def __init__(self, ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh, dia_chi, 
                 he_so_luong, luong_toi_da, vi_tri_cong_viec, ngay_bat_dau, khoan_phu_cap_quan_ly):
        super().__init__(ma_nhan_vien, ho_ten, nam_sinh, gioi_tinh, dia_chi, 
                        he_so_luong, luong_toi_da, vi_tri_cong_viec)
        self.ngay_bat_dau_quan_ly = ngay_bat_dau
        self.khoan_phu_cap_quan_ly = khoan_phu_cap_quan_ly

    def tinh_luong(self):
        luong_co_ban = super().tinh_luong()
        return luong_co_ban + self.khoan_phu_cap_quan_ly

    def xuat_thong_tin(self):
        super().xuat_thong_tin()   # Gọi lại của NhanVienChinhThuc
        print(f"Ngày bắt đầu QL: {self.ngay_bat_dau_quan_ly}")
        print(f"Phụ cấp quản lý: {self.khoan_phu_cap_quan_ly:,.0f} VNĐ")
        print(f"Lương thực nhận: {self.tinh_luong():,.0f} VNĐ")
        print("-" * 60)


#  CHƯƠNG TRÌNH CHÍNH 
if __name__ == "__main__":
    print("=== QUẢN LÝ NHÂN VIÊN ===\n")

    # Tạo các đối tượng
    ctv = CongTacVien("CTV001", "Nguyễn Thị Lan", 1998, "Nữ", "Hà Nội", 
                      1.8, 5000000, "6 tháng", 1200000)

    nvct = NhanVienChinhThuc("NV001", "Trần Văn Nam", 1995, "Nam", "Hồ Chí Minh", 
                             2.5, 8000000, "Chuyên viên kinh doanh")

    tp = TruongPhong("TP001", "Lê Thị Hồng", 1988, "Nữ", "Đà Nẵng", 
                     3.2, 12000000, "Trưởng phòng Kinh doanh", "15/03/2024", 4500000)

    # Xuất thông tin
    ctv.xuat_thong_tin()
    nvct.xuat_thong_tin()
    tp.xuat_thong_tin()
