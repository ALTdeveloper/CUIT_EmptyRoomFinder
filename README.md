# CUIT_EmptyRoomFinder

输入时间查询当前无课教室

你是不是还在为简陋的教务处查询功能感到烦恼？现在可以通过将教务处中的课表提取为csv文件，再对csv文件实现反向查询，快速找到没人上课的教室啦！

使用步骤：1.登录教务处，选择公共服务-公共课表查询 2.选择课表类型为教室课表，选中你所在的校区，确认查询 3.全选当前页面课表(当前教务系统显示有bug，一页只能显示100条，增加显示的按钮无效) 4.选择查看大课表 5.逐个保存大课表所在html，使用getCourseFromCuitjwc.py导出csv文件 5.手动合并多分csv文件，只保留一个表头，检查表格为如下形式

第一行：教室名称,星期一,星期一,星期一,星期一,......星期日
第二行：教室名称,1,2,3,4,5,6,7,8,9,10,.....
第三行开始是教室信息

# TODO:
-优化正则表达式
-基于最短移动距离的教室推荐算法

非计算机专业，限于能力该代码主要由Copilot完成，欢迎进一步细化开发：）
