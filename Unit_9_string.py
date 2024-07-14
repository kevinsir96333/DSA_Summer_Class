""" 

Unit_9

문자열에는 생각보다 다양한 기능이 숨겨져 있다. 
먼저 간단하게 파이썬 프롬프트에서 문자열에 Hello, World를 입력해보자

"""

hello = 'Hello, World'
print(hello)



""""

파이썬에서는 ' '나 " "로 문자열을 표현할 수 있다.
// C++에서는 ""를 이용해서 string을 표현하고 ' '를 이용해서 char을 표현한다.
// 파이썬에서는 ' '나 " "로 문자열을 표현할 수 있다.
물론 작은 따옴표 3개나 큰 따옴표 3개를 이용해서 표현할 수 있다. 

"""


hello = '''Hello, World
This is Python
'''

print(hello)


"""

문자열 안에 작은따옴표나 큰따옴표를 포함하고 싶을 때는 어떻게 해야 할까?
이때는 작은 따옴표와 큰따옴표를 사용하는 규칙이 달라진다. 
먼저 '를 넣고 싶다면 문자열을 "로 묶어준다. 이렇게 하면 문자열 안에 '를 넣을 수 있다. 
하지만 작은 따옴표 안에 작은 따옴표를 넣거나 큰 따옴표 안에 큰 따옴표를 넣을 수는 없다.
이 경우 구문 에러가 발생한다

하지만 여러 줄로 된 문자열은 작은 따옴표 안에 작은 따옴표와 큰 따옴표를 둘 다 넣을 수있다. 
또한 큰 따옴표 안에도 작은따옴표와 큰 따옴표를 넣을 수 있다.

"""
singleQuote = """Python's favorite 
food is 
perl
"""

doubleQuote = '"Python is very easy." he says.'

thirdQuote = '''"Python is very easy.

" 
he says.'''

fourthQuote = """Python is 'very easy.'"""

print(singleQuote)
print(doubleQuote)
print(thirdQuote)
print(fourthQuote)


"""

작은 따옴표 안에 작은 따옴표를 쓸 수 있는 방법이 있긴 하다. 그건 \를 붙이면 된다. 
즉 C언어와 같은 방법을 취하는 것이다. 


"""
