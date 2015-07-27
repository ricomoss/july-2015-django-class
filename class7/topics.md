Class 7 Topics
==============

The topics we'll be covering for class 6 involve a few use cases for decorators.

Motivation
----------

Several advanced techniques will take advantage of design patterns using decorators.  Decorators can modify functionality of a method.  If your design paradigm involves repetitive techniques you may find decorators useful.

Goals
-----

 - Create a decorator to take advantage of cache.
 - Create a decorator to allow multiple attempts before failure.

Tasks
-----

 - Create a file in common called "wrappers.py".
 - Create a decorator called "using_cache" in "wrappers.py" that will attempt to get values from cache before calling the function.
 - Create a decorator called "retry" in "wrappers.py" that will attempt to retry with gradually increasing wait time between attempts before ultimately failing.
