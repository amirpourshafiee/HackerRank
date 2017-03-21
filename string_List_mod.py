>>> string = "abracadabra"
You can access an index by:

>>> print string[5]
a
What if you would like to assign a value?

>>> string[5] = 'k'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
How would you approach this?

One solution is to convert the string to a list and then change the value.
Example

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
Another approach is to slice the string and join it back.
Example

>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra





Task
Read a given string, change the character at a given index and then print the modified string.

Input Format
The first line contains a string, .
The next line contains an integer , denoting the index location and a character  separated by a space.

Output Format
Using any of the methods explained above, replace the character at index  with character .

Sample Input

abracadabra
5 k
Sample Output

abrackdabra


def mutate_string(string, position, character):

    l = list (string)
    l[position] = character
    string = ''.join(l)
    print (string)

    return

str=input()
pos = input().split()
pos[0] = int(pos[0])
character = pos[1]
mutate_string(str, pos[0], character)
