# Textract Image Search
Retrieve local images more easily by retrieving their text content using Amazon Textract.

Motivation of this small Python project which uses only ONE from the 250+ AWS services: Amazon Textract.

* More than often I find myself searching for specific images I have in my collection, especially for diagrams or other images containing text like this one: ![Architecture Image](./images/Screenshot&#32;2022-04-01&#32;at&#32;13.17.06.png)

Solution:
* To support a text based search in images, you typically use an OCR (Optical Image Recognition) step before.
* Our OCR solution will be Amazon Textract - https://aws.amazon.com/textract/.
* The related Python script is creating a local database containing text files - one text (.txt) file for each image.
* As a second step, the script allows for a substring related search in that text file list, fetching all images which contain that substring.

Prerequisites:
* You need Python installed on your laptop.
* Preferrably your laptop is running MacOS, because in that case, opening the images using the "Preview" app is also done within the Python script.
* You need an AWS account and your Python script needs permission to use the Amazon Textract API.

Getting started:
*

Further steps:
* 
