# The Tech Spot

The Tech Spot was created as my fourth milestone project, built using a Django framework alongside sqlite.

![The Tech Spot. Screenshot of website]()

[View The Tech Spot on Heroku]()

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/rdhadda/the-tech-spot)
![GitHub language count](https://img.shields.io/github/languages/count/rdhadda/the-tech-spot)
![GitHub top language](https://img.shields.io/github/languages/top/rdhadda/the-tech-spot?color=red)

## CONTENTS

- [User Experience (UX)](#User-Experience-UX)

  - [User Stories](#User-Stories)

- [Design](#Design)

  - [Colour Scheme](#Colour-Scheme)
  - [Typography](#Typography)
  - [Imagery](#Imagery)
  - [Wireframes](#Wireframes)
  - [Database Design](#database-design)
  
- [Features](#Features)
    - [Web Pages](#web-pages)
    - [Accessibility](#Accessibility)

- [Technologies Used](#Technologies-Used)
  - [Languages Used](#Languages-Used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

- [Deployment and Local Development](#deployment--local-development)  
    - [Local Development](#Local-Development)
    - [Remote Deployment](#remote-deployment-heroku)
   

- [Testing](#Testing)

  - [Solved Bugs](#Solved-Bugs)
  - [Known Bugs](#Known-Bugs)

- [Credits](#Credits)
  - [Code Used](#Code-Used)
  - [Media](#Media)
  - [Acknowledgments](#Acknowledgments)

---

## User Experience (UX)

### Purpose

The Tech Spot is designed to provide users with an online platform where they can browse, purchase, and learn about the latest tech products, such as TVs, laptops, game consoles, and mobile phones. It aims to offer a convenient shopping experience with detailed product information and secure payment options.

#### Why The Site is Needed

- Convenience: Allows customers to shop from the comfort of their homes, saving time compared to visiting physical stores.

- 24/7 Availability: The platform provides users access to shop anytime, increasing potential sales and customer satisfaction.

- Broader Reach: Expands the customer base beyond local boundaries, enabling users from different regions to access the products.

#### Security Features

- Secure Payment Gateway: Integrates with secure payment service Stripe to handle transactions safely, ensuring credit card information is encrypted.

- User Authentication: Account creation and login require strong passwords and email verification to secure user profiles.

#### Target Audience

- Tech Enthusiasts: People interested in the latest gadgets and technology products.

- General Consumers: Anyone seeking electronic products for everyday use.

- Students and Professionals: Users looking for devices like laptops or mobile phones for work or study.

### User Stories

There are three types of user for The Tech Spot. 

- Guest User - A user who doesn't have an account.
- User - A user who has an account.
- Admins - A user(s) who has superuser status, giving them the ability to perform additional tasks such a manage orders, add/delete products.

| **ID** | **As A/AN** | **I Want To Be Able To** | **So I Can** |
|:---:|:---:|:---:|:---:|
|**Viewing and Navigation**|
| **1** | Shopper | Easily navigate the website | To find products/information on products |
| **2** | Shopper | Quickly view a certain category of product  | Locate specific products |
| **3** | Shopper | View individual product details | Determine the price, the description and product rating |
| **4** | Shopper | View the running total of potential purchases  | Keep track of spending |
| **5** | Shopper | View product deals | See which products are on offer  |
|**Registration & User Accounts**|
| **6** | Shopper | Register for an account | Access my profile |
| **7** | Shopper | Login & Out | Access my profile |
| **8** | Shopper | Recover my account incase I forget my password | Re-gain access to my account |
| **9** | Shopper | Receive a verification email after sign up | Verify the account was set up successfully |
| **10** | Shopper | Have a personalized profile page | Update my personal information |
|**Searching & Sorting**|
| **11** | Shopper | Sort products  | Easily sort the best rated, best priced and categorically sort products|
| **12** | Shopper | Sort a specific category of products | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name|
| **13** | Shopper | Sort multiple categories of products simultaneously |  Find the best-priced or best-rated products across all categories |
| **14** | Shopper | Search for products by name, description or keyword  | Easily locate a specific product|
| **15** | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available|
|**Purchasing & Checkout**|
| **16** | Shopper | Select the quantity of a product | Guarantee I select the correct quantity  |
| **17** | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive  |
| **18** | Shopper | Adjust the quantity of individual items in my bag  | Easily make changes to my purchase before checkout |
| **19** | Shopper | Easily enter my payment information | Check out quickly and with no hassle |
| **20** | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase |
| **21** | Shopper | View an order confirmation after checkout | Check that no mistakes have been made |
| **22** | Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records and have confidence that the shop has received my order |
|**Admin & Store Management**|
| **22** | Admin | Add a product | Add new items to my store |
| **22** | Admin | Edit/update a product | Change product prices, descriptions, images and other product criteria |
| **22** | Admin | Delete a product | Remove items that are no longer for sale |


## Design

### Colour Scheme

![The-Tech-Spot](documentation\images\the-tech-spot-colour-scheme.png)

The chosen colour scheme is designed to convey a sense of trust and modernity to The Tech Stop store. 

I believe, together, these colors create a balanced and visually appealing design that reinforces the site’s credibility and modernity, while ensuring a positive user experience.

### Typography

Google Fonts was used for the following fonts:

- Fira Sans Extra Condensed - All text across the site

![Typography](documentation\images\the-tech-spot-fire-sans-condensed.png)

- Bowlby One - The Tech Spot logo

![Typography](documentation\images\the-tech-spot-bowlby-one.png)

### Imagery

All images on the webpage were taken from Currys.co.uk. I have credited these in the [credits](#credits) section.

### Wireframes

Wireframes were created for mobile, tablet and desktop using Balsamiq.

### Database Design

The Tech Spot is based on a relational database. The database is made up of 7 tables:

1. Category
2. Product
3. Order
4. OrderLineItem
5. Contact
6. UserProfile
7. User (Django Default Table)

The relationship between the tables are as follows:

1. Category to Product - One-to-Many - One category can have many products

2. Product to OrderLineItem - Many-to-One - One product can be associated with multiple instances of OrderLineItem

3. Order to OrderLineItem - One-to-Many - A single order can have multiple OrderLineItem entries

4. Contact - This is a standalone table which doesn't have a relationship to any other table.

5. UserProfile to User - One-to-One - Only one user can have one user profile.

6. UserProfile to Order - One-to-Many - One user can have many orders.

![Database Schema](documentation/images/the-tech-spot-database-schema.png)

### Features

All pages of the website have the following elements in common:

- Navbar - The navbar consists of:

    - The Tech Spot logo which acts as a link back to the homepage.
    - A search bar to allow a user to easily search products. 
    - An account icon which allows a user to login/sign up.
    - A basket link which takes the user through to the bag page
    - Navigation links to different product categories

![Navbar](documentation/images/the-tech-spot-navbar.png)

- Footer - This consists of a link to the contact form, which allows a shopper to contact the store. Social links and reference to stripe payments

![Footer](documentation/images/the-tech-spot-footer.png)

#### Defensive Programming

Defensive programming has been used throughout the site where necessary to prevent unauthorized access to certain URLs. This has been achieved by using the @loginrequired decorator for certain functions. As a secondary defense the views also check whether the user is a superuser if not a toast is displayed informing the user they do not have access to the URL.

#### Home Page

The home page consist of a welcome message, a shop now button which takes the shopper through to all the products available and a grid of images related to the store.

![Homepage](documentation/images/the-tech-spot-homepage.png)

#### Products Page

The products page displays all of the products available within the store. The products are displayed utilizing a bootstrap grid and card class. Each product shows the name, image, price, category and rating. If the user is a superuser each product shows a update/delete link allowing the superuser to maintain the store.

The page also shows the number of products being displayed on the page on the top left of the page. Additionally if a certain category if being used then a link back to all products is shown and if a search term is used, this term will also be displayed.

To the right of the screen is a sort box allowing the shopper to sort products by price, category and rating.

![Products Page](documentation/images/the-tech-spot-products-page.png)

#### Product Detail Page

Once a user has clicked on a product from the products page they will be taken through to the product detail page. This page shows an image of the product, title, price rating, category and description. If the user is a super user the update/delete links are also displayed here allowing for easy store maintenance 

There is also a quantity input with plus and minus buttons allowing shoppers to select their desired quantity of a product. A shopper is unable to select less than one product. 

Shoppers then have the option to add the quantity to their basket. Once added to the basket a toast is displayed showing the shopper what has been added to the basket and a link to go to secure checkout from the toast.

There is also a keep shopping button which takes the shopper back to the previous page.

![Product Detail Page](documentation/images/the-tech-spot-product-detail-page.png)

#### Bag Page

The bag page displays all of the products which the shopper added to their bag. An image, description, product price, quantity and subtotal is shown for each product. 

The quantity field allows the shopper to update the quantity of the product directly from their shopping bag. The delete link allows the shopper to delete the entire product from their shopping bag.

The subtotal field calculates the quantity multiplied by the product price to give the shopper a subtotal for that product.

The page also displays a bag total, delivery total and grand total.

The keep shopping button takes the shopper back to the products page and the secure checkout button navigates the shopper through to the checkout process.

![Bag Page](documentation/images/the-tech-spot-bag-page.png)

#### Checkout Page

The checkout page requires the shopper to fill out a form based upon the UserProfile model. If a user is logged in the name and e-mail field are pre-populated. If a user has filled out their profile with their delivery information, the form will be pre-populated with this information. If the user has not pre-populated their delivery information they have the option to save the delivery information to their profile via a checkout box to allow for faster checkout for their next purchase. 

If a shopper does not have a user account/profile then the information will need to be manually entered. There will also be a link displayed underneath the country field to prompt the user to login or to create an account. 

Underneath the details and delivery section is a payment input which is processed by stripe. If a user enters incorrect information a warning message will be displayed underneath the payment input.

The adjust bag button will take the user back to the bag page. The complete order button will complete the purchase and take the user through to the checkout success page. Underneath the complete order button is a warning to the shopper, highlighting to them how much their card will be charged for the purchase.

On the right hand side of the checkout page, shows an order summary to the shopper.

![Checkout Page](documentation/images/the-tech-spot-checkout-page.png)

#### Checkout Overlay

Once a shopper has clicked on the complete order button a spinning overlay will be displaying, indicating to the shopper that their payment is being processed. If the payment is unsuccessful the shopper will be re-directed to the checkout page.

#### Checkout Success Page

Once the payment has been processed, the shopper will be presented with the checkout success page. This shows a summary of what has been purchased and informs the shopper that a confirmation email will be sent out to them.

A success toast is also displayed indicating that the purchase was successful.

At the bottom of the summary is a button which will take the shopper through to the stores latest deals.

![Checkout Success](documentation/images/the-tech-spot-checkout-success.png)

#### Profile Page

The profile page shows the users default delivery information. Users can update this information at anytime by entering their information and clicking on the update information button. If successful the user will be presented with a success toast. 

On the right hand side of the page displays the users past shopping history. The order number is a link to the order confirmation. 

![Profile Page](documentation/images/the-tech-spot-profile-page.png)

#### Contact Page

The contact page allows a shopper to easily contact the store. All fields are required fields. If a user is logged in their name and e-mail are pre-populated. Once a user has clicked on the send enquiry button they will be re-directed to the home page and a success toast will be displayed informing them a response can be expected in 1 day.

The cancel button re-directs the user through to the products page. 

![Contact Page](documentation/images/the-tech-spot-contact-page.png)

#### Add Product (Super Users Only)

Superusers have the ability to add products to the store directly from the website rather than through Django admin. The superuser is presented with a form which is based on the product model. This can be accessed via Account > Product Management link in the navbar. Required fields are marked with an star (*). 

The cancel button takes the user back through to the products page.

The add product button adds the product to the database and directs the user to the product detail page of the newly created product.

![Add Product](documentation/images/the-tech-spot-add-product-page.png)

#### Edit Product Page (Super Users Only)

Similar to the add product page, super users are able to edit products directly from the website. The edit product page is accessed from the update links next to the products on the product page and product detail page. The form will be pre-populated with the product details and a toast displayed showing the user which product they're updating. From here the superuser can make any necessary amendments.

The cancel button wil take the user back to the products page.

The update product will update the product details and directs the user to the product detail page of the updated product.

![Edit Product](documentation/images/the-tech-spot-edit-product-page.png)

#### Delete Product

When a superuser clicks on a delete link for a product they are presented with a modal confirming whether they would like to delete the product. 

![Delete Modal](documentation/images/the-tech-spot-delete-modal.png)

#### 400, 403, 404 & 500 Page

I've implemented my own custom error pages. These pages all follow the same design with a message indicated to the user that an error has occurred.


### Future Implementations

- Implement stock levels for each product.
- Add user reviews for each product.
- Implement social login.

## Accessbility

- Using semantic HTML.
- Creating sufficient colour contrast throughout the website.
- Using descriptive alt attributes for images throughout the site.

## Technologies Used

### Languages Used

- HTML, CSS, Javascript and Python

### Frameworks, Libraries and Programs Used

### Database Used

- sqlite3

### Frameworks Used

[Django](https://www.djangoproject.com/) - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

[Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - A framework for building responsive, mobile-first sites.

### Libraries and Packages Used

[Pip](https://pypi.org/project/pip/) - Tool for installing Python packages.

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine.

[Balsamiq](https://balsamiq.com/) - Used to create wireframes.

[Git](https://git-scm.com/) - For version control.

[Github](https://github.com/) - To save and store the files for the website.

[Gitpod](https://gitpod.com/) - IDE to create the project.

[Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

Google Dev Tools - To troubleshoot and test features, and solve issues with responsiveness and styling.

[Am I Responsive](https://ui.dev/amiresponsive) To show the website across a range of devices.

[Fontawsome](https://fontawesome.com/start) For the cross and tick.

[Shields](https://shields.io/) Add badges to README.

[Lucid Chart](https://lucid.app) To create the database schema.

[jQuery](https://jquery.com/) - A JavaScript Framework

[Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Used for authentication, registration & account management.

[django-countries](https://pypi.org/project/django-countries/7.2.1/) 

[django_crispy_forms](https://pypi.org/project/django-crispy-forms/) - 

[gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server

[pillow](https://pypi.org/project/Pillow/) - Python imaging library

[dj_databsae_url](https://pypi.org/project/dj-database-url/) - allows us to utilise the DATABASE_URL variable

[psycopg2](https://pypi.org/project/psycopg2/) - a postgres database adapter which allow us to connect with a postgres database

[django-storages](https://pypi.org/project/django-storages/) - a storage backend library

[boto3](https://pypi.org/project/boto3/) - Allows connection to AWS S3 bucket

[coverage](documentation/testing/coverage/checkout-forms.png) - Used to create test reports

### Stripe

[Stripe](https://stripe.com/gb) has been used in the project to implement the payment system.

The following card numbers can be used to test different payment scenarios.

| Type | Card No | Expiry | CVC | ZIP |
| :--- | :--- |:--- | :--- | :--- |
| Success| Visa | 4242 4242 4242 4242 | A date in the future | Any 3 digits | Any 5 digits |
| Require authorisation | 4000 0027 6000 3184 | A date in the future | Any 3 digits | Any 5 digits |
| Declined | 4000 0000 0000 0002 | A date in the future | Any 3 digits | Any 5 digits |


## Deployment & Local Development

### Local Development

#### Setup

### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.

2. Go to the repository for this project, [The Tech Spot](https://github.com/rdhadda/the-tech-spot).

3. Click the Fork button in the top right corner.

### Remote Deployment Heroku

## Testing

Please see [TESTING.md](TESTING.md) file for both automated and manual testing of The Tech Spot.

## Credits

### Code Used

### Media

### Acknowledgments