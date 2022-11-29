from random import randint
class question(object):
    def __init__(self,q="",a=""):
        self.question = q
        self.answer = a
    def removeQuestion(self):
        self.question = ""
        self.answer = ""
    def __add__(self,o):
        return self.question + o.question
def chooseQuestion():
        #list all questions and answers in lists, using lists because its faster than a dictonary
        qs = [" 'OS' computer abbreviation usually means?\n(A) Order of Significance\n(B) Open Software\n(C) Operating System\n(D) Optical Sensor",\
            " '.MOV' extension refers usually to what kind of file?\n(A) Image file\n(B) Animation/movie file\n(C) Audio file\n(D) MS Office document",\
                "'.MPG' extension refers usually to what kind of file?\n(A) Word Perfect Document file\n(B) MS Office document\n(C) Animation/movie file\n(D) Image file",\
                    "What is part of a database that holds only one type of information?\n(A) Report\n(B) Field\n(C) Record\n(D) File",\
                        "Who developed Yahoo?\n(A) Dennis Ritchie & Ken Thompson\n(B) David Filo & Jerry Yang\n(C) Vint Cerf & Robert Kahn\n(D) Steve Case & Jeff Bezos",\
                            "'DB' computer abbreviation usually means?\n(A) Database\n(B) Double Byte\n(C) Data Block\n(D) Driver Boot",\
                                " '.INI' extension refers usually to what kind of file?\n(A) Image file\n(B) System file\n(C) Hypertext related file\n(D) Image Color Matching Profile file",\
                                    "The sampling rate, (how many samples per second are stored) for a CD is?\n(A) 48.4 kHz\n(B) 22,050 Hz\n(C) 44.1 kHz\n(D) 48 kHz",\
                                        "What do we call a network whose elements may be separated by some distance? It usually involves two or more small networks and dedicated high-speed telephone lines.\n(A) URL (Universal Resource Locator)\n(B) LAN (Local Area Network)\n(C) WAN (Wide Area Network)\n(D) World Wide Web",\
                                            " Sometimes computers and cache registers in a foodmart are connected to a UPS system. What does UPS mean?\n(A) United Parcel Service\n(B) Uniform Product Support\n(C) Under Paneling Storage\n(D) Uninterruptable Power Supply",\
                                                "What is FMD?\n(A) Fast-Ethernet Measuring Device\n(B) Flashing Media Diode\n(C) Fluorescent Multi-Layer Disc\n(D) Flash Media Driver",\
                                                    "What is a URL?\n(A) A computer software program\n(B) A type of UFO\n(C) The address of a document or 'page' on the World Wide Web\n(D) An acronym for Uniform Resources Learning",\
                                                        "The Central Processing Unit is an embedded chip that acts as the 'brains' of a computer. What Intel chip was used in the Altair (the first real personal computer)?\n(A) 6502\n(B) 8080\n(C) 6400\n(D) 8286",\
                                                            "Where is the headquarters of Intel located?\n(A) Redmond, Washington\n(B) Tucson, Arizona\n(C) Santa Clara, California\n(D) Richmond, Virginia",\
                                                                "Who co-created the UNIX operating system in 1969 with Dennis Ritchie?\n(A) Bjarne Stroustrup\n(B) Steve Wozniak\n(C) Ken Thompson\n(D) Niklaus Wirth",\
                                                                    "'.BAT' extension refers usually to what kind of file?\n(A) Compressed Archive file\n(B) System file\n(C) Audio file\n(D) Backup file",\
                                                                        "What is the term to ask the computer to put information in order numerically or alphabetically?\n(A) Crop\n(B) Report\n(C) Record\n(D) Sort",\
                                                                            "What does EPROM stand for?\n(A) Electric Programmable Read Only Memory\n(B) Erasable Programmable Read Only Memory\n(C) Evaluable Philotic Random Optic Memory\n(D) Every Person Requires One Mind",\
                                                                                "In computer jargon, RAM refers to\n(A) Read Only Menu\n(B) Random Access Memory\n(C) Random Accent Memory\n(D) Read Access Memory",\
                                                                                    "Which of the following is not a computer language?\n(A) Windows 98\n(B) PASCAL\n(C) FORTRAN\n(D) C++"]
        ans = ["C","B","C","B","B","A","B","C","C","D","C","C","B","C","C","B","D","B","B","A"]
        l = len(qs)
        x = randint(0,l-1)
        tmp = question(qs[x],ans[x])
        return tmp
