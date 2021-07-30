import os
import pandas as pd



n = 0
b = []
a = []

for path, subdirs, files in os.walk(r'/media/patient/02/motu_shazada/Data_set/'):
#     print(path)
#     print(files)
    
    if n > 0:
        N_c = len(files)
        b.append(N_c)
    n+=1
    for filename in subdirs:
        f = os.path.join( filename)
        a.append(str(f))




# print(len(b))
# print(len(a))
# print(a)
# print(b)
final = dict()
final["folder_name"] = a
final["image_len"] = b
df = pd.DataFrame(final)
df.to_excel("Name and Images.xlsx")