# Textract Image Search
Retrieve local images more easily by retrieving their text content using Amazon Textract.

## Motivation of this small Python project which uses only ONE from the 250+ AWS services: Amazon Textract.

* More than often I find myself searching for specific images I have in my collection, especially for diagrams or other images containing text like this one:

![Architecture Image](./images/Screenshot&#32;2022-04-01&#32;at&#32;13.17.06.png)

## Solution:

* To support a **text based search in images**, you typically use an OCR (Optical Image Recognition) step before.
* Our OCR solution will be Amazon Textract - https://aws.amazon.com/textract/.
* The related Python script is creating a local database containing text files - one text (.txt) file for each image.
* As a second step, the script allows for a substring related search in that text file list, fetching all images which contain that substring.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* You need Python installed on your laptop.
* Preferrably your laptop is running MacOS, because in that case, opening the images using the "Preview" app is also done within the Python script.
* You need an AWS account and your Python script needs permission to use the Amazon Textract API.

## Getting started:

* Clone this github repo to your local laptop.
* The default image path is ./images, the default Amazon Textract output path for the text files is ./images/textract-data

## Further steps:

* If you a running on Windows or Linux, 
