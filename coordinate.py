class Point:
    def __init__(self, x:float, y:float, z:float):
        self.x = x
        self.y = y
        self.z = z

p = Point(1.0, 2.0, 3.0)
print(f"Point coordinates are x: {p.x}, y: {p.y}, z: {p.z}")    