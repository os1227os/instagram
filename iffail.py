def backpage():
    time.sleep(random.randrange(9,23))        # 반복작업 대기시간
    driver.back()                              # 뒷페이지로 이동
    time.sleep(random.randrange(8,25))        # 반복작업 대기시간
    driver.back()
    time.sleep(random.randrange(7,28))        # 반복작업 대기시간
    driver.back()                              # 뒷페이지로 이동
    time.sleep(random.randrange(10,26))        # 반복작업 대기시간
    return

def fall_through ():                           # 비공개 계정이거나 특수한 상황일때
    global total_like_number                   # 전체 횟수 전역 변수 설정
    global Private_number                      # 실패 횟수 전역 변수 설정
    now = time.strftime('%H시:%M분:%S초')
    total_like_number += 1                     # 전체 진행횟수에 + 1
    Private_number += 1                        # 좋아요 실패 횟수에 + 1
    print(f'< {now} >  =   총 횟수 : {total_like_number}  |  비공개 계정 및 실패 : {Private_number} 개\n') # 전체 진행 상황 안내
    time.sleep(random.randrange(1,6))
    driver.back()                              # 뒷페이지로 이동                            
    time.sleep(random.randrange(1,6))        # 반복작업 대기시간
    driver.back()                              # 뒷페이지로 이동
    time.sleep(random.randrange(1,6))        # 반복작업 대기시간
    return

# 타겟이 만약 두번째에 있을때 
def if_target_second_action_function(x,follower_range):
    global refresh_count
    print(f"\n------------------  타겟 : {x} 시작  --------------------\n")
    searchbar = driver.find_element_by_xpath('//section/nav/div[2]/div/div/div[2]/input') # 검색창 선택
    time.sleep(5.0)
    searchbar.send_keys(x)                     # 검색창에 입력할 타겟 입력
    time.sleep(5.0)                            # 검색 대기시간 
    move_id = driver.find_element_by_xpath('//section/nav/div[2]/div/div/div[2]/div[4]/div/a[2]/div/div[2]').click() # 타겟 선택 후 클릭
    time.sleep(8.0)                            # 타겟 이동 대기시간

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