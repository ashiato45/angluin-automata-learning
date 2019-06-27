# angluin-automata-learning

## What's this?
An implementation of Angluin's automata learning method based on the following paper:


>Dana Angluin,
>Learning regular sets from queries and counterexamples,
>Information and Computation,
>Volume 75, Issue 2,
>1987,
>Pages 87-106,
>ISSN 0890-5401,
>https://doi.org/10.1016/0890-5401(87)90052-6.
>(http://www.sciencedirect.com/science/article/pii/0890540187900526)

## Google Colab version is available!
Try it online: https://colab.research.google.com/drive/1zdFtXE1UpVJKmEFIWzaPh5ow8PS7Idf4#scrollTo=gt15JQ5gSd4m

## Usage
Please rewrite the bottom of angluin.py
1. Make a _teacher_ function that takes a string that consists of "a" and "b" and returns True or False like:
```
def teacher_even(s):
    return (s.count("a")%2 == 0 and s.count("b")%2 == 0)
```
2. (Optional) Make a list of strings that corresponds to the _counterexample_ like:
```
exs = ["ab","abab"]
```
These strings and their prefixes are added to the observation table when the table becomes consistent and closed.
3. Make a Learner by giving the _teacher_ function and run _learn_ like:
```
l = Learner(teacher_even)
l.learn(exs)    
```
_learn_ method takes the counterexample that you made in Step 2.  You can omit the list of counterexamples.
4. Run angluin.py:
```
python angluin.py > test.html
```
Then you get an HTML file that describes how the observation table (explained in the paper) grows.

