#include <iostream>
#include <list>
#include <string>

using namespace std;

// Sử dụng Class để quản lý đối tượng Phim
class Phim {
private:
    string maPhim;
    string tenPhim;
    string theLoai;
    double diemDanhGia;

public:
    // Hàm khởi tạo (Constructor)
    Phim(string ma, string ten, string tl, double diem) 
        : maPhim(ma), tenPhim(ten), theLoai(tl), diemDanhGia(diem) {}

    // Các hàm lấy dữ liệu (Getters)
    string getMaPhim() const { return maPhim; }
    double getDiem() const { return diemDanhGia; }

    // Hàm hiển thị thông tin phim
    void hienThi() const {
        cout << "Ma: " << maPhim << " | Ten: " << tenPhim 
             << " | The loai: " << theLoai << " | Rating: " << diemDanhGia << endl;
    }
};

int main() {
    list<Phim> dsPhim;
    int luaChon;

    do {
        cout << "\n========== MENU QUAN LY PHIM ==========" << endl;
        cout << "1. Nhap lieu (Them phim moi liên tuc)" << endl;
        cout << "2. Hien thi tat ca phim" << endl;
        cout << "3. Tim phim theo ma phim" << endl;
        cout << "4. Phim co diem danh gia CAO NHAT" << endl;
        cout << "5. Phim co diem danh gia THAP NHAT" << endl;
        cout << "0. Thoat" << endl;
        cout << "Nhap lua chon: ";
        cin >> luaChon;
        cin.ignore(); // Xóa bộ nhớ đệm

        switch (luaChon) {
            case 1: {
                char tiepTuc;
                do {
                    string ma, ten, tl;
                    double diem;
                    cout << "\n--- Nhap thong tin phim ---" << endl;
                    cout << "Nhap ma phim: "; getline(cin, ma);
                    cout << "Nhap ten phim: "; getline(cin, ten);
                    cout << "Nhap the loai: "; getline(cin, tl);
                    cout << "Nhap diem danh gia (1-10): "; cin >> diem;
                    
                    // Thêm phim vào danh sách
                    dsPhim.push_back(Phim(ma, ten, tl, diem));

                    // Hỏi người dùng có muốn nhập tiếp không
                    cout << "Ban co muon nhap tiep phim nua khong? (c/k): ";
                    cin >> tiepTuc;
                    cin.ignore(); // Xóa bộ nhớ đệm để không lỗi getline lần sau

                } while (tiepTuc == 'c' || tiepTuc == 'C'); 
                // Vòng lặp này giúp bạn nhập bao nhiêu phim tùy thích trước khi về Menu
                break;
            }
            case 2: {
                if (dsPhim.empty()) {
                    cout << "\n>> Danh sach hien dang trong!" << endl;
                } else {
                    cout << "\n--- DANH SACH PHIM ---" << endl;
                    for (const auto& p : dsPhim) p.hienThi();
                }
                break;
            }
            case 3: {
                string maTim;
                cout << "Nhap ma phim can tim: "; getline(cin, maTim);
                bool timThay = false;
                for (const auto& p : dsPhim) {
                    if (p.getMaPhim() == maTim) {
                        cout << "Ket qua: "; p.hienThi();
                        timThay = true;
                        break;
                    }
                }
                if (!timThay) cout << "Khong tim thay ma phim nay!" << endl;
                break;
            }
            case 4: {
                if (dsPhim.empty()) {
                    cout << "\n>> Danh sach trong, khong the tim phim cao nhat!" << endl;
                } else {
                    Phim pMax = dsPhim.front();
                    for (const auto& p : dsPhim) {
                        if (p.getDiem() > pMax.getDiem()) pMax = p;
                    }
                    cout << "\n>> Phim rating CAO NHAT: "; pMax.hienThi();
                }
                break;
            }
            case 5: {
                if (dsPhim.empty()) {
                    cout << "\n>> Danh sach trong, khong the tim phim thap nhat!" << endl;
                } else {
                    Phim pMin = dsPhim.front();
                    for (const auto& p : dsPhim) {
                        if (p.getDiem() < pMin.getDiem()) pMin = p;
                    }
                    cout << "\n>> Phim rating THAP NHAT: "; pMin.hienThi();
                }
                break;
            }
            case 0:
                cout << "Dang thoat chương trình..." << endl;
                break;
            default:
                cout << "Lua chon khong hop le! Vui long nhap lai." << endl;
        }
    } while (luaChon != 0);

    return 0;
}