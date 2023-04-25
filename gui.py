from tkinter import *
import area


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_shape = Frame(self.window)
        self.label_operation = Label(self.frame_shape, text='Shape\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_circle = Radiobutton(self.frame_shape, text='Circle', variable=self.radio_1, value=1,
                                        command=self.shape)
        self.radio_square = Radiobutton(self.frame_shape, text='Square', variable=self.radio_1, value=2,
                                        command=self.shape)
        self.radio_rectangle = Radiobutton(self.frame_shape, text='Rectangle', variable=self.radio_1, value=3,
                                           command=self.shape)
        self.radio_triangle = Radiobutton(self.frame_shape, text='Triangle', variable=self.radio_1, value=4,
                                          command=self.shape)
        self.radio_trapezoid = Radiobutton(self.frame_shape, text='Trapezoid', variable=self.radio_1, value=5,
                                           command=self.shape)
        self.radio_rhombus = Radiobutton(self.frame_shape, text='Rhombus', variable=self.radio_1, value=6,
                                         command=self.shape)
        self.radio_ellipse = Radiobutton(self.frame_shape, text='Ellipse', variable=self.radio_1, value=7,
                                         command=self.shape)
        self.label_operation.pack(side='left', padx=5)
        self.radio_circle.pack(side='left')
        self.radio_square.pack(side='left')
        self.radio_rectangle.pack(side='left')
        self.radio_triangle.pack(side='left')
        self.radio_trapezoid.pack(side='left')
        self.radio_rhombus.pack(side='left')
        self.radio_ellipse.pack(side='left')
        self.frame_shape.pack(anchor='w', pady=10)

        # First number
        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first)
        self.entry_first = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=20, side='left')
        self.entry_first.pack(padx=20, side='left')
        self.frame_first.pack(anchor='w', pady=10)
        self.entry_first.pack_forget()

        # Second number
        self.frame_second = Frame(self.window)
        self.label_second = Label(self.frame_second)
        self.entry_second = Entry(self.frame_second, width=40)
        self.label_second.pack(padx=20, side='left')
        self.entry_second.pack(padx=20, side='left')
        self.frame_second.pack(anchor='w', pady=10)
        self.entry_second.pack_forget()

        # Third number
        self.frame_third = Frame(self.window)
        self.label_third = Label(self.frame_third)
        self.entry_third = Entry(self.frame_third, width=40)
        self.label_third.pack(padx=20, side='left')
        self.entry_third.pack(padx=20, side='left')
        self.frame_third.pack(anchor='w', pady=10)
        self.entry_third.pack_forget()

        # Results label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Compute button
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='COMPUTE', command=self.compute)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def shape(self):
        self.entry_first.delete(0, END)
        self.entry_second.delete(0, END)
        self.entry_third.delete(0, END)
        self.label_result.config(text='')
        self.entry_first.pack()
        shape = self.radio_1.get()

        if shape == 1:
            self.label_first.config(text='Radius')
            self.label_second.config(text='')
            self.label_third.pack_forget()
            self.entry_second.pack_forget()
            self.entry_third.pack_forget()
        elif shape == 2:
            self.label_first.config(text='Side')
            self.label_second.config(text='')
            self.label_third.pack_forget()
            self.entry_second.pack_forget()
            self.entry_third.pack_forget()
        elif shape == 3:
            self.label_first.config(text='Length')
            self.label_second.config(text='Width')
            self.label_third.pack_forget()
            self.entry_second.pack()
            self.entry_third.pack_forget()
        elif shape == 4:
            self.label_first.config(text='Base')
            self.label_second.config(text='Height')
            self.label_third.pack_forget()
            self.entry_second.pack()
            self.entry_third.pack_forget()
        elif shape == 5:
            self.label_third.pack(padx=20, side='left')
            self.label_first.config(text='Base')
            self.label_second.config(text='Base(2)')
            self.label_third.config(text='Height')
            self.entry_second.pack()
            self.entry_third.pack()
        elif shape == 6:
            self.label_first.config(text='Width')
            self.label_second.config(text='Height')
            self.label_third.pack_forget()
            self.entry_second.pack()
            self.entry_third.pack_forget()
        elif shape == 7:
            self.label_first.config(text='Axis')
            self.label_second.config(text='Axis(2)')
            self.label_third.pack_forget()
            self.entry_second.pack()
            self.entry_third.pack_forget()

    def compute(self):
        try:
            first_num = self.entry_first.get()
            second_num = self.entry_second.get()
            third_num = self.entry_third.get()
            shape = self.radio_1.get()

            if shape == 1:
                self.label_result.config(text=f'Circle area = {area.circle(first_num)}')
            elif shape == 2:
                self.label_result.config(text=f'Square area = {area.square(first_num)}')
            elif shape == 3:
                self.label_result.config(text=f'Rectangle area = {area.rectangle(first_num, second_num)}')
            elif shape == 4:
                self.label_result.config(text=f'Triangle area = {area.triangle(first_num, second_num)}')
            elif shape == 5:
                self.label_result.config(text=f'Trapezoid area = {area.trapezoid(first_num, second_num, third_num)}')
            elif shape == 6:
                self.label_result.config(text=f'Rhombus area = {area.rhombus(first_num, second_num)}')
            elif shape == 7:
                self.label_result.config(text=f'Ellipse area = {area.ellipse(first_num, second_num)}')
            else:
                self.label_result.config(text='No operation selected')
        except ValueError:
            self.label_result.config(text='Enter numeric values')
        except TypeError:
            self.label_result.config(text='Values must be positive')
