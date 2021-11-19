message = " HI this is SCIENT CHAT BOT "
print(message)
command = ""
while True:
    command = input(">").lower()
    if command == "hi":
        print("how can i help you ?")
    elif command == "admission":
        print('''
        courses -> to check courses
        admission procedure -> to check admission_procedure
        application_form -> to check application_form
        administration -> to get details of administration
        fee structure -> to get fee details
        ''')
    elif command == "courses":
        print('''
        UG course -> undergraduate courses
        PG course -> post-graduate courses
        ''')
    elif command == "ug course":
        print('''
        CSE -> computer science of engineering
        EEE -> electronic and electronics engineering
        ECE -> electronics and communications engineering
        ''')
    elif command == "pg course":
        print('''
        MBA -> master of business administration
        ''')
    elif command == "admission procedure":
        print('''
        lateral entry
        b category 
        intermediate vocational pass outs
        certificates to be submitted
        ''')
    elif command == "lateral entry":
        print('''
        students who have passed the diploma they can join B.Tech.admissions 
        are governed by the TSCHE and ECET.
        ''')
    elif command == "b category":
        print('''
        the college has a provision to admit B-Category students in each branch(except diploma)
         with the eligibility criteria by the govt.
         ''')
        print("FEES: for convener seat it is Rs.58,000/-")
    elif command == "intermediate vocational pass outs":
        print('''
        students must pass in mathematics,biology and physical sciences.
        ''')
    elif command == "certificates to be submitted":
        print('''
        copies of 
        1) 10th class marks memo.
        2) school Bonafide certificate.
        3) Intermediate Marks memo and Transfer Certificate.
        4) Community Certificate.
        5) JEE Mains Rank Card.
        6) TS EAMCET Rank Card.
        7) Proof of NRI status.
        8) Equivalency from BIE for other state intermediate board,universities,schools in other countries.
        ''')
    elif command == "administration":
        print('''
        B.Vamsi Krishna Administrative Officer	9849068863.
        P.Phani Madava Rao	PA to Secretary	9441021848
        K.Vijay Kumar Reddy	Jr.Assistant	9866997660
        U.Shashikanth	Jr. Assistant-scholarship	9912500870
        Y.Penchala Reddy	Jr. Assistant-Exam Branch	8885996955
        M.Rajender	Transport Incharge	9885034031
        Mr.Prasad	Jr.Assistant-Exam Branch	8096192146
        D.Dileep Kumar	Jr.Assistant	9701686860
        ''')
    elif command == "help":
        print('''
        hi - to start the conversation
        admission - admission procedure
        quit - to stop the conversation
        ''')
    elif command == "quit":
        break
    else:
        print("sorry, I don't understand that !")
