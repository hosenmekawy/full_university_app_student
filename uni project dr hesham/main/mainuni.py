from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import font
import csv
import pandas as pd
import numpy as np
import mysql.connector
from math import sqrt, sin, cos, tan, log, log10, pi, e
import time


class student_main():
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title('project university')
        self.root.iconbitmap("logo\Wardiere-removebg-preview.ico")
        self.root.configure(background='white')
        self.root.resizable(True, True)

        # ------------- variables --------------------------------
        self.balance = 0
        self.courses = 0
        self.price_hr = 1450

        # -----------------  frame left --------------------------------

        left_frame = Frame(self.root, bg=whitey, )
        left_frame.place(x=1, y=1, width=350, height=1080)
        # ---------------------frame A------------
        left_frame_A = Frame(left_frame, bg='white',
                             width=350, height=200).place(x=1, y=1)
        # ----------- logo pic --------------------------------
        logo_pic_main = Image.open("main\logo.png")
        resized = logo_pic_main.resize((300, 195))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(left_frame_A, image=logo_pic_mainB, bg='white')
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=15, y=1)
        # ----------- end of logo pic --------------------------------

        left_frame_B = Frame(left_frame, bg='white',
                             width=350, height=300).place(x=1, y=206)
        left_frame_c = Frame(left_frame, bg='white',
                             width=350, height=267).place(x=1, y=512)
        # ------------------line cut straight -----------
        line_frame_between = Frame(
            self.root, bg=whitey, width=6, height=1080).place(x=348, y=1)

        top_frame = Frame(self.root, bg=light_black_blue)
        top_frame.place(x=355, y=1, width=1536, height=200)

        main_logo_text = Button(top_frame, text='PROJECT', font=(
            'Leelawadee', 40), bd=0, bg=light_black_blue, fg='#9F7944', command=self.main_page).place(x=475, y=40)
        under_main = Label(top_frame, text='university for science', font=(
            'Leelawadee', 10), fg='white', bg=light_black_blue).place(x=515, y=130)
        # ----------- illustrations --------
        # -------------------Assignments --------------------------------

        Assmnt = Image.open('illustrations\kassignments.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=417)

        # ---------------------Materials-----------------------------------

        Assmnt = Image.open('illustrations\material.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=357)

        # ---------------------Quizzes--------------------------------------

        Assmnt = Image.open('illustrations\#919191.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=297)

        # ---------------------student--------------------------------

        Assmnt = Image.open('illustrations\student.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=237)

        # ---------------------Fancial--------------------------------

        Assmnt = Image.open('illustrations\money.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=527)

        # -------------------------settings-----------------------------------

        Assmnt = Image.open(
            'illustrations\icons8-settings-50.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=707)

        #  -------------------------survey-----------------------------------

        Assmnt = Image.open('illustrations\survey.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=587)

        # ---------------------about-----------------------------------

        Assmnt = Image.open('illustrations\info.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=647)
        # --------------------end of illustrations -------------------------------


# Buttons in ------------------frame B---------------------

        self.A = Button(left_frame_B, text='STUDENT', bd=0, font=('Dubai Light', 15),
                        bg='white', width=11, fg='#919191', command=self.student).place(x=130, y=230)
        b = Button(left_frame_B, text='QUIZZES', bd=0, font=('Dubai Light', 15),
                   bg='white', width=11, fg='#919191', command=self.quiz).place(x=130, y=290)
        c = Button(left_frame_B, text='MATERIALS', bd=0, font=('Dubai Light', 15),
                   bg='white', width=11, fg='#919191', command=self.materials).place(x=130, y=350)
        d = Button(left_frame_B, text='ASSIGNMENTS', bd=0, font=('Dubai Light', 15),
                   bg='white', width=13, fg='#919191', command=self.Assignments).place(x=130, y=410)

#  Buttons in ----------------frame c ---------------------
        E = Button(left_frame_c, text='FINANCIAL', bd=0, font=(
            'Dubai Light', 15), bg='white', width=11, fg='#919191', command=self.money).place(x=130, y=520)
        G = Button(left_frame_c, text='SETTINGS', bd=0, font=(
            'Dubai Light', 15), bg='white', width=11, fg='#919191', command=self.settings).place(x=130, y=700)
        F = Button(left_frame_c, text='survey', bd=0, font=(
            'Dubai Light', 15), bg='white', width=11, fg='#919191', command = self.survey).place(x=130, y=580)
        H = Button(left_frame_c, text='about', bd=0, font=(
            'Dubai Light', 15), bg='white', width=11, fg='#919191', command = self.about).place(x=130, y=640)


# ------------------------ main page-----------------------

        main_page = Frame(self.root, width=1536, height=880,
                          bg='black',).place(x=355, y=202)
        photo_img_main = Image.open(
            'photos\parker-gibbons-kfwPJieZVwI-unsplash.jpg').resize((1300, 700))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_page, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=355, y=202)

        # -------------- connect to database --------------

        self.connection = mysql.connector.connect(

            host='localhost',
            user='root',
            port='3306',
            password='',
            database='py_dp_st',


        )

        self.c = self.connection.cursor()

        # -----------------------------------------------------

    def main_page(self):
        main_page = Frame(self.root, width=1536, height=880,
                          bg='black',).place(x=355, y=202)
        photo_img_main = Image.open(
            'photos\parker-gibbons-kfwPJieZVwI-unsplash.jpg').resize((1300, 700))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_page, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=355, y=202)

    def get_last_student_user_info(self):
        # Get a new cursor object
        self.c = self.connection.cursor()

        # Execute SELECT query to retrieve last row from table
        self.c.execute(
            "SELECT * FROM copy_single_student_user ORDER BY Time DESC LIMIT 1")

        # Fetch the result set
        result = self.c.fetchone()

        # Convert the result into a list and store it in student_user_info
        self.student_user_info = list(result)

        return self.student_user_info

    def student(self):

        student_user_info = self.get_last_student_user_info()
        nme = student_user_info[1]
        self.lvl = student_user_info[5]
        ids = student_user_info[0]
        print(nme, self.lvl, ids)

        main_pages = Frame(self.root, width=1536, height=880,
                           bg=whitey,).place(x=355, y=202)
        # --------------------student info -----------------------------------
        student_info_frame = Frame(
            main_pages, width=1130, height=250, bg='white').place(x=365, y=212)
        info_label_frame = Frame(
            student_info_frame, width=850, height=230, bg=whitey).place(x=617, y=222)
        Name_label = Label(info_label_frame, text='NAME : ' + nme, font=(' Microsoft Sans Serif', 30),
                           bg=whitey).place(x=630, y=230)

        level_label = Label(info_label_frame, text='LEVEL : ' + self.lvl, font=(' Microsoft Sans Serif', 30),
                            bg=whitey).place(x=630, y=280)

        id_label = Label(info_label_frame, text='ID : ' + ids, font=(' Microsoft Sans Serif', 30),
                         bg=whitey).place(x=630, y=330)

        status_label = Label(info_label_frame, text='STATUS : ' + 'passed', font=(' Microsoft Sans Serif', 30),
                             bg=whitey).place(x=630, y=380)
        student_image = Frame(main_pages, width=200,
                              height=200, bg=whitey).place(x=375, y=222)
        # aaaa

        photo_img_main = Image.open(
            'main\logo.png').resize((200, 200))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_pages, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=375, y=222)

        # eeee
        Label(main_pages, text='2023', bg='white').place(x=460, y=430)
        # table of timetable
        Table_frame = Frame(main_pages, width=560, height=300,
                            bg='white').place(x=365, y=472)

        Table_text = Label(Table_frame, text='your classes table', bg='white', font=(
            'Microsoft Sans Serif', 20)).place(x=515, y=482)

        # aa

        photo_img_main = Image.open(
            'photos\images.png').resize((180, 180))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_pages, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=375, y=522)

        photo_img_main = Image.open(
            'photos\images.png').resize((329, 180))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_pages, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=590, y=522)

        # ee
        btn_table_download = Button(Table_frame, text='DOWNLOAD', bg='#13325B', fg='#9F7944', font=(
            'Microsoft Sans Serif', 20)).place(x=375, y=700)
        btn_table_show = Button(Table_frame, text='SHOW TABLE', bg='#13325B', fg='White', font=(
            'Microsoft Sans Serif', 20), width=20).place(x=590, y=700)

        # end of time table

        GPA_frame = Frame(main_pages, width=560, height=300,
                          bg='white').place(x=935, y=472)

        photo_img_main = Image.open(
            'photos\images (1).png').resize((560, 300))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_pages, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=935, y=472)
# --------- quiz section -------------------

    def quiz(self):

        self.main_pages_quiz = tk.Frame(
            self.root, width=1536, height=880, bg=whitey, relief="solid")
        self.main_pages_quiz.place(x=355, y=202)

        static_text_a = Label(self.main_pages_quiz, text='Quizzes List', font=(
            "Open Sans", 20), bg=whitey, fg=Grey)
        static_text_a.place(x=10, y=10)

        self.frames = tk.Frame(self.main_pages_quiz,
                               width=1386, height=880, bg=whitey)
        self.frames.place(x=0, y=60)

        option_quizs = tk.Frame(
            self.main_pages_quiz, width=150, height=880, bg=light_black_blue)
        option_quizs.place(x=1030, y=0)

        calc_btn = tk.Button(option_quizs, text='    + / - ', bg=light_black_blue, bd=0, font=(
            'Courier New Greek', 20), fg=orange, command=self.calc_frame)
        calc_btn.place(x=10, y=10)

        notes_btn = tk.Button(option_quizs, text='Notes ', bg=light_black_blue, bd=0, font=(
            'Courier New Greek', 20), fg=orange, command=self.notes)
        notes_btn.place(x=10, y=110)

        label_texts = ["1 Quizzes as total 0 as not submitted", "1 Quizzes as total 0 as not submitted",
                       "1 Quizzes as total 0 as not submitted", "1 Quizzes as total 0 as not submitted"]
        button_texts = ["Artificial inteligence", "iot", "projects", "Math 1"]
        self.frame_quiz(4, label_texts, button_texts)


# - - - - - - - --- - quiz frame loop --------------------------------

    def frame_quiz(self, nom_frames, label_texts, btn_txt,):

        for i in range(nom_frames):

            frame = Frame(self.frames, width=950, height=100,  bg=black_whitey)
            frame.pack(side="bottom", padx=20, pady=10)
            upper_frame = Frame(frame, width=950, height=60, bg='white')
            upper_frame.place(x=0, y=40)
            # Add a label to the upper frame
            label1 = Label(upper_frame, text=label_texts[i], font=(
                "Arial", 10), fg="black", bg='white')
            label1.place(x=40, y=30)

            static_label = Label(upper_frame, text='Total Previous Quizzes. ', bg='white', font=(
                'Arial', 10), fg=Blue)
            static_label.place(x=20, y=10)

            btntxt = Button(frame, text=btn_txt[i], font=(
                "Arial", 10), fg="black", bg=black_whitey, bd=0)
            btntxt.place(x=20, y=8)


# ------------------------ calc -----------------------------------------------

    def calc_frame(self):
        self.calc = Frame(self.main_pages_quiz, width=350,
                          height=380, bg=light_black)
        self.calc.place(x=823, y=0)

        title_frame = Frame(self.calc, width=350,
                            height=40, bg=light_black_blue)
        title_frame.place(x=0, y=0)

        title_name = Label(title_frame, text='Calculator', font=(
            'Courier New Greek', 22), bg=light_black_blue, fg=orange)
        title_name.place(relx=0.5, rely=0.5, anchor=CENTER)

        btn_x = Button(self.calc, text='X', bg='red', bd=0, font=(
            'Courier New Greek', 10), width=4, height=2, command=self.destroy_frame_calc)
        btn_x.place(x=0, y=0)

        self.display = Entry(self.calc, width=27,  font=(
            "Arial", 16), justify="right", bg=light_black, bd=0, fg='white')
        self.display.place(x=13, y=42, height=50)

        self.keys1 = Frame(self.calc, width=350, height=288, bg=whitey)
        self.keys1.place(x=2, y=92)

        self.create_buttons()

    def destroy_frame_calc(self):
        self.calc.destroy()

    def create_buttons(self):
        buttons = [
            {"text": "C", "row": 1, "column": 0},
            {"text": "CE", "row": 1, "column": 1},
            {"text": "±", "row": 1, "column": 2},
            {"text": "√", "row": 1, "column": 3},
            {"text": "7", "row": 2, "column": 0},
            {"text": "8", "row": 2, "column": 1},
            {"text": "9", "row": 2, "column": 2},
            {"text": "/", "row": 2, "column": 3},
            {"text": "4", "row": 3, "column": 0},
            {"text": "5", "row": 3, "column": 1},
            {"text": "6", "row": 3, "column": 2},
            {"text": "*", "row": 3, "column": 3},
            {"text": "1", "row": 4, "column": 0},
            {"text": "2", "row": 4, "column": 1},
            {"text": "3", "row": 4, "column": 2},
            {"text": "-", "row": 4, "column": 3},
            {"text": "0", "row": 5, "column": 0},
            {"text": ".", "row": 5, "column": 1},
            {"text": "=", "row": 5, "column": 2},
            {"text": "+", "row": 5, "column": 3},
            {"text": "sin", "row": 2, "column": 4},
            {"text": "cos", "row": 3, "column": 4},
            {"text": "tan", "row": 4, "column": 4},
            {"text": "log", "row": 2, "column": 5},
            {"text": "ln", "row": 3, "column": 5},
            {"text": "pi", "row": 4, "column": 5},
            {"text": "e", "row": 5, "column": 5},
        ]

        for button in buttons:
            command = lambda x=button["text"]: self.calculate(x)
            tk.Button(self.keys1, text=button["text"], width=6, height=3, command=command).grid(
                row=button["row"], column=button["column"], padx=0, pady=0)

    def calculate(self, key):
        if key == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == "C":
            self.display.delete(0, tk.END)
        elif key == "CE":
            self.display.delete(0, tk.END)
        elif key == "±":
            try:
                value = self.display.get()
                if value[0] == "-":
                    self.display.delete(0)
                else:
                    self.display.insert(0, "-")
            except IndexError:
                pass
        elif key == "√":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, sqrt(value))
            except ValueError:
                pass
        elif key == "sin":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, sin(value))
            except ValueError:
                pass
        elif key == "cos":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, cos(value))
            except ValueError:
                pass
        elif key == "tan":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, tan(value))
            except ValueError:
                pass
        elif key == "log":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, log10(value))
            except ValueError:
                pass
        elif key == "ln":
            try:
                value = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, log(value))
            except ValueError:
                pass
        elif key == "pi":
            self.display.insert(tk.END, pi)

        elif key == "e":
            self.display.insert(tk.END, e)
        else:
            self.display.insert(tk.END, key)

    def notes(self):
        self.frame_notes = Frame(self.main_pages_quiz,
                                 width=350, height=380, bg='#F4F269')
        self.frame_notes.place(x=823, y=0)

        title_frame = Frame(self.frame_notes, width=350,
                            height=40, bg=light_black_blue)
        title_frame.place(x=0, y=0)

        title_name = Label(title_frame, text='Notes', font=(
            'Courier New Greek', 22), bg=light_black_blue, fg=orange)
        title_name.place(relx=0.5, rely=0.5, anchor=CENTER)

        btn_x = Button(self.frame_notes, text='X', bg='red', bd=0, font=(
            'Courier New Greek', 10), width=4, height=2, command=self.destroy_frame_notes)
        btn_x.place(x=0, y=0)

        txt_entry = tk.Text(self.frame_notes, bg='#F4F269',
                            width=350, height=340)
        txt_entry.place(x=0, y=40)

    def destroy_frame_notes(self):
        self.frame_notes.destroy()

    def money(self):
        self.money_main = Frame(self.root, width=1536, height=880,
                                bg='white',)
        self.money_main.place(x=355, y=202)

        # ---------- add payment button -------------

        frame1 = Frame(self.money_main, width=600, height=300, bg='red')
        frame1.grid(column=0, row=0)
        btn_1 = Button(frame1, text="Payment", font=(
            'Times New Roman', 50), command=self.add_payment, bg=light_black_blue, fg=orange)
        btn_1.place(x=0, y=0, width=600, height=300)

        # ---------- add course reg button -------------
        frame2 = Frame(self.money_main, width=600,  height=300, bg='white')
        frame2.grid(column=0, row=1)
        btn_2 = Button(frame2, text="Course Reg", font=(
            'Times New Roman', 50), command=self.course_reg, bg=light_black_blue, fg=orange)
        btn_2.place(x=0, y=0, width=600, height=300)
        # ---------- add Balance button -------------
        frame3 = Frame(self.money_main, width=600,  height=300, bg='pink')
        frame3.grid(column=1, row=0)
        btn_3 = Button(frame3, text="Balance", font=(
            'Times New Roman', 50), command=self.Balance, bg=light_black_blue, fg=orange)
        btn_3.place(x=0, y=0, width=600, height=300)

        # ---------- add History button -------------
        frame4 = Frame(self.money_main, width=600,  height=300, bg='purple')
        frame4.grid(column=1, row=1)
        btn_4 = Button(frame4, text="History", font=(
            'Times New Roman', 50), command=self.add_payment, bg=light_black_blue, fg=orange)
        btn_4.place(x=0, y=0, width=600, height=300)

    def add_payment(self):
        self.money_widget = Frame(self.root, width=1536, height=880,
                                  bg='white',)
        self.money_widget.place(x=355, y=202)
        self.add_payment3 = Frame(self.money_widget, width=1536, height=880,
                                  bg='white',)
        self.add_payment3.place(x=0, y=0)

        label_main = Label(self.add_payment3, text=" SELECT PAYMENT METHOD ", font=(
            'Times New Roman', 20), bg='white')
        label_main.place(x=40, y=30)

        self.btn_credits = Button(self.add_payment3, font=('Sans Serif Collection', 5), text='CREDIT CARD',
                                  bg=light_black_blue, bd=1, fg=orange, width=40, height=3, command=self.credit_card)
        self.btn_credits.place(x=40, y=80)
        btn_Bank = Button(self.add_payment3, text='BANK TRANSFER', font=(
            'Sans Serif Collection', 5), bg=light_black_blue, bd=1, fg=orange, width=40, height=3, ).place(x=400, y=80)
        btn_PayPal = Button(self.add_payment3, text='PAYPAL', font=('Sans Serif Collection', 5),
                            bg=light_black_blue, bd=1, fg=orange, width=40, height=3, ).place(x=760, y=80)

    def credit_card(self):

        credit_frame = Frame(self.add_payment3, width=1536,
                             height=730, bg='white')
        credit_frame.place(x=0, y=150)
        self.btn_credits.configure(background=orange, fg=light_black_blue)
