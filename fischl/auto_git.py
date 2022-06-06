import os
import sys
import subprocess


print(f"目前的目录是：{os.getcwd()}")
handle_1 = input("请确认此目录是否正确(yes)/(no): ")
handle_2 = input("请输入提交内容(feat)/(fix)/(docs)/(style)/(test): ")
if handle_1 != "no":
    print("正在更新代码...")
    subprocess.run(["git", "add", "."])
    # subprocess.run(["git", "commit", "-m", "auto_git update"])
    subprocess.run(["git", "commit", "-m", handle_2])
    subprocess.run(["git", "push"])
    print("更新完成！")
    sys.exit()
else:
    print("请重新运行程序！")
    #sys.exit()

