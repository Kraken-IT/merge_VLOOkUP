import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def process_tsv_files(file1_path, file2_path, output_file):
    try:
        # Birinci və ikinci faylları oxuyuruq
        file1_df = pd.read_csv(file1_path, sep='\t', header=None, names=['Key', 'Value'])
        file2_df = pd.read_csv(file2_path, sep='\t', header=None, names=['Key', 'Value'])

        # Birinci faylı dictionary olaraq saxlayırıq (açar: dəyər)
        file1_dict = pd.Series(file1_df.Value.values, index=file1_df.Key).to_dict()

        # İkinci fayldakı hər bir dəyər üçün uyğun dəyəri axtarırıq və tapırıqsa əlavə edirik
        file2_df['Value'] = file2_df['Key'].map(file1_dict).fillna("")

        # Nəticəni fayla yazdırırıq
        file2_df.to_csv(output_file, sep='\t', index=False, header=False)
        messagebox.showinfo("Success", f"Processing complete. Result saved as '{output_file}'.")
    except FileNotFoundError as e:
        messagebox.showerror("Error", f"Error: {e}. Please check the file paths.")

def select_file1():
    file_path = filedialog.askopenfilename(filetypes=[("TSV files", "*.tsv")])
    if file_path:
        file1_entry.delete(0, tk.END)
        file1_entry.insert(0, file_path)

def select_file2():
    file_path = filedialog.askopenfilename(filetypes=[("TSV files", "*.tsv")])
    if file_path:
        file2_entry.delete(0, tk.END)
        file2_entry.insert(0, file_path)

def process_files():
    file1_path = file1_entry.get()
    file2_path = file2_entry.get()
    output_file = os.path.join(os.getcwd(), 'result.tsv')
    process_tsv_files(file1_path, file2_path, output_file)

# Tkinter pəncərəsini yaradırıq
root = tk.Tk()
root.title("TSV File Merger")

# Birinci fayl üçün seçim düyməsi və giriş sahəsi
file1_label = tk.Label(root, text="Select File 1:")
file1_label.grid(row=0, column=0, padx=10, pady=10)

file1_entry = tk.Entry(root, width=50)
file1_entry.grid(row=0, column=1, padx=10, pady=10)

file1_button = tk.Button(root, text="Browse", command=select_file1)
file1_button.grid(row=0, column=2, padx=10, pady=10)

# İkinci fayl üçün seçim düyməsi və giriş sahəsi
file2_label = tk.Label(root, text="Select File 2:")
file2_label.grid(row=1, column=0, padx=10, pady=10)

file2_entry = tk.Entry(root, width=50)
file2_entry.grid(row=1, column=1, padx=10, pady=10)

file2_button = tk.Button(root, text="Browse", command=select_file2)
file2_button.grid(row=1, column=2, padx=10, pady=10)

# İşlət düyməsi
process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.grid(row=2, column=1, pady=20)

# Pəncərəni göstəririk
root.mainloop()
