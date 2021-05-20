def nextpage():
    time.sleep(random.randrange(9,15))        # 반복작업 대기시간
    next = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
    time.sleep(random.randrange(4,14))
    next = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
    time.sleep(random.randrange(5,12))
    return



def like_two(x):
    global tag_like 
    now = time.strftime('%H시:%M분:%S초')
    try:
        like_condition = driver.find_element_by_xpath("//article/div[3]/section[1]/span[1]/button/div/span//*[name() = 'svg']")
        like_condition_result = like_condition.get_attribute("aria-label")
        if like_condition_result == "좋아요 취소":
            print('----------- 이미 좋아요를 누른 사진입니다 !! --------------')
            print()
            print()
            nextpage()
            return
        like_it = driver.find_elements_by_xpath(like)
        time.sleep(random.randrange(10,18))
        like_it[0].click()
        tag_like += 1
        print(f"< {now} > : '{x}' 의 총 작업 개수 : {tag_like} 개 입니다 !! ")
        print()
        if tag_like > 1 and tag_like  % 2 == 0:
            print(f"{x}의 최신 게시물을 다시 불러오겠습니다. ")
            print()
            close = driver.find_element_by_xpath("/html/body/div[5]/div[3]/button/div").click()
            time.sleep(2.0)
            driver.refresh()
            time.sleep(10.0)
            frist_like()                
            return
        nextpage()
        return
    except:
        print("페이지 로딩이 길어지는것 같습니다 다음 사진으로 넘어갑니다 !")
        time.sleep(random.randrange(5,12))        # 반복작업 대기시간
        next = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
        time.sleep(random.randrange(6,13))
        return