class exam(question):
    def makeExam(self):
        self.q1 = chooseQuestion()
        self.q2 = chooseQuestion()
        self.q3 = chooseQuestion()
        self.q4 = chooseQuestion()
        self.q5 = chooseQuestion()
        # print(self.q1.question + self.q2.question)
    def takeExam(self):
        self.userAns = []
    
        print(self.q1.question, end=" ")
        uInput = input()
        self.userAns.append(uInput.upper())
        
        print(self.q2.question, end=" ")
        uInput = input()
        self.userAns.append(uInput.upper())
        
        print(self.q3.question, end=" ")
        uInput = input()
        self.userAns.append(uInput.upper())
        
        print(self.q4.question, end=" ")
        uInput = input()
        self.userAns.append(uInput.upper())
        
        print(self.q5.question, end=" ")
        uInput = input()
        self.userAns.append(uInput.upper())
    def gradeExam(self):
        self.gradesQs = []
        __corrA = []
        __corrA.append(self.q1.answer)
        __corrA.append(self.q2.answer)
        __corrA.append(self.q3.answer)
        __corrA.append(self.q4.answer)
        __corrA.append(self.q5.answer)
        self.counter = 0
        for i in range(len(self.userAns)):
            if self.userAns[i] == __corrA[i]:
                self.counter+=1
                self.gradesQs.append(1)
            else:
                self.gradesQs.append(0)
                continue
    def setExamScore(self):
        self.grade = self.counter
    def returnExamScore(self):
        return self.grade
class student(exam):
    def __init__(self,name="",id="xxxx",currentScore=0,highestScore=0):
        self.id = id
        self.currentScore = currentScore
        self.highestScore = highestScore
        self.name = name
    def setID(self, id):
        self.id = id
    def returnName(self):
        return self.name
    def takeQuiz(self):
        e = exam()
        self.makeExam()
        self.takeExam()
        self.gradeExam()
        self.setExamScore()
        self.currentScore = self.returnExamScore()
        if self.highestScore < self.currentScore:
            self.highestScore = self.returnExamScore()
    def returnCurrent(self):
        return str(self.currentScore) + "/5\n"
    def returnHighest(self):
        return str(self.highestScore) + "/5\n"
    def returnIndGrades(self):
        return self.gradesQs
def main():
    while True:
        inp = input("A:student\nB:exit")
        if inp.upper() == "B":
            break
        elif inp.upper() == "A":
            user = input("Please enter your name ")
            id = input("Please enter your 4 digit ID to take the exam: ")
            s = student(user,id)
            s.takeQuiz()
            print(s.returnCurrent())
            print(s.returnHighest())
            print(s.returnIndGrades())
            
            
        else:
            print("Enter a valid input!")
            
    
    
main()

