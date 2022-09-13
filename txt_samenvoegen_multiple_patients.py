import glob
from txt_samenvoegen import txt_samenvoegen
import os
from pathlib import Path

patient_id = []
input_folders = []
#Folder where the patient's names are listed
patient_folder = r'E:\DOXA_copy\PAR'



#Make a list of all the patient _id's
for file in os.listdir(patient_folder):
    d = os.path.join(patient_folder, file)
    if os.path.isdir(d):
        patient_id.append(os.path.basename(os.path.normpath(d)))




#directory voor de input txt files
for i in range(len(patient_id)):
    input_folders.append('E:/DOXA_copy/PAR/' + patient_id[i] + '/SpO₂')



#Plaats en de naam waar van de folder waar het txt bestand moet komen te staan en de naam van het txt bestand zelf
output_file = ["" for x in range(len(input_folders))]
output_folder = ["" for x in range(len(input_folders))]
for i in range(len(output_file)):
    output_folder[i]= r"E:\Doxa_nice_format" + '\\'  + patient_id[i]
    output_file[i]= r"E:\Doxa_nice_format" + '\\'  + patient_id[i] + '\\' + 'SpO2.txt'



#Create the output folder if it doesn't already exist
for i in range(len(output_folder)):

    os.mkdir(output_folder[i])

for i in range(len(input_folders)):
    txt_samenvoegen(input_folders[i],output_file[i])

