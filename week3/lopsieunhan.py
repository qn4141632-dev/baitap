class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return f"SieuNhan {self.ten} - Vũ khí: {self.vu_khi}, Màu sắc: {self.mau_sac}"


# Khởi tạo 2 đối tượng
sieu_nhan_A = SieuNhan("A", "kiếm", "đỏ")
sieu_nhan_B = SieuNhan("B", "khiên", "xanh")

# In ra để kiểm tra
print(sieu_nhan_A)
print(sieu_nhan_B)
