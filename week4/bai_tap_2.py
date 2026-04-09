class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class LineSegment:
    # 1. Hàm xây dựng mặc định
    def __init__(self, *args):
        if len(args) == 0:
            # d1(8,5), d2(1,0)
            self.d1 = Point(8, 5)
            self.d2 = Point(1, 0)
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            # Hàm xây dựng có đối số: LineSegment(Point d1, Point d2)
            self.d1 = args[0]
            self.d2 = args[1]
        elif len(args) == 4 and all(isinstance(a, int) for a in args):
            # Hàm xây dựng 4 đối số: LineSegment(x1, y1, x2, y2)
            self.d1 = Point(args[0], args[1])
            self.d2 = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            # Hàm xây dựng sao chép
            other = args[0]
            self.d1 = Point(other.d1.x, other.d1.y)
            self.d2 = Point(other.d2.x, other.d2.y)
        else:
            raise ValueError("Tham số không hợp lệ cho LineSegment")

    def __str__(self):
        return f"Đoạn thẳng từ {self.d1} đến {self.d2}"
// Vi du chay thu
if __name__ == "__main__":
    # Mặc định
    ls1 = LineSegment()
    print(ls1)

    # Tạo từ 2 Point
    p1 = Point(2, 3)
    p2 = Point(5, 7)
    ls2 = LineSegment(p1, p2)
    print(ls2)

    # Tạo từ 4 số nguyên
    ls3 = LineSegment(0, 0, 4, 4)
    print(ls3)

    # Sao chép đoạn thẳng
    ls4 = LineSegment(ls2)
    print(ls4)

