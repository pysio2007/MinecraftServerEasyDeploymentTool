# 免责申明 这是一个简易工具 所以会出现 IF里面有IF 看看就行（）
import wget  # 下载库
import os # 操控文件
import tempfile # 临时文件
import json # 解析JSON
import goto
from dominate.tags import label
from goto import with_goto # GOTO跳转
import time # 休眠


os.system("cls")
print("MineCraft 简易服务器部署工具V0.1")
Vanilla_DATA_URL= ""
Fabric_DATA_URL= ""
Forge_DATA_URL= ""
Paper_DATA_URL= ""



os.system("cls")
print()
print("1. 原版")
print("2. Fabric")
print("3. Forge")
print("4. Paper")

ClassInput = input("请输入你需要服务端类型的编号：")
if ClassInput == "1" :
    os.system("cls")
    print()
    VanillaVersion = input("请输入你要开服的版本号 例如1.7.10: ")
elif ClassInput == "2" :
    os.system("cls")
    print()
    FabricVersion = input("请输入你要开服的版本号 例如1.7.10: ")
elif ClassInput == "3" :
    os.system("cls")
    print()
    ForgeVersion = input("请输入你要开服的版本号 例如1.7.10: ")
elif ClassInput == "4" :
    os.system("cls")
    print()
    PaperVersion = input("请输入你要开服的版本号 例如1.7.10: ")