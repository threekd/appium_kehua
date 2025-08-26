from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.options.android import UiAutomator2Options

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '15', # 手机安卓版本，如果是鸿蒙系统，依次尝试 12、11、10 这些版本号
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.app.tideswing', # 启动APP Package名称
  'appActivity': '.ui.SplashActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 自动化需要输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', 
  options=UiAutomator2Options().load_capabilities(desired_caps))

# 设置缺省等待时间
driver.implicitly_wait(2)



input('**** Press to quit..')
driver.quit()