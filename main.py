from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import datetime
from selenium.webdriver.common.keys import Keys
import random
import pyautogui
import sys, os





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

def frist_like():   # 첫번쨰 피드 사진 선택 
    frist = driver.find_element_by_xpath("//section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
    time.sleep(random.randrange(3,7))
    return


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

def remove_list(final,target_list,like_type):
    global now
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
   

def user_information():         # 사용자 입력 함수   
    username = 'dae_2l'         # 사용자 아이디
    password = 'FKA1eo2dlf34@#'    # 사용자 비밀번호
    userid = driver.find_elements_by_name('username')[0].send_keys(username) # 유저 아이디 
    time.sleep(2.0)                                                          # 아이디 입력후 대기시간
    userpw = driver.find_elements_by_name('password')[0].send_keys(password) # 유저 패스워드
    time.sleep(2.0)                                                          # 비밀번호 입력후 대기시간
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click() # 로그인 버튼 클릭
    time.sleep(50.0)
    
    '''if usertime == "y":
        time.sleep(50.0)       #로그인 버튼 누른후 대기시간 ( 2차 비밀번호 인증시간 , 만약 2차 인증이 없다면 5초정도로 줄여도됌 )
        return
    elif usertime == "n":
        time.sleep(5.0)
        return
    '''


############################################################################################################
# 작동 코드 
############################################################################################################

target_list = []
tag = []

print("\n==================================")
print("Welcome to automatic like system !! ")
print("==================================\n")

'''
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

'''

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


user_information()              # 유저 정보 입력 
#user_information()

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


