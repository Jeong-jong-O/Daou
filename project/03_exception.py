# Exception : 예외(코드가 실행 시 발생될 수 있는 문제) -> 개발자가 혼자 해결할 수 있는 문제
            # [참고] error : 시스템 상에서 발생하는 문제 => 개발자가 혼자 해결할 수 없는 문제로, Exception과 다른 부분 존재하나 혼용되는 경우 많음.
    # 예외종류 : Syntax, Type, Name, Index, Indentation, Value, Key, ....
        # SyntaxError : 문법적으로 발생하는 예외
            # Ex) print('python) , a+-*b
        # TypeError : 자료형 타입이 알맞지 않은 연산 시 발생하는 예외
            # Ex) print("string"/2)
        # NameError : 참조변수가 초기화되지 않거나, 존재하지 않을 때 발생하는 예외
            #print(a) -> a에 대한 변수선언 없을 경우 발생하는 NameError
        # IndexError : 존재하지 않는 인덱스를 참조할 때 발생하는 예외
            # a = [1,2,3] ; print(a[4])
        # ValueError : 참조값이 존재하지 않는 경우 발생하는 예외
            # a = [1,2,3] ; print(a.index(0)) or print(a.remove(4))
        # KeyError : 딕셔너리에 존재하지 않는 Key를 이용할 때 발생하는 예외
            # a = {'name':'yb','age':25};  print(a['height']) => print(a.get['height'])시에는 None 출력되며, 예외 발생 X
        # AttributeError : 클래스 및 객체가 보유하지 않은 속성 및 메서드를 사용시 발생하는 예외  
            #import time
            #print(time.month())
        # FileNotFoundError : 존재하지 않는 파일 사용시 발생하는 예외
            # f = open('test.txt','r')
            
    # 예외 처리 : 예외가 발생하더라도, 해당 코드를 제외한 나머지 코드의 실행을 가능하게 함 <- 인터프리터 언어이므로, 앞줄의 수행이 안될 경우 뒷줄도 수행이 안됨.
                # 또한 파일 별로 연관성이 많아질 경우, 발생할 수 있는 오류의 가능성이 높아 예외처리 중요.
'''
        try:
            수행코드
        except(예외명) :
            예외 발생시 수행할 코드
        else :
            try와 except에 해당하지 않을 경우(정상작동할 경우) else 명령문 수행
        finally : 
            무조건 수행하는 코드 
'''

# 예외처리 1
'''
    last_name = ['lee','hong','kim']
    search_name ='kim'
    try :
        idx = last_name.index(search_name)
        print(f'{search_name}은 {idx+1}번째에 위치')
    except ValueError:
        print('검색하신 last name은 존재하지 않습니다.')                        
    except TypeError : 
        print('잘못된 자료형입니다.')
    else :
        print('예외가 발생하지 않았습니다.')
    finally : 
        print('무조건 실행되는 구문입니다.')
'''

# 예외처리 2
'''
    try:
        print('try')
    finally:
        print('finally')
'''

# 예외 처리3 : 'park'을 무조건 찾는 기능 => raise (발생시키는 함수)를 통해 원하는 에러를 발생시킬 수 있음
    # raise 예외명 : 예외를 발생시키는 명령 키워드
    # Exception : 모든 예외를 총칭하는 객체 -> Except 마지막 부분에 사용하는 것이 일반적(먼저 사용할 경우, 특정 예외에 대한 부분이 실행X)
        # 사용자 정의 예외 생성 : 에러에 대한 클래스 생성 후 해당 에러 사용 가능
'''
                class User_difined_Error(Exception):
                    print('사용자 정의 예외 --- ')
'''
             
'''
    try:
        last_name = 'kim'
        if last_name =='park':
            print('park을 찾았습니다.')
        else :
            raise ValueError
    except ValueError:
        print('park을 찾지 못했습니다.')
    except Exception # Exception : 모든 예외를 총칭하는 키워드
        print('ValueError를 제외한 다른 예외가 발생하였습니다.')
'''