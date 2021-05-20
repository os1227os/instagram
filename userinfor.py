def user_information():         # 사용자 입력 함수   
    #username = name         # 사용자 아이디
    #password = pass_word    # 사용자 비밀번호
    userid = driver.find_elements_by_name('username')[0].send_keys(username) # 유저 아이디 
    time.sleep(2.0)                                                          # 아이디 입력후 대기시간
    userpw = driver.find_elements_by_name('password')[0].send_keys(password) # 유저 패스워드
    time.sleep(2.0)                                                          # 비밀번호 입력후 대기시간
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click() # 로그인 버튼 클릭
    #time.sleep(5.0)
    
    if usertime == "y":
        time.sleep(50.0)       #로그인 버튼 누른후 대기시간 ( 2차 비밀번호 인증시간 , 만약 2차 인증이 없다면 5초정도로 줄여도됌 )
        return
    elif usertime == "n":
        time.sleep(5.0)
        return