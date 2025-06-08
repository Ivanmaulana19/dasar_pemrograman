import pandas as pd 
import matplotlib.pyplot as plt

file_path = 'Data_Penduduk.xlsx'
df = pd.read_excel(file_path)

grouped = df.groupbt(['Pndidikan_terakhir', 'jenis_Kelamin']).size().unstack(fill_value=0)
grouped.plot(kind='bar', figsize=(10,6))

plt.tittle('Jumlah Warga Berdasarkan Pendidikan terakhir dan jenis Kelamin')
plt.xlabel('Pendidikan Terakhir')
plt.ylabel('JUmlah Warga')
plt.xtricks(rotation=45)
plt.legend(tittle='jenis Kelamin')
plt.tight_layout()
plt.show
