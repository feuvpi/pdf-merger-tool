import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger();

for file in os.listdir(os.curdir):
    if file.ends(".pdf"):

        merger.append(file)
    merger.write("Merged_pdf")