# Fit Gear E-Commerce Store - Milestone Project 4

This e-commerce website was created for my 4th Milestone Project at The Code Institute. The website will utilise the languages and tools I learned so far in Front-End and Back-End, namely HTML5, CSS3, JavaScript, Python and Django.

>>> Photo of the finished website

---

## Description

This E-Commerce store allows users to browse among products available in the store, register and purchase products using online payment (Stripe).
Registered users are able to access their *Dashboard* where they can review their order history. Registered users are also able to share their success stories with the community and reflect on each other's stories in form of comments.

---

## User Experience

The aim of this website is for the site owner to sell fitness products, and for users to be able to purchase them. The concept was to create a simple, straightforward and intuitive website that allows users to browse among products with ease and make secure purchases easily. To encourage return visits, a *Success Stories* section has been added where registered users can share their blogposts.

### Strategy

The main goal of this 4th Milestone project was to build a website that has both Front-End and Back-End elements and can process data with Postgres database. Within that, the aim was to create an application that allows users to register to the website, search for products and make purchases, as well as being able to browse within products while displaying results in a visually appealing way. Registered users will have a bonus feature of *Success Stories* section to share their posts with the community.

#### User Stories

|  | AS A SITE USER |
| :---: | ----------- |
| USER STORY NO. | I WOULD LIKE... |
| 1 | A friendly layout that allows me to navigate the site with ease |
| 2 | To be able to register to the site to access extra features |
| 3 | An easy log in and log out |
| 4 | To receive an email confirmation after registering |
| 5 | To reset my password in case I forget it |
| 6 | To be able to purchase products easily and make secure payments |
| 6 | To have a dashboard where I can see my order history |

|  | AS A SHOPPER |
| :---: | ----------- |
| USER STORY NO. | I WOULD LIKE... |
| 7 | To view a selection of products in a clear layout |
| 8 | To filter products easily by category |
| 9 | To search for product name and description by entering a keyword |
| 10 | To see how many results my search found |
| 11 | To easily access the product details page to have additional details |
| 12 | To see product rating |
| 13 | To read product reviews |
| 14 | To be able to rate and write a review on a product |
| 15 | To be able to add and remove products in a basket |
| 16 | To be able to choose from variations of a product, such as different size or colour |
| 17 | To be able to modify the contents of the basket easily |
| 18 | To see how many items I have in the basket with the total price and breakdown |
| 19 | To be able to purchase the products and complete a secure payment |
| 20 | To be redirected to a confirmation page once the payment has completed |

|  | AS A SITE OWNER |
| :---: | ----------- |
| USER STORY NO. | I WOULD LIKE... |
| 21 | To add and remove products from the site |
| 22 | To edit product details and configure variants of the products |
| 23 | To update the quantity of the products that are available in the store |
| 24 | To be able to delete user reviews, in case inappropriate comments are added. |

### Scope

The scope of an E-Commerce store can be quite complex, however, to align with the course content at The Code Institue, the website will feature the basics of an E-Commerce website.
Users will be able to register to the website, browse among products, add to basket, able to modify the basket, then are able to check out and make secure payments.

### Structure

#### - Models and Apps

Below are listed all apps within this Django Project:

**FitGear**

This is the base app created with the projects.

**Accounts**

This contains 2 classes:
* Account: user information with personal details and system access (active or not, staff, admin or superadmin).
* MyAccountManager: to create users and superusers.

**Bag**

* Bag: the entire shopping bag, summary of the BagItems.
* BagItem: the individual items with the price, quantity and product variants.

**Blog**

* Post: Indivisual blog posts with *title, slug, author, content* and *created-on* date.
* Comment: comments for the individual blog posts.

**Category**

This containts the categories of the available products with a *category name, slug, description* and *category image.*

**Checkout**

This app containts 3 classes:
* Order: contains completed orders, identified by an order number. Includes billing address and total amount too.
* OrderProduct: the Line Items; a single product with their variations, belonging to an *Order.* One order can contain more line items / OrderProduct.
* Payment: this contains the paid amount for a completed order by the user.

**Store**

* Product: details of individual products, such as category they belong to, name, slug, description, image, stock, availibility, created date and modified date.
* Variation: contains variation category and variation value.
* VariationManager: variants of each product, such as different size or colour.
* Review: user review and ratings of a product.

#### - Database Schema

![Click Here for Database Diagram](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/db_schema_1.png)

### Skeleton

The skeleton of the website is designed with the wireframes below.
<br>

**Desktop wireframe:**

<details>
<summary>Index page</summary>
<br>

![Desktop Home Page](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/wireframes/01_home_desktop.png)
</details>

