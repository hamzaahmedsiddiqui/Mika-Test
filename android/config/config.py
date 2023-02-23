
import os

# Define the APK file name
apk_filename = "com.fosanis.android.cancer_companion-1.8.30-4176-develop-debug.apk"
# Getting the APK file path
apk_path = os.path.join(os.path.dirname(os.getcwd()), 'resources', apk_filename)


# Get the full path to the APK file
#apk_path ="/Users/hamzaahmed/Documents/Mika/MikaTestAutomation/android/resources/com.fosanis.android.cancer_companion-1.8.30-4176-develop-debug.apk"
print(apk_path)
android_desire_capability = {
  "platformName": "Android",
  "appium:platformVersion": "12",
  "appium:automationName": "UiAutomator2",
  "appium:app": apk_path,
  "appActivity": "com.fosanis.mika.app.MainActivity",
  "noReset": False
}
android_host = "http://127.0.0.1:4724/wd/hub"
login_email = "automation1@gmail.com"
login_passowrd = "abc1234!"
partner_code = "MEINMIKATOGOGFJR"


#"appium:appPackage": "com.fosanis.android.cancer_companion.debug"