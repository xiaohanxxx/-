import os,re
import time
# 获取所有的手机设备
def getDevicesAll():
    devices = []
    try:
        for dName_ in os.popen("adb devices"):#遍历 返回一个文件描述符号为fd的打开的文件对象 
            if "\t" in dName_:
                if dName_.find("emulator") < 0:
                    devices.append(dName_.split("\t")[0])
        devices.sort(cmp=None, key=None, reverse=False)
    except:
        pass
    print(u"\n设备名称: %s \n总数量:%s台" % (devices, len(devices)))
    return devices



### 导出手机端当前页面元素
##def export(devices_name):
##        # 页面xml保存到手机存储
##        step1 = os.popen('adb -s {0} shell uiautomator dump /sdcard/{1}.xml'.format(devices_name,devices_name)).read()
##        if step1.find('UI') != -1:
####            print(devices_name+'\txml写进手机存储成功') #输出判断
##            # 页面xml从手机存储推送到电脑，和当前运行程序同级
##            os.popen('adb -s {0} pull /sdcard/{1}.xml '.format(devices_name,devices_name))
####            print(devices_name+"\txml推送到电脑成功") #输出判断
##            with open(devices_name + ".xml",encoding="utf-8") as f:
##                res = f.read()
##            return res
##        else:
##            print(devices_name+"\txml写进手机存储失败")
##        return "null"
##
##
### 匹配函数
##def check_line(res,find_str):  #正则匹配拿到准确的数据
##    #res是返回的xml文件数据
####    list1 = re.findall( '<[^<]*?' + find_str + '[^>]*?>', res)
##    find_str = r'content-desc="."'
##    find_str1 = r'小程序、公众号、文章、朋友圈和表情等'
##    list1 = re.findall(find_str,res)
##    if list1:
##        return list1[0]
##    return "null"
##
##
##def main():#进行逻辑判断
##    # 以resource-id为基准进行匹配
##    findstr = 'resource-id="com.tencent.mm:id/anl"'
##    devices = getDevicesAll()
##    for d_name in devices:
##        str1 = ''
##        print("输入手机号：")
##        for phone in iter(input,str1):
##            os.system('adb shell input text "%s"'%phone)
##            os.system('adb shell input keyevent 66  ')
##            os.system('adb shell input keyevent 66  '*2)
##            time.sleep(2)
##            res = export(d_name)
##            res = export(d_name)
##            result = check_line(res,findstr)
##            if res!="null":
##                #result为正则匹配出来的数据
##                if result == "null":
##                    print(phone,"性别未知")
##                elif result == "小程序、公众号、文章、朋友圈和表情等":
##                    print(phone,"账号异常或不存在")
##                elif result.find("男") != -1:
##                    print(phone,"性别男")
##                elif result.find("女") != -1:
##                    print(phone,"性别女")
##            #返回程序
##            time.sleep(2)
##            if result == "小程序、公众号、文章、朋友圈和表情等":
##                os.system('adb shell input tap 984 111')
##            else:
##                os.system('adb shell input keyevent 4  ')
##                #清除数据
##                os.system('adb shell input tap 984 111') 
##
##
##if __name__=="__main__":
####    str1 = ''
####    for phone in iter(input,str1):
####        os.system('adb shell input text "%s"'%phone)
####    ##    os.system('adb shell input keyevent 66  ')
####        os.system('adb shell input keyevent 66  '*2)
####        #识别程序
##    main()
##
##    time.sleep(2)
##    #返回程序
##    os.system('adb shell input keyevent 4  ')
##    #清除数据
##    os.system('adb shell input tap 984 111') 
####        #返回程序
####        os.system('adb shell input keyevent 4  ')
####        #清除数据
####        os.system('adb shell input tap 840 56') 
####
##
##
