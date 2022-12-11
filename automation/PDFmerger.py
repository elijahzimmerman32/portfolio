import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        print(file)
        merger.append(file)
    #In the Write Below, Put the name of the title you want to Merge Together
    merger.write("CombinedBSUniDocs.pdf")

