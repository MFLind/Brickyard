# BrickYard

BrickYard is the webshop for collectable Lego bricks and pieces for Business to Consumer.

<img width="1507" alt="MicrosoftTeams-image (23)" src="https://github.com/MFLind/Brickyard/assets/106115510/433d0c10-c7b6-46a5-b999-7947b5ea18a1">


At BrickYard, we are passionate about LEGO and dedicated to bringing you a wide range of LEGO pieces to enhance your building adventures. Whether you're a seasoned LEGO enthusiast or just starting your brick collection, we have something for everyone.

BrickYard is actually starting up as a new company using my platform that is created in this project.

As part of the project I have defined a model for article number (SKU), Lego already today have their numbers, but they doesn't take in acount the color of bricks.

BrickYard app is managed on my Github as repository BrickYard, the final production solution is deployed on Heroku with using ElephantSQL as database backend.
Domain is registered via Godaddy.com and email service is Microsoft Office 365 for domain. 
For sending marketing mail MailChimp is used for managing mailing list, API is used for subscribing user and unsubscribing.
When sending other mails Heroku add-on Mailgun is used via AnyMail django plugin. 
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


# Business Model

*Brickyard* operates under the e-commerce business model where we purchase large quantities of old Lego sets from sources like eBay and other online marketplaces. We then refurbish these sets, break them down into individual pieces or figures (figs), and resell them on our platform. Our primary revenue comes from selling these unique and retro Lego bricks and figs to individual consumers, collectors, and enthusiasts. 

Our competitive edge lies in our ability to source, refurbish, and offer rare and unique pieces that might otherwise be difficult to find, providing a marketplace for the niche community of Lego enthusiasts.

We already have bought several lots of Lego over 100 kg (buying in bulk), for example in these lot we have refurbished over 250 minifigs, where just around 10 of these minifigs have repaid the original investment cost.

# Marketing Strategy

1. **Target Audience Identification:** Our primary audience includes Lego enthusiasts, collectors, and individuals looking for specific rare Lego pieces or figs. We will develop detailed buyer personas to help us understand and cater to our customers' needs effectively.

2. **Online Advertising:** We will leverage targeted social media advertisements and Google Ads. These platforms allow us to target ads based on interests (e.g., interest in Legos, collectibles), enhancing our ad's effectiveness.

3. **Content Marketing:** We will establish a blog on our website that shares interesting information about the Lego universe, collecting tips, rare piece features, and other relevant content. This will not only boost our SEO efforts but also position Brickyard as a trusted resource in the Lego community.

4. **Email Marketing:** Customers will be encouraged to sign up for newsletters when they visit our website. We can then use email marketing to keep our customers informed about new product arrivals, special promotions, and other updates.

5. **Partnerships and Collaborations:** We can partner with popular Lego influencers on platforms like Pinterest, YouTube or Instagram. They can feature our products, unbox them, or use them in a build, exposing our shop to their followers.

6. **SEO Strategy:** Optimize our website and product listings with relevant keywords to ensure we appear in search engine results when customers are looking for specific Lego pieces or collectibles.


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

# User Stories

## User Story: Browsing the Product Catalog
1.	Story for Browsing the Product Catalog
The customer should be able to browse various Lego sets by theme, age group, and price range.

**Acceptance Criteria:**
-	User can filter Lego sets by theme, age group, and price.
-	User can sort Lego sets by popularity, new releases, and price.
-	User can see product details like the name, price, picture, and age recommendation.
2.	Story for Adding Products to the Shopping Cart
The customer should be able to add Lego sets to my shopping cart,
So that they can collect all desired sets in one place before checkout.

**Acceptance Criteria:**
-	User can add a Lego set to the cart from the product detail page.
-	User can view the number of items in the cart.
-	User can view a summary of the items added to the cart.
3.	Story for Checking Out and Making a Purchase
The customer should be able to check out smoothly and securely,
So that they can confidently make a purchase.

**Acceptance Criteria:**
-	User can view a detailed breakdown of the cart total, including taxes and shipping charges.
-	User can enter shipping and billing information.
-	User can choose a payment method and complete the payment.
-	User receives a confirmation of the purchase via on-screen message and email.
4.	Story for Writing and Viewing Reviews
The customer should be able to read and write reviews about Lego sets,
So that they can make informed purchasing decisions and share my experience with others.

