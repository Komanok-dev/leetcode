# Leetcode problems
![Language](https://img.shields.io/badge/language-Python-green.svg)&nbsp;

* Here you can find my submitted solutions of Leetcode problems

## Reference

* Python
    * [Time Complexity](https://wiki.python.org/moin/TimeComplexity)
 * Handy Table
    * [Thinking Techniques](https://sites.google.com/site/mostafasibrahim/programming-competitions/thinking-techniques) as follows:

| n | Complexity | Possible Algorithms & Techniques |
| - | - | - |
| 10<sup>18</sup>+ | _O(1)_ | Math |
| 10<sup>18</sup> | _O(log<sub>n</sub>)_ | Binary & Ternary Search / Matrix Power / Cycle Tricks / Big Simulation Steps / Values Reranking / Math |
| 10<sup>16</sup> | _O(n<sup>1/2</sup>)_ | Math |
| 10<sup>8</sup> | _O(n)_ | Greedy / Ad-hoc / DP |
| 4×10<sup>7</sup> | _O(nlog<sub>n</sub>)_ | Linear # Calls to Binary & Ternary Search / Pre-processing & Querying / Divide and Conquer |
| 10<sup>4</sup> | _O(n<sup>2</sup>)_ | Ad-hoc / DP / Greedy / Divide and Conquer / Branch and Bound |
| 500 | _O(n<sup>3</sup>)_ | Ad-hoc / DP / Greedy / Divide and Conquer / Branch and Bound  |
| 90 | _O(n<sup>4</sup>)_ | Ad-hoc / DP / Greedy / Divide and Conquer / Branch and Bound |
| 50 | _O(n<sup>5</sup>)_ | Branch and Bound |
| 40 | _O(n×2<sup>n/2</sup>)_ | 	Meet in the Middle |
| 20 | _O(n×2<sup>n</sup>)_ | Backtracking / Generating 2<sup>n</sup> Subsets / Bitmask Technique |
| 11 | _O(n!)_ | Factorial / Permutation / Combination Algorithm |

## Solutions
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |-----|
1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](./two-sum.py) | _O(n)_ | _O(n)_ | Easy |Array, Hash Table|
2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [Python](./add-two-numbers.py) | _O(n)_ | _O(1)_ | Medium |Linked List, Math, Recursion|
3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](./longest-substring-without-repeating-characters.py) | _O(n)_ | _O(1)_ | Medium |Hash Table, String, Sliding Window|
4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Python](./median-of-two-sorted-arrays.py) | _O(log <sub>min(m, n)</sub>)_ | _O(1)_ | Hard |Array, Binary Search, Divide and Conquer|
5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](./longest-palindromic-substring.py) | _O(n^2)_ | _O(1)_ | Medium |String, Dynamic Programming|
7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | [Python](./reverse-integer.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Medium |Math|
8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | [Python](./string-to-integer-atoi.py) | _O(n)_ | _O(1)_ | Medium |String|
9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) |[Python](./palindrome-number.py) | _O(n)_ | _O(n)_ | Easy |Math|
11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) |[Python](./container-with-most-water.py) | _O(n)_ | _O(n)_ | Medium |Array, Tow Pointers, Greedy|
12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) |[Python](./integer-to-roman.py) | _O(1)_ | _O(1)_ | Medium |Hash Table, Math, String|
13 | [Roman To Integer](https://leetcode.com/problems/roman-to-integer/) |[Python](./roman-to-integer.py) | _O(n)_ | _O(n)_ | Easy |Hash Table, Math, String|
14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) |[Python](./longest-common-prefix.py) | _O(n)_ | _O(1)_ | Easy |String, Trie|
20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |[Python](./valid-parentheses.py) | _O(n)_ | _O(n)_ | Easy |String, Stack|
26 | [Remove Duplicates From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) |[Python](./remove-duplicates-from-sorted-array.py) | _O(n)_ | _O(1)_ | Easy |Array, Tow Pointers|
27 | [Find The Index Of The First Occurrence In A String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |[Python](./find-the-index-of-the-first-occurrence-in-a-string.py) | _O(n)_ | _O(1)_ | Easy |Array, Tow Pointers|
28 | [Remove Element](https://leetcode.com/problems/remove-element/) |[Python](./remove-element.py) | _O(n)_ | _O(1)_ | Easy |Tow Pointers, String, String Matching|
31 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) |[Python](./merge-two-sorted-lists.py) | _O(m+n)_ | _O(1)_ | Easy |Linked List, Recurcion|
33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) |[Python](./search-in-rotated-sorted-array.py) | _O(log<sub>n</sub>)_ | _O(n)_ | Medium |Array, Binary Search|
34 | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |[Python](./find-first-and-last-position-of-element-in-sorted-array.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Medium |Array, Binary Search|
35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) |[Python](./search-insert-position.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Easy |Array, Binary Search|
36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) |[Python](./valid-sudoku.py) | _O(9^2)_ | _O(1)_ | Medium |Array, Hash Table, Matrix|
37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) |[Python](./sudoku-solver.py) | _O((9!)^9)_ | _O(1)_ | Hard |Array, Hash Table, Backtracking, Matrix|
49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) |[Python](./group-anagrams.py) | _O(n)_ | _O(n)_ | Medium |Array, Hash Table, String, Sorting|
53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |[Python](./maximum-subarray.py) | _O(n)_ | _O(n)_ | Medium |Array, Divide and Conquer, Dynamic Programming|
56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) |[Python](./merge-intervals.py) | _O(n)_ | _O(n)_ | Medium |Array, Sorting|
58 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) |[Python](./lenght-of-last-word.py) | _O(nlog<sub>n</sub>)_ | _O(n)_ | Easy |Array, String|
62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) |[Python](./unique-paths.py) | _O(m*n)_ | _O(min(m,n))_ | Medium |Math, Dynamic Programming, Combinatorics|
63 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) |[Python](./unique-paths-ii.py) | _O(m*n)_ | _O(m+n)_ | Medium |Math, Dynamic Programming, Matrix|
66 | [Plus One](https://leetcode.com/problems/plus-one/) |[Python](./plus-one.py) | _O(n)_ | _O(1)_ | Easy |Array, Math|
67 | [Add Binary](https://leetcode.com/problems/add-binary/) |[Python](./add-binary.py) | _O(n)_ | _O(n)_ | Easy |Math, String, Bit Manipulation, Simulation|
69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) |[Python](./sqrt(x).py) | _O(log<sub>n</sub>)_ | _O(1)_ | Easy |Math, Binary Search|
70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) |[Python](./climbing-stairs.py) | _O(n)_ | _O(1)_ | Easy |Math, Dynamic Programming, Memorization|
74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) |[Python](./search-a-2d-matrix.py) | _O(log<sub>m</sub>+log<sub>n</sub>)_ | _O(1)_ | Medium |Array, Binary Search, Matrix|
83 | [Remove Duplicates From Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) |[Python](./remove-duplicates-from-sorted-list.py) | _O(n)_ | _O(n)_ | Easy |Linked List|
88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) |[Python](./merge-sorted-array.py) | _O(n)_ | _O(1)_ | Easy |Array, Two Pointers, Sorting|
92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) |[Python](./reverse-linked-list-ii.py) | _O(n)_ | _O(1)_ | Medium |Linked List|
94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) |[Python](./binary-tree-inorder-traversal.py) | _O(n)_ | _O(1)_ | Easy |Stack, Tree, Depth-First Search, Binary Tree|
118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) |[Python](./pascals-triangle.py) | _O(n^2)_ | _O(n^2)_ | Easy |Array, Dynamic Programming|
119 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle-ii) |[Python](./pascals-triangle-ii.py) | _O(n^2)_ | _O(n^2)_ | Easy |Array, Dynamic Programming|
121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |[Python](./best-time-to-buy-and-sell-stock.py) | _O(n)_ | _O(1)_ | Easy |Array, Dynamic Programming|
122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) |[Python](./best-time-to-buy-and-sell-stock-ii.py) | _O(n)_ | _O(1)_ | Medium |Array, Dynamic Programming, Greedy|
123 | [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) |[Python](./best-time-to-buy-and-sell-stock-iii.py) | _O(n)_ | _O(1)_ | Hard |Array, Dynamic Programming|
125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |[Python](./valid-palindrome.py) | _O(n)_ | _O(1)_ | Easy |Two Pointers, String|
128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) |[Python](./longest-consecutive-sequence.py) | _O(n)_ | _O(1)_ | Medium |Array, Hash Table, Union Find|
136 | [Single Number](https://leetcode.com/problems/single-number/) |[Python](./single-number.py) | _O(n)_ | _O(n)_ | Easy |Array, Bit Manipulation|
138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) |[Python](./copy-list-with-random-pointer.py) | _O(n)_ | _O(1)_ | Medium |Hash Table, Linked List|
135 | [Candy](https://leetcode.com/problems/candy/) |[Python](./candy.py) | _O(n)_ | _O(1)_ | Hard |Array, Greedy|
137 | [Single Number II](https://leetcode.com/problems/single-number-ii/) |[Python](./csingle-number-iiandy.py) | _O(n)_ | _O(1)_ | Medium |Array, Bit Manipulation|
141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) |[Python](./linked-list-cycle.py) | _O(n)_ | _O(1)_ | Easy |Hash Table, Linked List, Two Pointers|
142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) |[Python](./linked-list-cycle-ii.py) | _O(n)_ | _O(1)_ | Medium |Hash Table, Linked List, Two Pointers|
151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) |[Python](./reverse-words-in-a-string.py) | _O(n)_ | _O(1)_ | Medium |Two Pointers, String|
153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) |[Python](./find-minimum-in-rotated-sorted-array.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Medium |Array, Binary Search|
160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) |[Python](./intersection-of-two-linked-lists.py) | _O(n+m)_ | _O(1)_ | Easy |Hash Table, Linked List, Two Pointers|
167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |[Python](./two-sum-ii-input-array-is-sorted.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Medium |Array, Two Pointers, Binary Search|
168 | [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/) |[Python](./excel-sheet-column-title.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Easy |Math, String|
169 | [Majority Element](https://leetcode.com/problems/majority-element/) |[Python](./majority-element.py) | _O(n*k)_ | _O(n)_ | Easy |Array, Hash Table, Divide and Couquer, Sorting, Counting|
188 | [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) |[Python](./best-time-to-buy-and-sell-stock-iv.py) | _O(n)_ | _O(1)_ | Hard |Array, Dynamic Programming|
191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) |[Python](./number-of-1-bits.py) | _O(1)_ | _O(1)_ | Easy |Divide and Couquer, Bit Manipulation|
198 | [House Robber](https://leetcode.com/problems/house-robber/) |[Python](./house-robber.py) | _O(n)_ | _O(1)_ | Medium |Array, Dynamic Programming|
203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) |[Python](./remove-linked-list-elements.py) | _O(n)_ | _O(1)_ | Easy |Linked List, Recursion|
206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |[Python](./reverse-linked-list.py) | _O(n)_ | _O(1)_ | Easy |Linked List, Recursion|
217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) |[Python](./contains-duplicate.py) | _O(n)_ | _O(1)_ | Easy |Array, Hash Table, Sorting|
225 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) |[Python](./implement-stack-using-queues.py) | _O(n)_ | _O(1)_ | Easy |Stack, Design, Queue|
228 | [Summary Ranges](https://leetcode.com/problems/summary-ranges/) |[Python](./msummary-ranges.py) | _O(n)_ | _O(1)_ | Easy |Array|
229 | [Majority Element II](https://leetcode.com/problems/majority-element-ii/) |[Python](./majority-element-ii.py) | _O(n)_ | _O(1)_ | Medium |Array, Hash Table, Sorting, Counting|
238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) |[Python](./product-of-array-except-self.py) | _O(n)_ | _O(1)_ | Medium |Array, Prefix Sum|
242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) |[Python](./valid-anagram.py) | _O(n)_ | _O(n)_ | Easy |Hash Table, String, Sorting|
258 | [Add Digits](https://leetcode.com/problems/add-digits/) |[Python](./add-digits.py) | _O(1)_ | _O(1)_ | Easy |Math, Simulation, Number Theory|
260 | [Single Number III](https://leetcode.com/problems/single-number-iii/) |[Python](./single-number-iii.py) | _O(n)_ | _O(1)_ | Medium |Array, Bit Manipulation|
268 | [Missing Number](https://leetcode.com/problems/missing-number/) |[Python](./missing-number.py) | _O(n)_ | _O(1)_ | Easy |Array, Hash Table, Math|
287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) |[Python](./find-the-duplicate-number.py) | _O(n)_ | _O(1)_ | Medium |Array, Two Pointers, Binary Search, Bit Manipulation|
300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) |[Python](./longest-increasing-subsequence.py) | _O(nlog<sub>n</sub>)_ | _O(n)_ | Medium |Array, Binary Search, Dynamic Programming|
316 | [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) |[Python](./remove-duplicate-letters.py) | _O(n)_ | _O(k)_ | Medium |String, Stack, Greedy, Monotonic Stack|
319 | [Bulb Switcher](https://leetcode.com/problems/bulb-switcher/) |[Python](./bulb-switcher.py) | _O(1)_ | _O(1)_ | Medium |Math, Brainteaser|
326 | [Power of Three](https://leetcode.com/problems/power-of-three/) |[Python](./power-of-three.py) | _O(1)_ | _O(1)_ | Easy |Math, Resursion|
332 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) |[Python](./reconstruct-itinerary.py) | _O(log<sub>m/n</sub>)_ | _O(m+n)_ | Hard |Depth-First Search, Graph, Eulerian Circuit|
338 | [Counting Bits](https://leetcode.com/problems/counting-bits) |[Python](./counting-bits.py) | _O(n)_ | _O(n)_ | Easy |Dynamic Programming, Bit Manipulation|
341 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) |[Python](./flatten-nested-list-iterator.py) | _O(n)_ | _O(n)_ | Medium |Stack, Tree, Deep-First Search, Design, Queue, Iterator|
342 | [Power of Four](https://leetcode.com/problems/power-of-four/) |[Python](./power-of-four.py) | _O(1)_ | _O(1)_ | Easy |Math, Bit Manipulation, Recursion|
343 | [Integer Break](https://leetcode.com/problems/integer-break/) |[Python](./integer-break.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Medium |Math, Dynamic Programming|
347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |[Python](./top-k-frequent-elements.py) | _O(n)_ | _O(n)_ | Medium |Array, Hash Table, Divide and Conquer, Sorting|
377 | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) |[Python](./combination-sum-iv.py) | _O(n*t)_ | _O(t)_ | Medium |Array, Dynamic Programming|
383 | [Ransom Note](https://leetcode.com/problems/ransom-note/) |[Python](./ransom-note.py) | _O(n)_ | _O(1)_ | Easy |Hash Table, String, Counting|
389 | [Find The Difference](https://leetcode.com/problems/find-the-difference/) |[Python](./find-the-difference.py) | _O(n)_ | _O(n)_ | Easy |Hash Table, String, Bit Manipulation, Sorting|
392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) |[Python](./is-subsequence.py) | _O(n)_ | _O(1)_ | Easy |Two Pointers, String, Dynamic Programming|
434 | [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/) |[Python](./number-of-segments-in-a-string.py) | _O(n)_ | _O(1)_ | Easy |String|
441 | [Arranging Coins](https://leetcode.com/problems/arranging-coins/) |[Python](./arranging-coins.py) | _O(1)_ | _O(1)_ | Easy |Math, Binary Search|
456 | [132 Pattern](https://leetcode.com/problems/132-pattern/) |[Python](./132-pattern.py) | _O(n)_ | _O(1)_ | Medium |Array, Binary Search, Stack, Monotonic Stack, Ordered Set|
458 | [Poor Pigs](https://leetcode.com/problems/poor-pigs/) |[Python](./poor-pigs.py) | _O(n)_ | _O(1)_ | Hard |Math, Dynamic Programming, COmbinatorics|
459 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) |[Python](./repeated-substring-pattern.py) | _O(n)_ | _O(1)_ | Easy |String, String Matching|
485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) |[Python](./max-consecutive-ones.py) | _O(n)_ | _O(1)_ | Easy |Array|
492 | [Construct the Rectangle](https://leetcode.com/problems/construct-the-rectangle/) |[Python](./construct-the-rectangle.py) | _O(n)_ | _O(1)_ | Easy |Math|
495 | [Teemo Attacking](https://leetcode.com/problems/teemo-attacking/) |[Python](./teemo-attacking.py) | _O(n)_ | _O(1)_ | Easy |Array, Simulation|
501 | [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/) |[Python](./find-mode-in-binary-search-tree.py) | _O(n)_ | _O(n)_ | Easy |Tree, Deep-First Search, Binary Search Tree, Binary Tree|
515 | [Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/) |[Python](./find-largest-value-in-each-tree-row.py) | _O(n)_ | _O(1)_ | Medium |Tree, Depth_First Search, Breadth-First Search, Binary Tree|
551 | [Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/) |[Python](./student-attendance-record-i.py) | _O(n)_ | _O(1)_ | Easy |String|
557 | [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) |[Python](./reverse-words-in-a-string-iii.py) | _O(n)_ | _O(1)_ | Easy |Tow Pointers, String|
605 | [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/) |[Python](./can-place-flowers.py) | _O(n)_ | _O(1)_ | Easy |Array, Greedy|
606 | [Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/) |[Python](./construct-string-from-binary-tree.py) | _O(n)_ | _O(1)_ | Easy |String, Tree, Deep-First Search, Binary Tree|
704 | [Binary Search](https://leetcode.com/problems/binary-search/) |[Python](./binary-search.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Easy |Array, Binary Search|
706 | [Design HashMap](https://leetcode.com/problems/design-hashmap/) |[Python](./design-hashmap.py) | _O(1)_ | _O(1)_ | Easy |String|
709 | [To Lower Case](https://leetcode.com/problems/to-lower-case/) |[Python](./to-lower-case.py) | _O(n)_ | _O(1)_ | Easy |Array, Hash Table, Linked List, Design, Hash Function|
725 | [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/) |[Python](./split-linked-list-in-parts.py) | _O(n)_ | _O(n)_ | Medium |Linked List|
739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) |[Python](./daily-temperatures.py) | _O(n)_ | _O(n)_ | Medium |Array, Stack, Monotonic Stack|
746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) |[Python](./min-cost-climbing-stairs.py) | _O(n)_ | _O(1)_ | Easy |Array, Dynamic Programming|
779 | [K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) |[Python](./k-th-symbol-in-grammar.py) | _O(n)_ | _O(1)_ | Medium |Math, Bit Manipulation, Recursion|
799 | [Champagne Tower](https://leetcode.com/problems/champagne-tower/) |[Python](./champagne-tower.py) | _O(n)_ | _O(n)_ | Medium |Dynamic Programming|
815 | [Bus Routes](https://leetcode.com/problems/bus-routes/) |[Python](./bus-routes.py) | _O(m+n)_ | _O(m+n)_ | Hard |Array, Hash Table, Breadth-First Search|
823 | [Binary Trees With Factors](https://leetcode.com/problems/binary-trees-with-factors/) |[Python](./binary-trees-with-factors.py) | _O(n^2)_ | _O(n)_ | Medium |Array, Hash Table, Dynamic Programming, Sorting|
844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) |[Python](./backspace-string-compare.py) | _O(n)_ | _O(1)_ | Easy |Two Pointers, String, Stack, Simulation|
847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) |[Python](./shortest-path-visiting-all-nodes.py) | _O(n*2^n)_ | _O(n*2^n)_ | Hard |Dynamic Programming, Bit Manipulation, Deep-First Search, Graph, Bitmask|
867 | [Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) |[Python](./transpose-matrix.py) | _O(n)_ | _O(1)_ | Easy |Array, Matrix, Simulation|
875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) |[Python](./koko-eating-bananas.py) | _O(nlog<sub>n</sub>)_ | _O(1)_ | Medium |Array, Binary Search|
880 | [Decoded String at Index](https://leetcode.com/problems/decoded-string-at-index/) |[Python](./decoded-string-at-index.py) | _O(n)_ | _O(n)_ | Medium |String, Stack|
892 | [Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/) |[Python](./surface-area-of-3d-shapes.py) | _O(n^2)_ | _O(1)_ | Easy |Array, Math, Geometry, Matrix|
896 | [Monotonic Array](https://leetcode.com/problems/monotonic-array/) |[Python](./monotonic-array.py) | _O(n)_ | _O(1)_ | Easy |Array|
905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) |[Python](./sort-array-by-parity.py) | _O(n)_ | _O(1)_ | Easy |Array, Two Pointers, Sorting|
935 | [Knight Dialer](https://leetcode.com/problems/knight-dialer/) |[Python](./knight-dialer.py) | _O(n)_ | _O(1)_ | Medium |Dynamic Programming|
1048 | [Longest String Chain](https://leetcode.com/problems/longest-string-chain/) |[Python](./longest-string-chain.py) | _O(n)_ | _O(n)_ | Medium |Array, Hash Table, Two Pointers, String, Dynamic Programming|
1081 | [Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/) |[Python](./smallest-subsequence-of-distinct-characters.py) | _O(n)_ | _O(k)_ | Medium |String, Stack, Greedy, Monotonic Stack|
1095 | [Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/) |[Python](./find-in-mountain-array.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Hard |Array, Binary Search, Interactive|
1160 | [Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) |[Python](./find-words-that-can-be-formed-by-characters.py) | _O(n)_ | _O(1)_ | Easy |Array, Hash Table, String|
1220 | [Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/) |[Python](./problems/count-vowels-permutation.py) | _O(n)_ | _O(n)_ | Hard |Dynamic Programming|
1266 | [Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/) |[Python](./minimum-time-visiting-all-points.py) | _O(n)_ | _O(1)_ | Easy |Array, Math, Geometry |
1269 | [Number of Ways to Stay in the Same Place After Some Steps](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/) |[Python](./number-of-ways-to-stay-in-the-same-place-after-some-steps.py) | _O(n^2)_ | _O(n)_ | Hard |Dynamic Programming|
1282 | [Group the People Given the Group Size They Belong To](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/) |[Python](./group-the-people-given-the-group-size-they-belong-to.py) | _O(n)_ | _O(n)_ | Hard |Array, Hash Table|
1326 | [Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) |[Python](./minimum-number-of-taps-to-open-to-water-a-garden.py) | _O(n)_ | _O(n)_ | Hard |Array, Dynamic Programming, Greedy|
1337 | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) |[Python](./the-k-weakest-rows-in-a-matrix.py) | _O(n)_ | _O(n)_ | Easy |Array, Binary Search, Sorting, Heap(Priority Queue), Matrix|
1356 | [Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) |[Python](./sort-integers-by-the-number-of-1-bits.py) | _O(nlog<sub>n</sub>)_ | _O(1)_ | Easy |Array, Bit Manipulation, Sorting, Counting|
1359 | [Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/) |[Python](./count-all-valid-pickup-and-delivery-options.py) | _O(n)_ | _O(1)_ | Hard |Math, Dynamic Programming, Combinatorics|
1361 | [Validate Binary Tree Nodes](https://leetcode.com/problems/validate-binary-tree-nodes/) |[Python](./validate-binary-tree-nodes.py) | _O(n)_ | _O(n)_ | Medium |Tree, Deep-First Search, Breadth-First Search, Union Find, Graph, Binary Tree|
1420 | [Build Array Where You Can Find The Maximum Exactly K Comparisons](https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/) |[Python](./build-array-where-you-can-find-the-maximum-exactly-k-comparisons.py) | _O(n)_ | _O(1)_ | Hard |Dynamic Programming, Prefix Sum|
1424 | [Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/) |[Python](./diagonal-traverse-ii.py) | _O(m*n)_ | _O(m*n)_ | Medium |Array, Sorting, Heap(Priority Queue)|
1425 | [Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/) |[Python](./constrained-subsequence-sum.py) | _O(n)_ | _O(1)_ | Hard |Array, Dynamic Programming, Queue, Sliding Window, Heap(Priority Queue),  Monotonic Queue|
1441 | [Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/) |[Python](./build-an-array-with-stack-operations.py) | _O(n)_ | _O(1)_ | Medium |Array, Stack, Simulation|
1446 | [Consecutive Characters](https://leetcode.com/problems/consecutive-characters/) |[Python](./consecutive-characters.py) | _O(n)_ | _O(1)_ | Easy |String|
1450 | [Number of Students Doing Homework at a Given Time](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/) |[Python](./number-of-students-doing-homework-at-a-given-time.py) | _O(n)_ | _O(1)_ | Easy |String|
1458 | [Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) |[Python](./max-dot-product-of-two-subsequences.py) | _O(m*n)_ | _O(min(m,n))_ | Hard |Array, Dynamic Progarmming|
1470 | [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/) |[Python](./shuffle-the-array.py) | _O(n)_ | _O(1)_ | Easy |Array|
1503 | [Last Moment Before All Ants Fall Out of a Plank](https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/) |[Python](./last-moment-before-all-ants-fall-out-of-a-plank.py) | _O(n)_ | _O(1)_ | Medium |Array, Brainteaser, Simulation|
1512 | [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) |[Python](./number-of-good-pairs.py) | _O(n)_ | _O(1)_ | Hard |Array, Hash Table, Math, Counting|
1535 | [Find the Winner of an Array Game](https://leetcode.com/problems/find-the-winner-of-an-array-game/) |[Python](./find-the-winner-of-an-array-game.py) | _O(n)_ | _O(1)_ | Medium |Simulation|
1561 | [Maximum Number of Coins You Can Get](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/) |[Python](./maximum-number-of-coins-you-can-get.py) | _O(n)_ | _O(1)_ | Medium |Array, Math, Greedy, Sorting|
1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) |[Python](./min-cost-to-connect-all-points.py) | _O(n^2)_ | _O(n)_ | Medium |Array, Union Find, Graph, Minimum Spanning Tree|
1611 | [Minimum One Bit Operations to Make Integers Zero](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/) |[Python](./minimum-one-bit-operations-to-make-integers-zero.py) | _O(logn)_ | _O(1)_ | Hard |Dynamic Programming, Bit Manipulation, Memorization|
1630 | [Arithmetic Subarrays](https://leetcode.com/problems/arithmetic-subarrays/) |[Python](./arithmetic-subarrays.py) | _O(n)_ | _O(1)_ | Medium |Array, Sorting|
1631 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) |[Python](./path-with-minimum-effort.py) | _O(n)_ | _O(n)_ | Medium |Array, Binary Search, Deep-First Search, Breadth-First Search, Union Find, Heap (Priority Queue), Matrix|
1647 | [Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/) |[Python](./minimum-deletions-to-make-character-frequencies-unique.py) | _O(n)_ | _O(1)_ | Medium |Hash Table, String, Greedy, Sorting|
1658 | [Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) |[Python](./minimum-operations-to-reduce-x-to-zero.py) | _O(n)_ | _O(1)_ | Medium |Array, Hash Table, Binary Search, Sliding Window, Prefix Sum|
1662 | [Check If Two String Arrays are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/) |[Python](./check-if-two-string-arrays-are-equivalent.py) | _O(n)_ | _O(1)_ | Easy |Array, String|
1688 | [Count of Matches in Tournament](https://leetcode.com/problems/count-of-matches-in-tournament/) |[Python](./count-of-matches-in-tournament.py) | _O(1)_ | _O(1)_ | Easy |Math, Simulation|
1716 | [Calculate Money in Leetcode Bank](https://leetcode.com/problems/calculate-money-in-leetcode-bank/) |[Python](./calculate-money-in-leetcode-bank.py) | _O(1)_ | _O(1)_ | Easy |Math|
1727 | [Largest Submatrix With Rearrangements](https://leetcode.com/problems/largest-submatrix-with-rearrangements/) |[Python](./largest-submatrix-with-rearrangements.py) | _O(m*nlogn)_ | _O(1)_ | Medium |Array, Greedy, Sorting, Matrix|
1736 | [Latest Time by Replacing Hidden Digits](https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/) |[Python](./latest-time-by-replacing-hidden-digits.py) | _O(n)_ | _O(n)_ | Medium |Array, Hash Table|
1743 | [Restore the Array From Adjacent Pairs](https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/) |[Python](./restore-the-array-from-adjacent-pairs.py) | _O(n)_ | _O(1)_ | Medium |Array, Hash Table|
1759 | [Count Number of Homogenous Substrings](https://leetcode.com/problems/count-number-of-homogenous-substrings/) |[Python](./count-number-of-homogenous-substrings.py) | _O(n)_ | _O(1)_ | Medium |Math, String|
1793 | [Maximum Score of a Good Subarray](https://leetcode.com/problems/maximum-score-of-a-good-subarray/) |[Python](./maximum-score-of-a-good-subarray.py) | _O(n)_ | _O(1)_ | Hard |Array, Two Pointers, Binary Search, Stack, Monotonic Stack|
1814 | [Count Nice Pairs in an Array](https://leetcode.com/problems/count-nice-pairs-in-an-array/) |[Python](./count-nice-pairs-in-an-array.py) | _O(n)_ | _O(1)_ | Medium |Array, Hash Table, Math, Counting|
1838 | [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) |[Python](./frequency-of-the-most-frequent-element.py) | _O(n)_ | _O(1)_ | Medium |Array, Binary Search, Greedy, Sliding Window|
1845 | [Seat Reservation Manager](https://leetcode.com/problems/seat-reservation-manager/) |[Python](./seat-reservation-manager.py) | _O(n)_ | _O(n)_ | Medium |Design, Heap(Priority Queue)|
1846 | [Maximum Element After Decreasing and Rearranging](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/) |[Python](./maximum-element-after-decreasing-and-rearranging.py) | _O(n)_ | _O(1)_ | Medium |Array, Greedy, Sorting|
1877 | [Minimize Maximum Pair Sum in Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/) |[Python](./minimize-maximum-pair-sum-in-array.py) | _O(n)_ | _O(1)_ | Medium |Array, Two Pointers, Greedy, Sorting|
1887 | [Reduction Operations to Make the Array Elements Equal](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/) |[Python](./reduction-operations-to-make-the-array-elements-equal.py) | _O(nlog<sub>n</sub>)_ | _O(1)_ | Medium |Array, Sorting|
1903 | [Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string/) |[Python](./largest-odd-number-in-string.py) | _O(n)_ | _O(1)_ | Easy |Math, String, Greedy|
1921 | [Eliminate Maximum Number of Monsters](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/) |[Python](./eliminate-maximum-number-of-monsters.py) | _O(n)_ | _O(n)_ | Medium |Array, Greedy, Sorting|
1930| [Unique Length-3 Palindromic Subsequences](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/) |[Python](./unique-length-3-palindromic-subsequences.py) | _O(n)_ | _O(n)_ | Medium |Hash Table, String, Prefix Sum|
1980| [Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string/) |[Python](./find-unique-binary-string.py) | _O(n)_ | _O(1)_ | Medium |Array, String, Backtracking|
2009 | [Minimum Number of Operations to Make Array Continuous](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/) |[Python](./minimum-number-of-operations-to-make-array-continuous.py) | _O(nlogn)_ | _O(n)_ | Hard |Array, Binary Search|
2038 | [Remove Colored Pieces if Both Neighbors are the Same Color](https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) |[Python](./remove-colored-pieces-if-both-neighbors-are-the-same-color.py) | _O(n)_ | _O(1)_ | Medium |Math, String, Greedy, Game Theory|
2050 | [Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/) |[Python](./parallel-courses-iii.py) | _O(m+n)_ | _O(n)_ | Hard |Array, Dynamic Programming, Graph, Topological Sort|
2114 | [Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/) |[Python](./maximum-number-of-words-found-in-sentences/description.py) | _O(n)_ | _O(1)_ | Easy |Array, String|
2119 | [A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/) |[Python](./a-number-after-a-double-reversal.py) | _O(1)_ | _O(1)_ | Easy |Array|
2147 | [Number of Ways to Divide a Long Corridor](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/) |[Python](./number-of-ways-to-divide-a-long-corridor.py) | _O(n)_ | _O(1)_ | Hard |Math, String, Dynamic Programming|
2251 | [Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) |[Python](./number-of-flowers-in-full-bloom.py) | _O(m*n)_ | _O(1)_ | Hard |Array, Hash Table, Binary Search, Sorting, Prefix Sum, Ordered Set|
2264 | [Largest 3-Same-Digit Number in String](https://leetcode.com/problems/largest-3-same-digit-number-in-string/) |[Python](./largest-3-same-digit-number-in-string.py) | _O(n)_ | _O(1)_ | Easy |String|
2265 | [Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) |[Python](./count-nodes-equal-to-average-of-subtree.py) | _O(n)_ | _O(n)_ | Medium |Tree, Deep-First Search, Binary Tree|
2391 | [Minimum Amount of Time to Collect Garbage](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/) |[Python](./minimum-amount-of-time-to-collect-garbage.py) | _O(n)_ | _O(1)_ | Medium |Array, String, Prefix Sum|
2433 | [Find The Original Array of Prefix Xor](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/) |[Python](./find-the-original-array-of-prefix-xor.py) | _O(n)_ | _O(1)_ | Medium |Bit Manipulation|
2642 | [Design Graph With Shortest Path Calculator](https://leetcode.com/problems/design-graph-with-shortest-path-calculator/) |[Python](./design-graph-with-shortest-path-calculator.py) | _O(n)_ | _O(1)_ | Hard |Graph, Design, Heap(Priority Queue), Shortest Path|
2707 | [Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string/) |[Python](./extra-characters-in-a-string.py) | _O(n)_ | _O(n)_ | Medium |Array, Hash Table, String, Dynamic Programming, Trie|
2742 | [Painting the Walls](https://leetcode.com/problems/painting-the-walls/) |[Python](./painting-the-walls.py) | _O(n)_ | _O(n)_ | Hard |Array,Dynamic Programming|
2785 | [Sort Vowels in a String](https://leetcode.com/problems/sort-vowels-in-a-string/) |[Python](./sort-vowels-in-a-string.py) | _O(n)_ | _O(1)_ | Medium |String, Sorting|
2849 | [Determine if a Cell Is Reachable at a Given Time](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/) |[Python](./determine-if-a-cell-is-reachable-at-a-given-time.py) | _O(1)_ | _O(1)_ | Medium |Math|