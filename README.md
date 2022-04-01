# Textract Image Search
Retrieve local images more easily by retrieving their text content using Amazon Textract.

## Motivation of this small Python project which uses only ONE from the 250+ AWS services: Amazon Textract.

* More than often I find myself searching for specific images I have in my collection, especially for diagrams or other images containing text like this one:

![Architecture Image](./images/Screenshot&#32;2022-04-01&#32;at&#32;13.17.06.png)

But what to do if you have 1000+ images to look into?

## Solution:

* To support a **text based search in images**, you typically use an OCR (Optical Image Recognition) step before.
* Our OCR solution will be Amazon Textract - https://aws.amazon.com/textract/.
* The related Python script is creating a **local database containing text files** - one text (.txt) file for each image.
* As a second step, the script allows for a substring related search in that text file list, fetching all images which contain that substring.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* You need Python installed on your laptop.
* Preferably your laptop is running MacOS, because in that case, opening the images using the "Preview" app is also done within the Python script.
* You need an AWS account and your Python script needs permission to use the Amazon Textract API.

## Getting started:

* Download or clone this github repo to your local laptop.
* The default image path is ./images, the default Amazon Textract output path for the text files is ./images/textract-data
* Perform a test - copy and past the command below:
    ```
    python3 retrieve_images.py "gateway"
    ```
* As a result, the script will retrieve two image files containing "Gateway", the search is done irrespective of upper or lower case.
* For your transparency, check this repository's image files in ```images/``` and text files in ```images/textract-data/````.
* As you can see, Amazon Textract is also capable to retrieve text from handwritten input (file day_60.jpg - source indication is here: https://raw.githubusercontent.com/sarthaksavvy/100DaysOfAWS/main/images/6e6f13a0a20de75159d04a34e394f15cc16386d0.jpeg )


## Further steps:

* If you a running on Windows or Linux, 
