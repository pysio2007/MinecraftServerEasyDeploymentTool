# 免责申明 这是一个简易工具 所以会出现 IF里面有IF 看看就行（）
import wget  # 下载库
import os # 操控文件
import tempfile # 临时文件
import json # 解析JSON
import goto
from dominate.tags import label
from goto import with_goto # GOTO跳转
import time # 休眠

Vanilla_DATA_URL= "https://file.pysio.online/d/MineCraft/ServerCord/Vanilla/"
Forge_DATA_URL= "https://cdn.jsdelivr.net/gh/pysio2007/MinecraftServerEasyDeploymentTool/Version/Forge.json"
Paper_DATA_URL= "https://cdn.jsdelivr.net/gh/pysio2007/MinecraftServerEasyDeploymentTool/Version/Paper.json"


os.system("cls")
print("MineCraft 简易服务器部署工具V0.1")
print("正在下载最新服务端下载地址")

Paperf = open("Paper.json", "w")
Paperf.write("Woops! 请完整运行下载器")
Paperf.close()
os.remove("Paper.json")
wget.download(Paper_DATA_URL, out="Paper.json")
Paper_link_data_loda = open("Paper.json")
Paper_link_data = json.load(Paper_link_data_loda) 

Forgef = open("Forge.json", "w")
Forgef.write("Woops! 请完整运行下载器")
Forgef.close()
os.remove("Forge.json")
wget.download(Forge_DATA_URL, out="Forge.json")
Forge_link_data_loda = open("Forge.json")
Forge_link_data = json.load(Forge_link_data_loda) 


os.system("cls")
print()
print("请先安装JAVA再运行本脚本")
print("1. 原版")
print("2. Fabric")
print("3. Forge")
print("4. Paper")

ClassInput = input("请输入你需要服务端类型的编号：")
if ClassInput == "1" :
    os.system("cls")
    print()
    VanillaVersion = input("请输入你要开服的版本号 例如1.7.10: ")
    FileVanillaVersion = VanillaVersion + ".jar"
    print()
    print("正在下载服务器文件 请稍后")
    Vanilla_link_data = Vanilla_DATA_URL + FileVanillaVersion
    wget.download(Vanilla_link_data,out=FileVanillaVersion)
    print()
    print("下载完毕 使用java -jar " + FileVanillaVersion + "启动服务器")        #原版部分
    
elif ClassInput == "2" :
    os.system("cls")
    print()
    FabricVersion = input("请输入你要开服的版本号 例如1.20.1: ")
    FileFabricVersion = FabricVersion + ".jar"
    print()
    print("正在下载Fabric安装文件 请稍后")
    wget.download("https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.2/fabric-installer-0.11.2.jar",out="installer.jar")
    FabricInstall = "java -jar installer.jar server -mcversion " + FabricVersion + " -downloadMinecraft "
    print()
    print("正在执行安装Fabric服务器")
    Fabric_link_data = Vanilla_DATA_URL + FileFabricVersion
    os.system(FabricInstall)
    print()
    print("正在清理安装文件")
    os.remove("installer.jar")
    print()
    print("安装完成")            #Fabric部分

elif ClassInput == "3" :
    os.system("cls")
    print()
    ForgeVersion = input("请输入你要开服的版本号 例如1.7.10: ")
    FileForgeVersion = ForgeVersion + ".jar"
    print()
    print("正在下载服务器文件 请稍后")
    wget.download(Forge_link_data[ForgeVersion],out="Forge.zip")

elif ClassInput == "4" :
    os.system("cls")
    print()
    PaperVersion = input("请输入你要开服的版本号 例如1.7.10: ")
    FilePaperVersion = PaperVersion + ".jar"
    print()
    print("正在下载服务器文件 请稍后")
    wget.download(Paper_link_data[PaperVersion],out=FilePaperVersion)