attendance_list = []

def mark_present(student_name: str):
    if student_name not in attendance_list:
        attendance_list.append(student_name)
        print("marked present")
    else:
        print("already present")

def remove_student(student_name: str):
    if student_name in attendance_list:
        attendance_list.remove(student_name)
        print("marked absent")
    else:
        print("already absent")
        
def is_present(student_name: str) -> bool:
    return student_name in attendance_list

def display_attendance():
    if attendance_list:
        print("Students present today:")
        for student in attendance_list:
            print(f"{student}")
    else:
        print(" no one is present")


d=int(input("no. of students present"))
while d>0:
    a=input("enter the student names ")
    mark_present(a)
    d=d-1
display_attendance()
b=input("enter the student names to remove")
remove_student(b)
display_attendance()
c=input("enter the student to check present ")
print(is_present(c))
#sort the elements and apply quick sort eytchnique without using any inbuilt function using quicksort
