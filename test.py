
a=input("Are you ready to give your fitness test type Yes if u want to>>")
c=0
if a=="Yes":

    print('''Do you have had any of the following diseases?
               A:Heart disease
               B:Diabetes
               C:Lung Disease
               D:Hypertension
               E:None''')
    c1=input()
    if c1!="E":
        c = c + 1

    print('''Are you experiencing any of the following symptoms?
             A:Cough
             B:Fever
             C:Difficulty in breathing
             D:None''')
    c2=input()
    if c2!="D":
        c=c+1
    print('''Have you traveled anywhere in last 14 days?
              A:Yes
              B:No''')
    c3=input()
    if c3=="A":
        c=c+1
    print('''Which of the following apply to you?
            A:Recently contacted someone who had corona
            B:I am healthcare worker
            C:None''')
    c4=input()
    if c4!="C":
        c=c+1
    if c==0:
        print("you are safe :)")
    if c==1:
        print("you have low risk of infection :-|")
    if c==2:
        print("you have moderate risk of infection :(")
    if c==3:
        print("you should isolate yourself!")
    if c==4:
        print("you  must get a health check up asap!!!")
print("Stay Home Stay Safe")



