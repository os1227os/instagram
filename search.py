def tag_search(x):     # 타겟 설정 함수  ( 좋아요반사 태그 )
    searchbar = driver.find_element_by_xpath('//section/nav/div[2]/div/div/div[2]/input') # 검색창 선택
    time.sleep(3.0)
    searchbar.send_keys(f"#{x}")                     # 검색창에 입력할 타겟 입력
    time.sleep(4.0)                            # 검색 대기시간 
    move_id = driver.find_element_by_xpath('//div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div').click() # 타겟 선택 후 클릭
    time.sleep(5.0)                            # 타겟 이동 대기시간
    return


def target_search(x):     # 타겟 설정 함수  ( 외국인 좋아요 )
    time.sleep(3.0)
    searchbar = driver.find_element_by_xpath('//section/nav/div[2]/div/div/div[2]/input') # 검색창 선택
    time.sleep(3.0)
    searchbar.send_keys(x)                     # 검색창에 입력할 타겟 입력
    time.sleep(4.0)                            # 검색 대기시간 
    move_id = driver.find_element_by_xpath('//section/nav/div[2]//div[2]/div[3]//div[2]//div[1]/a//div[2]').click() # 타겟 선택 후 클릭
    time.sleep(5.0)                            # 타겟 이동 대기시간
    return


def scroll_follower (): # 팔로워창 데이터 스크롤
    move_follower = driver.find_element_by_xpath('//section/main//header/section/ul//a').click() # 팔로워 창 선택 클릭
    time.sleep(4.0)        # 대기 시간
    pyautogui.moveTo(815,450, 2) # 스크롤 창으로 이동 상대적 주소라 마우스 가는곳으로 스크롤 창 맞춰줘야함 아니면 원하는곳으로 상대 주소 수정 해야할것
    time.sleep(2.0) # 대기시간
    for i in range(40): # 스크롤 반복 횟수
        pyautogui.scroll(-15, x =815 , y = 450 ) # 15만큼 스크롤
        time.sleep(0.5) # 딜레이 시간 반영##
    driver.back() # 뒷 페이지 이동
    time.sleep(3.0) # 대기시간