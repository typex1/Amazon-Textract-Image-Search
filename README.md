# Amazon Textract Image Search
Retrieve local images incredibly fast - based on their extracted text using Amazon Textract.

## Motivation of this project:

More than often I find myself searching for specific images I have in my collection, especially for diagrams or other images containing text like this one: 

Where did I put that **Couchbase** related architecture diagram again?

![Architecture Image](./images/Screenshot&#32;2022-04-01&#32;at&#32;13.17.06.png)

Not a problem if you need to flip through **a dozen of images**.

But what to do if you have **1000+** images on your local computer?

## Solution:

* To support a **text based search in images**, you typically use an OCR (Optical Image Recognition) step before.
* Our OCR solution will be Amazon Textract - https://aws.amazon.com/textract/.
* The Python script contained in this repo is creating a **local flatfile database consisting of text files** - one text (.txt) file for each image.
* As a second step, the script allows for a substring related search in that text file list, mappping them to all images which contain that substring.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* You need Python3 installed on your laptop. On top, please install the AWS SDK named "boto3":
    ```
    pip install boto3
    ```
* Preferably your laptop is running MacOS, because in that case, opening the images using the "Preview" app is also done within the Python script.
* If you are running Linux or Windows, please exchange "Preview" with your preferred image viewer.
* You need an AWS account and your Python script needs permission to use the Amazon Textract API.

## Getting started:

* Download or clone this github repo to your local laptop.
* The default image path is ./images, the default Amazon Textract output path for the text files is ./images/textract-data
* Perform a test - copy and past the command below:
    ```
    python3 retrieve_images.py "gateway"
    ```
* As a result, the script will retrieve two image files containing "Gateway", the search is done irrespective of upper or lower case.
* Optionally, you can indicate an image file name constraint in the second parameter, e.g. filtering only those images containing "2022-04" in their names:
    ```
    python3 retrieve_images.py "gateway" "2022-04"
    ```
* For your understanding, check this repository's image files in ``` images/ ``` and text files in ``` images/textract-data/ ```.
* As you can see, Amazon Textract is also capable to retrieve text from handwritten input, e.g. [day_60.jpg](https://github.com/typex1/Amazon-Textract-Image-Search/blob/main/images/day_60.jpg) - the source of that image is [here](https://raw.githubusercontent.com/sarthaksavvy/100DaysOfAWS/main/images/6e6f13a0a20de75159d04a34e394f15cc16386d0.jpeg).
* Given the above image example containing images parts in light gray, so with very little contrast, you will see that also those faint areas will be detected correctly.

## Cost considerations:

* As indicated in the official [Textract Pricing Data](https://aws.amazon.com/textract/pricing/), scanning 1,000 images has an effective price of US$1.50.

## Further steps:

* If you a running on Windows or Linux, exchange your preferred image viewer in the Python script, in function ```show_results()```.