**Acceptance Criteria:**
-	User can view reviews on the product detail page.
-	User can write a review, giving a star rating and leaving a comment.
-	User can view their own reviews in their account.
5.	Story for Creating and Managing an Account
The customer should be able to create an account,
So that they can save my shipping information and track my orders.

**Acceptance Criteria:**
-	User can create an account with their email.
-	User can log in and out of their account.
-	User can update their shipping and billing information.
-	User can view their past purchases and track their current orders.

## Story for Adding to and Managing a Wishlist
The customer should be able to add Lego sets to my wishlist and manage it,
So that I can save sets I'm interested in for future consideration or purchase.

**Acceptance Criteria:**
-	User can add a Lego set to their wishlist from the product detail page.
-	User can view all items in their wishlist.
-	User can remove items from their wishlist.
-	User can move or add items from their wishlist directly to their shopping cart.
-	User can share their wishlist via email or social media.



# Differant view on the website.
From the UX design work I create by hand all the webpages in product (from experience the export functions in Figma isn't perfect, also got information about that from expert UX designer that my employer is using for their products).

The resulting real pages in BrickYard (https://brickyard.herokuapp.com / www.brickyard.se):

![image](https://github.com/MFLind/Brickyard/assets/106115510/dc245c5a-b33c-4ce6-b892-f7194723513a)
This is the home page. On here you can read litel about what BrickYard are. 

<img width="1325" alt="image" src="https://github.com/MFLind/Brickyard/assets/106115510/68d532a9-6414-4390-85a7-6b31300bcd21">
This is a view of the store page.

![image](https://github.com/MFLind/Brickyard/assets/106115510/2f9bb412-3c92-438a-bb4c-0408685fc816)
This is the abut us page. On hear you can read about us and contact us. You can also subscribe so you can gate emails when new praducts comms up.

![image](https://github.com/MFLind/Brickyard/assets/106115510/2ed9ef43-1048-4781-887a-4ef1cc5945ce)
This is the shoping basket. On hear you can se all your products you have shos to by.

![image](https://github.com/MFLind/Brickyard/assets/106115510/1c9f81ef-1414-4acd-8b74-6f3791daa862)
This is the loggin page. Hear can you login to you accont.

<img width="1325" alt="image" src="https://github.com/MFLind/Brickyard/assets/106115510/b3330299-d67f-4631-b9ad-deba29420150">
Signup page for mailing list, using Mailchimp in backend side.

# Features

The main functionalities for the Brickyard webshop platform is to provide a nice and easy interface for customer to read about products. Place in shopping basket and checkout to order products.

It possible to register and login as customer and a seperate Role for superuser.

Super user can add, edit and delete products in product register. Each product can have image and prices. 

User that has logged in for its account can add products to their wishlist.

Martketing support via Mailchimp for mailing list

Customer login for handling profiles and checkout

When placing a order, products get added to shopping basket, for Checkout is done Stripe payment service and verification emails are sent for order confirmation.

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


# Software solutions
In the Brickyard project different components and tools has been used for design, development and deployment.

## Development environment
The development environment consist of:
1. GitHub - Source control, project management and wikipage
2. Figma - Web based UX design tool for creating prototype look and UX design
3. GitPod - Web based Visual Code (also remote use of Visual code), development server and staging environment
4. Visual Code - Development IDE for writing and remote work against Gitpod servers
5. responsively-app - Open Source tool for check resposive web pages better than AmIResponsive (https://github.com/responsively-org/responsively-app)

## Production environment
The production enviroment is for final testing and system setup.
1. Heroku - Application server setup and build streams
2. ElephantSQL - For hosted PostgresSQL server
3. Godaddy - Registration of domain Brickyard.se and DNS servers
4. Microsoft 365 - Hosting mailserver for incoming mails for Brickyard.se
5. Mailchimp - Managing of mailling list
6. Stripe - Payment checkout service

## Module dependencies
- Django 4.1.6 - Used for backend and data model management and web rendering
- Stripe - Payment checkout service 
- Cloudinary - Storing and manage static files and media files
- Bootstrap 5.0 - Frontend templates for create CSS and design easy
- Django allauth - for user management
- AnyMail - for interface mail sending
- Pylint - Validation of PEP8 coding style (https://www.pylint.org/)
- Black - Python code formatter (https://github.com/psf/black)
- Pytest - Automatic testing (https://docs.pytest.org/en/7.3.x/)



# Testing and Validation

Validation and testing of Brickyard project has been done continuesly during the development, but in a structured way.

Validation been using different tools like Black and pylint.

Part of functionaly testing validation of different browsers and screen setup has been done.


## Validation
First level of verification is done in code validation and formatting by using Black formatter in Visual Code and also in command line. 

Second level of validation is done via using Pylint to validate coding and formatting error according to PEP8.

**Black**
Running Black (https://github.com/psf/black) to validate coding style and format, Black formatter is quite uncompromising and make code clearer and actually run faster.

All the code modules been run via Black formatter before running pylint.

**Pylint**
Pylint is runned in background of Visual and gives warning continuesly, where I have fixed and modified to comply with PEP8.

Most of the reported issues has been fixed, some constributed code has some details that are kept.

## Responsively App
The desktop app "responsively-app" is Open Source tool for check resposive web pages, which function better than AmIResponsive.

BrickYard webpage been validatate via that app.
<img width="579" alt="responsively" src="[a relative link](docs/images/responsivityapp.png)">

## Browser and platform testing

Validation of different operating systems and browsers to validate compability has been using devices like:
<img width="579" alt="rmacbook1_about" src="[a relative link](docs/images/macbook1_about.png)">


- Macbook PRO 16" - Mac OS Sonoma
    - Safari Version 17.0 (19616.1.14.11.11)
    - Firefox Version 114.0.1
    - Chrome Version 114.0.5735.106 (Officiell version) (arm64)
- iPhone Pro Max 14 - iOS 17 beta
    - Safari
    - Chrome

Screenshot from iPhone Pro Max 14:
<img width="579" alt="ios_safari" src="[a relative link](docs/images/ios_safari.png)">

Screenshot from Macbook Chrome:
<img width="579" alt="chrome_screenshot" src="[a relative link](docs/images/chrome_screenshot.png)">


## Google Chrome Lighthouse 

Google Chrome Lighthouse verification been done using Chrome and inspector view with lighthouse.

<img width="579" alt="lighthouse" src="[a relative link](docs/images/lighthouse.png)">






## Manual test case

*** More to be documented ***

- Registering new user
- Add products to basket and conclude purchase
- Add, edit and delete products

Testing with Stripe test according:
Testing interactively
When testing interactively, use a card number, such as 4242 4242 4242 4242. Enter the card number in the Dashboard or in any payment form.
Use a valid future date, such as 12/34.
Use any three-digit CVC (four digits for American Express cards).
Use any value you like for other form fields.

Objective: <what's the purpose of the test>

**Environment**

* <codebase and database>

**Pre-conditions**

# <environment setup>
# <any tests that need to be run first>

**Direct URL(s)**

# <URLs that will be used in the test steps>

**Input data**

# <some sort of title>
#* <data>

**Prerequisites**

# <instructions for setting up test>

**Instructions**

| Step No. | Step description |  Expected result |
| ------------- |:-------------:| -----:|
| 1. | <what a tester should do> | <what a tester should see when they do that> |

**Notes**

* <any notes>

## Automatic testing
Automatic testing has been built in to Brickyard codebase using Django-pytest framework.

To execute the testing according to:
```
python manage.py test product
python manage.py test wishlist
```

The main component for testings for the following modules and tests:
| Module | Description |  Expected result | Result |
| ------------- |:-------------:| -----:|
| Product | TBD| TDB | |
| Wishlist | TBD | TDB | |




# Bugs
The development was done iterative and testing and finding bugs occure during the coding process.

## Remaining bugs
- Image resizing via Cloudinary is required for the shop.


## Deployment
Deploying via Heroku and setting up ElefantSQL.
- Create a new App in Heroku
- Link to Brickyard repository in Github
- Add plugin Mailgun for mail service
- Add Buildpackage: heroku/python

Setup up propery parameters for the services:
```
SECRET_KEY=""
STRIPE_PUBLIC_KEY=""
STRIPE_SECRET_KEY=""
STRIPE_WH_SECRET=""
MAILCHIMP_API_KEY = ""
MAILCHIMP_REGION = ""
MAILCHIMP_MARKETING_AUDIENCE_ID = ""
CLOUD_NAME=""
API_KEY=""
API_SECRET=""
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
SENDER_EMAIL=""
MAILGUN_DOMAIN=""
MAILGUN_API_URL=""

```

# Credits
- Special thanks to Patrik Lindergren and Quagga Technologies AB for sponsering with Heroku and Figma account.


