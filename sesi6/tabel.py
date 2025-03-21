from datetime import datetime
tahun_ini = datetime(2025,9,13)
data = [
    {"nama": "Nugraha", "birtdate": "1989-09-13"},
    {"nama": "John", "birtdate": "1990-01-01"},
    {"nama": "jane", "birtdate": "1992-02-02"},
    {"nama": "Doe", "birtdate": "1994-03-03"},
     ]
print(f"{'No':<5}{'Nama':<15}{'Usia':<5}")
print ("_" * 25)


for index, person in enumerate(data, start=1):
    birthdate = datetime.strptime(person["birtdate"], "%Y-%m-%d")
    age = (tahun_ini - birthdate) .days // 365
    print(f"{index:<5}{person['nama']:<15}{age:<5}")
