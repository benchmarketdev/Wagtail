## Supported providers

- [Microsoft Cognitive Services](#microsoft-cognitive-services)
- [AWS Rekognition](#aws-rekognition)
- [Google Vision](#google-vision)


## Requirements

- Python 3.5+
- Wagtail 2+
- Access to any of the [supported providers](#providers)


## Installation

Install the library with pip:

```
$ pip install wagtailaltgenerator
```

Depending on your selected provider, you might also need extra requirements (example `pip install wagtailaltgenerator[rekognition]`. Please check the install instructions for the various providers below.


## Quick Setup (on Microsoft Cognitive Service)

1. Install `pip install wagtailaltgenerator`
2. Register an account on [Microsoft Cognitive Service](https://www.microsoft.com/cognitive-services/)
3. Retrieve API key for the product `Computer Vision - Preview`
4. Add the key to your django settings:

    ```
    COMPUTER_VISION_API_KEY = 'yourkey'
    ```
5. Make sure `wagtailaltgenerator` is added to your `INSTALLED_APPS`.

    ```python
    INSTALLED_APPS = (
        # ...
        'wagtailaltgenerator',
    )
    ```


## Usage

1. Upload an image through Wagtail
2. Watch the title and/or tags get generated...
3. ...And done!

### AWS Rekognition

Amazon's image analysis API. [Docs](https://aws.amazon.com/rekognition/)

- (+) Stable
- (-) Supports only tags

#### Installing

Add `...[rekognition]` when you install wagtailaltgenerator (this will install the extra packages required).

- `pip install wagtailaltgenerator[rekognition]`

#### Settings

The Rekognition provider is based on [boto](http://boto3.readthedocs.io/) and uses its [configuration](http://boto3.readthedocs.io/en/latest/guide/configuration.html).

These are three of the most common settings:

- `AWS_ACCESS_KEY_ID`: The access key for your AWS account
- `AWS_SECRET_ACCESS_KEY`: The secret key for your AWS account
- `AWS_DEFAULT_REGION`: The default region to use, e.g. us-west-2, eu-west-1, etc

You also need to define the provider:

- `ALT_GENERATOR_PROVIDER`: `'wagtailaltgenerator.providers.rekognition.Rekognition'`


