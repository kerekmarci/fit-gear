# TESTING of Fit Gear E-Commerce Store - Milestone Project 4

In this Readme, the testing of this E-Commerce Store can ben seen for my 4th Milestone Project at The Code Institute

## Validation

In the below section, the various automated testings are shown for each languages used.

### HTML - W3C Markup Validation Service

W3C Validation has been run on all HTML files via W3C Markup Validation Service at https://validator.w3.org/.
There were several warnings and errors regarding Jinja2 language which I will ignore as Jinja2 was used correctly.

There were other errors indicated that I have left in the project due to the explanations below:

*Non-space characters found without seeing a doctype first.*
Doctype was added in the base template, W3C did not recognise `{% extends "base.html" %}` correctly.
<br>

*Consider adding a lang attribute to the html start tag to declare the language of this document.*
Lang attribute was added in the base template, W3C did not recognise `{% extends "base.html" %}` correctly.
<br>

*Illegal character in path segment: { is not allowed.*
This is related to *Jinaja2* which was used correctly on these occasions.
<br>

*Element hr not allowed as child of element ul in this context.*
It did not impact functionality.
<br>

*Iframe: Bad value 100% for attribute width on element iframe: Expected a digit but saw % instead.*
This code inserted came from Google directly.
<br>

*Element div not allowed as child of element ul in this context.*
*Div* was essential on that occasion and did not impact functionality.

### CSS Validation

CSS Validation has been run on the CSS files at https://jigsaw.w3.org/css-validator/.

*No errors found* in any of the `.css` files.

### JavaScript Validation

JavaScript validation has been run on the JS files at https://jshint.com/.

*No errors found* in any of the `.js` files.

### Python Validation

Python validation has been run on all `.py` files at http://pep8online.com/.\
The site meets the PEP8 standards.

## Testing cross-browser compatibility

Other then testing with desktops, laptops and mobile phones available at myself and friends, a Cross Browser Testing Cloud called Lambdatest was used to simulate real-time testing. The website is available at https://www.lambdatest.com/ This website is able to simulate various types of browsers (Google Chrome, Firefox, Opera, etc.) in various versions and screen resolution real-time, so that I was able to ensure that all functionalities work in different environments. The website was showing the same result in simulation of Google Chrome, Firefox, Opera, Safari and Edge.

## Testing mobile-friendliness

For this test, Google's mobile friendly test was used: https://search.google.com/test/mobile-friendly

The result shown was: *Page is mobile friendly This page is easy to use on a mobile device*

## Testing responsiveness

A website called https://www.browserstack.com/responsive provides a quick and easy way to display a website in mobile, desktop and tablet views in the most common resolutions, including landscape and portrait views. Due to the media queries added and the Boostrap grid system used, the website was able to successfully resize to various screen sizes.

## Testing User Stories
<br>

|  | SITE USER STORIES | |
| :---: | ----------- | ----------- |
| USER STORY NO. | DESIRED FEATURE | RESULT |
| 1 | A friendly layout that allows me to navigate the site with ease. | The Navigation Bar is immediately visible on the top and the main pages can be reached within one click. |
| 2 | To be able to register to the site to access extra features. | The *Registration* feature is available on the top, and allows users to make purchases, review products, post and comment Success Stories blog posts. |
| 3 | An easy log in and log out | Both features are always available on the top right corner. |
| 4 | To receive an email confirmation after registering. | Automated email is sent out to reconfirm registration. |
| 5 | To reset my password in case I forget it. | Feature available on the login page. |
| 6 | To be able to purchase products easily and make secure payments. | Product page can be reached in one click, then a second click lands on the product where *Add to Bag* button is available. Stripe payment is integrated for secure payments. |
| 6 | To have a dashboard where I can see my order history. | Icon is always available on the Navbar. |

<br>

|  | SHOPPER USER STORIES | |
| :---: | ----------- | ----------- |
| USER STORY NO. | DESIRED FEATURE | RESULT |
| 7 | To view a selection of products in a clear layout. | Products are shown in card format on the *Store* page which is responsive to all screen sizes. |
| 8 | To filter products easily by category. | On the navigation bar, category selector drops down when hovering over the mouse. Once category has been selected and products are listed, the category titles are showing on the left. |
| 9 | To search for product name and description by entering a keyword. | Keyword search is available by clickin on the magnifier icon on the navigation bar. |
| 10 | To see how many results my search found. | Number of results are shown on the top of the results page. 
| 11 | To easily access the product details page to have additional details. | This is available by clickin on the product card. |
| 12 | To see product rating. | Product rating is available on the *product cards* so that users can see the star ratings before opening the *product details* page, as well as how many reviews had been given. Stars and exact average can be seen under the product title on the *Product Details* page. |
| 13 | To read product reviews. | Reviews are available on the *Product Details* page. |
| 14 | To be able to rate and write a review on a product. | This feature is available on the *Product Details* page for registered users. |
| 15 | To be able to add and remove products in a basket. | This can be done by pressing the + or - button on the *Shopping Bag* page next to the amount. There is an additional *Remove* button available with a confirmation modal. |
| 16 | To be able to choose from variations of a product, such as different size or colour. | This has been implemented in the form of drop-down menus on the *Product Details* page. |
| 17 | To be able to modify the contents of the basket easily. | New items can be easily added to the bag by simply clicking on the *Add to Bag* button on the *Product Details* page. Amounts can be changed by clicking on the + or - button on the *Shopping Bag* page. |
| 18 | To see how many items I have in the basket with the total price and breakdown | Current number of items can always be seen on the navibation bar by the shopping cart icon. By clickin on the shopping cart, itemised details are shown. |
| 19 | To be able to purchase the products and complete a secure payment. | User is navigated to the *Payment page* by clicking on the *Checkout* button on the *Shopping Bag* page. |
| 20 | To be redirected to a confirmation page once the payment has completed. | Orders are given a unique order number and redirected to a *Checkout Success* page. |