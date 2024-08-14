#这是该项目的集成库，共有函数会被移动到此

def extract_classroom_info(classroom_name):
    """
    从教室名称中提取楼号、层号和序号。
    参数:classroom_name (str): 教室名称，格式如 "H2102"
    返回:tuple: 楼号 层号 序号
    """
    building_number = classroom_name[1]  # 楼号
    floor_number = classroom_name[2]     # 层号
    sequence_number = classroom_name[3:] # 序号
    return building_number, floor_number, sequence_number

# 测试函数
#test_name = "H2102"
#extract_classroom_info(test_name)