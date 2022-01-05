while True :
    try :
        a = input()
        print(a)
    except EOFError : #입력이 없어 오류뜰시(EOFError) except
        break