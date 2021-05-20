def frist_like():   # 첫번쨰 피드 사진 선택 
    frist = driver.find_element_by_xpath("//section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
    time.sleep(random.randrange(3,7))
    return

