from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import datetime
from selenium.webdriver.common.keys import Keys
import random
import pyautogui
import sys, os
from userinfor import user_information
from search import tag_search, target_search, scroll_follower
from select_follower import move_follower
from feed_like import frist_like 
from like_two import nextpage, like_two
from iffail import backpage, fall_through, if_target_second_action_function
from target_feed import feed_like
from frist import action_function, like_reflection, remove_list






# 완료후 결과 작성 및 프로그램 종료


# 인스타그램 자동 좋아요 코드 


'''

시작에 앞서 import 되어 있는건 pipenv 를 이용해 설치해주어야하며 전원을 껏다키거나
비주얼 스튜디오를 껏다 켯을 경우엔 꼭 pipenv shell 을 사용해 가상환경 안으로 들어와야한다


1. 아이디와 비밀번호를 입력 ( username, password 에 입력 "" 대괄호안에 써야함 지우면 작동 안됌 )
2. 가장 중요한건 계정의 안전성이기 때문에 천천히 동작되도록 설계함 ( 원한다면 속도 조절 가능 하지만 비추 )
3. 두가지 타겟을 번갈아가며 좋아요를 누르는 원리 ( 원한다면 타겟을 더 추가해도 됌)
4. 동작을 멈추려면 터미널에 CONTROL + C 
5. 실행 하려면 터미널에 python main.py 입력
6. 아마 동작중에는 어플로 인스타그램 접속이 안되긴 할텐데 동작중에는 다른 경로를 통해 접속하지 않는걸 적극 권장
7. 프로그램 정지후에 바로 접속하지 않고 30분 정도 텀을 주고 접속 권장 ( 계정 안전을위한 개인적 생각 )
8. 창 최소화 말고 그냥 열어두고 다른거 해도 동작함 최소화 시키는건 안하는게 좋아보임

'''

   

############################################################################################################
# 작동 코드 
############################################################################################################

target_list = []
tag = []

print("\n==================================")
print("Welcome to automatic like system !! ")
print("==================================\n")


while True:
    name = input("사용할 아이디를 입력하세요 : \n")
    i = input(f"입력한 아이디가 {name} 이 맞습니까? (맞으면 y , 아니면 n )\n")
    if i == "y":
        break
    elif i == "n":
        continue
    else: print("y 또는 n 만 입력 가능합니다. ( 대소문자 구분 )\n")

while True:
    pass_word = input("사용할 비밀번호를 입력하세요 : \n")
    p = input(f"입력한 비밀번호가 {pass_word} 가 맞습니까? (맞으면 y , 아니면 n )\n")
    if p == "y":
        break
    elif p == "n":
        continue
    else:
        print("y 또는 n 만 입력 가능합니다. ( 대소문자 구분 )\n")

while True:
    bouns_count = 0
    usertime = input("2차 비밀번호 인증 시간이 필요합니까? (맞으면 y , 아니면 n )\n")
    print("참고 : y 선택시 50초 대기시간 , n 선택시 5초 대기시간 적용 !\n\n")
    if bouns_count == 0 and usertime == "y":
        print("2차 비밀번호 인증 대시기간이 적용 되었습니다. \n")
        break
    elif bouns_count == 0 and usertime == "n":
        print("2차 비밀번호 인증 대기시간이 적용 되지 않았습니다. \n")
        break
    elif usertime != "y" and usertime != "n":
        print("y 또는 n 만 입력 가능합니다. ( 대소문자 구분 )\n\n")
        bouns_count += 1
     
print("\n 아이디와 비밀번호가 입력 되었습니다 ! 작업할 종류를 선택해주세요.  \n")


