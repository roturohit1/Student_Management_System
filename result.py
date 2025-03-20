from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.config(bg="white")
        self.root.geometry("1200x480+80+170")
        self.root.focus_force()
        
        # Logo and Title
        try:
            # Try to load a logo image
            self.logo_img = Image.open("images/logo.png")
            self.logo_img = self.logo_img.resize((50, 50), Image.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(self.logo_img)
            title = Label(
                self.root, text="Add Student Result", padx=10, compound=LEFT,
                image=self.logo_img, font=("goudy old style", 20, "bold"),
                bg="orange", fg="#262626"
            )
        except Exception as ex:
            # If logo image fails to load, use text-only title
            title = Label(
                self.root, text="Add Student Result", font=("goudy old style", 20, "bold"),
                bg="orange", fg="#262626"
            )
            
        title.place(x=10, y=15, width=1180, height=50)
        
        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        
        # Fetch roll numbers from database
        self.fetch_roll()

        # widgets
        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 15, 'bold'), bg='white').place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg='white').place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, 'bold'), bg='white').place(x=50, y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, 'bold'), bg='white').place(x=50, y=280)   
        lbl_full_marks = Label(self.root, text="Full marks", font=("goudy old style", 15, 'bold'), bg='white').place(x=50, y=360)
    
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=("goudy old style", 15, 'bold'), state='readonly', justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")
        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=500, y=100, width=100, height=28)
        
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, 'bold'), bg='lightyellow', state="readonly").place(x=280, y=160, width=320)
        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, 'bold'), bg='lightyellow', state="readonly").place(x=280, y=220, width=320)
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, 'bold'), bg='lightyellow').place(x=280, y=280, width=320)
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, 'bold'), bg='lightyellow').place(x=280, y=340, width=320)
        
        # buttons
        btn_add = Button(self.root, text='Submit', font=("times new roman", 15), bg="lightgreen", activebackground="lightgreen", cursor="hand2", command=self.add)
        btn_add.place(x=150, y=400, width=110, height=40)
        btn_clear = Button(self.root, text='Clear', font=("times new roman", 15), bg="lightgray", activebackground="lightgray", cursor="hand2",command=self.clear)
        btn_clear.place(x=270, y=400, width=110, height=40)
        
        # Result image
        try:
            self.bg_img = Image.open("images/result.jpg")
            self.bg_img = self.bg_img.resize((500, 350), Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
            self.lbl_bg = Label(self.root, image=self.bg_img).place(x=650, y=100)
        except Exception as ex:
            # Create visually appealing placeholder if image is not found
            self.placeholder_frame = Frame(self.root, bg="#f0f0f0", bd=2, relief=RIDGE)
            self.placeholder_frame.place(x=650, y=100, width=500, height=350)
            
            # Add some decorative elements to the placeholder frame
            title_label = Label(self.placeholder_frame, text="Student Result System", 
                              font=("times new roman", 20, "bold"), bg="#033054", fg="white")
            title_label.pack(fill=X)
            
            info_text = "This system allows you to:\n\n• Add student results\n• Track academic performance\n• Calculate percentages automatically\n• Maintain complete student records"
            Label(self.placeholder_frame, text=info_text, font=("times new roman", 14), 
                  bg="#f0f0f0", justify=LEFT, padx=20, pady=20).pack(fill=BOTH, expand=True)
    
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")
    
    def fetch_roll(self):
        con = sqlite3.connect(database="pythonproject.db")
        cur = con.cursor()
        try:
           cur.execute("select roll from student")
           rows = cur.fetchall()  
           if len(rows) > 0:
               for row in rows:
                   self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
    
    def search(self):
        con = sqlite3.connect(database="pythonproject.db")
        cur = con.cursor()
        try:
           cur.execute(f"select name, course from student where roll=?", (self.var_roll.get(),))
           row = cur.fetchone() 
           if row != None: 
              self.var_name.set(row[0])
              self.var_course.set(row[1])
           else:
               messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def add(self):
        con = sqlite3.connect(database="pythonproject.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please first search student record", parent=self.root)
            elif self.var_marks.get() == "" or self.var_full_marks.get() == "":
                messagebox.showerror("Error", "Please enter marks", parent=self.root)
            else:
                try:
                    # Make sure marks are valid numbers
                    marks_ob = float(self.var_marks.get())
                    full_marks = float(self.var_full_marks.get())
                    
                    if marks_ob > full_marks:
                        messagebox.showerror("Error", "Obtained marks cannot be greater than full marks", parent=self.root)
                        return
                except ValueError:
                    messagebox.showerror("Error", "Marks should be numeric values", parent=self.root)
                    return
                
                cur.execute("select * from result where roll=? and course=?", (self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Result already present", parent=self.root)
                else:
                    per = (float(self.var_marks.get()) * 100) / float(self.var_full_marks.get())
                cur.execute("insert into result (roll, name, course, marks_ob, fullmarks, per) values(?, ?, ?, ?, ?, ?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)

                        ))
                    
                con.commit()
                messagebox.showinfo("Success", "Result added Successfully", parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
    def clear(self):
        self.var_roll.set("select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set(""),

if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()