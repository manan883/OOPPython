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
        tst = chooseQuestion()
        t2 = chooseQuestion()
        self.q1 = chooseQuestion()
        self.q2 = chooseQuestion()
        self.q3 = chooseQuestion()
        self.q4 = chooseQuestion()
        self.q5 = chooseQuestion()
        print(tst + t2)
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
            else:
                continue
    def setExamScore(self):
        self.grade = self.counter
    def returnExamScore(self):
        return str(self.grade) + "/5"

class student(object):
    def __init__(self,id="xxxx",currentScore=0,highestScore=0):
        self.id = id
        self.currentScore = currentScore
        self.highestScore = highestScore
    def setID(self, id):
        self.id = id
    
    def takeQuiz(self):
        e = exam()
        e.makeExam()
        e.takeExam()
    
e = exam()
e.makeExam()
# print(e.q1+e.q2)
# e.takeExam()
# e.gradeExam()
# e.setExamScore()
# print(e.returnExamScore())