import fitz 
import shutil
import os
from pathlib import Path

#DEFINE OUTPUT AND INPUT FILES
INPUT_FOLDER=Path('./PDF_compressor/ogPDF')
OUTPUT_FOLDER=Path('./PDF_compressor/compressedPDF')
ARCHIVE_FOLDER=Path('./PDF_compressor/archivePDF')

#if the outputs folders dont exist the prog creates it
for folder in [OUTPUT_FOLDER,ARCHIVE_FOLDER]:
        folder.mkdir(exist_ok=True)

#def compress_pdf(input, output): 
#    doc = fitz.open(input)
#
#    doc.save(output, garbage=4, deflate=True) 
#    doc.close()
#    print("compressed : {output}")



def compress_pdf_from_img(input,output):
    
    doc=fitz.open(input)
    new=fitz.open()
    for page in doc:
        pics=page.get_pixmap(dpi=85)
        new_p=new.new_page(width=page.rect.width,height=page.rect.height)
        new_p.insert_image(page.rect, pixmap=pics)
    new.save(output, garbage=4, deflate=True)
    new.close

#test
#compress_pdf_from_img('./ogPDF/test.pdf','./compressedPDF/comp.pdf')


def folder_processing():
     for files in INPUT_FOLDER.iterdir():
          if files.is_file() and files.suffix.lower() ==".pdf":
               name_no_ext= files.stem
               ext=files.suffix

               output_path= OUTPUT_FOLDER/f"{name_no_ext}_compressed{ext}"
               archive_path= ARCHIVE_FOLDER/files.name

               compress_pdf_from_img(files, output_path)

                #move the original file that is now co;pressed
               shutil.move(str(files), str(archive_path))
               print (f"Done for {files.name}")

folder_processing()