# Sử dụng vòng lặp for để lặp từ 0 đến 10 và chỉ in ra các số chẵn
mylist=[1,2,3,4,5,6,7,8,9,10]
for i in mylist:
     if i%2==0:
          print('so chan' ,i)

# Sử dụng vòng lặp để tìm ra số lớn nhất trong danh sách (list) không dùng hàm có sẵn
def find_max(lst):
    max_value = lst[0]  
    for num in lst[1:]:  
        if num > max_value:
            max_value = num
    return max_value
numbers = [3, 7, 2, 9, 5, 1]
print("So lon nhat:", find_max(numbers))

# Hãy sử dụng class trong python để xây dựng chương trình Quản lý sinh viên
class Student:
    def __init__(self, id, name, score):
        self.id, self.name, self.score = id, name, score

    def __str__(self):
        return f"{self.id} - {self.name} - {self.score}"

class StudentManagement:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def show(self):
        print("\n".join(map(str, self.students)) if self.students else "Danh sách trống.")

    def find(self, id):
        return next((s for s in self.students if s.id == id), None)

    def sort(self):
        self.students.sort(key=lambda s: s.score, reverse=True)

    def remove(self, id):
        self.students = [s for s in self.students if s.id != id]