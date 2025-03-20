from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from report import reportClass
import os
from result import ResultClass

class RGM:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.config(bg="white")
        self.root.geometry("1350x700+0+0")

        # Load logo image
        self.logo_img = Image.open("images/logo.png")
        self.logo_img = self.logo_img.resize((50, 50), Image.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(self.logo_img)

        # Title with logo
        title = Label(
            self.root, text="Student Result Management System", padx=10, compound=LEFT,
            image=self.logo_img, font=("goudy old style", 20, "bold"),
            bg="orange", fg="#262626"
        )
        title.place(x=0, y=0, relwidth=1, height=50)

        # Menu Frame (Grid Layout for Responsive Design)
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1300, height=80)

        # Configure grid layout
        M_Frame.columnconfigure((0, 1, 2, 3, 4,5), weight=1)  # All columns get equal weight

        # Menu Buttons (Auto-Resizing)
        btn_course = Button(M_Frame, text="Course", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                            cursor="hand2", command=self.add_course)
        btn_course.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        btn_student = Button(M_Frame, text="Student", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                             cursor="hand2", command=self.add_student)
        btn_student.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        btn_result = Button(M_Frame, text="Result", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                            cursor="hand2", command=self.add_result)
        btn_result.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        btn_view = Button(M_Frame, text="View Students Result", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                            cursor="hand2", command=self.add_report)
        btn_view.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

        btn_logout = Button(M_Frame, text="Logout", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                            cursor="hand2")
        btn_logout.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)

        btn_exit = Button(M_Frame, text="Exit", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2", command=root.quit)
        btn_exit.grid(row=0, column=5, sticky="nsew", padx=5, pady=5)

        # Background Image
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=400, y=180, width=920, height=350)

        # Update Details
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20),
                                bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20),
                                 bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20),
                                bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        # Footer
        footer = Label(self.root, text="SRMS - Student Result Management System\nContact us for technical issues: 7807425002",
                       font=("goudy old style", 12), bg="#033054", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    # Functions to open new windows
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = RGM(root)
    root.mainloop()
