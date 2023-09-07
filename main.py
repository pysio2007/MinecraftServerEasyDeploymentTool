# 免责申明 这是一个简易工具 所以会出现 IF里面有IF 看看就行（）
import wget  # 下载库
import os # 操控文件
import tempfile # 临时文件
import json # 解析JSON
import goto
from dominate.tags import label
from goto import with_goto # GOTO跳转
import time # 休眠

Vanilla_DATA_URL= "https://cdn.jsdelivr.net/gh/pysio2007/MinecraftServerEasyDeploymentTool/Version/Vanilla.json"
Fabric_DATA_URL= "https://cdn.jsdelivr.net/gh/pysio2007/MinecraftServerEasyDeploymentTool/Version/Fabric.json"
Forge_DATA_URL= "https://cdn.jsdelivr.net/gh/pysio2007/MinecraftServerEasyDeploymentTool/Version/Forge.json"
Paper_DATA_URL= "https://cdn.jsdelivr.net/gh/pysio2007/MinecraftServerEasyDeploymentTool/Version/Paper.json"


os.system("cls")
print("MineCraft 简易服务器部署工具V0.1")
print("正在下载最新服务端下载地址")

Vanillaf = open("Vanilla.json", "w")
Vanillaf.write("Woops! 请完整运行下载器")
Vanillaf.close()
os.remove("Vanilla.json")
wget.download(Vanilla_DATA_URL, out="Vanilla.json")
Vanilla_link_data_loda = open("Vanilla.json")
Vanilla_link_data = json.load(Vanilla_link_data_loda) 

Fabricf = open("Fabric.json", "w")
Fabricf.write("Woops! 请完整运行下载器")
Fabricf.close()
os.remove("Fabric.json")
wget.download(Fabric_DATA_URL, out="Fabric.json")
Fabric_link_data_loda = open("list.json")
Fabric_link_data = json.load(Fabric_link_data_loda) 

Paperf = open("Paper.json", "w")
Paperf.write("Woops! 请完整运行下载器")
Paperf.close()
os.remove("Paper.json")
wget.download(Paper_DATA_URL, out="Paper.json")
Paper_link_data_loda = open("list.json")
Paper_link_data = json.load(Paper_link_data_loda) 

Forgef = open("Forge.json", "w")
Forgef.write("Woops! 请完整运行下载器")
Forgef.close()
os.remove("Forge.json")
wget.download(Forge_DATA_URL, out="Forge.json")
Forge_link_data_loda = open("list.json")
Forge_link_data = json.load(Forge_link_data_loda) 


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