<details>
<summary>Store page</summary>
<br>

![Store Page](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/wireframes/02_store_desktop.png)
</details>

<details>
<summary>Product Detail Page</summary>
<br>

![Product Detail Page](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/wireframes/03_product_desktop.png)
</details>

<details>
<summary>Success Stories page</summary>
<br>

![Success Stories page](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/wireframes/04_success_stories_desktop.png)
</details>

<details>
<summary>Contact page</summary>
<br>

![Contact page](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/wireframes/05_contact_desktop.png)
</details>

<br>

**Mobile wireframe:**

<details>
<summary>Index page</summary>
<br>

![Desktop Home Page](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/wireframes/01_home_mobile.png)
</details>

<details>
<summary>Store page</summary>
<br>

![Store Page](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/wireframes/02_store_mobile.png)
</details>

<details>
<summary>Product Detail Page</summary>
<br>

![Product Detail Page](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/wireframes/03_product_mobile.png)
</details>

<details>
<summary>Success Stories page</summary>
<br>

![Success Stories page](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/wireframes/04_success_stories_mobile.png)
</details>

<details>
<summary>Contact page</summary>
<br>

![Contact page](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/wireframes/05_contact_mobile.png)
</details>

<br>

### Surface 

#### Colours

A light theme is more common and suitable for websites with large content, such as e-commerce stores. For this website, White and light grey are the dominant colours, the text is (almost black) to add good contrast for readibility. A green is a good match with both colours and can add a nice stylish interest to the site.

The colour palette is shown here with the colours used:

