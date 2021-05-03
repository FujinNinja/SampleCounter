import tkinter
from tkinter import font
from PIL import Image, ImageTk

def btn1_click():
    label1["text"] = str(int(label1["text"]) + 1)

def btn2_click():
    label1["text"] = str(int(label1["text"]) - 1)

def btn3_click():
    label1["text"] = "0"

window = tkinter.Tk()
window.title(u"カウンター")
window.geometry("500x380")

print(font.families())
labelFrame1font = font.Font(family='07やさしさゴシック', size=40, weight='bold')
labelFrame1 = tkinter.LabelFrame(
    window,
    text="現在のカウント",
    font=labelFrame1font,
    width = 460,
    height = 200,
    relief = 'ridge',
    borderwidth = 4
)
labelFrame1.grid(
    row=0,
    column=0,
    columnspan=3,
    padx=20,
    pady=10
)
labelFrame1.propagate(0)

label1font = font.Font(family='07やさしさゴシック', size=100, weight='bold')
label1 = tkinter.Label(
    labelFrame1,
    font=label1font,
    text="0"
)

label1.pack(
)

# サイズを変更する
resizeImg = Image.open("eye.jpg").resize((100, 100))

# 白色を作成する
whiteImg = Image.new('RGB', resizeImg.size, (255, 255, 255))

# 30%透過して重ねる
blendImg = Image.blend(resizeImg, whiteImg, 0.3)

# 画像表示
displayImg = ImageTk.PhotoImage(blendImg)

buttonfont = font.Font(family='07やさしさゴシック', size=40, weight='bold')

# １つ目のボタン作成
button1 = tkinter.Button(
    window,
    compound="center",
    font=buttonfont,
    text="+1",
    image=displayImg,
    width=100,
    height=100,
    bg="orange",
    command=btn1_click
)

# ２つ目のボタン作成
button2 = tkinter.Button(
    window,
    compound="center",
    font=buttonfont,
    text="-1",
    image=displayImg,
    width=100,
    height=100,
    bg="skyblue",
    command=btn2_click
)

# サイズを変更する
resizeImg2 = Image.open("eye.jpg").resize((150, 100))

# 白色を作成する
whiteImg2 = Image.new('RGB', resizeImg2.size, (255, 255, 255))

# 30%透過して重ねる
blendImg2 = Image.blend(resizeImg2, whiteImg2, 0.3)

# 画像表示
displayImg2 = ImageTk.PhotoImage(blendImg2)

# ３つ目のボタン作成
button3 = tkinter.Button(
    window,
    compound="center",
    font=buttonfont,
    text="reset",
    image=displayImg2,
    width=150,
    height=100,
    bg="green",
    command=btn3_click
)

button1.grid(
    row=1,
    column=0,
    columnspan=1,
    padx=20,
    pady=20
)

button2.grid(
    row=1,
    column=1,
    columnspan=1,
    padx=20,
    pady=20
)

button3.grid(
    row=1,
    column=2,
    columnspan=1,
    padx=20,
    pady=20
)

window.mainloop()

