Class 6 Topics
==============

The topics we'll be covering for class 6 revolve around how to create and run unit tests.

Motivation
----------

Unit tests are a subject under constant debate.  It is generally accepted that test coverage in a project is advantageous.  Some argue you should strive for 100% test coverage (testing every line of code).  Others argue the 80/20 rule (test the 20% of the code that does 80% of the work).  If you find yourself developing in a code base with no tests you should consider bringing this to the attention of your team and managers as a possible source of considerable technical debt.      

Goals
-----

 - Create sample test cases for use with the Django test suite.

Tasks
-----

 - Create a test module in the common app with a "test_models.py" file.
 - Create a test for the custom model method "average_rating" in the Review model.
 - Create a test module in the food app with a "test_views.py" file.
 - Create a test for the MealListView using Django's test client to verify the view will return a 200 status.
