import time
import sys
from tkinter import *
import tkinter.messagebox as msgbox
import io, pygame

version = "1.0"

root = Tk()
root.title("학원벨 " + version)
pygame.init()
def live_time():
    import time

    frame_time = LabelFrame(root, text="현재 시각")
    frame_time.grid(row=0, column=0, sticky=W+E+N+S, columnspan = 7)

    tm = time.localtime(time.time())
    if int(tm.tm_hour > 12):
        if tm.tm_min > 9:
            time = "오후 " + str(int(tm.tm_hour) - 12) + "시 " + str(tm.tm_min) + "분 " + str(tm.tm_sec) + "초 (0" + str(int(tm.tm_hour) - 12) +  ":"+ str(tm.tm_min) +")"
            label_test = Label(frame_time, text=time)
        else:
            time = "오후 " + str(int(tm.tm_hour) - 12) + "시 " + str(tm.tm_min) + "분 " + str(tm.tm_sec) + "초 (0" + str(int(tm.tm_hour) - 12) +  ":0"+ str(tm.tm_min) +")"
            label_test = Label(frame_time, text=time)
    else:
        if tm.tm_min > 9:
            time = "오전 " + str(tm.tm_hour) + "시 " + str(tm.tm_min) + "분 " + str(tm.tm_sec) + "초 (" + str(tm.tm_hour) +  ":"+ str(tm.tm_min) +")"
            label_test = Label(frame_time, text=time)
        else:
            time = "오전 " + str(tm.tm_hour) + "시 " + str(tm.tm_min) + "분 " + str(tm.tm_sec) + "초 (" + str(tm.tm_hour) +  ":0"+ str(tm.tm_min) +")"
            label_test = Label(frame_time, text=time)
    label_test.grid(row=0, column=1)
    label_test.configure(font=(70))
    root.after(1000, live_time)

root.after(100, live_time)

frame_schedule= LabelFrame(root, text="시작벨 스케줄")
frame_schedule.grid(row=1, column=0, columnspan=2, sticky=W+E+N+S)

put = Text(frame_schedule, width=15, height=15)
put.grid(row=1, column=1)

frame_schedule_end= LabelFrame(root, text="끝남벨 스케줄")
frame_schedule_end.grid(row=1, column=1, columnspan=2, sticky=W+E+N+S)

put1 = Text(frame_schedule_end, width=15, height=15)
put1.grid(row=1, column=0)

시작_음악_2 = io.open("data/시작 벨소리.txt", 'r', encoding="ANSI")
시작_음악_2 = 시작_음악_2.readlines()

끝남_음악_2 = io.open("data/끝남 벨소리.txt", 'r', encoding="ANSI")
끝남_음악_2 = 끝남_음악_2.readlines()

frame_music = LabelFrame(root, text="벨소리")
frame_music.grid(row=3, column=0, columnspan=2, sticky=W+E+N+S)

days = LabelFrame(root, text="수업 요일")
days.grid(row=2, column=0, sticky=W+E+N+S, columnspan=4)

sunyi = IntVar()
suny = Checkbutton(days, text="일")
suny.grid(row=1, column=1)

moni = IntVar()
mon = Checkbutton(days, text="월")
mon.grid(row=1, column=2)
mon.select()

tuesi = IntVar()
tues = Checkbutton(days, text="화")
tues.grid(row=1, column=3)
tues.select()

wedni = IntVar()
wedn = Checkbutton(days, text="수")
wedn.grid(row=1, column=4)
wedn.select()

thursi = IntVar()
thurs = Checkbutton(days, text="목")
thurs.grid(row=1, column=5)
thurs.select()

frii = IntVar()
fri = Checkbutton(days, text="금")
fri.grid(row=2, column=1)
fri.select()

sati = IntVar()
sat = Checkbutton(days, text="토")
sat.grid(row=2, column=2)

print(sati.get())
label1 = Label(frame_music, text = "시작 벨소리")
ent = Entry(frame_music, width=20)

start2 = io.open("data/시작벨 스케줄.txt", 'r', encoding="ANSI")
start2_lines = start2.readlines()

