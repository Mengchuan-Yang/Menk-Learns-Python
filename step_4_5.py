name=input("你的名字是什么？（用中文填写）")
age=int(input("你的年龄是多少？"))
height=float(input("你的身高是多少？"))
is_student=input("are you a student?(yes/no):").strip().lower()=="yes"
city=input("你居住在哪个城市？")

print("\n总结报告")
print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"身高：{height}")
print(f"是否学生：{is_student}")
print(f"所在城市：{city}")