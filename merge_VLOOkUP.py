
import pandas as pd
import os

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
        print(f"Processing complete. Result saved as '{output_file}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the file paths.")

# İşə salındığı qovluqda fayl yollarını müəyyən edirik
current_directory = os.getcwd()
file1_path = os.path.join(current_directory, 'file1.tsv')
file2_path = os.path.join(current_directory, 'file2.tsv')
output_file = os.path.join(current_directory, 'result.tsv')

# Funksiyanı çağırırıq
process_tsv_files(file1_path, file2_path, output_file)
    