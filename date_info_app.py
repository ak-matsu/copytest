import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate():
    date_str = entry_date.get()
    try:
        if len(date_str) == 8:
            date_obj = datetime.strptime(date_str, '%Y%m%d')
        else:
            date_obj = datetime.strptime(date_str, '%Y/%m/%d')
        weekday = date_obj.strftime('%A')
        zodiac = get_zodiac(date_obj.year)
        result_str = f"{date_str} ({weekday}) - 干支: {zodiac}"
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result_str)
    except ValueError:
        messagebox.showerror("エラー", "日付の形式が正しくありません。yyyy/mm/dd または yyyymmdd の形式で入力してください。")

def get_zodiac(year):
    zodiacs = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    return zodiacs[(year - 4) % 12]

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    messagebox.showinfo("コピー", "結果がクリップボードにコピーされました。")

root = tk.Tk()
root.title("日付と干支計算")

# ポップなスタイルの設定
root.configure(bg='#f0f0f0')
font_style = ('Helvetica', 14)

tk.Label(root, text="日付 (yyyy/mm/dd または yyyymmdd):", bg='#f0f0f0', font=font_style).grid(row=0, column=0, pady=10)
entry_date = tk.Entry(root, font=font_style)
entry_date.grid(row=0, column=1, pady=10)

tk.Button(root, text="結果", command=calculate, bg='#4CAF50', fg='white', font=font_style).grid(row=1, column=0, columnspan=2, pady=10)

result_entry = tk.Entry(root, width=50, font=font_style)
result_entry.grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(root, text="コピー", command=copy_to_clipboard, bg='#2196F3', fg='white', font=font_style).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
