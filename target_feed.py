def feed_like():      # 팔로워 피드에 들어가서 누르는 함수 설정
    global total_like_number                   # 전체 횟수 전역 변수 설정
    global success_like_number                 # 성공 횟수 전역 변수 설정
    global Private_number                      # 실패 횟수 전역 변수 설정
    now = time.strftime('%H시:%M분:%S초')
    now_follow_data = driver.find_element_by_xpath("//button[contains(text(),'팔로우')]")
    if now_follow_data.text == "맞팔로우 하기":
        print(' ------------ 이미 나를 팔로우하는 사람입니다 !! ------------------\n\n')
        fall_through()
        return
        
    else:
        try:
            following = driver.find_element_by_xpath("//section/main/div/header/section/ul/li[3]/a/span")
        except:
            following = driver.find_element_by_xpath("//section/main/div/header/section/ul/li[3]/span/span")
        follow_data = following.text
        follow_data = int(follow_data.replace(',',''))
        print(f"< {now} >  =   타겟 팔로잉 데이터 : {follow_data}  \n")
        if follow_data > 1000:
            print(f"-------  이사람은 팔로잉 하고 있는 사람이 {follow_data} 명이 넘습니다 !!  ---------- \n\n")
            fall_through()
            return 
            

        else :
            feed = driver.find_elements_by_xpath('//section/main//article//div[1]/a/div')[0].click() # 첫번째 사진 클릭
            time.sleep(5.0)
            like_condition = driver.find_element_by_xpath("//article/div[3]/section[1]/span[1]/button/div/span//*[name() = 'svg']")
            like_condition_result = like_condition.get_attribute("aria-label")
            if like_condition_result == "좋아요 취소":
                print('----------------- 이미 좋아요를 누른 사진입니다 !! ----------------------\n\n')
                backpage()
                return 
            time.sleep(random.randrange(10,20))        # 반복작업 대기시간
            like_it = driver.find_elements_by_xpath(like) # 좋아요 누르는 버튼
            time.sleep(random.randrange(8,19))        # 반복작업 대기시간
            like_it[0].click()                         # 좋아요 버튼 클릭
            total_like_number += 1                     # 전체 시도 횟수에 + 1 
            success_like_number += 1                   # 좋아요 성공 횟수에 + 1
            print(f'< {now} >  =   총 횟수 : {total_like_number}  |  좋아요 성공 :{success_like_number} 개\n') # 진행상황 안내
            backpage()
            return
    