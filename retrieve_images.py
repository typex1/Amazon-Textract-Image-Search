import boto3
import sys
import os
import platform

# fspiess, 2022-03-15
#
# allowed Texract input: PNG, JPG, TIFF, PDF
# see also https://docs.aws.amazon.com/textract/latest/dg/limits.html
#
# start: set variable IMAGE_DIR to match your image folder
#
# usage: python3 retrieve_images.py <search pattern> <optional: filename pattern, e.g. 2021-10-08>

debug = False
##### set IMAGE_DIR to match your image folder ##########
#IMAGE_DIR=os.environ['HOME']+'/Desktop/Screenshots'
IMAGE_DIR='./images'
TEXTRACT_OUTPUT_DIR = IMAGE_DIR + "/textract-data"

txtNames = []
imageList = []
imageString = ""
imageNumber = 0
fileNamePattern=""
contentPattern=""

def check_dirs(image_dir, textract_output_dir):
    if os.path.isdir(image_dir):
        if os.path.isdir(textract_output_dir):
            if debug:
                print('textract_output_dir exists: '+textract_output_dir)
            pass
        else:
            os.mkdir(textract_output_dir)
            if debug:
                print(textract_output_dir+ ' does not exist - creating it.')
    else:
        print('image directory '+image_dir+' does not exist.')
        exit(1)

# original source: https://github.com/aws-samples/amazon-textract-code-samples/blob/master/python/03-reading-order.py
def detect_text_in_reading_order(textract_response,fileName,textract_output_dir):
    # Detect columns and print lines
    columns = []
    lines = []
    for item in textract_response["Blocks"]:
          if item["BlockType"] == "LINE":
            column_found=False
            for index, column in enumerate(columns):
                bbox_left = item["Geometry"]["BoundingBox"]["Left"]
                bbox_right = item["Geometry"]["BoundingBox"]["Left"] + item["Geometry"]["BoundingBox"]["Width"]
                bbox_centre = item["Geometry"]["BoundingBox"]["Left"] + item["Geometry"]["BoundingBox"]["Width"]/2
                column_centre = column['left'] + column['right']/2

                if (bbox_centre > column['left'] and bbox_centre < column['right']) or (column_centre > bbox_left and column_centre < bbox_right):
                    #Bbox appears inside the column
                    lines.append([index, item["Text"]])
                    column_found=True
                    break
            if not column_found:
                columns.append({'left':item["Geometry"]["BoundingBox"]["Left"], 'right':item["Geometry"]["BoundingBox"]["Left"] + item["Geometry"]["BoundingBox"]["Width"]})
                lines.append([len(columns)-1, item["Text"]])

    lines.sort(key=lambda x: x[0])
    # fsp: fileName is not defined:
    output = open(textract_output_dir+"/"+fileName+'.txt','w')
    # Print detected text to file:
    for line in lines:
        output.write(line[1] + '\n')
    output.close()

def update_local_text_data(image_dir, textract_output_dir):
    textract = boto3.client('textract')
    textract_files = []
    for (dirpath, dirnames, filenames) in os.walk(image_dir):
        for file in filenames:
            if file.endswith('.jpg') or file.endswith('.png')\
              or file.endswith('.JPG') or file.endswith('.PNG'):
                imageList.append(file)
    if debug:
        print('image list:'+str(imageList))

    for fileName in imageList:
        fileName = fileName.strip()

        # skip call to Textract if .txt already exists:
        if os.path.isfile(textract_output_dir+"/"+fileName+'.txt'):
            if debug:
                print('  image '+fileName+' is alrady processed, skipping...')
            continue
        else:
            print("image to be processed by Textract: "+str(fileName))
            textract_files.append(str(fileName))
    if len(textract_files) > 0:
        print("\nAmazon Textract image processing for {} images will take approx. {} seconds".format(str(len(textract_files)),str(6*len(textract_files))))
    for fileName in textract_files:
        # Read document content
        with open(image_dir+"/"+fileName, 'rb') as document:
            imageBytes = bytearray(document.read())

        # Call Amazon Textract
        response = textract.detect_document_text(Document={'Bytes': imageBytes})
        detect_text_in_reading_order(response,fileName,textract_output_dir)

def show_results(image_dir, textract_output_dir):
    #global image_dir
    global imageString
    global imageNumber
    found = 0
    for fileName in imageList:
        if fileNamePattern != "" and fileNamePattern not in fileName:
            continue
        txtName = fileName.strip()+'.txt'

        with open(textract_output_dir+"/"+txtName) as f:
            if contentPattern.lower()  in f.read().lower():
                imageString = imageString + '\"'+image_dir+"/"+txtName[:-4]+'\"' + " "
                imageNumber = imageNumber + 1

    for i in imageString.split('" "'):
        i=i.replace('" ','')
        i=i.replace('"','')
        found+=1
    if imageString=='':
        found=0

    print("Found {} images: {}".format(found,imageString))
    # OS detection: Darwin (MacOS), Linux, Windows
    if found > 0 and platform.system() == 'Darwin':
        os.system('open -a Preview '+imageString)

def search_local_text():
    global fileNamePattern
    global contentPattern

    if len(sys.argv) ==3:
        fileNamePattern=sys.argv[2]
    if debug:
        print('fileNamePattern='+fileNamePattern)
    contentPattern=sys.argv[1]

# main
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("usage: python3 "+sys.argv[0]+" \"<search pattern>\" <optional: filename pattern, e.g. \"2021-10-08\">")
        sys.exit()

    check_dirs(IMAGE_DIR, TEXTRACT_OUTPUT_DIR)
    update_local_text_data(IMAGE_DIR, TEXTRACT_OUTPUT_DIR)
    search_local_text()
    show_results(IMAGE_DIR, TEXTRACT_OUTPUT_DIR)
