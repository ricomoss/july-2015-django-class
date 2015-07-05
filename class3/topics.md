Class 3 Topics
==============

The topics we'll be covering for class 3 revolve around Django's form validation.  We'll also go into more depth with customizing the ListView and DetailView created in class 2.

Motivation
----------

Using Django forms and CBVs provide functionality for validation and error handling.  There are natural methods to expand the validation functionality.

Goals
-----

 - Update the registration and login path to include Django's built-in form validation.

Tasks
-----

 - Update the registration RegisterForm to accept a confirmation password and validate against it.  Also ensure the username is unique.
 - Update the registration POST to use the form and return errors when applicable.
 - Update your field.html template to handle form errors.
 - Add a model in common called Review that will allow users to rate meals.
 - Modify the MealListView to include the average review rating.
 - Modify the MealDetailView to include a link to the ReviewListView, which links to the ReviewDetailView.  Create templates and routes for each.  (Use the generate_reviews management script to create some review data for testing.)
 