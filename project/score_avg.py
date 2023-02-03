with open('./resource/score.txt','r') as f:
    # 1
    # score_lst =list(map(int,f.read().split('\n')))
    # print(sum(score_lst)/len(score_lst))
    
    # 2-1
    contents = f.readlines()
    list_score = [int(i.replace('\n','')) if '\n' in i else int(i) for i in contents]
    print(sum(list_score)/len(list_score))
        # 2-2
        # list_score = []
        #for i in contents:
        #    if '\n' in i:
        #        list_score.append(int(i.replace('\n','')))
        #    else:
        #        list_score.append(int(i))
        #print(sum(list_score)/len(list_score))
    
    
                
    # 3    
    #contents = f.readlines()
    #sum_score = 0
    #for i in range(len(contents)):
    #    sum_score+=int(contents[i])
    #print(sum_score/len(contents))