name=input("Enter your name:")
age=int(input("Enter your age:"))
height=float(input("Enter your height in meters"))
is_student=input("Are your a student?(yes/no):").strip().lower()=="yes"

#输出结果
print("\nSummary")
print(f"Name:{name}")
print(f"Age:{age}")
print(f"Height:{height}")
print(f"Is student:{is_student}")