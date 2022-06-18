import os
import shutil

if __name__ == '__main__':

    image_formats = ["jpg","png","gif","webp","tiff","ps","dwg","jpeg"]
    audio_formats = ["mp3","wav"]
    video_formats = ["mp4","avi","webm","wav","mpg","wmv"]
    pdf_format = ["pdf"]
    data_format = ["csv","xlsx", "data", "dat","hkl","cif","pl","xls","ods","clf","xy","sum","out","cfl","pgrid"]
    program_format = ["exe","c","py","rdp","msi","sln","sh"]
    presentation_format = ["pptx", "ppsx","ppt","odp"]
    rar_format = ["rar","zip","bz2"]
    other_format = ["sym","prf","pcr","tif","avi","ai","ait","rtf","enw",
                    "crdownload","vesta","nb","nid","vi","vcf",
                    "bak","ris","rpa","asc","h3m","ics","bvs","step","o","ipt","map","psd","xml","swf"]
    txt_format = ["txt","names"]
    doc_docx_format = ["doc","docx","odt"]

    files = os.listdir("./")
    e = []
    for file in files:
        if os.path.isfile(file) and file != "segregator.py":
            ext = (file.split(".")[-1]).lower()
            #e += [ext]

            if ext in image_formats:
                shutil.move(file,"images/"+file)
            elif ext in audio_formats:
                shutil.move(file,"audio/"+file)
            elif ext in video_formats:
                shutil.move(file,"videos/"+file)
            elif ext in  pdf_format:
                shutil.move(file,"docs_pdfs/"+file)
            elif ext in data_format:
                shutil.move(file, "data/"+file)
            elif ext in program_format:
                shutil.move(file, "programs/"+file)
            elif ext in presentation_format:
                shutil.move(file,"presentations/"+file)
            elif ext in other_format:
                shutil.move(file, "others/" + file)
            elif ext in rar_format:
                shutil.move(file, "rar/" + file)
            elif ext in txt_format:
                shutil.move(file, "txt/" + file)
            elif ext in doc_docx_format:
                shutil.move(file, "doc_docx/" + file)
            else:
                continue