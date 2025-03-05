# Python Notes

## Built-in Data Structures

### Set
```python
    # init
    s = set()

    # add
    s.add("thing")

    # lookup
    if "thing" in s:
        print("thing in s")

    # remove
    s.remove("thing")
```

### Dict (Map)

```python
    
    # init 
    d = {}

    # add
    d["foo"] = "bar"

    # add (only insert if key not already present)
    d.setdefault("foo", "baz")

    # does key exist in dict
    if "foo" in d:
        print("foo in d")
    
    # get value from dict (returns None if not found)
    val = d.get("foo")
    
    # get value from dict, returns default val if not found
    val = d.get("foo", "")

    # get value from dict (throws error if not found)
    val = d["foo"]


    # remove
    del d["foo"]
```

### List
```python
    # shallow copy list
    l = [1,2,3]
    l_copy = l.copy()
    
    ## deep copy nested list (either list of objects or list of lists] 
    import copy
    l = [[1], [2]]
    l_copy = copy.deepcopy(l)
```


### Tuple
```python
    # declare tuple
    t1 = (1,2)
    t2 = (1,2,3)

    # loop list of tuples
    t = [
        (0,1)
        (1,0)
    ]

    for row, col in t:
        print(row, col)

    # use tuple as key in dict, or val in set (only works if vals are serializable)
    t = (0,1)
    seen.add(t)
    
    d = {}
    d[t] = true

```

### HeapQ

Python has a built-in heap type. It technically only supports min heap, however you can use negative numbers to make it a max heap.

Usage Min Heap:

```python
    import heapq
    
    minHeap = []
    
    heapq.heapMush(minHeap, 1)
    heapq.heapMush(minHeap, 2)
    heapq.heapMush(minHeap, 3)

    smallest = heapq.heappop(minHeap) # 1
    ```

Usage Max Heap:

```python
    import heapq
    
    maxHeap = []
    
    heapq.heapMush(maxHeap, 1)
    heapq.heapMush(maxHeap, 2)
    heapq.heapMush(maxHeap, 3)

    largest = -heapq.heappop(maxHeap) # 3
    ```

### Deque (Queue)
```python
    # init 
    queue = deque()

    # insert
    queue.push(1)

    # pop
    thing = queue.popleft()
```

## Loops

### Range Loop

### Enumerate 

### Iteration Loop
```python
    # loop from 0 to n 
    for i in range(n):
        print(i)

    # loop from 0 to n (with custom start)
    for i in range(0,n):
        print(i)
```

## Common Tricks / Operations

### Get Cardinal Directions Neighbours in Matrix

### Fill Map

### Iterate Map

### Sort Array

### Reverse Array
