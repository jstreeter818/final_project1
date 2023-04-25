from gui import *


def main():
    window = Tk()
    window.title('Shape Calculator')
    window.geometry('400x230')
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()