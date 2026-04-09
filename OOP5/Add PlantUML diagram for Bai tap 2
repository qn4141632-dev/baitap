@startuml
class NhanVien {
  - maNhanVien: String
  - hoTen: String
  - namSinh: int
  - gioiTinh: String
  - diaChi: String
  - heSoLuong: float
  - luongToiDa: float
  + tinhLuong()
  + xuatThongTin()
}

class CongTacVien {
  - thoiHanHopDong: String
  - khoanPhuCap: float
  + tinhLuong()
  + xuatThongTin()
}

class NhanVienChinhThuc {
  - viTriCongViec: String
  + xuatThongTin()
}

class TruongPhong {
  - ngayBatDauQuanLy: String
  - khoanPhuCapQuanLy: float
  + tinhLuong()
  + xuatThongTin()
}

CongTacVien --|> NhanVien
NhanVienChinhThuc --|> NhanVien
TruongPhong --|> NhanVienChinhThuc

@enduml
