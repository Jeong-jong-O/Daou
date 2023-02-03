# 파일 읽기, 쓰기

# 파일 모드
    # r : 읽기
    # w : 쓰기
    # a : (add)파일이 존재하지 않으면, 바로 뒤에 쓰기 또는 덧붙이기

# 파일 읽기 1 - open
    # open  : 파일을 특정 모드로 사용
f = open('./resource/python.txt','r')
#print(f)
    # read : 전체 내용 확인 및 읽기
contents = f.read()
#print(contents)
f.close()   # 자원에 대한 사용을 멈춰, 효율적인 메모리 관리를 수행하여야 함

# 파일 읽기 2 - with =>  autoclose를 지원하여, open하였던 파일을 자동으로 닫아 효율적인 메모리 관리 가능
with open('./resource/python.txt','r') as f:
    contents = f.readlines()        #readlines : 모든 줄을 읽어 한줄씩 리스트로 받아들이기(개행문자 포함) / readline : 한 줄 한 줄 읽기 / read : 모든 줄을 읽어 한 줄에 개행문자와 함께 받아들이기
    #print('>>>',contents)
    contents = f.read()
    #print('>>>',contents)
    #print(contents)
    #print(list(contents))   #개행문자를 포함하여, 모두 한 글자씩 끊어 리스트화
    

# 파일 읽기 3 - readlines() : 전체 내용을 읽은 뒤에, 라인 단위로 리스트로 저장
with open('./resource/python.txt','r') as f:
    contents = f.readlines()
    #print('>>>',contents)
    for content in contents:
        print(content,end = '')


# 파일 쓰기1 - write() 파일 생성
with open('./resource/info.txt','a') as f:  # 실제로 존재하지 않은 파일명 작성후 쓰기 모드로 작성
    f.write('\n nice day!')
     
# 파일 쓰기2 - writelines() : 라인을 기준으로 저장
with open('./resource/info2.txt','a') as f:  
    f.writelines('nice day!\nnice day!\nnice day!\n')
    f.writelines(['park\n','lee\n','hong\n'])

# 파일 쓰기3 - print 내 file 옵션 : 작성 후 파일로 바로 저장
with open('./resource/info3.txt','w') as f:
    print('freedom',file = f)

#- - - - - - - - - - - - -
    # 파일 읽고 평균 작성
    with open('./resource/score.txt','r') as score:
        score_lst = score.readlines()
        print(score)
        #print(sum(scores)/len(scores))