# --------- name_on_caard -----------
        self.lbl_name = Label(credit_frame, text='Card Holder Name', font=(
            'bold', 20), bg='white')
        self.lbl_name.place(x=40, y=20)
        self.Entry_name = Entry(credit_frame, width=60,
                                bd=2)
        self.Entry_name.place(x=40, y=60, height=40)
# --------- number_on_caard -----------

        self.lbl_number = tk.Label(credit_frame, text='Card Number', font=(
            'bold', 20), bg='white')
        self.lbl_number.place(x=40, y=130)

        self.Entry_number = Entry(credit_frame, width=60, bd=2)
        self.Entry_number.place(x=40, y=170, height=40)
# --------- date_on_caard -----------

        self.lbl_date = Label(credit_frame, text='Expiry Date', font=(
            'bold', 20), bg='white')
        self.lbl_date.place(x=40, y=240)
        self.Entry_date = StringVar()
        self.Entry_date = Entry(credit_frame, width=25,
                                bd=2)
        self.Entry_date.place(x=40, y=280, height=40)
# --------- name_on_card -----------

        self.lbl_cvv = Label(credit_frame, text='CVV', font=(
            'bold', 20), bg='white')
        self.lbl_cvv.place(x=250, y=240)

        self.Entry_cvv = Entry(credit_frame, width=25, bd=2)
        self.Entry_cvv.place(
            x=250, y=280, height=40)
