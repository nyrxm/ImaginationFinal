import js
p5 = js.window

Time_is_checked = False
Label_is_read = False
Paper_is_checked = False
Realise_No_Exam = False

NPC = 'DAD:'

program_state = 'START'

p5.imageMode(p5.CENTER)
p5.textAlign(p5.CENTER)
font = p5.loadFont('Terminal.ttf')
font2 = p5.loadFont('helvetica_medium.ttf')

AnomolyImg = p5.loadImage('Anomoly.png');
BadendImg = p5.loadImage('BadendV2.png');
CowImg = p5.loadImage('Cow.png');
DadImg = p5.loadImage('Dad.png');
DrivingImg = p5.loadImage('Driving.png');
EncounterImg = p5.loadImage('Encounter.png');
ExamImg = p5.loadImage('Exam.png');
LabelImg = p5.loadImage('Label.png');
LynnImg = p5.loadImage('Lynn.png');
QuestionsImg = p5.loadImage('Questions.png');
RepeatImg = p5.loadImage('Repeat.png');
RoadImg = p5.loadImage('Road.png');
S01C = p5.loadImage('S01C.png');
S02C = p5.loadImage('S02CV2.png');
S05C = p5.loadImage('S05C.png');
S08C = p5.loadImage('S08C.png');
S14C = p5.loadImage('S14CV2.png');
S18CF = p5.loadImage('S18CF.png');
S18CT = p5.loadImage('S18CT.png');
S21C = p5.loadImage('S21C.png');
S22C = p5.loadImage('S22C.png');
S23C = p5.loadImage('S23C.png');
StartImg = p5.loadImage('Start.png');
WakingupImg = p5.loadImage('Wakingup.png');
wakingup01Img = p5.loadImage('wakingup01.png');
wakingup02Img = p5.loadImage('wakingup02.png');
wakingup03Img = p5.loadImage('wakingup03.png');
WatchImg = p5.loadImage('Watch.png');
WoodsImg = p5.loadImage('Woods.png');
ZombiesImg = p5.loadImage('Zombies.png');
Zombies2Img = p5.loadImage('Zombies2.png');
HEImg = p5.loadImage('HE.png');



