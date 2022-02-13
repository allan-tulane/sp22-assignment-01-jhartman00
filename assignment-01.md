

# CMPS 2200 Assignment 1

**Name:** Jamie Hartman  
**Name:** Charles Tyndal


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 

    - This is true becuase, by definition of Big O f(n) is  O(g(n)) if eventually a constant multiple of g is bigger than or equal to f.
    - In this example if c = 3 and k = 1 we have 3*2^n >= 2^n+1 for all of n >= 1.
    - Therefore, 2^n+1 is O(2^n)
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
  
    - In this example if c = 2 and k = 1 we have 2*2^2^n >= 2^n for all of n >= 1.
    - Therefore, 2^n+1 is O(2^n)
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    

    - In this example if c = 2 and k = 1 we have 2*n^1.01 >= log^2*n for all of n >= 1.
    - Therefore n^1.01 is O(log^2 n)
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  

    - In this example if c = 2 and k = 1 we have 2*n^1.01 >= log^2*n for all of n >= 1.
    - Therefore n^1.01 is O(log^2 n) and not Omega(log^2 n)
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?

    - In this example if c = 2 and k = 1 we have 2*sqrt(n) >= (log n)^3 for all of n>=1
    - Therefore sqrt(n) is O((log x)^3)
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  

    - In this example if c = 2 and k = 1 we have 2*sqrt(n) >= (log n)^3 for all of n >= 1
    - therefor sqrt(n) is O((log x)^3) and not Omega((log x)^3)
.  
.  


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  
    - This function takes in a number (x)
    - if x is less than or equal to 1 it returns it.
    - if x is greater than 1 it returns x*foo(x-1).
    - This calls foo on x-1 until x = 1 or 0 (it shouldnt ever get to 0)
    - Once it gets to 1 it returns 1 and multiplies it by the x that origionally called that layer (i.e. x from one depth higher)
    - When it gets to the origional layer (depth = 0) it returns the final number
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  
.  
.  
.  
.  
.  
.  

