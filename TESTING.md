# TESTING of Fit Gear E-Commerce Store - Milestone Project 4

In this Readme, the testing of this E-Commerce Store can ben seen for my 4th Milestone Project at The Code Institute

## Automated testing

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