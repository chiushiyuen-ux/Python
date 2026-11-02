'''Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.'''

s=input()

have={}
left=0
#len_lst=[]
max_len=0
if s==0:
    print(0)
for right in range(len(s)):  # right is scanning every character
    char=str(s[right])
    if char in have and have[char]>=left:
        left=have[char]+1  #just left count from where the duplicated character was found
    have[char]=right
    current_length=right-left+1
    max_len=max(max_len, current_length)
    
    #len_lst.append(right-left+1)
#print(max(len_lst))

print(max_len)