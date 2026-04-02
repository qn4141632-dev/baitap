@startuml
skinparam classAttributeIconSize 0
skinparam shadowing false
skinparam dpi 300

class HangHoa {
    - maHang: String
    - tenHang: String
    - nhaSanXuat: String
    - gia: double
    + xuatThongTin()
}

class HangDienMay {
    - congSuat: double
    - dienAp: double
    - thoiGianBaoHanh: int
    + xuatThongTin()
}

class HangSanhSu {
    - loaiNguyenLieu: String
    + xuatThongTin()
}

class HangThucPham {
    - ngaySanXuat: String
    - ngayHetHan: String
    + xuatThongTin()
}

HangDienMay --|> HangHoa
HangSanhSu --|> HangHoa
HangThucPham --|> HangHoa

note right of HangHoa
  <b>Lớp cha</b>
  Thông tin chung của hàng hóa
end note

@enduml
