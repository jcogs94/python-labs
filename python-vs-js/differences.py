import math

# Get Name
# Write a method that accepts a name from the user and then returns it. Here’s the javascript:

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

def get_name():
    name = input('What is your name? ')
    return name

# # Test
# print('Your name is ' + get_name() + '.')


# Reverse It
# Write a method that reverses a string. Here’s the javascript:

# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

def reverse_it():
    string = 'a man, a plan, a calan, frenemies!'
    reverse = ''
    for i in range(len(string)):
        reverse += string[len(string) - (i + 1)]
    
    print(reverse)

# # Test
# reverse_it()


# Swap Em
# Write a method that swaps the values of two variables around. Here’s the javascript:

# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

def swap_em():
    a = 10
    b = 30

    temp = b
    b = a
    a = temp

    print('a is now ' + str(a) + ', and b is now ' + str(b))

# # Test
# swap_em()


# Multiply Array/List
# Write a method that multiplies all numbers in a given array/list and returns the final product. Here’s the javascript:

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

def multiply_array(ary):
    if len(ary) == 0: return 1

    total = 1
    # total = ary[0]

    for num in ary:
        total *= num
    
    return total

# # Test
# print(multiply_array([5, 2, 3]))


# Fizz Buzzer
# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:

# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

def fizzbuzzer(x):
    if (x % 3) == 0 and (x % 5) == 0:
        return 'fizzbuzz'
    elif (x % 3) == 0:
        return 'fizz'
    elif (x % 5) == 0:
        return 'buzz'
    else:
        return 'archer'

# # Test
# print(fizzbuzzer(7))


# Nth Fibonacci
# Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:

# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

def nth_fibonacci_number():
    fibs = [1, 1]
    num = input('which fibonacci number do you want? ')

    while len(fibs) < int(num):
        length = len(fibs)
        next_fib = fibs[length - 2] + fibs[length - 1]
        fibs.append(next_fib)
    
    print(str(fibs[len(fibs) - 1]) + ' is the fibonacci number at position ' + num)

# # Test
# nth_fibonacci_number()


# Search Array/List
# Write a method that searches through an array/list for a value and returns true or false depending on whether or not the value is present in the array/list. Here is the javascript:

# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };

def search_array(array, value):
    for index in array:
        if index == value:
            return True
    
    return -1

# # Test
# print('Result: ' + str(search_array([5, 9, 17, 34], 18)))


# Palindrome
# Write a method that checks whether or not a string is a palindrome. Here is the javascript:

# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };

def is_palindrome(str):
    for i in range(0, (math.ceil(len(str) / 2))):
        if (str[i] != str[len(str) - i - 1]):
            return False
    
    return True

# # Test
# print('Result: ' + str(is_palindrome('madam')))


# hasDupes
# Write a method that checks whether or not an array/list has any duplicates. Here is the javascript:

# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };

def has_dupes(arr):
    dict = {}
    for value in arr:
        if str(value) in dict:
            return True
        else:
            dict[str(value)] = True
    
    return False

# # Test
# print('Result: ', has_dupes([5, 7, 9, 20, 7, 49]))
