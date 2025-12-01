import calendar 
import tkinter as tk 
from tkinter import messagebox 
 
def generate_calendar(): 
    year = int(year_entry.get()) 
    month = int(month_entry.get()) 
 
    if year < 0 or month < 1 or month > 12: 
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные значения года и месяца в числах.") 
        return 
 
    cal_data = calendar.monthcalendar(year, month) 
 
    for widget in calendar_frame.winfo_children(): 
        widget.destroy() 
 

    month_names = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'] 
    month_label = tk.Label(calendar_frame, text=month_names[month - 1], font=("Arial", 16, "bold"), width=30, height=12) 
    month_label.grid(row=0, column=0, columnspan=7, pady=10, sticky="nsew") 
 
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'] 
    for i, day in enumerate(days): 
        label = tk.Label(calendar_frame, text=day, bg="lightgray", borderwidth=1, fg="black", relief="solid", font=("Arial", 10, "bold"), width=30, height=20) 
        label.grid(row=1, column=i, sticky="nsew") 
 
    for week, week_data in enumerate(cal_data, start=2): 
        for day, date in enumerate(week_data): 
            if date == 0: 
                continue 
            if day >= 5: 
                bg_color = "lightpink" 
                fg_color = "black" 
            else: 
                bg_color = "white" 
                fg_color = "black" 
 
            is_holiday = False 
            holidays = [(1, 1), (2, 1), (3, 1), (8, 3), (21, 3), (9, 5), (1, 9), (1, 10), (8, 12)]  
            if (date, month) in holidays: 
                bg_color = "lightgreen" 
                fg_color = "black" 
                is_holiday = True 
 
            label = tk.Label(calendar_frame, text=str(date), bg=bg_color, fg=fg_color, relief="solid", bd=1, width=30, height=20) 
            label.grid(row=week, column=day, sticky="nsew") 
 
def previous_month(): 
    current_year = int(year_entry.get()) 
    current_month = int(month_entry.get()) 
 
    if current_month == 1: 
        year_entry.delete(0, tk.END) 
        year_entry.insert(tk.END, str(current_year - 1)) 
        month_entry.delete(0, tk.END) 
        month_entry.insert(tk.END, "12") 
    else: 
        month_entry.delete(0, tk.END) 
        month_entry.insert(tk.END, str(current_month - 1)) 
 
    generate_calendar() 
 
def next_month(): 
    current_year = int(year_entry.get()) 
    current_month = int(month_entry.get()) 
 
    if current_month == 12: 
        year_entry.delete(0, tk.END) 
        year_entry.insert(tk.END, str(current_year + 1)) 
        month_entry.delete(0, tk.END) 
        month_entry.insert(tk.END, "1") 
    else: 
        month_entry.delete(0, tk.END) 
        month_entry.insert(tk.END, str(current_month + 1)) 
 
    generate_calendar() 
 
root = tk.Tk() 
root.title("Генератор календаря") 
root.geometry('1400x600+0+0') 
root.configure(bg="#99CCCC") 
 
year_label = tk.Label(root, text="Год:", font=("Arial", 12), bg="#99CCCC") 
year_label.pack() 
 
year_entry = tk.Entry(root, font=("Arial", 12), width=45) 
year_entry.pack() 
 
month_label = tk.Label(root, text="Месяц:", font=("Arial", 12), bg="#99CCCC") 
month_label.pack() 
 
month_entry = tk.Entry(root, font=("Arial", 12), width=45) 
month_entry.pack() 
 
controls_frame = tk.Frame(root) 
controls_frame.pack(pady=10) 
 
width_button = 30 
height_button = 2 
generate_button = tk.Button(controls_frame, text="Сгенерировать календарь", font=("Arial", 12), bg='blue', command=generate_calendar, width=width_button, height=height_button) 
generate_button.pack(side=tk.LEFT) 
 
prev_button = tk.Button(controls_frame, text="Предыдущий месяц", font=("Arial", 12), bg='green', command=previous_month, width=width_button, height=height_button) 
prev_button.pack(side=tk.LEFT) 
 
next_button = tk.Button(controls_frame, text="Следующий месяц", font=("Arial", 12), bg='yellow', command=next_month, width=width_button, height=height_button) 
next_button.pack(side=tk.LEFT) 
 
calendar_frame = tk.Frame(root, bg="white", bd=2, relief="solid") 
calendar_frame.pack(pady=50, padx=50) 
 
rows = 8 
columns = 7 
for row in range(rows): 
    calendar_frame.grid_rowconfigure(row, weight=1) 
for col in range(columns): 
    calendar_frame.grid_columnconfigure(col, weight=1) 
 
root.mainloop()