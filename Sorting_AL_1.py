"""
    
- 알고리즘 개괄 


: 알고리즘은 문제 정의에 필요한 것들을 입력으로 받고, 일련의 변환을 수행하여 결과를 출력.
알고리즘의 좋고 나쁨은 알고리즘 동작의 효율성에 의해서 결정됨. 
또는 알고리즘 수행에 필요한 명령의 개수도 판단에 근거가 될 수 있다

: 알고리즘 수행에 필요한 단계 수를 입력 크기에 대한 함수 형태로 나타낸 것. 
복잡한 알고리즘일수록 입력 크기가 증가함에 따라 급격한 증가세를 보여주며. 
일정 크기 이상의 입력에 대해서는 최신 컴퓨터 시스템을 사용하더라도 실행이 불가능할 수 있다.

:분할 정복 유형의 알고리즘은 주어진 문제를 작은 문제로 나누고, 나눠진 각 부분 문제의 솔루션을 구하고
각 부분 문제 솔루션을 합쳐서 전체 문제에 대한 솔루션을 구하는 방식으로 동작한다.

분할 정복 접근 방법의 핵심 이론은 매우 단순하고 직관적이다. 

(1) 분할: 주어진 문제를 동일한 방식으로 해결할 수 있는 여러 부분 문제로 나눔. 
(2) 정복: 각 부분 문제에 대한 해답을 구한다. 
(3) 결합: 각 부분 문제의 해답을 전체 문제에 대한 해답을 구한다. 


정렬 알고리즘 구현에 필요한 요구 사항은 다음과 같다. 
(1) 모든 데이터 타입에 대해 동작해야 한다. 정수, 실수 등의 자료 형에 모두 사용할 수 있어야 하고
심지어 C++ 구조체 또는 클래스에 대해서도 서로 다른 멤버를 기준으로 정렬할 수 있어야 한다

(2) 정렬 알고리즘은 많은 양의 데이터를 처리할 수 있어야 한다. 
즉, 컴퓨터의 메인 메모리보다 큰 용량의 데이터에 대해서도 동작해야 한다. 
-> 외부 정렬, 즉 컴퓨터의 메인 메모리에 데이터가 상주하지 않은 상태에서 수행되는 정렬을 필요로 함.
외부정렬 알고리즘은 실행 중 임의 시점에서 전체 데이터의 일부만 메모리에 올려놓고 동작할 수 있다.

(3) 정렬 알고리즘은 점근적 시간 복잡도 측면이나 실제 동작 시에 빠르게 동작해야 한다.    
    
    
"""