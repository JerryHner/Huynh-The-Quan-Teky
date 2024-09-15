import random

__PATH = "C:/Users/Admin/Desktop/ai_la_ti_phu"

BO_CAU_HOI_FILE_NAME = 'bo_cau_hoi.txt'
CAU_TRA_LOI_FILE_NAME = 'cau_tra_loi.txt'
GIAI_THUONG_FILE_NAME = 'giai_thuong.txt'

BO_CAU_HOI = __PATH + '/' + BO_CAU_HOI_FILE_NAME
CAU_TRA_LOI = __PATH + '/' + CAU_TRA_LOI_FILE_NAME
GIAI_THUONG = __PATH + '/' + GIAI_THUONG_FILE_NAME

with open(BO_CAU_HOI , 'r', encoding='utf-8') as f:
    BO_CAU_HOI_LIST = f.readlines()

with open(CAU_TRA_LOI , 'r', encoding='utf-8') as f:
    CAU_TRA_LOI_LIST = f.readlines()

with open(GIAI_THUONG , 'r', encoding='utf-8') as f:
    GIAI_THUONG_LIST = f.readlines()

vi_tri = random.randint(1, 19)

print(BO_CAU_HOI_LIST[vi_tri])
print(CAU_TRA_LOI_LIST[vi_tri])
print(GIAI_THUONG_LIST[vi_tri])