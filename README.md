The Floyd's Cycle Finding Algorithm, also known as the "tortoise and hare" algorithm.

We'll use two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time, while the fast pointer moves two steps.

The main idea is that if there's a cycle, the fast pointer will catch up to the slow pointer. If there's no cycle, the fast pointer will reach the end of the list.
