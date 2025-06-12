import datetime as dt
import tkinter as tk
from tkinter import messagebox

def hitung_umur():
    try:
        tanggal = int(entry_tanggal.get())
        bulan = int(entry_bulan.get())
        tahun = int(entry_tahun.get())

        tanggal_lahir = dt.date(tahun, bulan, tanggal)
        hari_ini = dt.date.today()
        umur_hari = hari_ini - tanggal_lahir
        umur_tahun = umur_hari.days // 365
        umur_bulan_sisa = (umur_hari.days % 365) // 30

        hasil = (
            f"Tanggal lahir Anda: {tanggal_lahir} ({tanggal_lahir:%A})\n"
            f"Hari ini: {hari_ini}\n"
            f"Umur Anda: {umur_tahun} tahun, {umur_bulan_sisa} bulan"
        )
        messagebox.showinfo("Hasil", hasil)
    except Exception as e:
        messagebox.showerror("Error", f"Input tidak valid.\n{e}")


# Setup window
window = tk.Tk()
window.title("Hitung Umur")
window.geometry("300x250")

# Label dan Entry Tanggal
tk.Label(window, text="Masukkan Tanggal Lahir Anda").pack(pady=10)

tk.Label(window, text="Tanggal (1-31)").pack()
entry_tanggal = tk.Entry(window)
entry_tanggal.pack()

tk.Label(window, text="Bulan (1-12)").pack()
entry_bulan = tk.Entry(window)
entry_bulan.pack()

tk.Label(window, text="Tahun (YYYY)").pack()
entry_tahun = tk.Entry(window)
entry_tahun.pack()

# Tombol Proses
tk.Button(window, text="Hitung Umur", command=hitung_umur).pack(pady=15)

# Jalankan window
window.mainloop()