![Click Here for Colour Palette](https://github.com/kerekmarci/fit-gear/blob/main/media/readme_files/color_palette.JPG)

#### Typography

For the text content of the website, traditional-looking fonts were selected that are easy to read. The main font is called *Roboto.* This is a suitable font for both the content and a headlines, with various font-weights to add some interest to the titles.

---

## Technologies Used

### Languages

* HTML5
* CSS3
* JavaScript
* Python

### Libraries

* Bootstrap: HTML, CSS and JavaScript library to create modern websites and web apps
* Balsamiq: an industry standard low-fidelity wireframing tool
* Google Fonts: for providing stylish fonts across the website
* JQuery: a fast, small, and feature-rich JavaScript library that helps web developers to add extra functionalities to their websites

### Framework

* Django: a high-level free and open source Python web framework that encourages rapid development and clean, pragmatic design

### Database

* Postgres: a powerful, open source object-relational database system

### Version control

* GitHub: is used to store all codes
* Gitpod: is used as a IDE and to push code to GitHub

### Hosting

* Heroku: the web app is hosted on Heroku Cloud Application Platform

### Storage

* Amazon AWS S3 to store static files

### Payments

* Stripe: an APIs that web developers can use to integrate payment processing into their websites and mobile applications

---

## Features

Below are the existing features listed for the website.

### Base template

The base template contains the links to all external resources, such as Bootstrap, Jquery, Fontawesome, Custom Style Sheets and custom JavaScript. This also includes *Navbar* and *Footer* which is common across all site.

### Shop / Products page

The *Shop* link is available on the navigation bar - when hovering the mouse, the categories appear in a drop-down menu, and the bottom menu item is *All Products.* This will land on a page where products are listed in card view with an appealing picture, and by clicking on them, the user will land on the individual product page. The product list is paginated to avoid too many products on one page. \
Once the user is on the Products page, the category selector will become available on the left hand side as well to facilitate switching among categories.\
THe individual product cards show the basic features of the product: an image, a star-rating and a button to open the *Product Detail* page.

### Product Detail page

Once the user clicks on the product card on the *Product page,* they are directed to the page of the individual product.\
On this page, a large image of that product is shown, along with the start rating and the description, plus the option in a drop-down menu to select different variations, such as sizes and colours.\
Registered users are also able to rate the product by giving 1-5 starts along with their comment.

### User Registration and Login

Site owners would like to achieve more returning guests to the store, therefore the registration feature is essential. Also, there should be added value when user registers to unlock extra features of the website.\
The registration feature is available on the top right corner of the navigation bar, and is also essential to complete a purchase.\
Registered users are able to make purchases, review products, post and reflect on blogposts as well.

### Registration Confirmation

Once a user registers, they receive a confirmation email to activate their account. This is a security feature to ensure only users with their genuine email addresses register.

### Forgot Password / Password Reset

In case a registered user forgets their password, they have the option to reset their password on the login page. Users will receive an email with a link to reset their password. If the username does not exist, the system will not proceed.

### Product Search

Beyond the category search available on the *Shop* drop-down menu and *Products* page, there is a magnifier button on the navigation bar that allows users to search for products by keywords. Search will run search in the products name and description.

### Shopping Basket / Bag

From the *Product Detail* page, users can add items into their shoppig bag. The icon next to the bag will indicate the number of items currently in the bag.\
* Variations: users have the option to select variations for the given product, such as size and colour.
* Changing quantity: in the basket page, users can easily change the quantity of the given product with the plus and minus sign next to the quantity.
* Identifying same variations: if user already has a particular variation in the shopping bag, and adds the same product with the same variation again from the *Product Detail* page, the system will identify this and will increase the quantity instead of adding as a new product.
* Delete from Bag: There is a delete button available for each product to remove item from the shopping bag. When clicking on the button, a prompt will appear to reconfirm deletion. The product also gets deleted when user decreases the quantity by clicking on the minus sign and quantity reaches zero.
* Empty bag: if the user clicks on the bag icon but there are no products in the bag, a message is shown *Your Shopping Bag is Empty* and a button is encouraging the user to *Continue Shopping.*
* Product name: The product names act as a link, and by clicking on them, the user is directed to the individual *Product Detail* page.

### Checkout

Once user has added all required products in the bag, they can complete purchase by clicking on the *Checkout* button.\
This will land on an order summary page where user can review the items to be ordered, can enter shipping address and credit card details.

### Stripe Payments

Stripe is a reliable payment services provider that has been integrated into the store. Users can securely enter the card details and the payment will be processed via Stripe, then user will land on the *Order Confirmation* page.

### Order Confirmation

After a successful payment, user is directed to the *Order Confirmation* page where they can review the products ordered, the itemised and total amounts, as well as the shipping address.

### Dashboard

Registered users can access their *Dashboard* after their log in. This will contain a summary of their orders in a chart format, and by clicking on the order number, they can see the itemised order history.

### Product Review

Registered users are able to leave review on the products on the individual *Product Detail* page. Star rating is available from 1-5 as well as written commetns. The *Product Detail* page also shows a summary of the average ratings in a star format under the product name (for example for the average of 4.5, 4 stars are filled and one half star is shown).

### Success Stories Blog

As the goal of the site owner is to encourage return visitors, creating a community is a great way of achieving that. Registered users can share their *Success Stories* in the form of a blog and also comment on other users' posts.

### Comment Section

Registered users can reflect on the success stories blog post by leaving a short comment below. Comments are showing the username and the time how long ago the comment was posted.

### Contact Page

A simple, yet informative page shows the location of the store on google maps, plus contact details such as address, email address and phone number.

---

## Features to Implement

An E-Commerce website can boast endless functionalites; although the requirements for this Milestone Project are quite complex, there are still a variety of features that I am planning to implement as an extension of this website after its submission (on a separate branch or repository).

* Profile Page and Profile Picture: users can upload a profile picture for their account. This photo would appear in a small circle next to the blogpost title and their comment so give a more personalised content to the blogposts and comments.
* Change Password: although users can already request a reset for their password, a *Change Password* feature will allow users to replace their password on the user dashboard.
* Product gallery with multiple images: on the *Product Details* page, there will be a mini carusel under the product image so that users can see more photos of the same product.
* Stripe webhooks: to notify my application when an event happens in your account.
* Order confirmation email: user to receive a confirmation email of their successful order.
* User management: site owner can nominate staff members, admins and superadmins with various user rights (superusers have all there rights defined already).

---

### Testing

Testing of this E-Commerce Store can be found in a separate [Testing Documentation](https://github.com/kerekmarci/fit-gear/blob/main/TESTING.md).

---

## Deployment

The project has been developed on Gitpod and the code is pushed to GitHub in its repository. The ready website has been deployed to Heroku, and static files are stored on Amazon AWS in an Amazon Web Services S3 Bucket.

### Setting up GitHub

1. As a starting point, I used the base templated provided by The Code Institute: https://github.com/Code-Institute-Org/gitpod-full-template
2. I clicked on the button called *Use this template*
3. Entered a name for my new repository, then clicked on the *Create repository from this template* button. Now the development environment has been created.

### Setting up Environment Variables

Sensitive data needs to be hidden, therefore these variables are securely stored under the *Heroku Config Vars.* To be accessible on Gitpod, they are also set up in the *Variables* section under Gitpod settings, applied to this workspace.

The variables are as follows:

| VARIABLE | VALUE | FUNCTIONALITY |
| ----------- | ----------- | ----------- |
| SECRET_KEY | *Django secret key* | Requirement from Django to secure signed data |
| DATABASE_URL | *Link to Postgres database* | To store data in Postgres
| STRIPE_PUBLIC_KEY | *Stripe Public Key* | Generated on Stripe to to tokenize payment information |
| STRIPE_SECRET_KEY | *Stripe Secret Key* | Secure password to my payment accont |
| AWS_ACCESS_KEY_ID | *AWS Access Key ID* | Required to make programmatic calls to AWS |
| AWS_SECRET_ACCESS_KEY | *AWS Secret Access Key* | Unique password for AWS Access |
| EMAIL_HOST_USER | *My Email address* | Emails from this account will be sent to communiate with user, such as registration confirmation and password reset.
| EMAIL_HOST_PASS | *Email password for host user* | Password to authorise use of this email host |
| USE_AWS | *True* | True value to enable static data storage on AWS |
| DEVELOPMENT | True or False | Enable or Disable debug mode |

### Requirements for Heroku

Heroku needs the *Procfile* and the *Requirements* in order to run the app.
To create the file for the requirements, the following needs to be created: `pip3 freeze --local > requirements.txt`.
In the *Procfile*, the following line needs to be added so that Heroku will know which file to run: `web: python app.py`.

### Django configuration

**Allowed hosts**

This is a list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent HTTP Host header attacks.

As the site has been deployed to Heroku, on the main app > settings.py, the below had to be set up:\
`ALLOWED_HOSTS = ['fit-gear.herokuapp.com', 'localhost']`
<br>

**Database**

As Postgres is used to store database tables for the deployed site, it needs to be set up in the settings. The way it is set up in this project is to distinguish whether the app runs locally or on Heroku. If runs locally, the local *Sqlite* database is used, otherwise Postgres.\
In the Heroku *Config Variables*, a variable name *DATABASE URL* is set up with a link to Postgres database (see above). In the main app > settings.py, the below if-else statement has been added: (with indentation)\
`if 'DATABASE_URL' in os.environ:`\
    `DATABASES = {`\
        `'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))`\
    `}`\
`else:`\
    `DATABASES = {`\
        `'default': {`\
            `'ENGINE': 'django.db.backends.sqlite3',`\
            `'NAME': BASE_DIR / 'db.sqlite3',`\
        `}`\
    `}`

### Cloning

To clone the GitHub repository, follow these steps:\  

1. Go to my GitHub repository - https://github.com/kerekmarci/fit-gear
2. Click on the CODE button
3. Copy the link with the HTTPS option selected
4. Open your IDE
5. Type git clone in the terminal, followed by pasting the link. For example: *git clone https://github.com/kerekmarci/fit-gear.git*
6. Press Enter, and now a local clone has been created

---

## Credits

In this section, I would like to give credit to all tools, sources and support that inspired and helped me towards the success of my project:
* Code Institute project called *Boutique Ado * in the Full-Stack Frameworks with Django module that provided an excellent and complex example project to understand how to combine all these technologies together.
* An E-Commerce Store tutorial on Udemy that gave me inspiration on how to set up my models, views and logic to create a functional store - in particular the logic for the *Product Variation* section to set up different variations for the same product - https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/
* Base template: although I aimed to create a custom website, the main focus of this Project was to utilise Django and Back-End. To facilitate this, I used a template called *Zay Shop* as a staring point for my base template and tailored it to my needs.
* Product Variations: although mainly the above tutorial was used, this video was also an intersting learning - https://www.youtube.com/watch?v=cRbU7OH1RaQ
* Success Stories blog feature: inspiration from this video - https://djangocentral.com/building-a-blog-application-with-django/
* CSS star rating on the *Product Details* page: https://codepen.io/andreacrawford/pen/NvqJXW
* Product images and descriptions:
    * https://uk.gymshark.com/
    * https://www.pursuefitness.co.uk/
    * https://www.allbirds.co.uk/
    * https://www.polar.com/
* Sample Success Stories posts:
    * https://www.muscleandstrength.com/transformation/khang-nung
    * https://www.mentalfloss.com/article/545150/11-ways-motivate-yourself-go-gym
* Django email verification: https://www.youtube.com/watch?v=Rbkc-0rqSw8
* Code Institute Tutor support who assisted with moving on when I felt I was stuck.
* The below documentation to support the implementation of Pagination:
    * https://docs.djangoproject.com/en/3.2/topics/pagination/* 
* Images: the below websites were used to source the product images:
    * https://www.pursuefitness.co.uk/
    * https://uk.gymshark.com/
    * https://www.gymwear.co.uk/
* My mentor at Code Institute Nishant Kumar for his valuable advice throughout the consultations.
