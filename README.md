# ThingLogix
### AWS Lambda function to convert an address to lat lon and vice-versa

## Installation guide
Clone this repository, then zip all of the contents. Upload the zip file to AWS Lambda as a Lambda function with runtime Python 3.6. The handler should be convert_format.lambda_handler. Set an environment variable called "key" which is your Google Maps Developer API key.

## Installation guide  

You will first need to clone this repository to your device.  You can do this from this git hub page by clicking the green
'clone or download' button found on the right side of the screen and clicking 'download as zip'.<br>

Sign into your AWS account and navigate to the AWS Lambda page, this can be found from the console by clicking the
'Lambda' button under the 'Compute' section.<br>

Click the 'Create Function' button in the upper right.<br>

Under 'Author from scratch', make sure that you have each of the following:
- Name can be anything you want
- Runtime must be 'Python 3.6'
- Role must be 'Choose an existing role'
- In the 'Existing role' drop down menu, select 'lambda_basic_execution'

Go ahead and create your lambda function by clicking the orange button in the bottom right corner

In the lambda configuration screen scroll down to the page the says 'Function Code'
in the 'Code Entry Type' drop down, select 'Upload a .ZIP file'

In the 'Handler' menu, type *convert_format.lambda_handler*

Set an environment variable called "key" which is your Google Maps Developer API key.

The last step is to upload code.  Under the 'Function package' section, click the Upload button and find the .zip that you just downloaded.

### Usage instructions
To use this AWS Lambda function, once it has been installed, you have the option of converting an address to lat lon or a lat lon to address. Below is how you should pass values to the Lambda function.
For the former:
```
{
    "address": "1042 Walnut St, San Luis Obispo, CA"
}
```
For the latter:
```
{
    "lat": "35.285884",
    "lon": "-120.663390"
}
```
