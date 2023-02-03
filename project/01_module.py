# 모듈 : 기능 단위로 구분되어진 파일 뭉치 > 일반 파일처럼 .py의 확장자를 가졌으며, 해당 파일의 함수를 불러오는 형식
# 패키지 : 모듈을 모아둔 디렉터리
# pip install 모듈명 : 해당 모듈을 설치
# 모듈 경로 확인  : import inspect -> import random -> print(inspect.getfile(random))

# 모듈 사용 예시 1(클래스) => '클래스.함수'를 이용
from pkg.Calculator import Calculator as cal
print(cal.plus(1,2))

# 모듈 사용 예시 2(함수) => 그냥 함수 이용
from pkg.calculator2 import plus as pl
print(pl(1,2))

# 모듈 사용 예시 3 - 기본 내장 모듈 이용
import builtins
print(dir(builtins))