# btn save card information
        btn_save = Button(credit_frame, text='Save', command=self.save_card, font=(
            'bold', 20), bg=light_black_blue, fg=orange, )
        btn_save.place(x=250, y=340, width=155)

        card_frame = Frame(credit_frame, width=380,
                           height=240, bg=light_black_blue)
        card_frame.place(x=710, y=60)

        Name_company = Label(card_frame, text='CARD DETAILS', font=(
            ' Tw Cen MT Condensed Extra Bold', 17), bg=light_black_blue, fg='#FFEAEA').place(x=50, y=20)
        bena_frame = Frame(card_frame, width=50, height=35,
                           bg=light_black_blue, bd=0)
        bena_frame.place(x=50, y=70)
        # '''

        IMAGE_PATH = 'main\chip.png'

        canvas = tk.Canvas(bena_frame, width=55, height=55,
                           bg=light_black_blue, bd=0,  highlightbackground=light_black_blue)
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open(
            IMAGE_PATH).resize((50, 50), Image.ANTIALIAS))
        # Keep a reference in case this code is put in a function.
        canvas.background = img
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # '''

        lbl_Number_in_card = Label(
            card_frame, text='Card Number', bg=light_black_blue, fg='#c67149')
        lbl_Number_in_card.place(x=50, y=120)
        self.Number_in_card = Label(
            card_frame, text='', bg=light_black_blue, font=('sans ', 20), fg='#FFDEB9')
        self.Number_in_card.place(x=50, y=140)
        self.Entry_number.bind('<KeyRelease>', self.update_card_details)
        lbl_Name_in_card = Label(
            card_frame, text='Name', bg=light_black_blue, fg='#c67149')
        lbl_Name_in_card.place(x=140, y=70)
        self.Name_in_card = Label(
            card_frame, text='', bg=light_black_blue, font=('sans ', 15), fg='#FFDEB9')
        self.Name_in_card.place(x=140, y=90)
        self.Entry_name.bind('<KeyRelease>', self.update_card_details)

        lbl_DATE_in_card = Label(
            card_frame, text='VALID THRU ', bg=light_black_blue, fg='#c67149')
        lbl_DATE_in_card.place(x=50, y=180)

        self.Date_in_card = Label(
            card_frame, text='', bg=light_black_blue, font=('sans ', 20), fg='#FFDEB9')
        self.Date_in_card.place(x=50, y=200)
        self.Entry_date.bind('<KeyRelease>', self.update_card_details)

    def update_card_details(self, *args):
        self.Number_in_card.config(text=self.Entry_number.get())
        self.Name_in_card.config(text=self.Entry_name.get())
        self.Date_in_card.config(text=self.Entry_date.get())
        # self.CVV_in_card.config(text=self.Entry_cvv.get())

    def save_card(self):
        number_card = self.Entry_number.get().strip()
        name_card = self.Entry_name.get().strip()
        cvv_card = self.Entry_cvv.get().strip()
        date_card = self.Entry_date.get().strip()
        len_num = len(number_card)
        len_cvv = len(cvv_card)
        student_user_info = self.get_last_student_user_info()
        phone = student_user_info[2]
        # self.balance = 0
        b = self.connection.cursor()
        query = "SELECT * FROM payment WHERE `user's phone` = %s"
        b.execute(query, (phone,))

        print(len_cvv)
        if len_num == 16 and len_cvv == 3 and len(name_card) > 0 and len(date_card) > 0:
            if len_num == 16:
                if len_cvv == 3:
                    if b.fetchone() is None:
                        student_user_info = self.get_last_student_user_info()
                        phone = student_user_info[2]
                        vals = (phone, name_card, number_card, date_card,
                                time.strftime('%Y-%m-%d %H:%M:%S'), self.balance)
                        insert_query = "INSERT INTO `payment`(`user's phone`, `credit name`, `credit number`, `credit date`, `time added credit`, `total balance`) VALUES (%s, %s, %s, %s, %s, %s)"
                        self.c.execute(insert_query, vals)
                        self.connection.commit()
                        print('gh')
                        messagebox.showinfo(
                            'success saving', 'thanks for saving')
                    else:
                        messagebox.showerror(
                            'error saving', 'there are saved payment method')
                else:
                    messagebox.showerror('error saving', 'cvv is wrong')
            else:
                messagebox.showerror(
                    'error saving', 'please enter credit number Right')

                self.lbl_number.config(fg='red')
        else:
            messagebox.showerror('error saving', 'cannot')

    def course_reg(self, **args):
        # dataBase setup :
        student_user_info = self.get_last_student_user_info()
        lvl = student_user_info[5]
        facu = student_user_info[-2]
        print(lvl + facu)

        main_frame = Frame(self.root, width=1536, height=880,
                           bg=black_whitey)
        main_frame.place(x=355, y=202)
        # add label course registration
        lbl_course_registration = Label(main_frame, text="Course registration", font=(
            'Times New Roman', 30), bg=black_whitey).place(x=50, y=20)
        line_frame = Frame(main_frame, width=1536, height=3,
                           bg='black', ).place(x=0, y=80)
        # frame that will add content over it
        self.frame_over = Frame(main_frame, width=1536,
                                height=795, bg=black_whitey)
        self.frame_over.place(x=0, y=90)

        # add label called number of hours
        lbl_no_hrs = Label(self.frame_over, text='Number of Hours',
                           font=('', 20), bg=black_whitey)
        lbl_no_hrs.place(x=80, y=10)

        # add Entry box to enter number of hours
        self.Entry_hrs = Spinbox(
            self.frame_over, activebackground=light_black_blue, bd=2, from_=0, to_=50, width=5)
        self.Entry_hrs.place(y=19, x=320)

        self.value = self.Entry_hrs.get()
        # add btn pay
        btn_pay = Button(self.frame_over, text='Pay', font=(
            '', 20), bg=light_black_blue, fg=orange, bd=0, command=self.pay_money)
        btn_pay.place(x=1000, y=10, width=130, height=60)

        # add label called total Balance :
        lbl_tB = Label(self.frame_over, text="Total Balance :  ",
                       font=('', 20), bg=black_whitey)
        lbl_tB.place(x=80, y=60)

        lbl_value_tb = Label(self.frame_over, text=self.new_balance, font=(
            '', 20), bg=black_whitey, fg='white')
        lbl_value_tb.place(x=300, y=60)
        print(self.balance)

        lbl_Egp = Label(self.frame_over, text='EGP', font=(
            '', 20), bg=black_whitey,).place(x=460, y=60)
        # add line
        line_frame2 = Frame(self.frame_over, width=1536, height=3,
                            bg='black', ).place(x=0, y=110)

        # add whitey frame in middle of page
        frame_over_whitey = Frame(
            self.frame_over, width=1536, height=285, bg=whitey)
        frame_over_whitey.place(x=0, y=114)

        # add label called total hours registered
        lbl_hours_registration = Label(
            frame_over_whitey, text="Total Hours Registed : ", font=('', 20), bg=whitey)
        lbl_hours_registration.place(x=80, y=10)

        lbl_value_hours_registration = Label(
            frame_over_whitey, text=self.courses, font=('', 20), bg=whitey, fg=orange)
        lbl_value_hours_registration.place(x=380, y=10)
        # add Total courses regested : 6

        lbl_tcr = Label(
            frame_over_whitey, text="Total courses regested : ", font=('', 20), bg=whitey)
        lbl_tcr.place(x=80, y=60)

        # add your Faculty :   AI         your Level :  2

        lbl_your_faculty = Label(
            frame_over_whitey, text="your Faculty : ", font=('', 20), bg=whitey)
        lbl_your_faculty.place(x=80, y=110)

        lbl_value_faculty = Label(
            frame_over_whitey, text=facu, font=('', 20), bg=whitey, fg=orange)
        lbl_value_faculty.place(x=280, y=110)

        lbl_your_level = Label(
            frame_over_whitey, text="your Level : ", font=('', 20), bg=whitey)
        lbl_your_level.place(x=80, y=160)

        lbl_value_level = Label(
            frame_over_whitey, text=lvl, font=('', 20), bg=whitey, fg=orange)
        lbl_value_level.place(x=280, y=160)

        # TODO: add 4 buttons 1- Pay 2- Balance 3- courses 4- payment

        btn_Balance = Button(self.frame_over, text='Balance', font=(
            '', 20), bg=light_black_blue, fg=orange, bd=0)
        btn_Balance.place(x=80, y=420, width=130, height=60)

        btn_courses = Button(self.frame_over, text='courses', font=(
            '', 20), bg=light_black_blue, fg=orange, bd=0)
        btn_courses.place(x=480, y=420, width=130, height=60)

        btn_payment = Button(self.frame_over, text='Payment', font=(
            '', 20), bg=light_black_blue, fg=orange, bd=0, command=self.add_payment)
        btn_payment.place(x=880, y=420, width=130, height=60)

        # add line in down
        line_frame3 = Frame(self.frame_over, width=1536, height=3,
                            bg='black', ).place(x=0, y=400)

    def pay_money(self):

        self.receipt_frame = Frame(
            self.frame_over, bg=whitey, borderwidth=2,  relief="solid")
        self.receipt_frame.place(x=420, y=50,  width=400, height=400,)
        # add frame in top add in it title and exit button
        title_frame = Frame(self.receipt_frame, bg=black_whitey,
                            borderwidth=1, relief="solid")
        title_frame.place(x=0, y=0, width=396, height=60)
        # add btn x to exit
        btn_exit = Button(title_frame, bg='red', text=' X ',
                          font=('', 25), command=self.destroy_receipt)
        btn_exit.place(x=330, y=0)
        # add title "Receipt"
        lbl_Receipt = Label(title_frame, bg=black_whitey,
                            font=('', 25), text="Receipt")
        lbl_Receipt.place(x=120, y=4)

        lbl_no_of_hrs = Label(self.receipt_frame, text='Number of hours : ' +
                              str(self.Entry_hrs.get()), font=('', 15), bg=whitey)
        lbl_no_of_hrs.place(x=30, y=80)

        lbl_price_of_hrs = Label(
            self.receipt_frame, text='Price of one hour : ' + str(self.price_hr), font=('', 15), bg=whitey)
        lbl_price_of_hrs.place(x=30, y=130)

        lbl_total_of_balance_available = Label(
            self.receipt_frame, text='Your Balance : ' + str(self.current_money), font=('', 15), bg=whitey)
        lbl_total_of_balance_available.place(x=30, y=180)

        # add black line frame
        line_frame = Frame(self.receipt_frame, bg='black')
        line_frame.place(x=0, y=220, width=400, height=3)

        total_price = int(self.Entry_hrs.get()) * self.price_hr

        lbl_total = Label(self.receipt_frame, text='Total :   ' +
                          str(total_price) + '   EGP', font=('', 15), bg=whitey)
        lbl_total.place(x=30, y=270)

        btn_pay = Button(self.receipt_frame, text='Pay', font=(
            '', 20), bg=whitey, fg=light_black, bd=1, relief=SOLID)
        btn_cancel = Button(self.receipt_frame, text='cancel', font=(
            '', 20), bg='red', fg=light_black, bd=1, relief=SOLID, command=self.destroy_receipt)

        btn_pay.place(x=30, y=330, width=150)
        btn_cancel.place(x=210, y=330, width=150)

        # TODO: add funcion to be sure there is money in balance  then take money from the balance and save it in database
    def check_if_balance_exists(self):
        pass
        # TODO: add function to view the balance and add money to the balance and save the details in database

    def Balance(self):
        student_user_info = self.get_last_student_user_info()
        phone = student_user_info[2]

        cursor = self.connection.cursor()

        # Execute SELECT query to retrieve last row from table
        query = "SELECT `total balance` FROM `payment` WHERE `user's phone` = %s"
        cursor.execute(query, (phone,))

        # Fetch the result set
        result = cursor.fetchone()
        if result is not None:
            self.current_money = result[-1]
            print(result[-1])
        else:
            print("No results found")
            self.current_money = 0

        self.frame_Balance_main = Frame(self.root, width=1536, height=880, bg=black_whitey)
        self.frame_Balance_main.place(x=355, y=202)

        lbl_Balance = Label(self.frame_Balance_main, text="Balance", font=('Times New Roman', 30), bg=black_whitey).place(x=50, y=20)
        line_frame = Frame(self.frame_Balance_main, width=1536, height=3, bg='black')
        line_frame.place(x=0, y=80)

        self.frame_over_Balance = Frame(self.frame_Balance_main, width=1536, height=795, bg=black_whitey)
        

        self.frame_over_Balance.place(x=0, y=90)

        self.new_balance = self.balance+int(self.current_money)

        # add label called current Balance
        lbl_current_balance = Label(self.frame_over_Balance, text='Current Balance :   ' + str(self.new_balance), font=('', 20), bg=black_whitey)
        lbl_current_balance.place(x=80, y=10)

        Btn_add_money = Button(self.frame_over_Balance, text='add money', font=('', 20), bg=black_whitey, command=self.add_money_to_data)
        Btn_add_money.place(x=80, y=160)

        lbl_add_money = Label(self.frame_over_Balance, text='add money ', font=('', 20), bg=black_whitey)
        lbl_add_money.place(x=80, y=60)

        self.New_Balance = Entry(self.frame_over_Balance)
        self.New_Balance.place(x=280, y=73)

    def add_money_to_data(self):
        b = self.connection.cursor()
        bb = self.New_Balance.get()
        student_user_info = self.get_last_student_user_info()
        phone = student_user_info[2]
        update_query = "UPDATE `payment` SET `total balance`= %s WHERE `user's phone` = %s"
        vals = (bb, phone)
        b.execute(update_query, vals)
        self.connection.commit()

    def destroy_receipt(self):
        self.receipt_frame.destroy()

    def Assignments(self):
        self.main_Assignments = Frame(self.root, width=1536, height=880,
                                      bg=whitey,)
        self.main_Assignments.place(x=355, y=202)
        static_text_a = Label(self.main_Assignments, text='Assignments List', font=(
            'Open Sans', 20), bg=whitey, fg=Grey)
        static_text_a.place(x=10, y=10)

        self.frames_ASS = tk.Frame(self.main_Assignments,
                                   width=1386, height=880, bg=whitey)
        self.frames_ASS.place(x=0, y=60)

        label_texts = ["1 Assignments as total 0 as not submitted", "1 Assignments as total 0 as not submitted",
                       "1 Assignments as total 0 as not submitted", "1 Assignments as total 0 as not submitted"]
        button_texts = ["Artificial inteligence", "iot", "projects", "Math 1"]
        self.frame_assignments(4, label_texts, button_texts)

    def frame_assignments(self, nom_frames, label_texts, btn_txt,):

        for i in range(nom_frames):

            frame = Frame(self.frames_ASS, width=950,
                          height=100,  bg=black_whitey)
            frame.pack(side="bottom", padx=20, pady=10)
            upper_frame = Frame(frame, width=950, height=60, bg='white')
            upper_frame.place(x=0, y=40)
            # Add a label to the upper frame
            label1 = Label(upper_frame, text=label_texts[i], font=(
                "Arial", 10), fg="black", bg='white')
            label1.place(x=40, y=30)

            static_label = Label(upper_frame, text='Total Previous Assignments. ', bg='white', font=(
                'Arial', 10), fg=Blue)
            static_label.place(x=20, y=10)

            btntxt = Button(frame, text=btn_txt[i], font=(
                "Arial", 10), fg="black", bg=black_whitey, bd=0)
            btntxt.place(x=20, y=8)

    def materials(self):
        self.main_materials = Frame(self.root, width=1536, height=880,
                                    bg=whitey,)
        self.main_materials.place(x=355, y=202)
        static_text_a = Label(self.main_materials, text='Materials List', font=(
            'Open Sans', 20), bg=whitey, fg=Grey)
        static_text_a.place(x=10, y=10)

        self.frames_ASS = tk.Frame(self.main_materials,
                                   width=1386, height=880, bg=whitey)
        self.frames_ASS.place(x=0, y=60)

        button_texts = ["Artificial inteligence", "iot", "projects", "Math 1"]
        self.frame_materials(4, button_texts)

    def frame_materials(self, nom_frames,  btn_txt,):

        for i in range(nom_frames):

            frame = Frame(self.frames_ASS, width=950,
                          height=50,  bg=black_whitey)
            frame.pack(side="bottom", padx=20, pady=10)

            btntxt = Button(frame, text=btn_txt[i], font=(
                "Open Sans", 15), fg="black", bg=black_whitey, bd=0)
            btntxt.place(x=20, y=8)

    def survey(self):
        main_pages = Frame(self.root, width=1536, height=880,
                           bg='grey',).place(x=355, y=202)

    def about(self):
        main_pages = Frame(self.root, width=1536, height=880,
                           bg='white',).place(x=355, y=202)

    def settings(self):
        # dataBase setup :
        student_user_info = self.get_last_student_user_info()
        id = student_user_info[0]
        user_name = student_user_info[1]
        phone = student_user_info[2]
        Email = student_user_info[3]
        password = student_user_info[4]
        lvl = student_user_info[5]
        facu = student_user_info[6]
        print(lvl + facu)
        
        
        
        self.main_pages_settings = Frame(self.root, width=1536, height=880,
                           bg='white',)
        self.main_pages_settings.place(x=355, y=202)

        lbl_settings = Label(self.main_pages_settings, text="settings", font=(
            'Times New Roman', 30), bg='white').place(x=50, y=15)
        line_frame = Frame(self.main_pages_settings, width=1536, height=3,
                           bg='black', ).place(x=0, y=80)
        
        lbl_profile = Label(self.main_pages_settings, text="profile", font=(
            'Times New Roman', 30), bg='white' , fg = Grey).place(x=50, y=100)
        
        self.over_main_pages_settings = Frame(self.main_pages_settings, width=1536, height=880,
                           bg='white',)
        self.over_main_pages_settings.place(x=0, y=160)
        
        lbl_user_name = Label(self.over_main_pages_settings, text = 'user name  :   ' + user_name, font = ('Times New Roman', 20) , bg = 'white' ).place(x =30 , y =20 )
        lbl_phone =Label(self.over_main_pages_settings, text = 'user phone  :   ' + phone, font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y = 70 )
        lbl_email =Label(self.over_main_pages_settings, text = 'user email  :   ' + Email, font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y = 120)
        lbl_password =Label(self.over_main_pages_settings, text = 'user password  :   ' + password, font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y =170 )
        lbl_faculty =Label(self.over_main_pages_settings, text = 'user faculty  :   ' + facu, font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y =220 )
        lbl_id =Label(self.over_main_pages_settings, text = 'user ID  :   ' + id, font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y = 270 )
        lbl_level =Label(self.over_main_pages_settings, text = 'user level  :   ' + lvl, font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y =320 )
        
        btn_edit =  Button(self.over_main_pages_settings, command= self.update_data,text = 'CHANGE', font =('Times New Roman',25), bg = light_black_blue , fg = orange)
        btn_edit.place(x = 30 , y = 370)
        
    def update_data(self):
    # dataBase setup :
        student_user_info = self.get_last_student_user_info()
        id = student_user_info[0]
        user_name = student_user_info[1]
        phone = student_user_info[2]
        Email = student_user_info[3]
        password = student_user_info[4]
        lvl = student_user_info[5]
        facu = student_user_info[6]
        self.frame_edit = Frame(self.main_pages_settings , bg = 'white' , width=1536, height=880)
        self.frame_edit.place(x=0, y=160)
        
        
        lbl_user_name = Label(self.frame_edit, text = 'user name  :   ' , font = ('Times New Roman', 20) , bg = 'white' ).place(x =30 , y =20 )
        
        self.entry_user_name = Entry(self.frame_edit, width = 30 ,cursor='hand2' , font=('Microsoft YaHei UI Light', 15) ,  fg = Grey , borderwidth= 2 , relief= SOLID)
        self.entry_user_name.place(x=230 , y= 25)
        self.entry_user_name.insert(0, user_name)
        
        lbl_phone =Label(self.frame_edit, text = 'user phone  :   '  , font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y = 70 )
        
        self.entry_user_phone = Entry(self.frame_edit, width = 30 ,cursor='hand2' , font=('Microsoft YaHei UI Light', 15) ,  fg = Grey , borderwidth= 2 , relief= SOLID)
        self.entry_user_phone.place(x=230 , y= 75)
        self.entry_user_phone.insert(0, phone)
        
        
        
        lbl_email =Label(self.frame_edit, text = 'user email  :   '  , font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y = 120)
        
        self.entry_user_email = Entry(self.frame_edit, width = 30 ,cursor='hand2' , font=('Microsoft YaHei UI Light', 15) ,  fg = Grey , borderwidth= 2 , relief= SOLID)
        self.entry_user_email.place(x=230 , y= 125)
        self.entry_user_email.insert(0, Email)
        
        lbl_password =Label(self.frame_edit, text = 'user password  :   ' , font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y =170 )
        
        self.entry_user_password = Entry(self.frame_edit, width = 30 ,cursor='hand2' , font=('Microsoft YaHei UI Light', 15) ,  fg = Grey , borderwidth= 2 , relief= SOLID)
        self.entry_user_password.place(x=230 , y= 175)
        self.entry_user_password.insert(0, password)
        
        lbl_faculty =Label(self.frame_edit, text = 'user faculty  :   ' , font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y =220 )
        
        self.entry_user_faculty = Entry(self.frame_edit, width = 30 ,cursor='hand2' , font=('Microsoft YaHei UI Light', 15) ,  fg = Grey , borderwidth= 2 , relief= SOLID)
        self.entry_user_faculty.place(x=230 , y= 225)
        self.entry_user_faculty.insert(0, facu)
        
        lbl_id =Label(self.frame_edit, text = 'user ID  :   ' , font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y = 270 )
        
        self.entry_user_id = Entry(self.frame_edit, width = 30 ,cursor='hand2' , font=('Microsoft YaHei UI Light', 15) ,  fg = Grey , borderwidth= 2 , relief= SOLID)
        self.entry_user_id.place(x=230 , y= 275)
        self.entry_user_id.insert(0, id)
        
        lbl_level =Label(self.frame_edit, text = 'user level  :   ', font = ('Times New Roman', 20) , bg = 'white').place(x =30 , y =320 )
        
        self.entry_user_level = Entry(self.frame_edit, width = 30 ,cursor='hand2' , font=('Microsoft YaHei UI Light', 15) ,  fg = Grey , borderwidth= 2 , relief= SOLID)
        self.entry_user_level.place(x=230 , y= 325)
        self.entry_user_level.insert(0, lvl)
        
        
        
        btn_save = Button(self.frame_edit , text = 'save' , command = self.set_update_to_database)
        btn_save.place(x= 30 , y= 400)
        
    def set_update_to_database(self):
        self.name_value = str(self.entry_user_name.get())
        self.phone_value = str(self.entry_user_phone.get())
        self.email_value = str(self.entry_user_email.get())
        self.password_value = str(self.entry_user_password.get())
        self.faculty_value = str(self.entry_user_faculty.get())
        self.id_value = str(self.entry_user_id.get())
        self.level_value = str(self.entry_user_level.get())

        # Verify that the phone number entered is valid
        if not self.phone_value.isdigit() or len(self.phone_value) != 11:
            messagebox.showerror("Error", "Invalid phone number")
            return

        # Use a try-except block to catch any database errors
        try:
            cursor = self.connection.cursor()
            query = "UPDATE copy_single_student_user SET id=%s, NAME=%s, PHONE=%s, EMAIL=%s, PASSWORD=%s, LEVEL=%s, FACULTY=%s WHERE PHONE=%s"
            values = (self.id_value, self.name_value, self.phone_value, self.email_value, self.password_value, self.level_value, self.faculty_value, self.phone_value)
            cursor.execute(query, values)
            self.connection.commit()
            messagebox.showinfo("Success", "User information updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error updating user information: {str(e)}")
            return
light_green = '#OECFAO'
light_black_blue = '#171546'
light_black = '#010127'
orange = '#FF772B'
whitey = '#F7F7F2'
black_whitey = '#949491'
Grey = '#717171'
Blue = '#4cc0c1'
root = Tk()
# create an instance of student_main with the root window as argument
page = 0
oop = student_main(root)
root.mainloop()
