from gui import *


def main():
    window = Tk()
    window.title('Shape Calculator')
    window.geometry('700x425')
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