while True:
    like_type = int(input("1. 팔로워 좋아요 작업    2. 좋아요 반사      3. 둘 다 하기 \n"))
    if like_type == 1 or like_type == 2 or like_type == 3:
        if like_type == 1:
            print("1. 팔로워 좋아요 작업을 선택하셨습니다. \n")
            while True:
                follower_range = input("한 타겟당 몇번 반복 하시겠습니까 ?\n")
                try:
                    follower_range = int(follower_range)
                    print(f"타겟당 {follower_range}번 반복합니다. \n")
                    break
                except:
                    print("숫자만 입력해주세요. \n")
            while True:
                print(f"현재 타겟 목록 : {target_list}\n")
                target_append = input("팔로워 작업할 사람 추가 : (종료시 x 입력)\n")
                if target_append == "x":
                    final = input("삭제 하고 싶은 목록이 있습니까? (있으면 y , 없으면 n)\n")
                    remove_list(final,target_list,like_type)
                    break
                else:
                    target_list.append(target_append)

        elif like_type == 2:
            print("2. 좋아요 반사 작업을 선택하셨습니다. \n")
            while True:
                tag_range = input("한 태그당 몇번 반복 하시겠습니까 ?\n")
                try:
                    tag_range = int(tag_range)
                    print(f"타겟당 {tag_range}번 반복합니다. \n")
                    break
                except:
                    print("숫자만 입력해주세요. \n")
            while True:
                print(f"현재 태그 추가 목록 : {tag}\n")
                append_tag = input("좋아요 작업 할 태그 추가 : (종료시 x 입력)\n")
                if append_tag == "x":
                    final = input("삭제 하고 싶은 목록이 있습니까? (있으면 y , 없으면 n)\n")
                    remove_list(final,tag,like_type)
                    break
                else:
                    tag.append(append_tag)

        elif like_type == 3:
            print(" 3. 둘 다 하기를 선택하셨습니다. \n")
            time.sleep(1.0)
            print("팔로워 좋아요 작업 할 타겟 먼저 추가 하겠습니다 . \n\n")
            while True:
                follower_range = input("한 타겟당 몇번 반복 하시겠습니까 ?\n")
                try:
                    follower_range = int(follower_range)
                    print(f"타겟당 {follower_range}번 반복합니다. \n")
                    break
                except:
                    print("숫자만 입력해주세요. \n")
            while True:
                print(f"현재 타겟 목록 : {target_list}\n")
                target_append = input("팔로워 작업할 사람 추가 : (종료시 x 입력)\n")
                if target_append == "x":
                    final = input("삭제 하고 싶은 목록이 있습니까? (있으면 y , 없으면 n)\n")
                    remove_list(final,target_list,like_type)
                    break
                else:
                    target_list.append(target_append)      
            print("\n\n좋아요 반사할 태그도 추가 하겠습니다. \n\n")

            while True:
                tag_range = input("한 태그당 몇번 반복 하시겠습니까 ?\n")
                try:
                    tag_range = int(tag_range)
                    print(f"타겟당 {tag_range}번 반복합니다. \n")
                    break
                except:
                    print("숫자만 입력해주세요. \n")
            while True:
                print(f"현재 태그 추가 목록 : {tag}\n")
                append_tag = input("좋아요 작업 할 태그 추가 : (종료시 x 입력)\n")
                if append_tag == "x":
                    final = input("삭제 하고 싶은 목록이 있습니까? (있으면 y , 없으면 n)\n")
                    now = time.strftime('%m월%d일 %H시:%M분')
                    if final == "y":
                        while True:
                            select = input("어떤 목록을 지울까요? (x 입력시 종료)\n")
                            if select in tag:
                                print(f"{select} 가 삭제됩니다. \n")
                                tag_list.remove(select)
                                print(f"{select} 삭제 완료.\n")
                                print(f"현재 목록 : {tag}\n")
                            elif select == "x":
                                f = open("tag_list.txt",'a')
                                f.write('\n')
                                f.write(f"{now} : ")
                                f.writelines(','.join(tag))
                                f.close()    
                                break            
                            else:
                                print("존재 하지 않는 값입니다. 다시 입력해주세요.\n")
                                print(tag,'\n\n')
                    elif final == "n":
                        f = open("tag_list.txt",'a')
                        f.write('\n')
                        f.write(f"{now} : ")
                        f.writelines(','.join(tag))
                        f.close()
                    break
                else:
                    tag.append(append_tag)           
        break
    else:
        continue

