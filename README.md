# 66-days challenge
---
## Day55
---

### 1.Import tkinter
```
from tkinter import *
```

### 2.Define pressed button
```
def button_pressed(value):
    number_entry.insert("end",value)
    print(value,"pressed")
```

### 3.Basic settings
- Set title as Calculator, and set the window size as 200x160
```
root = Tk()
root.title("Calculator")
root.geometry("200x160")
```

### 4.Making space for entered value
- Set width and location by using entry,grid command
```
entry_value = StringVar(root,value="")
number_entry = Entry(root,textvariable=entry_value,width=12)
number_entry.grid(row=0,columnspan=3)
```

### 5.Making buttons
- Repeated tasks were condensed using a for loop
- Calculating function buttons were also created and applied
```
for i in range(3):
    for j in range(3):
        k = 3*i+j+1
        globals()['button{}'.format(k)] = Button(root, text=k, command = lambda:button_pressed('k'))
        globals()['button{}'.format(k)].grid(row=(3-i), column=j)
button_div = Button(root, text="/", command = lambda:math_button_pressed('/'))
button_div.grid(row=1, column=3)
button_mult = Button(root, text="*", command = lambda:math_button_pressed('*'))
button_mult.grid(row=2, column=3)
button_add = Button(root, text="+", command = lambda:math_button_pressed('+'))
button_add.grid(row=3, column=3)
button_ac = Button(root, text="AC", command = lambda:button_pressed('AC'))
button_ac.grid(row=4, column=0)
button0 = Button(root, text="0", command = lambda:button_pressed('0'))
button0.grid(row=4, column=1)
button_equal = Button(root, text="=", command = lambda:equal_button_pressed())
button_equal.grid(row=4, column=2)
button_sub = Button(root, text="-", command = lambda:math_button_pressed('-'))
button_sub.grid(row=4, column=3)
```

### 6.Mainloop
- Generate Event loops
```
root.mainloop()
```

---
## Day54
---

### 1.Initialize variables
```
num, res = set(), set()
```

### 2.Discriminate decimals 2 to 1M
- Use sieve of Eratosthenes
```
for n in range(2,1000001):
    c = True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            c = False
            continue
    if c == True:
        num.add(n)
a = num.copy()
```

### 3.Discriminate circular prime
- Rotate each digit to obtain len(n) natural numbers and place them in a new set. Then, determine if this set is a subset of the set of all prime numbers
```
while a:
    tnum = set()
    t = str(a.pop())
    for _ in range(len(t)):
        t = t[-1:]+t[:-1]
        tnum.add(int(t))
    if len(tnum&num)==len(tnum):
        res.update(tnum)
    a -= tnum
```

### 4.Print result
```
print(len(res)) #55
```

---
## Day55
---

### Prime Factorization
- Define new function named soultion. This function prints all the prime factors of n.
```
def solution(n):
    res = []
    i = 2
    while i<=n:
        if n%i==0:
            n /= i
            if not i in res:
                res.append(i)
        else:
            i += 1
    return res
```
