# ThingLogix
### AWS Lambda function to convert an address to lat lon and vice-versa

## Installation guide
Clone this repository, then zip all of the contents. Upload the zip file to AWS Lambda as a Lambda function with runtime Python 3.6. The handler should be convert_format.lambda_handler. Set an environment variable called "key" which is your Google Maps Developer API key.

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
