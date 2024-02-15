## 함수 선언부


## 전역 변수부
katok = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
print(katok)

# 데이터 추가 : 모모에게 1회 카톡 옴
# 1단계 : 빈칸 확보
katok.append(None)
# 2단계 : 마지막 칸에 넣기
katok[5] = '모모'

print(katok)

# !! 데이터 삽입 : 미나에게 연속 40회 카톡 --> 미나를 3등으로.
# 1단계 : 빈칸 확보
katok.append(None)
# 2단계 : 한 칸씩 뒤로 이동 (모모 5등 ~ 사나 3등)
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
katok[3] = "미나"

print(katok)