counting = 0
for line in start2_lines:
    if not start2_lines[counting] == "\n" and not start2_lines[counting] == "":
        put.insert(END, start2_lines[counting])
    counting = counting + 1

end2 = io.open("data/끝남벨 스케줄.txt", 'r', encoding="ANSI")
end2_lines = end2.readlines()

counting2 = 0
for line in end2_lines:
    if not end2_lines[counting2] == "\n" and not end2_lines[counting2] == "":
        put1.insert(END, end2_lines[counting2])
    counting2 = counting2 + 1

label1.grid(row=1, column=0)
ent.grid(row=1, column=1)

ent.insert(0, 시작_음악_2)

label2 = Label(frame_music, text = "끝남 벨소리")
ent1 = Entry(frame_music, width=20)

label2.grid(row=2, column=0)
ent1.grid(row=2, column=1)
ent1.insert(0, 끝남_음악_2)

def btncmd():
    with io.open("data/시작벨 스케줄.txt", 'r+', encoding="ANSI") as w1:
        w1.truncate(0)
    w12 = io.open("data/시작벨 스케줄.txt", 'w', encoding="ANSI")
    data2 = put.get("1.0", END).split("\n")
    c = 0
    for line in data2:
        w12.write(data2[c] + '\n')
        c = c + 1
    w12.close()

    with io.open("data/끝남벨 스케줄.txt", 'r+', encoding="ANSI") as w2:
        w2.truncate(0)
    w13 = io.open("data/끝남벨 스케줄.txt", 'w', encoding="ANSI")
    data3 = put1.get("1.0", END).split("\n")
    c2 = 0
    for line in data3:
        w13.write(data3[c2] + '\n')
        c2 = c2 + 1
    w13.close()

    w1 = io.open("data/끝남 벨소리.txt", 'w', encoding="ANSI")
    data = ent1.get()
    w1.write(data)
    w1.close()

    w2 = io.open("data/시작 벨소리.txt", 'w', encoding="ANSI")
    data = ent.get()
    w2.write(data)
    w2.close()

    msgbox.showinfo("알림", "정상적으로 저장 되었습니다.")

def btncmd4():
    끝남_음악3 = io.open("data/끝남 벨소리.txt", 'r', encoding="ANSI")
    끝남_음악3 = 끝남_음악3.readlines()
    sd = pygame.mixer.Sound(끝남_음악3[0])
    sd.play()

def btncmd5():
    msgbox.showinfo("알림", "준비되지 않았습니다.")

def btncmd2():
    response = msgbox.askyesno("경고", "초기화 후, 되돌릴 수 없습니다. 계속 하시겠습니까?")

    if response == 1:
        ent1.delete(0, END)
        ent.delete(0, END)
        put1.delete("1.0", END)
        put.delete("1.0", END)

        with io.open("data/시작 벨소리.txt", 'r+', encoding="ANSI") as f1:
            f1.truncate(0)

        with io.open("data/끝남 벨소리.txt", 'r+', encoding="ANSI") as f4:
            f4.truncate(0)

        with io.open("data/시작벨 스케줄.txt", 'r+', encoding="ANSI") as f3:
            f3.truncate(0)

        with io.open("data/끝남벨 스케줄.txt", 'r+', encoding="ANSI") as f2:
            f2.truncate(0)

        msgbox.showinfo("알림", "정상적으로 초기화 되었습니다.")

    elif response == 0:
        return -1

frame_tool = LabelFrame(root, text="툴")
frame_tool.grid(row=5, column=0, columnspan=2, sticky=W+E+N+S)

btn2 = Button(frame_tool, width=14, text="모두 초기화", command=btncmd2)
btn2.grid(row=5, column=0)

btn1 = Button(frame_tool, width=14, text="저장하기", command=btncmd)
btn1.grid(row=5, column=1, sticky=W+E+N+S)

btn1 = Button(frame_tool, width=14, text="지금 벨 울리기", command=btncmd4)
btn1.grid(row=6, column=0, columnspan=2, sticky=W+E+N+S)

