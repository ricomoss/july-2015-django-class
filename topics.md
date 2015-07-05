July 2015 Django Class
======================

To provide a practical motivation for the Django project we'll be building a simple restaurant website.  Although the primary focus of the course will be examples of each topic listed below it'll be built in the context of our restaurant.  Throughout the course we'll be ensuring not only the understanding of these topics but also the importance of best practices.  All code must follow PEP8.  Period.  Secondly, we'll focus on how to create a clean and understandable code base.  All decisions for design will focus on readability, modularity and scalability.  Understanding not only why this is important, but also how to properly implement a project using these will provide you a foundation for being a productive member of a development team. 

Zen of Python, by Tim Peters
============================

Beautiful is better than ugly.<br>
Explicit is better than implicit.<br>
Simple is better than complex.<br>
Complex is better than complicated.<br>
Flat is better than nested.<br>
Sparse is better than dense.<br>
Readability counts.<br>
Special cases aren't special enough to break the rules.<br>
Although practicality beats purity.<br>
Errors should never pass silently.<br>
Unless explicitly silenced.<br>
In the face of ambiguity, refuse the temptation to guess.<br>
There should be one-- and preferably only one --obvious way to do it.<br>
Although that way may not be obvious at first unless you're Dutch.<br>
Now is better than never.<br>
Although never is often better than *right* now.<br>
If the implementation is hard to explain, it's a bad idea.<br>
If the implementation is easy to explain, it may be a good idea.<br>
Namespaces are one honking great idea -- let's do more of those!<br>

Topics
======

July 6th - Custom Environments (Django Setup)
---------------------------------------------

We'll spend time to get environments setup, discuss how the class will work and formulate an outline for the topics.

July 9th - Class-Based Views
----------------------------

It's time to dive into a massively overlooked topic.  Class-Based Views (CBVs) provide an incredible amount of flexibility and functionality.  We'll discuss a few examples of CBV types and when and how to use them.

July 13th - Form Validation
---------------------------

Together with CBVs the Django forms can do an amazing amount of work for you.  Why go through the trouble of validation checking when Django can do it for you?

July 16th - Formsets
--------------------

Django provides a method for POSTing a single HTML form and providing multiple Django forms to handle the validation and workload.  The learning curve might be steep, but the benefits are worth it!

July 20th - Caching
-------------------

Caching can be very helpful in providing a quick and light-weight solution to storage problems.  We'll discuss how to setup caching in Django and how to use caching properly.

July 23rd - Unit Testing
------------------------

Although testing your code can be a love-hate relationship it's always a best practice to do so.  We'll discuss testing techniques, examples and the philosophy around testing.

July 27th - Decorators
----------------------

Through decorators you are able to do some pretty remarkable things.  We'll discuss how they work, how to use them and provide some problems to solve using decorators.

July 30th - Module-Level Inheritance Paradigms
----------------------------------------------

It's very often the case that your technical need revolves around providing a service that has several, fundamentally different, design needs.  Consider a service that parses results from several different sources.  We'll discuss a design paradigm that let's you build, at the module level, a structure to allow easy expansion of such a service.
