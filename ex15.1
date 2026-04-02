class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, corner: Point, width, height):
        # corner là góc trái trên (top-left)
        self.corner = corner
        self.width = width
        self.height = height

    def corners(self):
        """Trả về danh sách 4 góc của hình chữ nhật"""
        x, y = self.corner.x, self.corner.y
        return [
            Point(x, y),  # top-left
            Point(x + self.width, y),  # top-right
            Point(x, y + self.height),  # bottom-left
            Point(x + self.width, y + self.height)  # bottom-right
        ]


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius


def distance(p1: Point, p2: Point):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def point_in_circle(circle: Circle, point: Point):
    """Kiểm tra điểm nằm trong hoặc trên đường tròn"""
    return distance(circle.center, point) <= circle.radius


def rect_in_circle(circle: Circle, rect: Rectangle):
    """Kiểm tra toàn bộ hình chữ nhật nằm trong hoặc trên đường tròn"""
    for corner in rect.corners():
        if not point_in_circle(circle, corner):
            return False
    return True


def rect_circle_overlap(circle: Circle, rect: Rectangle):
    """Kiểm tra nếu có góc nào của hình chữ nhật nằm trong đường tròn"""
    for corner in rect.corners():
        if point_in_circle(circle, corner):
            return True
    return False


