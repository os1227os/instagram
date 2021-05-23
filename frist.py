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


def remove_list(final,target_list,like_type):
    now = time.strftime('%m월%d일 %H시:%M분')
    if final == "y":
        while True:
            select = input("어떤 목록을 지울까요? (x 입력시 종료)\n")

            if select in target_list:
                print(f"{select} 가 삭제됩니다. \n")
                target_list.remove(select)
                print(f"{select} 삭제 완료.\n")
                print(f"현재 목록 : {target_list}\n")

            elif select == "x":
                if like_type == 2:
                    f = open("tag_list.txt",'a')
                    f.write('\n')
                    f.write(f"{now} : ")
                    f.writelines(','.join(target_list))
                    f.close()
                    break
                f = open("target_list.txt",'a')
                f.write('\n')
                f.write(f"{now} : ")
                f.writelines(','.join(target_list))
                f.close()    
                break
                
            else:
                print("존재 하지 않는 값입니다. 다시 입력해주세요.\n")
                print(target_list,'\n\n')
                
    elif final == "n":
        if like_type == 2:
            f = open("tag_list.txt",'a')
            f.write('\n')
            f.write(f"{now} : ")
            f.writelines(','.join(target_list))
            f.close()
            return
        f = open("target_list.txt",'a')
        f.write('\n')
        f.write(f"{now} : ")
        f.writelines(','.join(target_list))
        f.close()
        return
