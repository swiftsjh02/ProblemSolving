def selfnum(k):
    answer=0
    k=str(k)
    for i in k:
        answer=answer+int(i)
    answer=answer+int(k)
    return(answer)
        



print(selfnum(33))