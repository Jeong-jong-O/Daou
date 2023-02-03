####################
# Python - DB 연결 #
####################

# pymysql 설치 : pip install pymysql
import pymysql

# SQL 실행 절차
# 1. Python과 MySQL 연결해 데이터 베이스에 접속(host,  User,  계정에 대한 Password, 사용할 DB(스키마),  ... 등의 정보가 필요)
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'scott',
                       charset = 'utf8'
                       ) #localhost ; 나 자신의 서버 / charset : 문자열에 대한 인코딩 방식

print(conn)

# 2. DB 내 커서(cursor ; 작업을 수행하고 결과값을 보유하는 객체) 생성
cur = conn.cursor()
print(cur)

# 3. SELECT/DML 등의 명령 수행 -> COMMIT, ROLLBACK 등의 작업 동반
# Ex) deptno = 10인 사원들의 모든 정보 출력
    # 3-1 . SELECT
        # dept_no = input()
        # sql_1 = f'select * from emp where deptno ={dept_no}'
        # cur.execute(sql_1)

        # for record in cur : 
        #     print(type(record))
        #     print(record[0])    # 부서번호
        #     print(record[:2])   # 부서번호, 이름

    # 3-2. INSERT : (50, PROGRAMMING, SUJI)를 삽입
        # 3-2-1 . 직접 값 입력
            # sql_insert = 'INSERT INTO dept(deptno,dname,loc) VALUES(50, \'Programming\', \'Suji\')'
            # cur.execute(sql_insert)-
            # conn.commit()

        # 변수명으로 값을 전달받아 입력
            # sql_insert_2 = 'INSERT INTO dept(deptno,dname,loc) VALUES(%s, %s, %s)'
            # dept_no = input('>>부서 번호를 입력하세요 : ')
            # dname = input('>>부서명을 입력하세요 : ')
            # loc = input('>>부서 위치를 입력하세요 : ')
            # new_values = (dept_no, dname, loc)
            # cur.execute(sql_insert_2, new_values)
            # conn.commit()

    # 명령 결과값 확인
        # sql_insert_check = 'SELECT * FROM dept'
        # cur.execute(sql_insert_check)

        # print(list(cur)[-1])

# 4. 연결 해제 - close
conn.close()

