from abc import ABC, abstractmethod

# ====================== CUSTOM EXCEPTIONS ======================
class TuoiKhongHopLe(Exception):
    pass

class BacKhongHopLe(Exception):
    pass

# ====================== ABSTRACT CLASS ======================
class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe("Tuổi phải từ 18 đến 65")
        self._tuoi = value

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self.ho_ten} - {self.tuoi} tuổi - {self.gioi_tinh} - {self.dia_chi}"

    def __repr__(self):
        return f"CanBo(ho_ten={self.ho_ten}, tuoi={self.tuoi})"

    def __eq__(self, other):
        return (self.ho_ten, self.tuoi) == (other.ho_ten, other.tuoi)

    def __lt__(self, other):
        return self.ho_ten < other.ho_ten

# ====================== SUBCLASSES ======================
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe("Bậc công nhân phải từ 1 đến 10")
        self._bac = value

    def mo_ta(self):
        return f"Công nhân bậc {self.bac}"

    def __str__(self):
        return super().__str__() + f" | {self.mo_ta()}"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def mo_ta(self):
        return f"Kỹ sư ngành {self.nganh_dao_tao}"

    def __str__(self):
        return super().__str__() + f" | {self.mo_ta()}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"Nhân viên công việc: {self.cong_viec}"

    def __str__(self):
        return super().__str__() + f" | {self.mo_ta()}"

# ====================== QUẢN LÝ CÁN BỘ ======================
class QLCB:
    def __init__(self, filename="canbo.txt"):
        self.danh_sach = []
        self.filename = filename

    def them_moi(self, canbo):
        self.danh_sach.append(canbo)

    def tim_kiem(self, ten):
        return [cb for cb in self.danh_sach if ten.lower() in cb.ho_ten.lower()]

    def hien_thi(self):
        for cb in sorted(self.danh_sach):
            print(cb)

    # Context manager để lưu/đọc file
    def __enter__(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    print("Đọc từ file:", line.strip())
        except FileNotFoundError:
            print("Chưa có file dữ liệu, bắt đầu mới.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.filename, "w", encoding="utf-8") as f:
            for cb in self.danh_sach:
                f.write(str(cb) + "\n")
        print("Danh sách cán bộ đã được lưu vào file.")

#  DEMO 
if __name__ == "__main__":
    with QLCB() as ql:
        ql.them_moi(CongNhan("Nguyễn Văn A", 30, "Nam", "Hà Nội", 5))
        ql.them_moi(KySu("Trần Thị B", 28, "Nữ", "Hải Phòng", "Cơ khí"))
        ql.them_moi(NhanVien("Lê Văn C", 25, "Nam", "Đà Nẵng", "Kế toán"))

        print("\n=== Danh sách cán bộ ===")
        ql.hien_thi()

        print("\n=== Tìm kiếm theo tên 'B' ===")
        for cb in ql.tim_kiem("B"):
            print(cb)
