import tkinter as tk
from tkinter import messagebox
import random

class SCADATangki:
    def __init__(self, root):
        self.level = 50
        self.mode_otomatis = True
        self.pompa_status = False

        # Penanda agar alarm tidak muncul berkali-kali
        self.sudah_alarm_kosong = False
        self.sudah_alarm_penuh = False

        self.root = root
        self.root.title("SCADA - Monitoring Tangki Air")

        # Label Level Air
        self.label_level = tk.Label(root, text=f"Level Air: {self.level}%", font=("Arial", 14))
        self.label_level.pack()

        # Bar Air
        self.canvas = tk.Canvas(root, width=200, height=30)
        self.bar = self.canvas.create_rectangle(0, 0, 2*self.level, 30, fill="blue")
        self.canvas.pack()

        # Status Sistem
        self.label_status = tk.Label(root, text="Status: NORMAL", font=("Arial", 12))
        self.label_status.pack()

        # Mode Otomatis / Manual
        self.radio_mode = tk.StringVar(value="otomatis")
        tk.Radiobutton(root, text="Otomatis", variable=self.radio_mode, value="otomatis", command=self.ganti_mode).pack()
        tk.Radiobutton(root, text="Manual", variable=self.radio_mode, value="manual", command=self.ganti_mode).pack()

        # Status Pompa
        self.label_pompa = tk.Label(root, text="Pompa: OFF", font=("Arial", 12))
        self.label_pompa.pack()

        # Tombol Manual
        self.btn_on = tk.Button(root, text="ON", command=self.nyalakan_pompa)
        self.btn_on.pack(side="left", padx=10)

        self.btn_off = tk.Button(root, text="OFF", command=self.matikan_pompa)
        self.btn_off.pack(side="left")

        self.update()

    def ganti_mode(self):
        self.mode_otomatis = (self.radio_mode.get() == "otomatis")

    def nyalakan_pompa(self):
        if not self.mode_otomatis:
            self.pompa_status = True

    def matikan_pompa(self):
        if not self.mode_otomatis:
            self.pompa_status = False

    def tampilkan_alarm(self, pesan, warna):
        messagebox.showwarning("⚠️ Alarm!", pesan)

    def update(self):
        if self.mode_otomatis:
            if self.level < 20:
                self.pompa_status = True
            elif self.level > 80:
                self.pompa_status = False

        if self.pompa_status:
            self.level += 1
        else:
            self.level -= 1

        self.level = max(0, min(100, self.level))

        # Update GUI
        self.label_level.config(text=f"Level Air: {self.level}%")
        self.canvas.coords(self.bar, 0, 0, 2*self.level, 30)

        # Status warna
        if self.level <= 20:
            status = "KOSONG"
            warna = "red"
        elif self.level >= 80:
            status = "PENUH"
            warna = "orange"
        else:
            status = "NORMAL"
            warna = "green"

        self.label_status.config(text=f"Status: {status}", fg=warna)
        self.label_pompa.config(text=f"Pompa: {'ON' if self.pompa_status else 'OFF'}")

        # Cek alarm
        if self.level < 10 and not self.sudah_alarm_kosong:
            self.tampilkan_alarm("⚠️ Tangki Hampir Kosong!", "red")
            self.sudah_alarm_kosong = True
        elif self.level >= 10:
            self.sudah_alarm_kosong = False  # Reset alarm jika aman

        if self.level > 90 and not self.sudah_alarm_penuh:
            self.tampilkan_alarm("⚠️ Tangki Hampir Penuh!", "orange")
            self.sudah_alarm_penuh = True
        elif self.level <= 90:
            self.sudah_alarm_penuh = False  # Reset alarm jika aman

        self.root.after(500, self.update)

# Jalankan Aplikasi
root = tk.Tk()
app = SCADATangki(root)
root.mainloop()

