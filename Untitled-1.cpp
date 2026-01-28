#include <iostream>
#include <string>
using namespace std;

// ===== Class Phim =====
class Movie {
public:
    string maPhim;
    string tenPhim;
    string theLoai;
    float rating;

    Movie* prev;
    Movie* next;

    Movie(string ma, string ten, string loai, float r) {
        maPhim = ma;
        tenPhim = ten;
        theLoai = loai;
        rating = r;
        prev = next = NULL;
    }
};

// ===== Class Danh sách phim =====
class MovieList {
private:
    Movie* head;

public:
    MovieList() {
        head = NULL;
    }
    void addMovie() {
        string ma, ten, loai;
        float r;

       



        cin.ignore();
        cout << "Nhap ma phim: ";
        getline(cin, ma);
        cout << "Nhap ten phim: ";
        getline(cin, ten);
        cout << "Nhap the loai: ";
        getline(cin, loai);
        cout << "Nhap rating (1-10): ";
        cin >> r;

        Movie* newMovie = new Movie(ma, ten, loai, r);

        if (head == NULL) {
            head = newMovie;
        }
        else {
            Movie* temp = head;
            while (temp->next != NULL)
                temp = temp->next;
            temp->next = newMovie;
            newMovie->prev = temp;
        }
    }

    // Hiển thị danh sách phim
    void displayAll() {
        if (head == NULL) {
            cout << "Danh sach rong!\n";
            return;
        }

        Movie* temp = head;
        while (temp != NULL) {
            cout << "\nMa phim: " << temp->maPhim;
            cout << "\nTen phim: " << temp->tenPhim;
            cout << "\nThe loai: " << temp->theLoai;
            cout << "\nRating: " << temp->rating << endl;
            temp = temp->next;
        }
    }

    // Tìm phim theo mã
    void searchById() {
        if (head == NULL) {
            cout << "Danh sach rong!\n";
            return;
        }

        string ma;
        cin.ignore();
        cout << "Nhap ma phim can tim: ";
        getline(cin, ma);

        Movie* temp = head;
        while (temp != NULL) {
            if (temp->maPhim == ma) {
                cout << "\nTim thay phim:";
                cout << "\nTen phim: " << temp->tenPhim;
                cout << "\nThe loai: " << temp->theLoai;
                cout << "\nRating: " << temp->rating << endl;
                return;
            }
            temp = temp->next;
        }
        cout << "Khong tim thay phim!\n";
    }

    // Phim rating cao nhất
    void highestRating() {
        if (head == NULL) return;

        Movie* maxMovie = head;
        Movie* temp = head->next;

        while (temp != NULL) {
            if (temp->rating > maxMovie->rating)
                maxMovie = temp;
            temp = temp->next;
        }

        cout << "\nPhim co rating cao nhat:";
        cout << "\nTen phim: " << maxMovie->tenPhim;
        cout << "\nRating: " << maxMovie->rating << endl;
    }


    // Phim rating thấp nhất
    void lowestRating() {
        if (head == NULL) return;

        Movie* minMovie = head;
        Movie* temp = head->next;

        while (temp != NULL) {
            if (temp->rating < minMovie->rating)
                minMovie = temp;
            temp = temp->next;
        }

        cout << "\nPhim co rating thap nhat:";
        cout << "\nTen phim: " << minMovie->tenPhim;
        cout << "\nRating: " << minMovie->rating << endl;
    }
};

// ===== Main =====
int main() {    
    MovieList list;
    int choice;

    do {
        cout << "\n===== MENU =====";
        cout << "\n1. Them phim";
        cout << "\n2. Hien thi danh sach";
        cout << "\n3. Tim phim theo ma";
        cout << "\n4. Phim rating cao nhat";
        cout << "\n5. Phim rating thap nhat";
        cout << "\n0. Thoat";
        cout << "\nChon: ";
        cin >> choice;

        switch (choice) {
        case 1: list.addMovie(); break;
        case 2: list.displayAll(); break;
        case 3: list.searchById(); break;
        case 4: list.highestRating(); break;
        case 5: list.lowestRating(); break;
        }
    } while (choice != 0);

    return 0;
}