def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    global Time_is_checked
    global Label_is_read
    global Paper_is_checked
    global Realise_No_Exam
    
    global program_state

    global NPC
    p5.background(255)

    p5.fill(255)
    p5.textFont(font2)
    p5.textSize(12)
    
    if(program_state == 'START'):
        p5.image(StartImg, 150, 150)
        p5.textSize(18)
        p5.text('CLICK TO START', 150, 45)
        p5.textSize(12)
        p5.text('Hmm...I love boba tea...', 150, 280)
    elif(program_state == 'S01'):
        p5.image(StartImg, 150, 150)
        p5.text('VOICE: How’s your drink?', 150, 280)
    elif(program_state == 'S01C'):
        p5.image(StartImg, 150, 150)
        p5.image(S01C, 150, 150)
    elif(program_state == 'S02'):
        p5.image(DadImg, 150, 150)
        p5.text('DAD: Mine’s too sweet to my liking.', 150, 280)
    elif(program_state == 'S02C'):
        p5.image(DadImg, 150, 150)
        p5.image(S02C, 150, 150)
    elif(program_state == 'S03'):
        p5.image(LabelImg, 150, 150)
        p5.text('[Can’t See Clearly]', 150, 280)
    elif(program_state == 'S04'):
        p5.image(DadImg, 150, 150)
        p5.text('DAD: They didnt ask me?', 150, 280)
    elif(program_state == 'S05'):
        p5.image(DadImg, 150, 150)
        p5.text('DAD: Lets go pick up your sister.', 150, 280)
    elif(program_state == 'S05C'):
        p5.image(DadImg, 150, 150)
        p5.image(S05C, 150, 150)
    elif(program_state == 'S06'):
        p5.image(WatchImg, 150, 150)
        p5.text('[Can’t See Clearly]', 150, 280)
    elif(program_state == 'S07'):
        p5.image(RoadImg, 150, 150)
        p5.text(str(NPC) + ' Drive slower...', 150, 280)
    elif(program_state == 'S08'):
        p5.image(DrivingImg, 150, 150)
        p5.text(str(NPC) + ' Whats that on the road?', 150, 280)
    elif(program_state == 'S08C'):
        p5.image(AnomolyImg, 150, 150)
        p5.image(S08C, 150, 150)
    elif(program_state == 'S09'):
        p5.image(ZombiesImg, 150, 150)
        p5.text('Wait...is that...ZOMBIES...!?', 150, 280)
    elif(program_state == 'S10'):
        p5.image(EncounterImg, 150, 150)
        p5.text('We have to run!', 150, 280)
    elif(program_state == 'S11'):
        p5.image(WoodsImg, 150, 150)
        p5.text(str(NPC) + ' Into the woods...!', 150, 280)
    elif(program_state == 'S12'):
        p5.image(Zombies2Img, 150, 150)
        p5.text('They are catching up!', 150, 280)
    elif(program_state == 'BE'):
        p5.image(BadendImg, 150, 150)
        p5.text('NOOOooooooOOoo————!!', 150, 280)
    elif(program_state == 'S13'):
        p5.image(CowImg, 150, 150)
        p5.text(str(NPC) + ' Do you know a cow have four stomachs?', 150, 280)
    elif(program_state == 'S14'):
        p5.image(QuestionsImg, 150, 150)
        p5.text('I remember the teacher talking about this in lecture...', 150, 280)
    elif(program_state == 'S14C'):
        p5.image(QuestionsImg, 150, 150)
        p5.image(S14C, 150, 150) 
    elif(program_state == 'S15'):
        p5.image(ExamImg, 150, 150)
        p5.text('Its approaching the time limit for the exam....', 150, 280)
    elif(program_state == 'S16'):
        p5.image(ExamImg, 150, 150)
        p5.text('And I didn’t write a word...', 150, 280)
    elif(program_state == 'S17'):
        p5.image(ExamImg, 150, 150)
        p5.text('WHAT WOULD I DO NOW?', 150, 280)
    elif(program_state == 'S18'):
        p5.image(ExamImg, 150, 150)
        p5.text('[Look at Classroom]', 150, 280)
    elif(program_state == 'S18C'):
        p5.image(ExamImg, 150, 150)
        p5.image(S18CF, 150, 150)
        if(Time_is_checked == True) and (Label_is_read == True) and (Paper_is_checked == True) and (Realise_No_Exam == True):
            p5.image(S18CT, 150, 150)
    elif(program_state == 'S19'):
        p5.image(RepeatImg, 150, 150)
        p5.text('[Look at Menu]', 150, 280)
    elif(program_state == 'Wakingup'):
        p5.image(WakingupImg, 150, 150)
    elif(program_state == 'S20'):
        p5.image(QuestionsImg, 150, 150)
        p5.text('Can’t see clearly...', 150, 280)
    elif(program_state == 'S21'):
        p5.image(RoadImg, 150, 150)
        p5.text(str(NPC) + ' Are you ready for the exam?', 150, 260)
    elif(program_state == 'S21C'):
        p5.image(RoadImg, 150, 150)
        p5.image(S21C, 150, 150)
    elif(program_state == 'S22'):
        p5.image(LynnImg, 150, 150)
        p5.text('LYNN: What do you have?', 150, 260)
    elif(program_state == 'S22C'):
        p5.image(LynnImg, 150, 150)
        p5.image(S22C, 150, 150)
    elif(program_state == 'S23'):
        p5.image(LynnImg, 150, 150)
        p5.text('LYNN: Noon break is almost up.', 150, 250)
        p5.text('We should go back to the classroom.', 150, 270)
    elif(program_state == 'S23C'):
        p5.image(RoadImg, 150, 150)
        p5.image(S23C, 150, 150)
    elif(program_state == 'S24'):
        p5.image(LabelImg, 150, 150)
        p5.text('[Can’t Read Clearly]', 150, 260)
    elif(program_state == 'S25'):
        p5.image(WatchImg, 150, 150)
        p5.text('Can’t read clearly...', 150, 260)
    elif(program_state == 'S26'):
        p5.image(RoadImg, 150, 150)
        p5.text('what do you say we skip class today?', 150, 260)
    elif(program_state == 'wakingup01'):
        p5.image(wakingup01Img, 150, 150)
    elif(program_state == 'wakingup02'):
        p5.image(wakingup02Img, 150, 150)
    elif(program_state == 'wakingup03'):
        p5.image(wakingup03Img, 150, 150)
        p5.text('What a dream...', 150, 260)
    elif(program_state == 'HE'):
        p5.image(HEImg, 150, 150)
        p5.textSize(24)
        p5.fill(214, 128, 40)
        p5.text('Congratulation!', 150, 150)
        p5.fill(0)
        p5.textSize(12)
        p5.text('You have successfully woken up', 150, 250)
        p5.text('from the endless nightmare.', 150, 270)
        p5.textSize(15)
        p5.fill(100, 100, 100)
        p5.text('Click to Restart', 150, 175)
        p5.fill(255)
        

