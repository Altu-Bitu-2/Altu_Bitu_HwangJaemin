# 3613: Java vs C++

'''
<문제 분석>
Java 형식 변수 이름은 C++ 형식으로, C++ 형식 변수 이름은 Java 형식으로 변경
'Error!'이 출력되는 경우
- 알파벳 소문자로 시작하지 않음(Java, C++ 공통)
- 언더바가 등장(Java)
- 언더바가 연속해서 등장(C++)
- 대문자가 등장(C++)
* 입력으로 주어진 경우가 두 형식 모두 부합하는 경우도 있음

<코드 구조 설계>
파이썬에서 string은 변경이 불가능한 객체이기 때문에 단어에 포함된 원소를 따로
저장해서 결과값을 만들어야 함


'''


import sys # sys 불러옴
input = sys.stdin.readline # 가독성을 위해 input에 대입


def to_cpp(word): # cpp 형식으로 바꾸는 함수
    result = "" # 결과 저장을 위한 변수

    for c in word: # 입력받은 단어에 들어있는 원소들에 대해서
        if c == c.upper(): # 원소가 대문자라면
            result += '_' # result에 언더바 추가
        result += c.lower() # 원소를 소문자로 바꾸어서 result에 넣음
    
    return result # 결과값 반환

def to_java_if_possible(word_list): # 가능하면 java형식으로 바꾸는 함수
    result = [] # 결과 저장을 위한 리스트
    for word in word_list: # 입력받은 단어에 들어있는 원소들에 대해
        if len(word) == 0 or word != word.lower(): # 원소중에 대문자가 있거나 띄어쓴 부분이 있을 경우
            return "Error!" # 에러 출력
        result.append(word.capitalize()) # 문자열 첫글자만 대문자로 바꾸어서 result 리스트에 집어넣음

    result[0] = result[0].lower() # 첫 단어는 capitalize하면 안됨
    return ''.join(result) # 결과 출력

# 입력
word = input().rstrip() # 변수명 입력받음


if (not word[0].isalpha()) or word[0] == word[0].upper(): # 공통 예외에 포함되는 경우
    print("Error!") # 에러 출력
elif word.isalpha():    # Java식 변수인 경우
    print(to_cpp(word)) # 결과 출력
else:   # 나머지 경우 (error || cpp식 변수)
    word_list = word.split('_') # word_list에 결과 대입
    print(to_java_if_possible(word_list)) # 결과 출력 
