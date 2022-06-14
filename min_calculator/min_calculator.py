import tkinter as tk


class calculator:
    is_int = True

    def __init__(self) -> None:
        self.is_int = True
        # self.formula = ''
        # self.bracket_num = 0
        self.ui = tk.Tk()
        self.InitUi()

    def PressBtn(self, btn_value) -> None:
        old_num = self.data.get()
        if btn_value in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            if old_num == '0':
                new_num = btn_value
            else:
                new_num = old_num + btn_value
        elif btn_value == '.':
            if not self.is_int:
                return
            self.is_int = False
            new_num = old_num + btn_value
        elif btn_value == '%':
            new_num = str(eval(old_num + '/100'))
            self.is_int = False if '.' in new_num else True
        elif btn_value in ['+', '-', '*', '/']:
            formula = self.history.get()
            if len(formula) == 0 or formula[-1] != '=':
                formula = formula + old_num + btn_value
            else:
                formula = old_num + btn_value
            new_num = 0
            self.is_int = True
            self.history.set(formula)
        elif btn_value == 'BACK':
            if len(old_num) <= 1:
                new_num = '0'
            else:
                if old_num[-1] == '.':
                    self.is_int = True
                new_num = old_num[0:-1]
        elif btn_value == 'AC':
            self.history.set('')
            new_num = '0'
            self.is_int = True
        elif btn_value == '=':
            formula = self.history.get()
            if len(formula) == 0 or formula[-1] != '=':
                formula += old_num
                new_num = str(eval(formula))
                self.is_int = False if '.' in new_num else True
                formula += btn_value
            else:
                new_num = old_num
                formula = old_num + btn_value
            self.history.set(formula)
        self.data.set(new_num)

    def InitUi(self) -> None:
        self.ui.minsize(280, 400)
        self.ui.resizable(False, False)
        self.ui.title('计算器')
        self.data = tk.StringVar()
        self.data.set(0)
        self.history = tk.StringVar()
        self.history.set('')
        #######################################显示屏部分#######################################
        # 历史框
        history_label = tk.Label(self.ui,
                                 font=("Helvetica", 12),
                                 bg='#EEE9E9',
                                 bd='9',
                                 fg='#828282',
                                 anchor='se', textvariable=self.history)
        history_label.place(x=0, y=0, width=280, height=70)
        # 输入数据框
        data_label = tk.Label(self.ui,
                              font=("Helvetica", 24),
                              bg='#EEE9E9',
                              bd='9',
                              fg='black',
                              anchor='se', textvariable=self.data)
        data_label.place(x=0, y=70, width=280, height=60)
        ##############################数字键、小数点键、撤回键部分###############################
        tk.Button(self.ui,
                  text='7',
                  font=("Helvetica", 20),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('7')).place(x=0, y=185, width=70, height=55)
        tk.Button(self.ui,
                  text='8',
                  font=("Helvetica", 20),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('8')).place(x=70, y=185, width=70, height=55)
        tk.Button(self.ui,
                  text='9',
                  font=("Helvetica", 20),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('9')).place(x=140, y=185, width=70, height=55)

        tk.Button(self.ui,
                  text='4',
                  font=("Helvetica", 20),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('4')).place(x=0, y=240, width=70, height=55)
        tk.Button(self.ui,
                  text='5',
                  font=("Helvetica", 20),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('5')).place(x=70, y=240, width=70, height=55)
        tk.Button(self.ui,
                  text='6',
                  font=("Helvetica", 20),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('6')).place(x=140, y=240, width=70, height=55)

        tk.Button(self.ui,
                  text='1',
                  font=("Helvetica", 20),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('1')).place(x=0, y=295, width=70, height=55)
        tk.Button(self.ui,
                  text='2',
                  font=("Helvetica", 20),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('2')).place(x=70, y=295, width=70, height=55)
        tk.Button(self.ui,
                  text='3',
                  font=("Helvetica", 20),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('3')).place(x=140, y=295, width=70, height=55)

        tk.Button(self.ui,
                  text='.',
                  font=("Helvetica", 30),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('.')).place(x=0, y=350, width=70, height=55)
        tk.Button(self.ui,
                  text='0',
                  font=("Helvetica", 20),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('0')).place(x=70, y=350, width=70, height=55)
        tk.Button(self.ui,
                  text='↩',
                  font=("Helvetica", 30),
                  fg=('#4F4F4F'),
                  bd=0.5,
                  command=lambda: self.PressBtn('BACK')).place(x=140, y=350, width=70, height=55)
        #######################################功能键部分#######################################
        # # AC
        btn_ac = tk.Button(self.ui,
                           text='AC',
                           font=("Helvetica", 20),
                           fg=('#4F4F4F'),
                           bg=('#DCDCDC'),
                           bd=0.5,
                           command=lambda: self.PressBtn('AC'))
        btn_ac.place(x=0, y=130, width=140, height=55)

        # percent
        btn_percent = tk.Button(self.ui,
                                text='%',
                                font=("Helvetica", 20),
                                fg=('#4F4F4F'),
                                bg=('#DCDCDC'),
                                bd=0.5,
                                command=lambda: self.PressBtn('%'))
        btn_percent.place(x=140, y=130, width=70, height=55)

        # div
        btn_div = tk.Button(self.ui,
                            text='x',
                            font=("Helvetica", 24),
                            fg=('#4F4F4F'),
                            bg=('#DCDCDC'),
                            bd=0.5,
                            command=lambda: self.PressBtn('*'))
        btn_div.place(x=210, y=130, width=70, height=55)
        # mul
        btn_mul = tk.Button(self.ui,
                            text='÷',
                            font=("Helvetica", 24),
                            fg=('#4F4F4F'),
                            bg=('#DCDCDC'),
                            bd=0.5,
                            command=lambda: self.PressBtn('/'))
        btn_mul.place(x=210, y=185, width=70, height=55)
        # add
        btn_add = tk.Button(self.ui,
                            text='+',
                            font=("Helvetica", 24),
                            fg=('#4F4F4F'),
                            bg=('#DCDCDC'),
                            bd=0.5,
                            command=lambda: self.PressBtn('+'))
        btn_add.place(x=210, y=240, width=70, height=55)
        # sub
        btn_sub = tk.Button(self.ui,
                            text='-',
                            font=("Helvetica", 24),
                            fg=('#4F4F4F'),
                            bg=('#DCDCDC'),
                            bd=0.5,
                            command=lambda: self.PressBtn('-'))
        btn_sub.place(x=210, y=295, width=70, height=55)
        # equal
        btn_equal = tk.Button(self.ui,
                              text='=',
                              font=("Helvetica", 20),
                              fg=('#000000'),
                              bg=('#00CDCD'),
                              bd=0.5,
                              command=lambda: self.PressBtn('='))
        btn_equal.place(x=210, y=350, width=70, height=55)

    def DoModal(self) -> None:
        self.ui.mainloop()


cal = calculator()
cal.DoModal()
