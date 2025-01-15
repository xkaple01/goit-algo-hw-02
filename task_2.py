from collections import deque


def check_palindrome(s: str) -> str:
    s: str = s.replace(' ', '').lower()
    if len(s) == 0:
        return 'Please, provide a string with at least 1 non-space character.'
    
    dq: deque = deque()
    
    for c in s:
        dq.appendleft(c)

    while len(dq) > 1:
        c_left: str = dq.popleft()
        c_right: str = dq.pop()
        
        if c_left != c_right:
            return f'Provided string {s} is not a palindrome.'
        
    return f'Provided string {s} is a palindrome.'


if __name__ == '__main__':
    print(check_palindrome(s='abcb'))
    print(check_palindrome(s='abccba'))
    print(check_palindrome(s='abcba'))
    print(check_palindrome(s='a Bba '))
    
    s: str = input('\nEnter an arbitrary string:')
    print(check_palindrome(s=s))
    