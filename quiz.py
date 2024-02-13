Questions=("Which is the biggest country of the world?",
           "Which coundtry did Hitler ruled?",
           "Which is safest car in India?",
           "Which is the financial capital of India?",
           "Which is the first capital of british India?")
Options=(("A.United States","B.Canada","C.India","D.China","E.Russia"),
         ("A.France","B.Poland","C.Austria","D.Germany","E.Egypt"),
         ("A.Harrier","B.Alto","C.Swift","D.Verna","E.Seltos"),
         ("A.Pune","B.Delhi","C.Mumbai","D.Bhopal","E.Chandigarh"),
         ("A.Mysore","B.Delhi","C.Patna","D.Kolkata","E.Bombay"))

Correct_answers=("E","D","A","C","D")
points=0
user_input=[]
q=0
for x in Questions:
    print("---------------------------")
    print(x)
    for y in Options[q]:
        print(y)
    ans=input("Enter your answer:").upper()
    user_input.append(ans)
    if ans==Correct_answers[q]:
        points+=1
        print("Correct Answer")
    else:
        print("Incorrect Answer")
    q+=1
print("---------------------------")
print("Correct Answers are:",end=" ")
for k in Correct_answers:
    print(k,end="")
print("\nYour Answers are:",end=" ")
for l in user_input:
    print(l,end="")
print("\nYour Score is:",points//len(Questions)*100,"%")
    