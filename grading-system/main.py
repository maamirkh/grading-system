name = input("Enter your name :")
rollNo = input("Enter your roll number :")
physics = int(input("Physics Marks out of 100 :"))
chemistry = int(input("Chemistry Marks out of 100 :"))
maths = int(input("Maths Marks out of 100 :"))
english = int(input("English Marks out of 100 :"))
urdu = int(input("Urdu Marks out of 100 :"))

# Calculating percentage
total = physics + chemistry + maths + english + urdu
percentage = total * 100 / 500

if percentage >= 90:
    result = ("Grade A")
elif percentage >= 80 and percentage < 90:
    result = ("Grade B")
elif percentage >= 70 and percentage < 80:
    result = ("Grade C")
elif percentage >= 60 and percentage < 70:
    result = ("Grade D")

else:
    print("Failed")

print(f"?Name : {name} Roll No : {rollNo}")
print(f"Physics : {physics} , Chemistry : {chemistry} , Maths : {maths} , English : {english} , Urdu : {urdu}")
print(f"Total Marks Out of 500 : {total}")
print(f"Percentage : {percentage}%")
print(f"Result : {result}")
