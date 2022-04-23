import zipfile
import os


with zipfile.ZipFile('final-final-compressed.zip','r') as myzipfile:

	liste = myzipfile.namelist()

	myzipfile.extractall('files')

toplam = 0

os.chdir("./files")

for i in liste:

	with zipfile.ZipFile(i , 'r') as file:

		liste1 = file.namelist()

		toplam += len(liste1)

		file.extractall()

print(toplam)