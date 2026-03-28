🚀 What is Recursion?

Recursion is a technique where a function calls itself to solve a smaller version of the same problem.

💡 “Break the problem → Solve smaller → Combine results”


⚡ Key Components

1. Base Case (Most Important ❗)
	•	Stops infinite recursion
	•	Smallest valid input

    if n == 0:
    return

2. Recursive Call
	•	Function calling itself
	•	Moves towards base case

    recursion(n-1) 

3. Work / Processing
	•	What you do at each step (before or after call)

🛠️ Steps to Solve Recursion Problems
	1.	Identify the smallest problem (base case)
	2.	Assume recursion works for smaller input
	3.	Write recursive relation
	4.	Add work before/after call


🎯 Tips to Master Recursion
	•	Always dry run with small input (n = 2, 3)
	•	Visualize stack flow
	•	Practice patterns again & again
	•	Convert recursion → iteration (for deeper understanding)
	•	Focus on:
	•	Base case
	•	Transition (n → n-1)

⸻

🧪 Time & Space Complexity
	•	Time: Depends on number of calls
	•	Space: O(n) due to recursion stack


🏁 Final Notes (Must Remember ⭐)
	•	Every recursion must have a base case
	•	Think: “How can I reduce the problem?”
	•	Recursion = Divide → Solve → Combine
	•	Stack plays a crucial role
	•	Practice is the only way to master
