# 导入所需的库
import pandas as pd
import re
from functools import reduce

# 定义一个函数，用于处理CSV文件并提取教室信息
def extract_classroom_info(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path, engine='python',header=None)#忽略头
    # 初始化一个字典来存储教室信息
    classroom_info = {}

    #提取时间
    course_week = df.iloc[0, 1:].tolist()
    course_time = df.iloc[1, 1:].tolist()
    # 提取教室名称，第一列是教室名称
    classroom_names = df.iloc[2:, 0].tolist()
    #print(classroom_names)
    
    classroom_info = {}
    for classroom_index, classroom in enumerate(classroom_names):#迭代每一个教室
        classroom_info[classroom] = [] # 初始化键值对，值是列表
        classroom_data = df.iloc[classroom_index+2, 1:].tolist() # 抽出对应的行信息
        #print(classroom_data)
        for index, course in enumerate(classroom_data):#迭代每一个时间段看看有没有课
            if pd.isna(course) == False:
                #classroom_info[classroom].append([course_week[index],course_time[index], course])#把课程信息添加到教室键
                classroom_info[classroom].append([course_week[index],course_time[index], get_UseWeek(course)])#把占用信息提取出来添加到教室键
    return classroom_info

def get_UseWeek(text):
    # 使用正则表达式查找所有匹配的模式
    matches = re.findall(r'\[(\d+)-(\d+)\]', text)
    # 提取数字并放入列表
    return [tuple(map(int, match)) for match in matches]
    #这里有bug，同一时间段有多个课程不同周时概率只能识别第一个，检查表达式的适配
    #0613 debug中

def find_available_classrooms(data, week, day, period):
    available_classrooms = []

    for classroom, schedule in data.items():#拿出来依次比较每个信息
        is_available = True
        for entry in schedule:
            if entry[0] == day and entry[1] == period:
                for week_range in entry[2]:
                    if week_range[0] <= week <= week_range[1]:
                        is_available = False
                        break
                if not is_available:
                    break
        if is_available:
            available_classrooms.append(classroom)
    return available_classrooms

def find_UseableClassroom(data, week, day, start_lesson, end_lesson):#似乎有bug
    classroom = []
    for lesson in range(start_lesson, end_lesson):
        classroom.append(set(find_available_classrooms(data, week, day, str(lesson))))
    #print(classroom)

    common_room = reduce(lambda s1, s2: s1.intersection(s2), classroom).difference(roomblacklist)
    print(common_room)
    return classroom

roomblacklist = set(['第二篮球场1', '第二田径场1', '健身房', '第二篮球场3', '第二篮球场4', '台球室', '健美操房1', 
                    '健美操房2','羽毛球场3', '排球场1', '羽毛球场1', '乒乓球场1', '跆拳道馆1', '网球场1', '网球场2',
                    '第一田径场1', '棋牌室', '武术馆', '排球场2', '乒乓球场2', '跆拳道馆2', '羽毛球场2', '瑜伽馆1',
                    '乒乓球场3', '第二篮球场2', '瑜伽馆2'])#黑名单房间，不会出现在可行列表里
# 调用函数并处理CSV文件
classroom_info = extract_classroom_info('./2501course_tableAll.csv')
find_UseableClassroom(classroom_info, 3, '星期四', 5, 8)
print(classroom_info['H4112'])
#print(find_available_classrooms(classroom_info, 1, '星期四', '6'))
#print(classroom_info['第二篮球场1'])