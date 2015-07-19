Class 5 Topics
==============

The topics we'll be covering for class 5 revolve around how to setup and use cache in your Django project.

Motivation
----------

It is often the case that you will need to information that is expensive to extract or create.  If the information has some level of persistence caching is often a good solution to provide a more pleasant user experience.  

Goals
-----

 - Setup a caching backend for production and development.

Tasks
-----

 - Setup the production caching backend to use Memcached.
 - Setup the development caching backend to use the database table "review_cache"
 - Create the cache table using "./manage.py createcachetable"
 - Implement the use of caching when calculating the review average
