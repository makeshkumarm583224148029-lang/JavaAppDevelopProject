#my 12th mark list
marks=[92,95,81,81,82,57]
heighest=max(marks)
lowest=min(marks)



total_count=0
pass_count=0
fail_count=0

for m in marks:
    total_count+=m
    if(m>=35):
        result="pass"
        pass_count+=1
    else:
        result="fail"
        fail_count+=1
print(pass_count)
print(fail_count)



Average=total_count/len(marks)

print(Average)

print("\n==================student_Result=====================")

print("Number_of_Pass_Subjects:",pass_count)
print("Number_of_Fail_Subjects",fail_count)
print("Total_marks:",total_count)
print("Heighest_marks:",heighest)
print("Lowest_marks:",lowest)
print("Average_marks:",Average)


