def computepay(hours, rate):
    # print("네가 입력한거", hours, rate)
    if hours > 40 :
        req = rate * hours # 정량시간에 대한 계산
        otp = (hours - 40.0) * (rate*1.5) 
        pay = reg + otp
    else:
        pay  = hours * rate
    return pay

    
sh = input("몇시간?: ")
sr = input("참여율?: ")

fh = float(sh) # 실수형으로 변환
fr = float(sr)


xp = computepay(fh, fr)

print("너의 급여는: ", xp)