def loop():
    tm = time.localtime(time.time())

    start = io.open("data/시작벨 스케줄.txt", 'r', encoding="ANSI")
    start_lines = start.readlines()

    end = io.open("data/끝남벨 스케줄.txt", 'r', encoding="ANSI")
    end_lines = end.readlines()

    시작_음악 = io.open("data/시작 벨소리.txt", 'r', encoding="ANSI")
    시작_음악 = 시작_음악.readlines()

    끝남_음악 = io.open("data/끝남 벨소리.txt", 'r', encoding="ANSI")
    끝남_음악 = 끝남_음악.readlines()
    
    counts = 0
    for line in start_lines:
        from datetime import datetime
        date = str(tm.tm_year) +"-"+str(tm.tm_mon)+'-'+str(tm.tm_mday)
        datetime_date = datetime.strptime(date, '%Y-%m-%d')
        if (int(sunyi.get()) == 1 and int(datetime_date.weekday()) == 6) or (int(moni.get()) == 1 and int(datetime_date.weekday()) == 0) or (int(tuesi.get()) == 1 and int(datetime_date.weekday()) == 1) or (int(wedni.get()) == 1 and int(datetime_date.weekday()) == 2) or (int(thursi.get()) == 1 and int(datetime_date.weekday()) == 3) or (int(frii.get()) == 1 and int(datetime_date.weekday()) == 4) or (int(sati.get()) == 1 and int(datetime_date.weekday()) == 5):
            print("h")

      #  print(datetime_date.weekday())
        일정_시작 = start_lines[counts].strip()
        일정_시작 = 일정_시작.replace("시 ", ":").replace("분", ":")
        일정_시작 = 일정_시작.split(':')
        if 일정_시작[0] != "":
            if '오후' in 일정_시작[0]:
                일정_시작[0] = str(int(일정_시작[0].replace("오후 ", "")) + 12)
            elif '오전' in 일정_시작[0]:
                일정_시작[0] = 일정_시작[0].replace("오전 ", "")
        if 일정_시작[0] != "":
            if int(일정_시작[0]) == int(tm.tm_hour) and int(일정_시작[1]) == int(tm.tm_min) and 0 == int(tm.tm_sec):
                if (int(일정_시작[0]) > 12):
                    print('(시작벨) 오후 ' + str(int(일정_시작[0]) - 12) + '시 ' + str(int(일정_시작[1])) + '분 0초에 울려야 하는 벨이 울렸습니다')
                else:
                    print('(시작벨) 오전 ' + str(int(일정_시작[0])) + '시 ' + str(int(일정_시작[1])) + '분 0초에 울려야 하는 벨이 울렸습니다')
                sd = pygame.mixer.Sound(시작_음악[0])
                sd.play()
        counts = counts + 1

    counts2 = 0
    for lines in end_lines:
        일정_끝남 = end_lines[counts2].strip()
        일정_끝남 = 일정_끝남.replace("시 ", ":").replace("분", ":")
        일정_끝남 = 일정_끝남.split(':')
        if 일정_끝남[0] != "":
            if '오후' in 일정_끝남[0]:
                일정_끝남[0] = str(int(일정_끝남[0].replace("오후 ", "")) + 12)
            elif '오전' in 일정_끝남[0]:
                일정_끝남[0] = 일정_끝남[0].replace("오전 ", "")
        if 일정_끝남[0] != "":
            if int(일정_끝남[0]) == int(tm.tm_hour) and int(일정_끝남[1]) == int(tm.tm_min) and 0 == int(tm.tm_sec):
                if (int(일정_끝남[0]) > 12):
                    print('(끝남벨) 오후 ' + str(int(일정_끝남[0]) - 12) + '시 ' + str(int(일정_끝남[1])) + '분 0초에 울려야 하는 벨이 울렸습니다')
                else:
                    print('(끝남벨) 오전 ' + str(int(일정_끝남[0])) + '시 ' + str(int(일정_끝남[1])) + '분 0초에 울려야 하는 벨이 울렸습니다')
                sd = pygame.mixer.Sound(끝남_음악[0])
                sd.play()
        counts2 = counts2 + 1

    start.close()
    end.close()

    root.after(2000, loop)

root.after(2000, loop)

root.mainloop()