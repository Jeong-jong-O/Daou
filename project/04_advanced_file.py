# Excel, CSV(Comma Seperated Values) 등의 파일 다루기

# 미디어 타입 (MIME Type) - https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types 내 Text 파일 내 csv차일
import csv

# CSV1 : comma(,)로 구분된 csv
#with open('./resource/sample1.csv','r') as f : 
#    contents = csv.reader(f)
    #print(contents)    # 객체에 대한 간략한 정보 확인
    #print(dir(contents))   # 객체 내 클래스를 확인하여, 'iter'가 있다는 것을 확인하며 반복을 사용할 수 있다는 것을 확인할 수 있다. => 즉, for문을 통해 한줄씩 읽기 확인
#    next(contents)  # CSV 파일의 다음줄로 커서가 이동한 후 파일을 읽어, 헤더를 읽지 않을 수 있음 
#    for content in contents:
#        print(content)

# CSV2 : bar(|)로 구분된 csv
#with open('./resource/sample2.csv','r') as f : 
#    contents = csv.reader(f,delimiter = '|') # delimiter : 구분자 설정
#    next(contents)  # CSV 파일의 다음줄로 커서가 이동한 후 파일을 읽어, 헤더를 읽지 않을 수 있음 
#    for content in contents:
#        print(content)

# CSV 3 : dict로 구분하여 읽기 => Header에 대한 내용이 key로 읽는 딕셔너리의 형태로 읽음
#with open('./resource/sample1.csv','r') as f : 
#    contents = csv.DictReader(f) 
    #print(contents)    # 객체에 대한 간략한 정보 확인
    #print(dir(contents))   # 객체 내 클래스를 확인하여, 'iter'가 있다는 것을 확인하며 반복을 사용할 수 있다는 것을 확인할 수 있다. => 즉, for문을 통해 한줄씩 읽기 확인
#    for content in contents:
        #print(content)
#        for k, v in content.items():
#            print(k,v)
#        print('----')


# CSV 4 : list => csv
data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#with open('./resource/sample3.csv','w') as f:
#with open('./resource/sample3.csv','w',newline ='') as f:    # newline : '\n'이 기본값으로, 새로운 행을 입력 시 어떻게 입력할 지에 대한 설정 가능 
#    wt = csv.writer(f)
    # print(wt)            # 객체에 대한 간략한 정보 확인
    # print(dir(wt))      # 객체 내 클래스를 확인하여,'writerow'와 'writerows'가 포함되어 있음을 확인할 수 있다.
#    for content in data:
#        wt.writerow(content)   # 한 줄씩 입력
#    wt.writerows(data)  # 리스트 내 요소별로 줄단위로 입력

#for lst in data:
#    for a,b,c in lst:
#        print(a,b,c)
#    for a,b,c in lst:
#        print(a,b,c)


# xlsx, xls 파일 : 
    # 1. pandas
import pandas as pd

#sample = pd.read_excel('./resource/sample.xlsx')
# print(sample.head())
# print(sample.shape)

#sample.to_excel('./resource/result.xlsx')
#sample.to_csv('./resource/result.csv')

    # 2. openpyxl -> 엑셀을 직접 다룰 수 있다는 장점
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = 'daou'
wb.save('openpy.xlsx')
wb.close()  #효율적 메모리 관리를 통해 활성화한  workbook을 닫기