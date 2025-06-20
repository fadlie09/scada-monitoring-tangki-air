# SCADA Monitoring Tangki Air 💧

Proyek ini merupakan simulasi sistem SCADA (Supervisory Control and Data Acquisition) sederhana menggunakan Python GUI (Tkinter) untuk memantau level air dalam tangki. Pompa dikendalikan otomatis maupun manual berdasarkan level air yang terdeteksi.

## 🎯 Tujuan Sistem
- Memantau level air dalam tangki (0-100%)
- Mengatur status pompa secara otomatis/manual
- Memberikan indikator status: Kosong, Normal, Penuh
- Mempresentasikan HMI sederhana seperti di dunia industri/offshore

## 🛠️ Tools & Teknologi
- Python 3.10
- Tkinter (GUI Library)
- VS Code sebagai IDE
- GitHub untuk version control dan dokumentasi

## 🖥️ Tampilan Aplikasi

![flowchart](flowchart.png)

## 🔁 Logika Sistem

```plaintext
Jika Level < 20%  → Pompa ON → Status KOSONG (Merah)
Jika Level > 80%  → Pompa OFF → Status PENUH (Oranye)
Jika 20% < Level < 80% → Status NORMAL (Hijau)
