import pandas as pd 
import matplotlib.pyplot as plt 

file_path = 'Data_penduduk.xlsx'
df = pd.read_excel(file_path)

hitung_profesi = df['Profesi'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(
    hitung_profesi,
    labels=hitung_profesi.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.Set3.colors
)
plt.tittle('Distributin Profesi Warga Desa Cibodas')
plt.axix('equal')
plt.tight_layout()
plt.show()