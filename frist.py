def action_function(x,follower_range):
    global refresh_count
    print(f"\n------------------  타겟 : {x} 시작  --------------------\n")
    target_search(x)     # 타겟 설정
    scroll_follower()
    for number in range(1,follower_range+1):    # 한 계정당 반복 횟수
        move_follower(number)     # 팔로워창 설정
        try:
            feed_like()     # 팔로워 피드 함수
        except: 
            fall_through()  # 좋아요 실패시 함수
    driver.refresh()              # 새로고침 해줘야 새로운 팔로워들이 다시 보이는것 같음 
    refresh_count += 1 
    print(f'---------  다음 타겟으로 넘어가기  < {refresh_count} 번째 > !!!!  --------------\n')
    time.sleep(5.0)               # 페이지 로딩 대기시간
    return



def like_reflection(x,tag_range):
    global tag_like
    print(f"------------- 좋아요 반사 시작 =  태그명 : {x}  --------------------\n")
    tag_search(x)
    frist_like()
    for a in range(0,tag_range+1):
        like_two(x)
        if a == tag_range - 1:
            close = driver.find_element_by_xpath("/html/body/div[5]/div[3]/button/div").click()
            time.sleep(5.0)
            return 


