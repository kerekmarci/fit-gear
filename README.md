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

![Click Here for Database Diagram](https://github.com/kerekmarci/fit-gear/blob/main/static/readme_files/db_schema_1.png)

### Skeleton

The skeleton of the website is designed with the wireframes below.

<br>
**Desktop wireframe:**

<details>
<summary>Index page</summary>
<br>
![Click Here for Database Diagram](https://github.com/kerekmarci/fit-gear/blob/main/static/readme_files/db_schema_1.png)
</details>

<details>
<summary>Store page</summary>
<br>
</details>

<details>
<summary>Individual Product page</summary>
<br>
</details>

<details>
<summary>Success Stories page</summary>
<br>
</details>

<details>
<summary>Contact page</summary>
<br>
</details>

<br>

**Mobile wireframe:**

<details>
<summary>Index page</summary>
<br>
![Click Here for Database Diagram](https://github.com/kerekmarci/fit-gear/blob/main/static/readme_files/db_schema_1.png)
</details>

<details>
<summary>Store page</summary>
<br>
</details>

<details>
<summary>Individual Product page</summary>
<br>
</details>

<details>
<summary>Success Stories page</summary>
<br>
</details>

<details>
<summary>Contact page</summary>
<br>
</details>

<br>

### Surface 

#### Colours

A light theme is more common and suitable for websites with large content, such as e-commerce stores. For this website, White and light grey are the dominant colours, the text is (almost black) to add good contrast for readibility. A green is a good match with both colours and can add a nice stylish interest to the site.

The colour palette is shown here with the colours used:

![Click Here for Colour Palette](https://github.com/kerekmarci/fit-gear/blob/main/static/readme_files/color_palette.JPG)

#### Typography

For the text content of the website, traditional-looking fonts were selected that are easy to read. The main font is called *Roboto.* This is a suitable font for both the content and a headlines, with various font-weights to add some interest to the titles.

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

Once the user clicks on the product card on the *Product page,* they are directed to the pgae of the individual product. 

### User Registration and Login

### Registration Confirmation

### Forgot Password / Password Reset

### Product Search

### Shopping Basket / Bag

### Dashboard

### Checkout

### Order Confirmation

### Product Review

### Success Stories Blog

### Comment Section

### Contact Page

---

## Deployment

---

## Credit

