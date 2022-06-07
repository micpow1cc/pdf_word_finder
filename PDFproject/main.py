import re
import os
from pdfminer.high_level import extract_text


def how_many_files_in_dict():
    global count, files
    count = 0
    directory = os.fsencode("pdfs")
    for root_dir, cur_dir, files in os.walk(r'C:\Users\micpo\PycharmProjects\PDFproject\pdfs'):
        count += len(files)


def find_pdf():
    global files
    path = r'C:\Users\micpo\PycharmProjects\PDFproject\pdfs'
    files = os.listdir(path)
    pdf_txt = []
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            pdf_txt.append(os.path.join(root, name))
    what_to_find = "Gdańsk University of Technology"
    for i in range(0, count):
        text = extract_text(pdf_txt[i])
        if re.search(what_to_find, text):
            print(pdf_txt[i])


if __name__ == '__main__':
    how_many_files_in_dict()
    find_pdf()




