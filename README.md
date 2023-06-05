# BrickYard

BrickYard is the webshop for collectable Lego bricks and pieces.

At BrickYard, we are passionate about LEGO and dedicated to bringing you a wide range of LEGO pieces to enhance your building adventures. Whether you're a seasoned LEGO enthusiast or just starting your brick collection, we have something for everyone.

BrickYard is actually starting up as a new company using my platform that is created in this project.

As part of the project I have defined a model for article number (SKU), Lego already today have their numbers, but they doesn't take in acount the color of bricks.

BrickYard app is managed on my Github as repository BrichYard, the final production solution is deployed on Heroku with using ElephantSQL as database backend.
Domain is registered via Godaddy.com and email service is Microsoft Office 365 for domain. 
For sending marketing mail MailChimp is used for managing mailing list, API is used for subscribing user and unsubscribing.
When sending other mails Heroku addon Mailgun is used via AnyMail django plugin. 
Payment service is integrated against Stripe.

My next step is to improve the service and go public with webshop as a real business.


The definition is: articleno = [number]-[color]
Example: 451511-002 White Lego Pieces

| color number | Color |
|--- | --- |
| 001 | Blue |
| 002 | Black |
| 003 | White |
| 004 | Red |
| 005 | Yellow | 
| 006 | Brown |
| 007 | Gray |



# UX design
During the project UX design where done in Figma as tool for concept and prototyping. 
Example of pages from UX design:

<img width="901" alt="image" src="https://github.com/MFLind/Brickyard/assets/106115510/5498ab2f-cecd-4f61-9d40-c1bba848f0e0">

This is the home page.

<img width="787" alt="image" src="https://github.com/MFLind/Brickyard/assets/106115510/22cb8852-7c48-4b76-b99c-afc586525eb4">

This is the shop page.

<img width="762" alt="image" src="https://github.com/MFLind/Brickyard/assets/106115510/e6370e7d-25d0-4ec3-b69c-ae13578473f9">

This is the item deatel page where you can read more about every item when you have clickt on it.

<img width="762" alt="image" src="https://github.com/MFLind/Brickyard/assets/106115510/1e843b6d-573a-45c2-804b-964080d1e660">

This is the about us page and on this page you have the information to contact us with.

<img width="853" alt="image" src="https://github.com/MFLind/Brickyard/assets/106115510/a63a65b5-c2a1-46c0-86da-131f84838dd3">

This is the checkout page. This page are mising som staf on the ux disign. 

<img width="773" alt="image" src="https://github.com/MFLind/Brickyard/assets/106115510/9eb267eb-4562-4521-b3fa-f55fdc3708a7">

This is the page that comes up when you have a 404 error.

# Differant view on the website.
From the UX design work I create by hand all the webpages in product (from experience the export functions in Figma isn't perfect, also got information about that from expert UX designer that my employer is using for their products).

The resulting real pages in BrickYard (www.brickyard.se):

![image](https://github.com/MFLind/Brickyard/assets/106115510/dc245c5a-b33c-4ce6-b892-f7194723513a)
This is the home page. On here you can read litel about what BrickYard are. 

<img width="1325" alt="image" src="https://github.com/MFLind/Brickyard/assets/106115510/68d532a9-6414-4390-85a7-6b31300bcd21">
This is a view of the store page.

![image](https://github.com/MFLind/Brickyard/assets/106115510/2f9bb412-3c92-438a-bb4c-0408685fc816)
This is the abut us page. On hear you can read about us and contact us. You can also subscribe so you can gate emails when new praducts comms up.

![image](https://github.com/MFLind/Brickyard/assets/106115510/2ed9ef43-1048-4781-887a-4ef1cc5945ce)
This is the shoping basket. On hear you can se all your products you have shos to by.

![image](https://github.com/MFLind/Brickyard/assets/106115510/1c9f81ef-1414-4acd-8b74-6f3791daa862)
This is the loggin page. Hear can you loggin to you accont.

# Features
- Managed product handling via super user login for adding, edit and delete products.
- Martketing support via Mailchimp for mailing list
- Customer login for handling profiles and checkout
- Checkout via Stripe

## Future improvement
- Handle product stock and warehousing
- Enable bought TLS/SSL certificate of the Heroko service
- My own step in development is to study and learn React (and also React Native), so my goal is to change frontend code to React Frontend.

# Data model
Datamodel is implemented with Django framework.

![MicrosoftTeams-image (22)](https://github.com/MFLind/Brickyard/assets/106115510/4d3a98f3-227b-4d66-8e10-d056cbc60ada)

  
 # Social media
  I have created Pintrest (@brickyard_lego_store) and Instagram (@brickyard_lego_store) account for BrickYard, these social networks are the primary channel for BrickYards customers.
  
  But I have made a mockup Facebook for Business page as below:
  
  ![facebook_brickyard](https://github.com/MFLind/Brickyard/assets/106115510/2e255929-5054-45e3-b51d-4402662e2c82)


# Testing

I have done manual testing with the following methods:
- Running thru pylint for PEP8 validation, some warning exists but most are cleaned up.
- Running Black (https://github.com/psf/black) to validate coding style and format
- Validation of different operating systems and browsers to validate compability
- Registering new user
- Add products to basket and concluse purchase
- Add, edit and delete products


## Bugs
The development was done iterative and testing and finding bugs occure during the coding process.

## Remaining bugs
- Some Pylint issues still exists.
- gfdsag

## Validator Testing
- PEP8 via pylint locally on my computer
- Black locally on my computer

## Deployment
Deploying via Heroku and setting up ElefantSQL.
- Create a new App in Heroku
- Link to Brickyard repository in Github
- Add plugin Mailgun for mail service
- Add Buildpackage: heroku/python

Setup up propery parameters for the services:
SECRET_KEY=""
STRIPE_PUBLIC_KEY=""
STRIPE_SECRET_KEY=""
STRIPE_WH_SECRET=""
MAILCHIMP_API_KEY = ""
MAILCHIMP_REGION = ""
CLOUD_NAME=""
API_KEY=""
API_SECRET=""
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
O365_MAIL_TENANT_ID=""

# Credits
- Special thanks to Patrik Lindergren and Quagga Technologies AB for sponsering with Heroku and Figma account.


