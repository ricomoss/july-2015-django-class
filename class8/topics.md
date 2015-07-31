Class 8 Topics
==============

The topics we'll be covering for class 6 involve a few use cases for decorators.

Motivation
----------

When developing systems it is common to need several custom clients for a specific need.  There are several programming paradigms that can be used to solve this problem.  One of which is module-level inheritence paradigms.

Goals
-----

 - Create a module for interfacing with "vendors".  Each vendor will have a unique handler for the API.
 - Create a view, form and template for selecting a vendor and an action.

Tasks
-----

 - Create a module in food called "vendors".
 - Create files in the new vendors module for each vendor and a base - "base.py", "flavor_of_the_month.py", "tasty_food_yum_yum.py", "we_got_yo_food.py".
 - In the "base.py" file create a BaseVendor to define a basic interface with the "handler()" method doing the actual "work".
 - In each of the vendor files create a vendor class that inherits from BaseVendor and implements all the interface methods but does not override the handler().
 - Create an "options" constant in the vendors "__init__.py" file for the form to use.
 - Create a view in the food app to handle a GET and POST request.
 - Create a form in the food app to handle validation for the POST request in the new view.
 - In the view accept the form action and use introspection to instantiate the correct vendor handler.
