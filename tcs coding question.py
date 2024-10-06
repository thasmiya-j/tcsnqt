# 4 REVERSE A GIVEN ARRAY
    class Solution:
        def reverseString(self, s: List[str]) -> None:
            """
            Do not return anything, modify s in-place instead.
            """
            i=0
            j=len(s)-1
            while(i<=j):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1


#5
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ind = []
        for index,num in enumerate(nums):
            if num==x:
                ind.append(index)
        ans =[]
        for q in queries:
            if q > len(ind):
                ans.append(-1)
            else:
                ans.append(ind[q-1])
        return ans



    
# 6. Rearrange array in increasing-decreasing order

def process(arr):
  arr.sort()
  n = len(arr)
  for i in range(n // 2):
    print(arr[i], end=" ")
  for i in range(n - 1, n // 2 - 1, -1):
    print(arr[i], end=" ")


arr = list(map(int, input().split()))
process(arr)




#7.Sum of Array


class Solution:

  def _sum(self, arr):
    sum = 0
    for i in range(len(arr)):
      sum += arr[i]
    return sum




#8.left rotate array by 1


def rotate(arr):
  n = len(arr)
  temp = arr[0]
  for i in range(1, n):
    arr[i - 1] = arr[i]
  arr[n - 1] = temp
  print(arr)


arr = list(map(int, input().split()))
rotate(arr)


#9.Left rotate an array by k positions
class Solution:

  def reverse(self, arr, start, end):
    while start < end:
      arr[start], arr[end] = arr[end], arr[start]  # Swap the elements
      start += 1
      end -= 1

  def leftRotate(self, arr, d):
    n = len(arr)
    d = d % n  # In case d is larger than n

    self.reverse(arr, 0, d - 1)  # Reverse the first part
    self.reverse(arr, d, n - 1)  # Reverse the second part
    self.reverse(arr, 0, n - 1)  # Reverse the whole array


#10.median of array


class Solution:

  def find_median(self, arr):
    arr.sort()
    for i in range(n):
      if n % 2 != 0:
        return arr[n // 2]
      else:
        return (arr[n // 2] + arr[n // 2 - 1]) // 2

#11.Remove duplicate elements from sorted array

class Solution:
  def removeDuplicates(self, arr: List[int]) -> int:
      n = len(arr)
      j = 1
      for i in range(1,n):
          if arr[i] != arr[i-1]:
              arr[j] = arr[i]
              j +=1
      return j
#j starts at 1: Since the first element is always unique, the variable j keeps track of the position where the next unique element should be placed.
# Loop starts from index 1: The loop starts at index 1 and compares each element with the previous one.
 #   Placing unique elements: When a new unique element is found, it's placed at index j, and j is incremented.
  #  Return j: The function returns j, representing the number of unique elements in the array.


#12.Remove duplicate elemnts from unsorted array
#when we need number of unique elements
#sol1 
class Solution:
  def removeDuplicates(self, arr: List[int]) -> int:
      seen = {}  # Dictionary to track seen elements
      j = 0  # Pointer for the next unique element's position

      for i in range(len(arr)):
          if arr[i] not in seen:
              seen[arr[i]] = True  # Mark element as seen
              arr[j] = arr[i]  # Place unique element in the correct position
              j += 1

      return j

# sol2
class Solution:

def removeDuplicate(self, arr):
    # code here
    s = set()
    v = []

    # Traverse the input list
    for item in arr:
        # If not present, then put it in
        # the set and add it to the result list
        if item not in s:
            s.add(item)
            v.append(item)

    return v
#13.adding element in an array

def insertion(arr):
   arr.insert(0,6)
   arr.insert(4,8) # first insert in middle then first and last
   arr.append(7)

arr= list(map(int,input().split()))
insertion(arr)
print(arr)

#14.Find all repeating elements in an array

def repeatingelement(arr):
   dictionary ={}
   ans =[]
   for i in range(len(arr)):
       if arr[i] not in dictionary:
           dictionary[arr[i]] = 1 
       else:
           dictionary[arr[i]] +=1

   for key,value in dictionary.items():
       if value > 1:
           ans.append(key)
   return ans


arr= list(map(int,input().split()))

print(repeatingelement(arr))

#15.find all non repeating elements in an array
#exact same code as above but instead of value > 1 we put value  == 1

def repeatingelement(arr):
   dictionary ={}
   ans =[]
   for i in range(len(arr)):
       if arr[i] not in dictionary:
           dictionary[arr[i]] = 1 
       else:
           dictionary[arr[i]] +=1

   for key,value in dictionary.items():
       if value == 1:
           ans.append(key)
   return ans


arr= list(map(int,input().split()))

print(repeatingelement(arr))

#16. Function to find and print all symmetric pairs
def findSymPairs(arr):
    # Dictionary to store pairs
    pair_dict = {}

    # Iterate over the array of pairs
    for i in range(len(arr)):
        first = arr[i][0]
        second = arr[i][1]

        # Check if the symmetric pair exists in the dictionary
        if (second, first) in pair_dict:
            print("(", first, ",", second, ")")
        else:
            # Store the current pair in the dictionary
            pair_dict[(first, second)] = True
#17.Maximum product subarray
#brute force : generate all possible subarray and find max
class Solution:


def maxProduct(self, arr, n):
    result = float('-inf')  

    if n == 1:
        return arr[0]  
    for i in range(n):
        for j in range(i, n):
            product = 1  
            for k in range(i, j+1):
                product *= arr[k]
                result = max(result, product)
    return result 

#optimized 
class Solution:

# Function to find maximum product subarray
def maxProduct(self, arr, n):
    if n == 1:
        return arr[0]

    pre = 1
    suf = 1
    ans = float('-inf')  # Start with negative infinity

    for i in range(n):
        # Reset pre and suf to 1 if they encounter zero
        if pre == 0:
            pre = 1
        if suf == 0:
            suf = 1

        # Calculate prefix and suffix products
        pre *= arr[i]
        suf *= arr[n-i-1]

        # Update the maximum product found so far
        ans = max(ans, pre, suf)

    return ans

#18.Find equlibirium point in an array
def equlibrium(arr):
    n = len(arr)
    for i in range(n):
        leftsum = sum(arr[:i])
        rightsum = sum(arr[i+1:])

        if leftsum == rightsum:
            return i 

    return -1

arr= list(map(int,input().split()))
print(equlibrium(arr))

#19.check if arr2 is subset of arr1 
def isSubset(a1, a2, n, m):
    # Create a frequency dictionary for elements in a1
    d = {}
    for i in a1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    # Check if each element in a2 is present in d with the required frequency
    for i in a2:
        if i not in d or d[i] == 0:
            return "No"
        else:
            d[i] -= 1  # Decrement the count for the element in the dictionary

    return "Yes"

#PROBLEMS ON NUMBERS

#1.palindrome
def palindrome(num):
    num_str = str(num)
    if num_str != num_str[::-1]:  
        return "No"  
    else:
        return "Yes"  

num = int(input())
print(palindrome(num))

#2.sum of digit is palindrome or not
class Solution:
    def isDigitSumPalindrome(self, n):
        sum = 0
        for digit in str(n):
            sum += int(digit)
            string = str(sum)
        if string  == string[::-1]:
            return 1
        else:
            return 0
#3.range of palindrome
def palindrome(n):
    return str(n) == str(n)[::-1]
def rangeof(mini,maxi):
    for i in range(mini,maxi+1):
        if palindrome(i):
            print(i)
mini = int(input())
maxi = int(input())

print(rangeof(mini,maxi))

#4.prime numbers
class Solution:
    def isPrime (self, N):
        if N < 2:
            return 0
        for i in range(2,int(N*0.5)):
            if N % i == 0:
                return 0
        return 1

#5.armstrong number

class Solution:
    def armstrongNumber(self, n):
        ans = 0
        str_n = str(n)
        length = len(str_n)

        for i in str_n:  # Loop through the digits as strings
            ans += int(i) ** length  # Convert the digit back to an integer and raise to the power of length

        if n == ans:  # Compare the original number with the calculated sum
            return "true"
        else:
            return "false"

#6. perfect number
class Solution:
    def isPerfectNumber(self, N):
        ans = 0
        for i in range(1,N//2 +1):
            if N % i == 0:
                ans += i
        if ans == N:
            return 1
        else:
            return 0
#7. sum of n natural number
# formula n(n+1)//2

#8.reverse an number
def reverse_number(num):
    reversed_num = 0

    while num > 0:
        last_digit = num % 10  # Get the last digit
        reversed_num = reversed_num * 10 + last_digit  # Append the last digit to reversed_num
        num = num // 10  # Remove the last digit from num

    return reversed_num

# Example usage:
num = 12345
print(reverse_number(num))  # Output: 54321




# PROBLEMS ON STRINGS

#1.Count number of vowels, consonants, spaces in String

def countCharacterType(str): 
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0 
    for i in range(len(str)):
        
        if ( (ch >= 'a' and ch <= 'z') or
            (ch >= 'A' and ch <= 'Z') ): 
            ch = ch.lower() 

            if (ch == 'a' or ch == 'e' or ch == 'i'
                        or ch == 'o' or ch == 'u'): 
                vowels += 1
            else: 
                consonant += 1

        elif (ch >= '0' and ch <= '9'): 
            digit += 1
        else: 
            specialChar += 1

    print("Vowels:", vowels) 
    print("Consonant:", consonant) 
    print("Digit:", digit) 
    print("Special Character:", specialChar) 

#2.REMOVE ALL VOWELS FROM A STRING
class Solution:
    def removeVowels(self, S):
        N = ''
        for i in range(len(S)):
            if  s[i] not in 'aeiouAEIOU':
                N+=(S[i])
        return N

#3.remove spaces from string

class Solution:
    def modify(self, s):
        N=''
        for i in range(len(s)):
            if s[i] != ' ':
                N+=s[i]
        return N

#4.Remove characters from a string except alphabets
class Solution:
    def modify(self, s):
        N = ''
        for i in range(len(s)):
            if s[i].isalpha():  # Check if the character is an alphabet
                N += s[i]
        return N
 
#5.sum of all numbers in a string
class Solution:
    def findSum(self,s):
        temp = '0'
        sum = 0 
        for i in s:
            if (i.isdigit()):
                temp +=i
            else:
                sum += int(temp)
                temp = '0'

        return sum + int(temp)

#For input "abc123def45ghi6", the program will:

#Extract numbers 123, 45, and 6.
#Calculate 123 + 45 + 6 = 174.

#6.Capitalize first and last character of each word of a string


def capitalize_first_last(s):
    words = s.split()  # Split the string into words
    capitalized_words = []

    for i in words:
        if len(i) > 1:
            i = i[0].upper() + i[1:-1] + i[-1].upper()  
        else:
            i = i.upper()  
        capitalized_words.append(i)

    return ' '.join(capitalized_words)

# 8 .Maximum Occuring Character

class Solution:
    def getMaxOccurringChar(self, s):
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1 

        max_char = ' ' 
        max_count = 0
        for i in d:
            if d[i] > max_count or (d[i] == max_count and i < max_char):
                max_count = d[i]
                max_char = i

        return max_char

#9.  first Non repeating character in a string

class Solution:
    def nonrepeatingCharacter(self,s):
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in s:
            if d[i] == 1:
                return i
        return '$'
# 10.return all non repeating elements in the array

class Solution:

    def nonrepeatingCharacters(self, s):
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        non_repeating = []

        for i in s:
            if d[i] == 1:
                non_repeating.append(i)

        return non_repeating 
# 11.anagram

class Solution:

def isAnagram(self, s, t):
    if len(s) != len(t):
        return -1
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in t:
        if i in d:
            d[i] -= 1
        else:
            return "not anagram"
    for i in d.values():
        if i != 0:
            return "not anagram"

    return "Anagram"

#12.Count common sub-sequence in two strings
#13.Check if two strings match where one string contains wildcard characters

#14.Remove duplicates from a string
def removedupliacate(s):
    seen = set() # hash set
    result = ' '
    for i in s:
        if i not in seen:
            result+=(i)
            seen.add(i)
    return result

s = input()
print(removedupliacate(s))

#15.print all duplicate in a string

def print_duplicates(S):
    d = {}
    for char in S:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    for char, count in d.items():
        if count > 1:
            print(f"{char}, count = {count}") #f is shorthand for formatted string

#14.Remove characters from the first string which are present in the second string

def removeChars(string1, string2):
    for i in string2:
        while i in string1:
            itr = string1.find(i)
            string1 = string1.replace(i, '')

    return string1

#15.Modify the string such that every character gets replaced with the next character 

def next_lexicographic_char(s):
    result = []
    for char in s:
        if char.isalpha():
            if char == 'z':
                result.append('a')
            elif char == 'Z':
                result.append('A')
            else:
                result.append(chr(ord(char) + 1))
        else:
            result.append(char)  # Keep non-alphabet characters unchanged
    return ''.join(result)

#16.Program to find Smallest and Largest Word in a String


def find_smallest_largest_words(sentence):
    words = sentence.split()
    smallest_word = largest_word = words[0]
    for word in words:
        if len(word) < len(smallest_word): 
            smallest_word = word
        if len(word) > len(largest_word): 
            largest_word = word
    return smallest_word, largest_word

#17.sort a string

def sort_characters_in_string(s):
    sorted_string = ''.join(sorted(s))
    return sorted_string





