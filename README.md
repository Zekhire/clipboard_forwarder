# Clipboard forwarder

#### Technologies
Project was created and tested with:
* Windows 10
* Python 3.6.5
* selenium 3.141.0
* urllib3 1.26.2

Currently project is working with Google Chrome Browser only.


#### Description
Project created in order to automate process of copy and paste text into google translator. This should be useful especially during reading text in foreign language, when this text is copyable.


#### Example application
User can integrate this program with Visual Novel Reader (VNR in short). In order to do that, user need to enable option in VNR to copy dialog text to clipboard, then automatically this text is pasted to Google Translator. This Combination gives user much more translation suggestions than using VNR only. This is much more efficient when read visual novel is written in foreign language (eg. Japanese). Then we recommend to use also translating plug-in to give much more more precised translation suggestions.


#### Setup
- Run command in clipboard_forwarder\ catalogue:
```
pip install -r requirements.txt
```
- Download chromedriver from https://chromedriver.chromium.org/downloads and unpack it into desired catalogue (eg. D:\cf\chromedriver)
- Copy C:\Users\\[YOUR USERNAME]\AppData\Local\Google\Chrome\User Data\Default catalogue (eg. D:\cf\chromeprofile)
- Adjust clipboard_forwader\browsers_data.json paths so that indicate paths to:
	- Google Chrome browser, 
	- chromedriver.exe,
	- copied "default" catalogue


#### Run
Go to clipboard_forwarder\ and run command:
```
python clipboard_forwarder.py
```