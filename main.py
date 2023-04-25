from gui import *


def main():
    window = Tk()
    window.title('Shape Calculator')
    window.geometry('600x300')
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()