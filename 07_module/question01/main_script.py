# ### 문제 1: **다람쥐의 팀원 소개 모듈**

# 다람쥐는 대기업에 입사한 후, 팀원들의 역할을 소개하는 프로그램을 작성하려고 합니다. `team_module.py`라는 모듈을 생성하고 이를 사용해 아래 요구사항을 구현하세요.

# 1. **`team_module.py` 내용**:
#     - 함수 `introduce_manager()`: "저는 팀장입니다. 팀을 이끌고 있습니다." 반환
#     - 함수 `introduce_developer()`: "저는 개발자입니다. LLM 서비스를 개발하고 있습니다." 반환
#     - 변수 `company`: "주식회사 SQUIRREL"
# 2. 메인 스크립트에서 `team_module.py`를 불러와 아래와 같이 출력하세요:

# "안녕하세요, 주식회사 SQUIRREL입니다."
# "저는 팀장입니다. 팀을 이끌고 있습니다."
# "저는 개발자입니다. 프로젝트를 개발하고 있습니다."

from team_module import company, introduce_manager, introduce_developer

print(f'안녕하세요, {company}입니다.')
print(introduce_manager())
print(introduce_developer())



# ### 문제 2: **다람쥐의 출퇴근 관리 모듈**

# 다람쥐는 팀원들의 출퇴근 시간을 관리하는 프로그램을 작성하고자 합니다. `attendance_module.py`를 생성하고 이를 사용해 아래 요구사항을 구현하세요.

# 1. **`attendance_module.py` 내용**:
#     - 함수 `record_attendance(name, time)`: "{name}님이 {time}에 출근했습니다." 반환
#     - 함수 `record_leave(name, time)`: "{name}님이 {time}에 퇴근했습니다." 반환
# 2. 메인 스크립트에서 `attendance_module.py`를 불러와 아래와 같이 출력하세요:

# "다람쥐님이 9:00에 출근했습니다."
# "다람쥐님이 18:00에 퇴근했습니다."

from attendance_module import record_attendance, record_leave

print(record_attendance('다람쥐', '09:00'))
print(record_leave('다람쥐', '18:00'))



# ### 문제 3: **다람쥐의 업무 진행 모듈**

# 다람쥐는 팀에서 업무 진행 상황을 기록하는 프로그램을 작성하려 합니다. `task_module.py`를 생성하고 이를 사용해 아래 요구사항을 구현하세요.

# 1. **`task_module.py` 내용**:
#     - 함수 `start_task(task_name)`: "작업 '{task_name}'이(가) 시작되었습니다." 반환
#     - 함수 `complete_task(task_name)`: "작업 '{task_name}'이(가) 완료되었습니다." 반환
# 2. 메인 스크립트에서 `task_module.py`를 불러와 아래와 같이 출력하세요:

# "작업 '코드 리뷰'이(가) 시작되었습니다."
# "작업 '코드 리뷰'이(가) 완료되었습니다."

from task_module import start_task, complete_task

task_name = '코드 리뷰'

print(start_task(task_name))
print(complete_task(task_name))



# ### 문제 4: **내장 모듈을 활용한 다람쥐의 업무 효율성 계산**

# 다람쥐는 자신의 업무 효율성을 계산하려고 합니다. `math` 모듈을 사용하여 아래 요구사항을 구현하세요.

# 1. 매일 처리한 업무량을 기록한 배열이 [10, 12, 8, 15, 9]라면 평균 업무량을 출력하세요.
# 2. 평균 업무량보다 많이 처리한 날의 개수를 계산하세요.

import math

works = [10, 12, 8, 15, 9]
works_avg = sum(works) / len(works)
print(f'평균 업무량: {works_avg}')

works_avg = math.ceil(works_avg)
print(f'평균 업무량: {works_avg}')

works_avg = math.floor(works_avg)
print(f'평균 업무량: {works_avg}')

count = 0
for works_time in works:
    if works_time > works_avg:
        count += 1
# count = sum(1 for works_time in works if works_time > works_avg)

print(f'평균 업무량보다 많이 처리한 날: {count}')



# ### 문제 5: **내장 모듈을 활용한 다람쥐의 업무 보고서 작성**

# 다람쥐는 팀원의 업무 보고서를 작성하려고 합니다. `datetime` 모듈을 사용하여 현재 날짜와 시간을 포함한 보고서를 생성하세요.

# 1. 현재 날짜와 시간. 팀원 이름과 작업 내용을 출력하세요.

# [2024-12-24 08:55:31] 다람쥐님이 작업 '코드 리뷰'을(를) 완료했습니다.

from datetime import datetime

# 현재 날짜와 시간 출력
print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 다람쥐님이 작업 '코드 리뷰'을(를) 완료했습니다.")
