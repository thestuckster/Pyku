
from Tkinter import *
from roku import Roku

roku = Roku.discover(timeout=5)[0]
apps = roku.apps

text = None


def main():

    window = Tk()
    # window.geometry("800x600")
    window.title("Pyku Controller")

    build_tk_window(window)
    mainloop()


def build_tk_window(window):

    text_box = Entry(window, textvariable=text)
    text_box.pack()

    enter_button = Button(window, text="enter", command= lambda: enter_search(text_box))
    enter_button.pack()

    home_button = Button(window, text="home", command=home)
    home_button.pack()

    down_button = Button(window, text="down", command=down)
    down_button.pack(side=BOTTOM)

    up_button = Button(window, text="up", command=up)
    up_button.pack(side=TOP)

    left_button = Button(window, text="left", command=left)
    left_button.pack(side=LEFT)

    right_button = Button(window, text="right", command=right)
    right_button.pack(side=RIGHT)

    ok_button = Button(window, text="ok", bg="green", command=select)
    ok_button.pack()




def home():
    roku.home()


def left():
    roku.left()


def right():
    roku.right()


def down():
    roku.down()


def up():
    roku.up()


def select():
    roku.select()


def enter_search(text_box):
    if text_box is not None:
        text = text_box.get()
        if text is not None:
            roku.literal(text)


if __name__ == "__main__":
    main()
else:
    print ("Error: This is not a library!")