computer_end = input("모든 준비가 완료 됐습니다 . 작업 후 컴퓨터를 종료 하시겠습니까 ? ( 종료하려면 y , 종료하지 않으려면 n )\n")
while True:
    if computer_end == "y" or computer_end == "n":
        if computer_end == "y":
            print("작업 종료후 컴퓨터를 종료하겠습니다 . 이제 작업을 시작합니다 . \n")
            break
        else:
            print("작업 후 컴퓨터를 종료하지 않겠습니다. 이제 작업을 시작합니다 . \n")
            break
            
    else:
        computer_end = input("y 또는 n 만 입력 가능합니다 . \n")





url = 'https://www.instagram.com/'    # 인스타 그램 주소 

driver = webdriver.Chrome(ChromeDriverManager().install())    # 구글 크롬 드라이버 연동 매니저

driver.get(url)   # 사이트 열기 

time.sleep(3.0)   # 로딩 대기시간

driver.set_window_size(1200, 977) # 창 크기 조절

time.sleep(3.0)

like = "//article//section/span/button"   # 좋아요 버튼 소스

total_like_number = 0       # 좋아요 누르는 전체 시도 횟수
success_like_number = 0     # 실제 좋아요 누른 횟수
Private_number = 0          # 비공개 계정 갯수 (좋아요 못누른 횟수)
count = 0                   # 사람 선택용 카운트
refresh_count = 0           # 새로고침 카운트 
tag_like  = 0               # 태그 좋아요 갯수


#user_information(name,pass_word,usertime)              # 유저 정보 입력 
user_information()

try:
    time.sleep(5.0)
    first = driver.find_element_by_xpath('//div/div/div/div[3]/button[2]').click()
    time.sleep(3.0)
    # 팔로워 작업
    if like_type == 1:
        for x in target_list:
            now = time.strftime('%H시:%M분:%S초')
            action_function(x,follower_range)

    # 좋아요 반사 작업
    elif like_type == 2:
        for i in range(len(tag)):
            for x in tag:
                like_reflection(x,tag_range)

    # 좋아요 반사 후 팔로워 작업
    elif like_type == 3:
        for i in range(len(tag)):
            for x in tag:
                like_reflection(x,tag_range)

        for x in target_list:
            now = time.strftime('%H시:%M분:%S초')
            action_function(x,follower_range)

except:
    # 팔로워 작업
    if like_type == 1:
        for x in target_list:
            now = time.strftime('%H시:%M분:%S초')
            action_function(x,follower_range)

    # 좋아요 반사 작업
    elif like_type == 2:
        for i in range(len(tag)):
            for x in tag:
                like_reflection(x,tag_range)

    # 좋아요 반사 후 팔로워 작업
    elif like_type == 3:
        for i in range(len(tag)):
            for x in tag:
                like_reflection(x,tag_range)

        for x in target_list:
            now = time.strftime('%H시:%M분:%S초')
            action_function(x,follower_range)


all_result = [total_like_number,success_like_number,Private_number,tag_like] 
result_list = ["total", "success", "fail", "tagsuccess"]

now = time.strftime('%H시:%M분:%S초')



result = open("like_result.txt",'a')
result.write('\n')
result.write(f"{now} : ")
result.writelines(','.join(result_list))
result.write('\n')
result.write(f"{now} : ")
result.writelines(','.join(map(str,all_result)))
result.close()


print("모든 작업이 완료되었습니다 .\n")
if computer_end == "y":
    print("작업 완료후 컴퓨터 종료를 선택하셨습니다 . 3초뒤 컴퓨터를 종료합니다 .\n")
    for i in range(3,0,-1):
        print(i)
        time.sleep(1.0)
    print("\n안녕.")
    os.system("shutdown -s")


############################################################################################################

############################################################################################################


