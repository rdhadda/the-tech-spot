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



### Future Implementations

## Accessbility

## Technologies Used

### Languages Used

- HTML, CSS, Javascript and Python

### Frameworks, Libraries and Programs Used

### Database Used

### Frameworks Used

### Libraries and Packages Used

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