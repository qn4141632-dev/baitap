class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return f"SieuNhan {self.ten} - Vũ khí: {self.vu_khi}, Màu sắc: {self.mau_sac}"


# Danh sách siêu nhân
ds_sieu_nhan = []

# Nhập danh sách bằng vòng lặp while
while True:
    ten = input("Nhập tên siêu nhân (hoặc 'q' để thoát): ")
    if ten.lower() == 'q':
        break
    vu_khi = input("Nhập vũ khí: ")
    mau_sac = input("Nhập màu sắc: ")

    sn = SieuNhan(ten, vu_khi, mau_sac)
    ds_sieu_nhan.append(sn)

print("\nDanh sách siêu nhân:")
# In danh sách bằng vòng lặp for
for sn in ds_sieu_nhan:
    print(sn)
