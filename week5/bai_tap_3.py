class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def __str__(self):
        return f"{self.ho_ten} - {self.tuoi} tuổi - {self.gioi_tinh} - {self.dia_chi}"

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        if not (1 <= bac <= 10):
            raise ValueError("Bậc công nhân phải từ 1 đến 10")
        self.bac = bac

    def __str__(self):
        return super().__str__() + f" | Công nhân bậc {self.bac}"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def __str__(self):
        return super().__str__() + f" | Kỹ sư ngành {self.nganh_dao_tao}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def __str__(self):
        return super().__str__() + f" | Nhân viên công việc: {self.cong_viec}"

class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them_moi(self, canbo):
        self.danh_sach.append(canbo)

    def tim_kiem(self, ten):
        return [cb for cb in self.danh_sach if ten.lower() in cb.ho_ten.lower()]

    def hien_thi(self):
        for cb in self.danh_sach:
            print(cb)

#  DEMO 
if __name__ == "__main__":
    ql = QLCB()

    # Thêm cán bộ
    ql.them_moi(CongNhan("Nguyễn Văn A", 30, "Nam", "Hà Nội", 5))
    ql.them_moi(KySu("Trần Thị B", 28, "Nữ", "Hải Phòng", "Cơ khí"))
    ql.them_moi(NhanVien("Lê Văn C", 25, "Nam", "Đà Nẵng", "Kế toán"))

    print("=== Danh sách cán bộ ===")
    ql.hien_thi()

    print("\n=== Tìm kiếm theo tên 'B' ===")
    ket_qua = ql.tim_kiem("B")
    for cb in ket_qua:
        print(cb)

