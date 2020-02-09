
# 3rd Party Libraries
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import (QApplication, QLineEdit, QLabel, QPushButton, QCheckBox, QShortcut,
                             QFrame, QWidget, QListWidget, QMenu, QSystemTrayIcon)
from PyQt5.QtGui import QKeySequence, QFont

# Custom Libraries
from staticmethods import *


def initUI(self):
    app = QApplication([])
    self.setWindowTitle('DecoWall Windows')
    self.setWindowIcon(QIcon('favicon.png'))
    self.setGeometry(self.width / 2 - 300, self.height / 2 - 300, 600, 600)
    self.setFixedSize(600, 600)
    window = QWidget()
    self.setCentralWidget(window)

    with open('stylesheet.qss', 'r') as file:
        self.setStyleSheet(file.read())

    '''---------------------------------------------------------------------------------'''

    self.image_label = QLabel('Image', window)
    self.image_label.setGeometry(QRect(0, 0, 600, 339))
    self.image_label.setAlignment(Qt.AlignCenter)
    self.image_label.setObjectName('viewingArea')

    self.previous_image_btn = QPushButton(window)
    self.previous_image_btn.setGeometry(QRect(10, 360, 91, 30))
    self.previous_image_btn.clicked.connect(self.previous_image)
    previous_image_shortcut = QShortcut(QKeySequence("LEFT"), self)
    previous_image_shortcut.activated.connect(self.previous_image)

    self.set_as_wallpaper_btn = QPushButton(window)
    self.set_as_wallpaper_btn.setGeometry(QRect(150, 360, 100, 30))
    self.set_as_wallpaper_btn.clicked.connect(self.set_as_wallpaper)
    set_as_wallpaper_shortcut = QShortcut(QKeySequence("DOWN"), self)
    set_as_wallpaper_shortcut.activated.connect(self.set_as_wallpaper)

    self.add_to_favs_btn = QPushButton(window)
    self.add_to_favs_btn.setGeometry(QRect(350, 360, 111, 30))
    self.add_to_favs_btn.clicked.connect(self.add_to_favs)
    add_to_favs_shortcut = QShortcut(QKeySequence("UP"), self)
    add_to_favs_shortcut.activated.connect(self.add_to_favs)

    self.next_image_btn = QPushButton(window)
    self.next_image_btn.setGeometry(QRect(510, 360, 81, 30))
    self.next_image_btn.setLayoutDirection(Qt.LeftToRight)
    self.next_image_btn.clicked.connect(self.next_image)
    next_image_shortcut = QShortcut(QKeySequence("RIGHT"), self)
    next_image_shortcut.activated.connect(self.next_image)

    self.addsub = QLineEdit(window)
    self.addsub.setObjectName('listValue')
    self.addsub.setGeometry(QRect(10, 420, 171, 30))
    self.addsub.setPlaceholderText('          Add subreddit')
    # self.addsub.setFocus()

    self.addsub_btn = QPushButton(window)
    self.addsub_btn.setGeometry(QRect(200, 420, 70, 30))
    self.addsub_btn.clicked.connect(self.addsub_to_list)
    addsub_shortcut = QShortcut(QKeySequence("RETURN"), self)
    addsub_shortcut.activated.connect(self.addsub_to_list)

    self.listWidget = QListWidget(window)
    self.listWidget.setGeometry(QRect(10, 460, 171, 121))
    self.listWidget.addItems(get_config('sub-list'))

    self.remove_sub_btn = QPushButton(window)
    self.remove_sub_btn.setGeometry(QRect(200, 460, 70, 30))
    self.remove_sub_btn.clicked.connect(self.remove_sub)

    self.clear_sub_btn = QPushButton(window)
    self.clear_sub_btn.setGeometry(QRect(200, 505, 70, 30))
    self.clear_sub_btn.clicked.connect(self.clear_sub)

    self.download_btn = QPushButton(window)
    self.download_btn.setGeometry(QRect(200, 550, 70, 30))
    self.download_btn.clicked.connect(self.download_thread)

    self.change_every_label = QLabel(window)
    self.change_every_label.setGeometry(QRect(330, 420, 91, 30))

    self.change_every_value = QLineEdit(window)
    self.change_every_value.setText(str(get_config('change-every')))
    self.change_every_value.setGeometry(426, 420, 35, 30)
    self.change_every_value.setAlignment(Qt.AlignCenter)
    self.change_every_value.setObjectName('changeValue')

    self.change_every_btn = QPushButton(get_config('time-format'), window)
    self.change_every_btn.setObjectName('timeBtn')
    self.change_every_btn.setGeometry(QRect(457, 420, 59, 30))
    self.change_every_btn.clicked.connect(self.time_btn)

    self.activate_change_every_btn = QPushButton("Activate", window)
    self.activate_change_every_btn.setGeometry(529, 420, 61, 30)
    self.activate_change_every_btn.clicked.connect(self.change_every_activate)

    self.directory_label = QLabel(window)
    self.directory_label.setGeometry(QRect(330, 516, 70, 13))

    self.download_cbox = QCheckBox(window)
    self.download_cbox.setGeometry(QRect(410, 515, 70, 17))

    self.fav_cbox = QCheckBox(window)
    self.fav_cbox.setGeometry(QRect(500, 515, 70, 17))

    self.shuffle_cbox = QCheckBox(window)
    self.shuffle_cbox.setGeometry(QRect(330, 468, 91, 17))

    self.auto_changer_cbox = QCheckBox(window)
    self.auto_changer_cbox.setGeometry(QRect(455, 468, 91, 17))
    self.auto_changer_cbox.setChecked(False)

    self.run_at_startup_cbox = QCheckBox(window)
    self.run_at_startup_cbox.setGeometry(QRect(330, 557, 91, 17))

    self.systray_cbox = QCheckBox(window)
    self.systray_cbox.setGeometry(QRect(455, 557, 135, 17))

    self.v_line = QFrame(window)
    self.v_line.setGeometry(QRect(300, 410, 20, 171))
    self.v_line.setFrameShape(QFrame.VLine)
    self.v_line.setFrameShadow(QFrame.Sunken)

    self.h1_line = QFrame(window)
    self.h1_line.setGeometry(QRect(9, 395, 581, 16))
    self.h1_line.setFrameShape(QFrame.HLine)
    self.h1_line.setFrameShadow(QFrame.Sunken)

    self.h2_line = QFrame(window)
    self.h2_line.setGeometry(QRect(315, 490, 276, 16))
    self.h2_line.setFrameShape(QFrame.HLine)
    self.h2_line.setFrameShadow(QFrame.Sunken)

    self.previous_image_btn.setText("Previous Image")
    self.set_as_wallpaper_btn.setText("Set as Wallpaper")
    self.add_to_favs_btn.setText("Add to favourites")
    self.next_image_btn.setText("Next Image")
    self.addsub_btn.setText("+")
    self.remove_sub_btn.setText("-")
    self.clear_sub_btn.setText("Clear")
    self.download_btn.setText("Download")
    self.change_every_label.setText("Change every :")

    self.directory_label.setText("Directory :")
    self.download_cbox.setText("Download")
    self.download_cbox.setChecked(True)
    self.download_cbox.stateChanged.connect(lambda: self.cbox_state(self.download_cbox))

    self.fav_cbox.setText("Favourites")
    self.fav_cbox.setChecked(True)
    self.fav_cbox.stateChanged.connect(lambda: self.cbox_state(self.fav_cbox))

    self.shuffle_cbox.setText("Shuffle Images")
    self.shuffle_cbox.setChecked(False)
    self.shuffle_cbox.stateChanged.connect(lambda: self.cbox_state(self.shuffle_cbox))

    self.auto_changer_cbox.setText("Auto-Changer")
    self.auto_changer_cbox.setChecked(get_config('auto-change'))
    self.auto_changer_cbox.stateChanged.connect(lambda: self.cbox_state(self.auto_changer_cbox))

    self.run_at_startup_cbox.setText("Run at Startup")
    self.run_at_startup_cbox.setChecked(get_config('startup'))
    self.run_at_startup_cbox.stateChanged.connect(lambda: self.cbox_state(self.run_at_startup_cbox))

    self.systray_cbox.setText("Activate System Tray")
    self.systray_cbox.setChecked(get_config('activate-system-tray'))
    self.systray_cbox.stateChanged.connect(lambda: self.cbox_state(self.systray_cbox))

    exit_shortcut = QShortcut(QKeySequence("ESC"), self)
    exit_shortcut.activated.connect(self.close)  # calls built-in/overridden closeEvent() stimulating 'X'

    '''------------------------- SYSTEM TRAY UI ELEMENTS ----------------------------------------------'''

    self.tray_icon = QSystemTrayIcon(QIcon('favicon.png'))
    self.tray_icon.setToolTip('Open DecoWall')
    self.tray_icon.hide()

    tray_menu = QMenu()
    bold_font = QFont()
    bold_font.setBold(True)
    open_action = tray_menu.addAction("Open DecoWall")
    open_action.setFont(bold_font)
    open_action.triggered.connect(self.open_action_fn)
    tray_menu.addSeparator()

    next_action = tray_menu.addAction("Next Wallpaper                   Ctrl+Right")
    next_action.triggered.connect(self.next_action_fn)

    previous_action = tray_menu.addAction("Previous Wallpaper                Ctrl+Left")
    previous_action.triggered.connect(self.previous_action_fn)
    tray_menu.addSeparator()

    favourite_action = tray_menu.addAction("Add to Favourites                   Ctrl+Up")
    favourite_action.triggered.connect(self.favourite_action_fn)
    download_action = tray_menu.addAction("Download Wallpapers         Ctrl+Down")
    download_action.triggered.connect(self.download_action_fn)

    shuffle_action = tray_menu.addAction("Shuffle Wallpapers            Ctrl+Shift+S")
    shuffle_action.triggered.connect(self.shuffle_action_fn)

    tray_menu.addSeparator()
    quit_action = tray_menu.addAction("Quit DecoWall")
    quit_action.triggered.connect(app.exit)

    tray_menu.setStyleSheet('QMenu {padding-top: 4px; padding-bottom: 3px; padding-left: 0px;'
                            ' width: 275px; font-size:12.5px;}')
    self.tray_icon.setContextMenu(tray_menu)
    self.tray_icon.activated.connect(self.tray_icon_doubleclick)

    '''------------------------ END OF SYSTEM TRAY UI ELEMENTS --------------------------------------------'''
