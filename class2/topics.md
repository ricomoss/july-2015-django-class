Class 2 Topics
==============

The topics we'll be covering for class 2 revolve around Django's Class-Based Views (CBVs).

Motivation
----------

Class-Based Views provide expanded functionality for HTTP request and response handling.  Perhaps even more importantly they provide a framework for creating an intuitive workflow.  The more intuitive and readable the code, the better the code.  "Readability counts."

Goals
-----

 - Implement View, ListView, TemplateView, DetailView

Tasks
-----

 - Create a base.html file in the templates folder with a head, header, nav and footer - keep it simple.
 - Create a favicon and use core Bootstrap in the base.html.
 - Create a simple index.html file and use a TemplateView in the website/urls.py file.
 - Using View create a RegisterView in the accounts/views.py file (handle both GET and POST w/ a RegisterForm and register.html).
 - Using View create LoginView and LogoutView to handle logging in and logging out respectively (you'll need a login.html and LoginForm).
 - Create another app called food.  Create a few models in this new app called Item and Meal where Meal has a many-to-many with Item.  (You'll need to migrate)
 - Using a ListView create a MealView in the food/views.py and a meal_list.html file.  Use an app-level urls.py file to route this view.  Display the meal and the item name for each item in the meal.  Create a link on each meal name to the detail view for each meal.  (Use the generate_meals management script to create some food items for testing.)
 - Using a DetailView create a MealDetailView in the food/views.py and a meal_details.html file.  Display the details of each item in the meal.
