import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

df_baru = df.copy()

for index, x in df_baru.iterrows():
    df_baru.at[index, 'Gaji'] = (lambda x: x * 1.05)(x['Gaji'])

# # Menampilkan DataFrame baru
# print(df_baru)

# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame setelah peningkatan gaji 5%:")
print(df_baru)

# Ringkasan perubahan yang telah terjadi
print("\nRingkasan perubahan:")
print("Setiap gaji karyawan ditingkatkan sebesar 5%.")
print()

# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
for index, row in df_baru.iterrows():
    if row['Usia'] > 30:
        df_baru.at[index, 'Gaji'] = (lambda x: x * 1.02)(row['Gaji'])

# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("DataFrame setelah peningkatan tambahan 2% untuk usia di atas 30 tahun:")
print(df_baru)

# Ringkasan hasil
print("\nRingkasan hasil:")
print("Karyawan di atas 30 tahun menerima peningkatan tambahan sebesar 2% dari gaji mereka setelah peningkatan sebesar 5%.")


# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://gitlab.com/itenas/tugas_pemdas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.