def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    global program_state

    global NPC

    global Time_is_checked
    global Label_is_read
    global Paper_is_checked
    global Realise_No_Exam
    
    if(program_state == 'START'):
        program_state = 'S01'
    elif(program_state == 'S01'):
        program_state = 'S01C'
    elif(program_state == 'S01C'):
        if(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 46) and (p5.mouseY < 105):
            program_state = 'S02'
            NPC = 'DAD:'
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 124) and (p5.mouseY < 184):
            program_state = 'S22'
            NPC = 'LYNN:'
    elif(program_state == 'S02'):
        program_state = 'S02C'
    elif(program_state == 'S02C'):
        if(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 46) and (p5.mouseY < 105):
            program_state = 'S03'
            Label_is_read = True
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 124) and (p5.mouseY < 184):
            program_state = 'S04'
        #elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 200) and (p5.mouseY < 258):
    elif(program_state == 'S03'):
        program_state = 'S02C'
    elif(program_state == 'S04'):
        program_state = 'S05'
    elif(program_state == 'S05'):
        program_state = 'S05C'
    elif(program_state == 'S05C'):
        if(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 46) and (p5.mouseY < 105):
            program_state = 'S07'
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 124) and (p5.mouseY < 184):
            program_state = 'S21'
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 200) and (p5.mouseY < 258):
            program_state = 'S06'
            Time_is_checked = True
    elif(program_state == 'S06'):
        program_state = 'S05C'
    elif(program_state == 'S07'):
        program_state = 'S08'
    elif(program_state == 'S08'):
        program_state = 'S08C'
    elif(program_state == 'S08C'):
        if(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 46) and (p5.mouseY < 105):
            program_state = 'S09'
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 124) and (p5.mouseY < 184):
            program_state = 'S13'
    elif(program_state == 'S09'):
        program_state = 'S10'
    elif(program_state == 'S10'):
        program_state = 'S11'
    elif(program_state == 'S11'):
        program_state = 'S12'
    elif(program_state == 'S12'):
        program_state = 'BE'
        Time_is_checked = False
        Label_is_read = False
        Paper_is_checked = False
        Realise_No_Exam = False
    elif(program_state == 'BE'):
        program_state = 'START'
    elif(program_state == 'S13'):
        program_state = 'S14'
    elif(program_state == 'S14'):
        program_state = 'S14C'
    elif(program_state == 'S14C'):
        if(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 46) and (p5.mouseY < 105):
            program_state = 'S15'
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 124) and (p5.mouseY < 184):
            program_state = 'S18'
            Realise_No_Exam = True
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 200) and (p5.mouseY < 258):
            program_state = 'S20'
            Paper_is_checked = True
    elif(program_state == 'S20'):
        program_state = 'S14C'
    elif(program_state == 'S15'):
        program_state = 'S16'
    elif(program_state == 'S16'):
        program_state = 'S17'
    elif(program_state == 'S17'):
        program_state = 'BE'
    elif(program_state == 'S18'):
        program_state = 'S18C'
    elif(program_state == 'S18C'):
        if(Time_is_checked == True) and (Label_is_read == True) and (Paper_is_checked == True) and (Realise_No_Exam == True):
            if(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 46) and (p5.mouseY < 105):
                program_state = 'S19'
            elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 124) and (p5.mouseY < 184):
                program_state = 'Wakingup'
        else:
            if(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 46) and (p5.mouseY < 105):
                program_state = 'S19'
                Time_is_checked = False
                Label_is_read = False
                Paper_is_checked = False
                Realise_No_Exam = False
    elif(program_state == 'S19'):
        program_state = 'START'
    elif(program_state == 'S21'):
        program_state = 'S21C'
    elif(program_state == 'S21C'):
        if(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 46) and (p5.mouseY < 105):
            program_state = 'S14'
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 124) and (p5.mouseY < 184):
            program_state = 'S07'
    elif(program_state == 'S22'):
        program_state = 'S22C'
    elif(program_state == 'S22C'):
        if(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 46) and (p5.mouseY < 105):
            program_state = 'S23'
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 124) and (p5.mouseY < 184):
            program_state = 'S24'
            Label_is_read = True
    elif(program_state == 'S24'):
        program_state = 'S22C'
    elif(program_state == 'S23'):
        program_state = 'S23C'
    elif(program_state == 'S23C'):
        if(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 46) and (p5.mouseY < 105):
            program_state = 'S21'
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 124) and (p5.mouseY < 184):
            program_state = 'S25'
            Time_is_checked = True
        elif(p5.mouseX < 254) and (p5.mouseX > 45) and (p5.mouseY > 200) and (p5.mouseY < 258):
            program_state = 'S08'
    elif(program_state == 'S25'):
        program_state = 'S23C'
    elif(program_state == 'Wakingup'):
        program_state = 'wakingup01'
    elif(program_state == 'wakingup01'):
        program_state = 'wakingup02'
    elif(program_state == 'wakingup02'):
        program_state = 'wakingup03'
    elif(program_state == 'wakingup03'):
        program_state = 'HE'
        Time_is_checked = False
        Label_is_read = False
        Paper_is_checked = False
        Realise_No_Exam = False
    elif(program_state == 'HE'):
        program_state = 'START'
        


