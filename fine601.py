ch="yes"
while ch.lower()=="yes":



  att=int(input("Enter Students Attendance:"))
  
  if att<0 or att>100:
    print("Please Enter Valid Attendence..")
  else: 
   print(f"Your attendence is {att}%")


  if att<=100 and att>=95:
    print("Congratulations You Might Get a Reward!!")
  elif att<95 and att>=90:
    print("Congratulations You Don't Have to give any fine")
  elif att<90 and att>=85:
    print("oops You have to pay the fine--500RS")
  elif att<85 and att>=80:
    print("oops You have to pay the fine--1000RS")
  elif att<80 and att>=75:
    print("oops You have to pay the fine--1500RS + You have to do 1 assignment of each subject")
  elif att<75 and att>=70:
    print("oops You have to pay the fine--2000RS + You have to do 2 assignment of each subject")
  elif att<70 and att>=65:
    print("oops You have to pay the fine--2500RS + You have to do 3 assignment of each subject")
  elif att<65 and att>=60:
    print("oops You have to pay the fine--3000RS + You have to do 4 assignment of each subject")
  elif att<60 and att>=55:
    print("oops You have to pay the fine--3500RS + You have to do 5 assignment of each subject")
  elif att<55 and att>=50:
    print("oops You have to pay the fine--4000RS + You have to do All assignments of each subject")
  elif att<50:
    print("__Your attendence is less than 50%!!\n You are not eligible for test. Please Contact Your Coordinator__")


  if att<90:
      med=input(("If you have any medical condition type yes:"))
      
    
      if med.lower()=="yes":
        
        
        new=int(input("How many days were you sick according to medical certificate:-"))
        newatt=new*7
        per=(newatt/500)*100
        att=att+per
        if att>100:
            print("Your attendance is exceeding 100 plese enter correct leave days")
        else:
             
             print("please submit your Medical certificate to the HOD with an application")
             
             print(f"---------your new attendance is:{att} by considering your medical certificate---------")
             print("Your Revised fine is:\n")
             if att<=100 and att>=95:
                 print("Congratulations You Might Get a Reward!!")
             elif att<95 and att>=90:
                 print("You Don't Have to give any fine")
             elif att<90 and att>=85:
                 print("You have to pay the fine--500RS")
             elif att<85 and att>=80:
                 print("You have to pay the fine--1000RS")
             elif att<80 and att>=75:
                 print("You have to pay the fine--1500RS + You have to do 1 assignment of each subject")
             elif att<75 and att>=70:
                  print("You have to pay the fine--2000RS + You have to do 2 assignment of each subject")
             elif att<70 and att>=65:
                 print("You have to pay the fine--2500RS + You have to do 3 assignment of each subject")
             elif att<65 and att>=60:
                  print("You have to pay the fine--3000RS + You have to do 4 assignment of each subject")
             elif att<60 and att>=55:
                 print("You have to pay the fine--3500RS + You have to do 5 assignment of each subject")
             elif att<55 and att>=50:
                 print("You have to pay the fine--4000RS + You have to do All assignments of each subject")
             elif att<50:
                 print("__Your attendence is less than 50%!!\n You are not eligible for test Please Contact Your Coordinator__")
      else: 
          print("submit the mentioned fine")
  ch=input("If you want to check more attendence enter yes: ")
