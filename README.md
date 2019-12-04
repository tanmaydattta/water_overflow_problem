# water_overflow_problem
Water overflow problem coding challenge for another firm in Melbourne. 
The final result was "no answer" the firm was kind enough to not bother to even give an answer after wasting my 1 day. 

Feel free to copy, use, abuse this code. Any suggestion how to over engineer this code is welcome :).. 

In my personal opinion I would not hire anyone who would write such solution for such a simple question,
But the requirements says that manager wanted to see TDD and want to see "approach" and all corporate bullshit. 


# Travis build and test runs status 
[![Build Status](https://travis-ci.org/tanmaydattta/water_overflow_problem.svg?branch=master)](https://travis-ci.org/tanmaydattta/water_overflow_problem)



Author:Tanmay

Arch linux 5.0.8

Python:3.7.3

# To run
 `python run.py <jth glass> <ith row> <K liter of water poured>`

 run python run.py -h for more details on options
 
 # Help
 `python run.py -h`
 
 # Assumptions:
  If water is not present in some level, then run do not throw excpetion but the stack does. Run just returns 0

# To debug
- Set logging level to Debug
- Run Tests

# To test
    `make test_all`
