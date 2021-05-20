def move_follower(number):    # 팔로워 누르는 함수
    try:
        move_follower = driver.find_element_by_xpath('//section/main//header/section/ul//a').click() # 팔로워 창 선택 클릭
    except:
        driver.back()
        time.sleep(7.0)
        move_follower = driver.find_element_by_xpath('//section/main//header/section/ul//a').click() # 팔로워 창 선택 클릭
    time.sleep(random.randrange(10,25))        # 반복 작업은 대기시간 길게 두어서 의심 안받게 함
    
    try:
        try:
            driver.find_element_by_xpath('//div//ul/div/li[{0}]//span/a'.format(number)).click() #  팔로워들 누르는 반복적 작업
            time.sleep(random.randrange(9,22))        # 반복 작업은 대기시간 길게 두어서 의심 안받게 함
        except:
            move_follower = driver.find_element_by_xpath('//section/main//header/section/ul//a').click() # 팔로워 창 선택 클릭
            time.sleep(6.0)        # 대기 시간
            driver.find_element_by_xpath('//div//ul/div/li[{0}]//span/a'.format(number)).click() #  팔로워들 누르는 반복적 작업
            time.sleep(random.randrange(9,22))
    except:
        time.sleep(5.0)
        pyautogui.moveTo(815,450, 2) # 스크롤 창으로 이동 상대적 주소라 마우스 가는곳으로 스크롤 창 맞춰줘야함 아니면 원하는곳으로 상대 주소 수정 해야할것
        time.sleep(3.0) # 대기시간
        for i in range(40): # 스크롤 반복 횟수
            pyautogui.scroll(-15, x =815 , y = 450 ) # 15만큼 스크롤
            time.sleep(0.5) # 딜레이 시간 반영##
        driver.find_element_by_xpath('//div//ul/div/li[{0}]//span/a'.format(number)).click() #  팔로워들 누르는 반복적 작업
        time.sleep(random.randrange(9,22))        # 반복 작업은 대기시간 길게 두어서 의심 안받게 함
