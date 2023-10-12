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
56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) |[Python](./merge-intervals.py) | _O(n)_ | _O(n)_ | Medium |Array, Sorting|
58 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) |[Python](./lenght-of-last-word.py) | _O(nlog<sub>n</sub>)_ | _O(n)_ | Easy |Array, String|
62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) |[Python](./unique-paths.py) | _O(m*n)_ | _O(min(m,n))_ | Medium |Math, Dynamic Programming, Combinatorics|
63 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) |[Python](./unique-paths-ii.py) | _O(m*n)_ | _O(m+n)_ | Medium |Math, Dynamic Programming, Matrix|
66 | [Plus One](https://leetcode.com/problems/plus-one/) |[Python](./plus-one.py) | _O(n)_ | _O(1)_ | Easy |Array, Math|
67 | [Add Binary](https://leetcode.com/problems/add-binary/) |[Python](./add-binary.py) | _O(n)_ | _O(n)_ | Easy |Math, String, Bit Manipulation, Simulation|
69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) |[Python](./sqrt(x).py) | _O(log<sub>n</sub>)_ | _O(1)_ | Easy |Math, Binary Search|
70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) |[Python](./climbing-stairs.py) | _O(n)_ | _O(1)_ | Easy |Math, Dynamic Programming, Memorization|
83 | [Remove Duplicates From Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) |[Python](./remove-duplicates-from-sorted-list.py) | _O(n)_ | _O(n)_ | Easy |Linked List|
88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) |[Python](./merge-sorted-array.py) | _O(n)_ | _O(1)_ | Easy |Array, Two Pointers, Sorting|
92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) |[Python](./reverse-linked-list-ii.py) | _O(n)_ | _O(1)_ | Medium |Linked List|
94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) |[Python](./binary-tree-inorder-traversal.py) | _O(n)_ | _O(1)_ | Easy |Stack, Tree, Depth-First Search, Binary Tree|
118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) |[Python](./pascals-triangle.py) | _O(n^2)_ | _O(n^2)_ | Easy |Array, Dynamic Programming|
119 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle-ii) |[Python](./pascals-triangle-ii.py) | _O(n^2)_ | _O(n^2)_ | Easy |Array, Dynamic Programming|
125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |[Python](./valid-palindrome.py) | _O(n)_ | _O(1)_ | Easy |Two Pointers, String|
136 | [Single Number](https://leetcode.com/problems/single-number/) |[Python](./single-number.py) | _O(n)_ | _O(n)_ | Easy |Array, Bit Manipulation|
138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) |[Python](./copy-list-with-random-pointer.py) | _O(n)_ | _O(1)_ | Medium |Hash Table, Linked List|
121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |[Python](./best-time-to-buy-and-sell-stock.py) | _O(n)_ | _O(1)_ | Easy |Array, Dynamic Programming|
135 | [Candy](https://leetcode.com/problems/candy/) |[Python](./candy.py) | _O(n)_ | _O(1)_ | Hard |Array, Greedy|
137 | [Single Number II](https://leetcode.com/problems/single-number-ii/) |[Python](./csingle-number-iiandy.py) | _O(n)_ | _O(1)_ | Medium |Array, Bit Manipulation|
141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) |[Python](./linked-list-cycle.py) | _O(n)_ | _O(1)_ | Easy |Hash Table, Linked List, Two Pointers|
142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) |[Python](./linked-list-cycle-ii.py) | _O(n)_ | _O(1)_ | Medium |Hash Table, Linked List, Two Pointers|
151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) |[Python](./reverse-words-in-a-string.py) | _O(n)_ | _O(1)_ | Medium |Two Pointers, String|
160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) |[Python](./intersection-of-two-linked-lists.py) | _O(n+m)_ | _O(1)_ | Easy |Hash Table, Linked List, Two Pointers|
168 | [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/) |[Python](./excel-sheet-column-title.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Easy |Math, String|
169 | [Majority Element](https://leetcode.com/problems/majority-element/) |[Python](./majority-element.py) | _O(n)_ | _O(1)_ | Easy |Array, Hash Table, Divide and Couquer, Sorting, Counting|
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
316 | [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) |[Python](./remove-duplicate-letters.py) | _O(n)_ | _O(k)_ | Medium |String, Stack, Greedy, Monotonic Stack|
319 | [Bulb Switcher](https://leetcode.com/problems/bulb-switcher/) |[Python](./bulb-switcher.py) | _O(1)_ | _O(1)_ | Medium |Math, Brainteaser|
326 | [Power of Three](https://leetcode.com/problems/power-of-three/) |[Python](./power-of-three.py) | _O(1)_ | _O(1)_ | Easy |Math, Resursion|
332 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) |[Python](./reconstruct-itinerary.py) | _O(log<sub>m/n</sub>)_ | _O(m+n)_ | Hard |Depth-First Search, Graph, Eulerian Circuit|
338 | [Counting Bits](https://leetcode.com/problems/counting-bits) |[Python](./counting-bits.py) | _O(n)_ | _O(n)_ | Easy |Dynamic Programming, Bit Manipulation|
343 | [Integer Break](https://leetcode.com/problems/integer-break/) |[Python](./integer-break.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Medium |Math, Dynamic Programming|
377 | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) |[Python](./combination-sum-iv.py) | _O(n*t)_ | _O(t)_ | Medium |Array, Dynamic Programming|
383 | [Ransom Note](https://leetcode.com/problems/ransom-note/) |[Python](./ransom-note.py) | _O(n)_ | _O(1)_ | Easy |Hash Table, String, Counting|
389 | [Find The Difference](https://leetcode.com/problems/find-the-difference/) |[Python](./find-the-difference.py) | _O(n)_ | _O(n)_ | Easy |Hash Table, String, Bit Manipulation, Sorting|
392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) |[Python](./is-subsequence.py) | _O(n)_ | _O(1)_ | Easy |Two Pointers, String, Dynamic Programming|
434 | [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/) |[Python](./number-of-segments-in-a-string.py) | _O(n)_ | _O(1)_ | Easy |String|
441 | [Arranging Coins](https://leetcode.com/problems/arranging-coins/) |[Python](./arranging-coins.py) | _O(1)_ | _O(1)_ | Easy |Math, Binary Search|
456 | [132 Pattern](https://leetcode.com/problems/132-pattern/) |[Python](./132-pattern.py) | _O(n)_ | _O(1)_ | Medium |Array, Binary Search, Stack, Monotonic Stack, Ordered Set|
459 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) |[Python](./repeated-substring-pattern.py) | _O(n)_ | _O(1)_ | Easy |String, String Matching|
485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) |[Python](./max-consecutive-ones.py) | _O(n)_ | _O(1)_ | Easy |Array|
492 | [Construct the Rectangle](https://leetcode.com/problems/construct-the-rectangle/) |[Python](./construct-the-rectangle.py) | _O(n)_ | _O(1)_ | Easy |Math|
495 | [Teemo Attacking](https://leetcode.com/problems/teemo-attacking/) |[Python](./teemo-attacking.py) | _O(n)_ | _O(1)_ | Easy |Array, Simulation|
551 | [Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/) |[Python](./student-attendance-record-i.py) | _O(n)_ | _O(1)_ | Easy |String|
557 | [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) |[Python](./reverse-words-in-a-string-iii.py) | _O(n)_ | _O(1)_ | Easy |Tow Pointers, String|
605 | [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/) |[Python](./can-place-flowers.py) | _O(n)_ | _O(1)_ | Easy |Array, Greedy|
706 | [Design HashMap](https://leetcode.com/problems/design-hashmap/) |[Python](./design-hashmap.py) | _O(1)_ | _O(1)_ | Easy |String|
709 | [To Lower Case](https://leetcode.com/problems/to-lower-case/) |[Python](./to-lower-case.py) | _O(n)_ | _O(1)_ | Easy |Array, Hash Table, Linked List, Design, Hash Function|
725 | [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/) |[Python](./split-linked-list-in-parts.py) | _O(n)_ | _O(n)_ | Medium |Linked List|
799 | [Champagne Tower](https://leetcode.com/problems/champagne-tower/) |[Python](./champagne-tower.py) | _O(n)_ | _O(n)_ | Medium |Dynamic Programming|
847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) |[Python](./shortest-path-visiting-all-nodes.py) | _O(n*2^n)_ | _O(n*2^n)_ | Hard |Dynamic Programming, Bit Manipulation, Deep-First Search, Graph, Bitmask|
880 | [Decoded String at Index](https://leetcode.com/problems/decoded-string-at-index/) |[Python](./decoded-string-at-index.py) | _O(n)_ | _O(n)_ | Medium |String, Stack|
892 | [Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/) |[Python](./surface-area-of-3d-shapes.py) | _O(n^2)_ | _O(1)_ | Easy |Array, Math, Geometry, Matrix|
896 | [Monotonic Array](https://leetcode.com/problems/monotonic-array/) |[Python](./monotonic-array.py) | _O(n)_ | _O(1)_ | Easy |Array|
905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) |[Python](./sort-array-by-parity.py) | _O(n)_ | _O(1)_ | Easy |Array, Two Pointers, Sorting|
1048 | [Longest String Chain](https://leetcode.com/problems/longest-string-chain/) |[Python](./longest-string-chain.py) | _O(n)_ | _O(n)_ | Medium |Array, Hash Table, Two Pointers, String, Dynamic Programming|
1081 | [Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/) |[Python](./smallest-subsequence-of-distinct-characters.py) | _O(n)_ | _O(k)_ | Medium |String, Stack, Greedy, Monotonic Stack|
1095 | [Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/) |[Python](./find-in-mountain-array.py) | _O(log<sub>n</sub>)_ | _O(1)_ | Hard |Array, Binary Search, Interactive|
1282 | [Group the People Given the Group Size They Belong To](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/) |[Python](./group-the-people-given-the-group-size-they-belong-to.py) | _O(n)_ | _O(n)_ | Hard |Array, Hash Table|
1326 | [Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) |[Python](./minimum-number-of-taps-to-open-to-water-a-garden.py) | _O(n)_ | _O(n)_ | Hard |Array, Dynamic Programming, Greedy|
1337 | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) |[Python](./the-k-weakest-rows-in-a-matrix.py) | _O(n)_ | _O(n)_ | Easy |Array, Binary Search, Sorting, Heap(Priority Queue), Matrix|
1359 | [Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/) |[Python](./count-all-valid-pickup-and-delivery-options.py) | _O(n)_ | _O(1)_ | Hard |Math, Dynamic Programming, Combinatorics|
1420 | [Build Array Where You Can Find The Maximum Exactly K Comparisons](https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/) |[Python](./build-array-where-you-can-find-the-maximum-exactly-k-comparisons.py) | _O(n)_ | _O(1)_ | Hard |Dynamic Programming, Prefix Sum|
1446 | [Consecutive Characters](https://leetcode.com/problems/consecutive-characters/) |[Python](./consecutive-characters.py) | _O(n)_ | _O(1)_ | Easy |String|
1450 | [Number of Students Doing Homework at a Given Time](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/) |[Python](./number-of-students-doing-homework-at-a-given-time.py) | _O(n)_ | _O(1)_ | Easy |String|
1458 | [Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) |[Python](./max-dot-product-of-two-subsequences.py) | _O(m*n)_ | _O(min(m,n))_ | Hard |Array, Dynamic Progarmming|
1470 | [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/) |[Python](./shuffle-the-array.py) | _O(n)_ | _O(1)_ | Easy |Array|
1512 | [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) |[Python](./number-of-good-pairs.py) | _O(n)_ | _O(1)_ | Hard |Array, Hash Table, Math, Counting|
1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) |[Python](./min-cost-to-connect-all-points.py) | _O(n^2)_ | _O(n)_ | Medium |Array, Union Find, Graph, Minimum Spanning Tree|
1631 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) |[Python](./path-with-minimum-effort.py) | _O(n)_ | _O(n)_ | Medium |Array, Binary Search, Deep-First Search, Breadth-First Search, Union Find, Heap (Priority Queue), Matrix|
1647 | [Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/) |[Python](./minimum-deletions-to-make-character-frequencies-unique.py) | _O(n)_ | _O(1)_ | Medium |Hash Table, String, Greedy, Sorting|
1658 | [Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) |[Python](./minimum-operations-to-reduce-x-to-zero.py) | _O(n)_ | _O(1)_ | Medium |Array, Hash Table, Binary Search, Sliding Window, Prefix Sum|
2009 | [Minimum Number of Operations to Make Array Continuous](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/) |[Python](./minimum-number-of-operations-to-make-array-continuous.py) | _O(nlogn)_ | _O(n)_ | Hard |Array, Binary Search|
2038 | [Remove Colored Pieces if Both Neighbors are the Same Color](https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) |[Python](./remove-colored-pieces-if-both-neighbors-are-the-same-color.py) | _O(n)_ | _O(1)_ | Medium |Math, String, Greedy, Game Theory|
2114 | [Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/) |[Python](./maximum-number-of-words-found-in-sentences/description.py) | _O(n)_ | _O(1)_ | Easy |Array, String|
2119 | [A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/) |[Python](./a-number-after-a-double-reversal.py) | _O(1)_ | _O(1)_ | Easy |Array|
2251 | [Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) |[Python](./number-of-flowers-in-full-bloom.py) | _O(m*n)_ | _O(1)_ | Hard |Array, Hash Table, Binary Search, Sorting, Prefix Sum, Ordered Set|
2707 | [Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string/) |[Python](./extra-characters-in-a-string.py) | _O(n)_ | _O(n)_ | Medium |Array, Hash Table, String, Dynamic Programming, Trie|