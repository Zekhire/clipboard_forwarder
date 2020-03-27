import psutil
import pywinauto.application
import json


# pids = psutil.pids()
# atmgrid=0
# for pid in pids:
#     p = psutil.Process(pid)
#     print(p)
#     if p.name().find("pythonw.exe") == 0:
#         atmgrid=pid
#         break
#
# print("pythonw id is %d" % atmgrid)

while True:
    # try:
        atmgrid = 4976

        app = pywinauto.application.Application(backend="uia").connect(process=atmgrid)
        # pywinauto.findbestmatch.MatchError: Could not find 'FloatActionBar' in 'dict_keys(['Kagami', 'Pane', 'KagamiPane', 'Custom', 'Spring Board - 1 games', 'Spring Board - 1 gamesDialog', 'Dialog', 'TitleBar', 'Menu', 'SystemMenu', 'System', 'SystemMenuItem', 'System0', 'System1', 'System2', 'MenuItem', 'Button', 'Minimalizuj', 'MinimalizujButton', 'Button0', 'Button1', 'Button2', 'Maksymalizuj', 'MaksymalizujButton', 'Button3', 'Zamknij', 'ZamknijButton', 'Custom0', 'Custom1', 'Custom2'])'
        # app.window(best_match='KagamiPane', top_level_only=False).print_control_identifiers()
        # app.window(best_match='Kagami', top_level_only=False).print_control_identifiers()
        # app.window(best_match='Pane', top_level_only=False).print_control_identifiers()
        app.
        # app.DialogTitle.PrintControlIdentifiers()
        # for x in app.descendants():
        #     print(x.window_text())
        #     print(x.class_name())
        # win = app.window(best_match='KagamiPane', top_level_only=False)
        # win = app.window(best_match='Kagami', top_level_only=False)
        # win = app.window(best_match='Pane', top_level_only=False)
        #
        # with open('Kagami.json', 'w') as f:
        #     json.dumps(win)
        #
        # win = app.window(best_match='KagamiPane', top_level_only=False)
        # with open('KagamiPane.json', 'w') as f:
        #     json.dumps(win)
    # except:
    #     continue
    # break