'''
A:student
B:exitA
Please enter your name alice
Please enter your 4 digit ID to take the exam: 1234
In computer jargon, RAM refers to
(A) Read Only Menu
(B) Random Access Memory
(C) Random Accent Memory
(D) Read Access Memory b
What do we call a network whose elements may be separated by some distance? It usually involves two or more small networks and dedicated high-speed telephone lines.
(A) URL (Universal Resource Locator)
(B) LAN (Local Area Network)
(C) WAN (Wide Area Network)
(D) World Wide Web b
'DB' computer abbreviation usually means?
(A) Database
(B) Double Byte
(C) Data Block
(D) Driver Boot a
Which of the following is not a computer language?
(A) Windows 98
(B) PASCAL
(C) FORTRAN
(D) C++ a
'DB' computer abbreviation usually means?
(A) Database
(B) Double Byte
(C) Data Block
(D) Driver Boot a
current: 4/5

highest: 4/5

[1, 0, 1, 1, 1]

Would you like to take it again
A: yes
B: no
B

test2: 
A:student
B:exitA
Please enter your name mark
Please enter your 4 digit ID to take the exam: 1234
In computer jargon, RAM refers to
(A) Read Only Menu
(B) Random Access Memory
(C) Random Accent Memory
(D) Read Access Memory b
What do we call a network whose elements may be separated by some distance? It usually involves two or more small networks and dedicated high-speed telephone lines.
(A) URL (Universal Resource Locator)
(B) LAN (Local Area Network)
(C) WAN (Wide Area Network)
(D) World Wide Web b
'DB' computer abbreviation usually means?
(A) Database
(B) Double Byte
(C) Data Block
(D) Driver Boot a
Which of the following is not a computer language?
(A) Windows 98
(B) PASCAL
(C) FORTRAN
(D) C++ a
'DB' computer abbreviation usually means?
(A) Database
(B) Double Byte
(C) Data Block
(D) Driver Boot a
current: 4/5

highest: 4/5

[1, 0, 1, 1, 1]

Would you like to take it again
A: yes
B: no
A

In computer jargon, RAM refers to
(A) Read Only Menu
(B) Random Access Memory
(C) Random Accent Memory
(D) Read Access Memory b
What do we call a network whose elements may be separated by some distance? It usually involves two or more small networks and dedicated high-speed telephone lines.
(A) URL (Universal Resource Locator)
(B) LAN (Local Area Network)
(C) WAN (Wide Area Network)
(D) World Wide Web b
'DB' computer abbreviation usually means?
(A) Database
(B) Double Byte
(C) Data Block
(D) Driver Boot a
Which of the following is not a computer language?
(A) Windows 98
(B) PASCAL
(C) FORTRAN
(D) C++ a
'DB' computer abbreviation usually means?
(A) Database
(B) Double Byte
(C) Data Block
(D) Driver Boot a
current: 4/5

highest: 4/5

[1, 0, 1, 1, 1]

Would you like to take it again
A: yes
B: no
A

In computer jargon, RAM refers to
(A) Read Only Menu
(B) Random Access Memory
(C) Random Accent Memory
(D) Read Access Memory b
What do we call a network whose elements may be separated by some distance? It usually involves two or more small networks and dedicated high-speed telephone lines.
(A) URL (Universal Resource Locator)
(B) LAN (Local Area Network)
(C) WAN (Wide Area Network)
(D) World Wide Web b
'DB' computer abbreviation usually means?
(A) Database
(B) Double Byte
(C) Data Block
(D) Driver Boot a
Which of the following is not a computer language?
(A) Windows 98
(B) PASCAL
(C) FORTRAN
(D) C++ a
'DB' computer abbreviation usually means?
(A) Database
(B) Double Byte
(C) Data Block
(D) Driver Boot a
current: 4/5

highest: 4/5

[1, 0, 1, 1, 1]

Would you like to take it again
A: yes
B: no
B

test3:
A:student
B:exita
Please enter your name bob
Please enter your 4 digit ID to take the exam: 1234
Who developed Yahoo?
(A) Dennis Ritchie & Ken Thompson
(B) David Filo & Jerry Yang
(C) Vint Cerf & Robert Kahn
(D) Steve Case & Jeff Bezos b
In computer jargon, RAM refers to
(A) Read Only Menu
(B) Random Access Memory
(C) Random Accent Memory
(D) Read Access Memory c
 '.INI' extension refers usually to what kind of file?
(A) Image file
(B) System file
(C) Hypertext related file
(D) Image Color Matching Profile file d
 '.INI' extension refers usually to what kind of file?
(A) Image file
(B) System file
(C) Hypertext related file
(D) Image Color Matching Profile file a
The Central Processing Unit is an embedded chip that acts as the 'brains' of a computer. What Intel chip was used in the Altair (the first real personal computer)?
(A) 6502
(B) 8080
(C) 6400
(D) 8286 a
1/5

1/5

[1, 0, 0, 0, 0]

Would you like to take it again
A: yes
B: no
A
Who developed Yahoo?
(A) Dennis Ritchie & Ken Thompson
(B) David Filo & Jerry Yang
(C) Vint Cerf & Robert Kahn
(D) Steve Case & Jeff Bezos b
In computer jargon, RAM refers to
(A) Read Only Menu
(B) Random Access Memory
(C) Random Accent Memory
(D) Read Access Memory c
 '.INI' extension refers usually to what kind of file?
(A) Image file
(B) System file
(C) Hypertext related file
(D) Image Color Matching Profile file d
 '.INI' extension refers usually to what kind of file?
(A) Image file
(B) System file
(C) Hypertext related file
(D) Image Color Matching Profile file a
The Central Processing Unit is an embedded chip that acts as the 'brains' of a computer. What Intel chip was used in the Altair (the first real personal computer)?
(A) 6502
(B) 8080
(C) 6400
(D) 8286 a
1/5

1/5

[1, 0, 0, 0, 0]

Would you like to take it again
A: yes
B: no
B
test4
A:student
B:exita
Please enter your name web
Please enter your 4 digit ID to take the exam: 1234
What do we call a network whose elements may be separated by some distance? It usually involves two or more small networks and dedicated high-speed telephone lines.
(A) URL (Universal Resource Locator)
(B) LAN (Local Area Network)
(C) WAN (Wide Area Network)
(D) World Wide Web a
'DB' computer abbreviation usually means?
(A) Database
(B) Double Byte
(C) Data Block
(D) Driver Boot a
Who co-created the UNIX operating system in 1969 with Dennis Ritchie?
(A) Bjarne Stroustrup
(B) Steve Wozniak
(C) Ken Thompson
(D) Niklaus Wirth a
What is FMD?
(A) Fast-Ethernet Measuring Device
(B) Flashing Media Diode
(C) Fluorescent Multi-Layer Disc
(D) Flash Media Driver a
'.BAT' extension refers usually to what kind of file?
(A) Compressed Archive file
(B) System file
(C) Audio file
(D) Backup file a
1/5

1/5

[0, 1, 0, 0, 0]

would you like to take it again
A: yes
B: no
B

test5
A:student
B:exita
Please enter your name ned
Please enter your 4 digit ID to take the exam: 1234
'DB' computer abbreviation usually means?
(A) Database
(B) Double Byte
(C) Data Block
(D) Driver Boot a
What is the term to ask the computer to put information in order numerically or alphabetically?
(A) Crop
(B) Report
(C) Record
(D) Sort b
 'OS' computer abbreviation usually means?
(A) Order of Significance
(B) Open Software
(C) Operating System
(D) Optical Sensor c
What is the term to ask the computer to put information in order numerically or alphabetically?
(A) Crop
(B) Report
(C) Record
(D) Sort d
What do we call a network whose elements may be separated by some distance? It usually involves two or more small networks and dedicated high-speed telephone lines.
(A) URL (Universal Resource Locator)
(B) LAN (Local Area Network)
(C) WAN (Wide Area Network)
(D) World Wide Web b
3/5

3/5

[1, 0, 1, 1, 0]
would you like to take it again
A:yes
B:no
B
'''