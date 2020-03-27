def first():
    import win32gui
    import time
    import win32process
    i = 0
    while i <= 1:
        time.sleep(3)
        w=win32gui
        w.GetWindowText (w.GetForegroundWindow())
        print (str(w.GetWindowText (w.GetForegroundWindow())))



def second():
    import win32gui
    import time
    import psutil
    import win32process
    i = 0
    while i <= 1:
        time.sleep(3)
        w=win32gui
        w.GetWindowText(w.GetForegroundWindow())
        pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())
        print(psutil.Process(pid[-1]).name(), "\t\t", str(w.GetWindowText(w.GetForegroundWindow())))
        # print(str(w.GetWindowText(w.GetForegroundWindow())))

def third():
    import time
    import win32gui
    while True:
        window = win32gui.GetForegroundWindow()
        # window = win32gui.GetActiveWindow()
        title = win32gui.GetWindowText(window)
        print(title)
        if title == 'Kagami':
            control = win32gui.FindWindowEx(window, 0, "static", None)
            getwin = win32gui.GetWindowText(control)
            print('text: ', win32gui.GetWindowText(control))
            win32gui.ChildWindowFromPointEx()
        time.sleep(1)

# third()

def fourth():
    import ctypes

    CF_TEXT = 1

    kernel32 = ctypes.windll.kernel32
    kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
    kernel32.GlobalLock.restype = ctypes.c_void_p
    kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
    user32 = ctypes.windll.user32
    user32.GetClipboardData.restype = ctypes.c_void_p

    def get_clipboard_text():
        user32.OpenClipboard(0)
        try:
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                return value
        finally:
            user32.CloseClipboard()

    print(get_clipboard_text())


def fifth():
    import pywinauto

    # prog = pywinauto.application.Application()
    # prog.connect_(path=r'D:\MOJE\NARZEDZIA\Visual Novel Reader\Visual Novel Reader.exe')
    # w_handle = pywinauto.findwindows.find_windows(title=u'Kagami', class_name='#32770')[0]

    prog = pywinauto.Application().start(r'D:\MOJE\NARZEDZIA\Visual Novel Reader\Visual Novel Reader.exe')
    w_handle = pywinauto.findwindows.find_windows(title=u'Kagami')[0]

    window = prog.window(handle=w_handle)
    # c = prog.Fightplansettingsdialog.Texts()
    all_texts = []
    for child in window.children():
        all_texts.extend(child.Texts())
        print(child.Texts())
    all_texts = filter(lambda t: t, all_texts)  # clear empty texts

# while True:
#     third()
#     # fifth()
fifth()


# # import win32gui
# #
# # hwnd = win32gui.FindWindow("#32770", "Kagami")
# # # got back the correct handle to the dialog
# # win32gui.SetForegroundWindow(hwnd)
# #
# # btnhdl = win32gui.FindWindowEx(hwnd, 0, "Button", "&Yes")
# # # returns 0
# #
# # import pywinauto
# # while True:
# #     try:
# #         prog = pywinauto.application.Application()
# #         # prog.connect_(path=r'D:\MOJE\NARZEDZIA\Visual Novel Reader\Visual Novel Reader.exe')
# #         w_handle = pywinauto.findwindows.find_windows(title=u'Kagami', class_name='#32770')[0]
# #     except:
# #         continue
#
# import pywinauto
# app = pywinauto.Application().start(r'D:\MOJE\NARZEDZIA\Visual Novel Reader\Visual Novel Reader.exe')
# # prog = pywinauto.application.Application().connect_(path=r'D:\MOJE\NARZEDZIA\VisualNovelReader\VisualNovelReader.exe')
# # app = pywinauto.application.Application(backend='uia').connect_(process=16188)
# w_handle = pywinauto.findwindows.find_windows(title=u'Kagami')[0]
# # app = pywinauto.Application().start(r'asdsadsadsadsa')
# window = app.window_(handle=w_handle)
#
# while True:
#     # print(w_handle)
#     # print(window)
#     print(app.HelpTopics.ListBox.texts())
#     input()

