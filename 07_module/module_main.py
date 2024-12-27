# 공통문제

# our_class.py 모듈을 가져와서
# 강사님 이름과 학생 수를 출력하고
# study() 함수와 lecture() 함수를 호출하고
# 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!

##############################################################################

# case 1: import 구문으로 문제 해결하기

# our_class.py 모듈을 가져와서
# import our_class

# 강사님 이름과 학생 수를 출력하고
# print(our_class.teacher_name, our_class.student_count)

# study() 함수와 lecture() 함수를 호출하고
# our_class.study()
# our_class.lecture()

# 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
# menus = ['한식', '중식', '일식', '양식', '분식']

# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
# print(our_class.go_lunch(menus))

##############################################################################

# case 1-1: import 구문 별칭으로 문제 해결하기

# our_class.py 모듈을 가져와서
# import our_class as oc

# 강사님 이름과 학생 수를 출력하고
# print(oc.teacher_name, oc.student_count)

# study() 함수와 lecture() 함수를 호출하고
# oc.study()
# oc.lecture()

# 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
# menus = ['한식', '중식', '일식', '양식', '분식']

# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
# print(oc.go_lunch(menus))

##############################################################################

# case 2: from - import 구문으로 문제 해결하기

# our_class.py 모듈을 가져와서
# from our_class import teacher_name, student_count, study, lecture, go_lunch

# 강사님 이름과 학생 수를 출력하고
# print(teacher_name, student_count)

# study() 함수와 lecture() 함수를 호출하고
# study()
# lecture()

# 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
# menus = ['한식', '중식', '일식', '양식', '분식']

# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
# print(go_lunch(menus))

##############################################################################

# case 3: 패키지 내의 모듈 import

# official_module.py 모듈은 import로 가져오고고
# our_class_dir.unofficial.unofficial_module.py 모듈은 from - import로 가져와서
import our_class_dir.official.official_module   # as off_md
from our_class_dir.unofficial.unofficial_module import study, go_lunch

# official_module.py 모듈에 내장되어 있는 변수인
# 강사님 이름과 학생 수를 출력하고
print(our_class_dir.official.official_module.teacher_name)
print(our_class_dir.official.official_module.student_count)

# unofficial_module.py 모듈에 있는 study() 함수와
# official_module.py 모듈에 있는 lecture() 함수를 호출하고
study()
our_class_dir.official.official_module.lecture()

# 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
menus = ['한식', '중식', '일식', '양식', '분식']

# unofficial_module.py 모듈에 있는
# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
print(go_lunch(menus))
