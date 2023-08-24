from PyPDF2 import PdfReader
from PIL import Image
from PIL.ExifTags import TAGS
import argparse
from mutagen.mp3 import MP3

def printErrorMessage():
        print(" Error while extracting.\n Make sure you have specified the proper arguments.enter -h to know more")

def extract_audio_metadata(path):
    try:
        audio_metadata = MP3(path)
        for tag,value in audio_metadata.items():
            print(f"{tag:29} {value}")

    except:
        printErrorMessage()


def extract_pdf_metadata(path):
    try:
        pdf_reader = PdfReader(path)
        metadata = pdf_reader.metadata
        for tag,value in metadata.items():
            print(f"{tag:25} {value}")
    except:
        printErrorMessage()

def extract_image_metadata(path):

    try:
        file = Image.open(path)
        exif_data = file.getexif()

        for tagid in exif_data:
            tag_name =TAGS.get(tagid,tagid)
            tag_value = exif_data.get(tagid)

            print(f"{tag_name:25} {tag_value}")
    except:
        printErrorMessage()








description_message = "Extract metadata from files"
parser = argparse.ArgumentParser(description=description_message,usage=" -f/--file: to specify file path \n -t/--type: to specify file type \n -h: to know more")

parser.add_argument("-f","--file", help = "Add file path",required=True, dest="file_path")
parser.add_argument("-t","--type" ,help="Add file type", dest="type",choices=["image","pdf","audio","video"],required=True)

args  = parser.parse_args()

if(args.type=='image'):
    extract_image_metadata(args.file_path)
elif(args.type=='pdf'):
    extract_pdf_metadata(args.file_path)
elif(args.type=="audio"):
    if("mp3" not in args.file_path):
        print("Supports only mp3 file only. :(")
    else:
        extract_audio_metadata(args.file_path)
else:
    print("Not supported yet!")

