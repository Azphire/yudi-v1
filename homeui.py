from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import qtawesome
import os
from PyQt5.QtCore import pyqtSignal

class MainUi(QtWidgets.QMainWindow):
    def setupUi(self,MainWindow):
        MainWindow.setFixedSize(1200,740)
        MainWindow.setObjectName("MainWindow")
        self.main_widget = QtWidgets.QWidget(MainWindow)  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占8行9列
        MainWindow.setCentralWidget(self.main_widget) # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("") # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("") # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("快乐学习")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("个人中心")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comments',color='white'),"初涉江湖")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.commenting-o',color='white'),"一气呵成")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.hand-peace-o',color='white'),"题王争霸")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.user-o',color='white'),"基本信息")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.book',color='white'),"错题集")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.list',color='white'),"学习计划")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star',color='white'),"关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
        self.left_layout.addWidget(self.left_close, 0, 2,1,1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1,1,0,1,3)
        self.left_layout.addWidget(self.left_button_1, 2, 0,1,3)
        self.left_layout.addWidget(self.left_button_2, 3, 0,1,3)
        self.left_layout.addWidget(self.left_button_3, 4, 0,1,3)
        self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
        self.left_layout.addWidget(self.left_button_4, 6, 0,1,3)
        self.left_layout.addWidget(self.left_button_5, 7, 0,1,3)
        self.left_layout.addWidget(self.left_button_6, 8, 0,1,3)
        self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
        self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
        self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        # self.right_bar_widget = QtWidgets.QWidget() # 右侧顶部搜索框部件
        # self.right_bar_layout = QtWidgets.QGridLayout() # 右侧顶部搜索框网格布局
        # self.right_bar_widget.setLayout(self.right_bar_layout)
        # self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' '+'搜索  ')
        # self.search_icon.setFont(qtawesome.font('fa', 16))
        # self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        # self.right_bar_widget_search_input.setPlaceholderText("输入歌手、歌曲或用户，回车进行搜索")

        # self.right_bar_layout.addWidget(self.search_icon,0,0,1,1)
        # self.right_bar_layout.addWidget(self.right_bar_widget_search_input,0,1,1,8)

        # self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)


        self.right_recommend_label = QtWidgets.QLabel("热门诗词")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget() # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout() # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("《出塞》[唐]王昌龄") # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('icon/1.jpg')) # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(105,105)) # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # 设置按钮形式为上图下文

        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText("《相思》[唐]王维")
        self.recommend_button_2.setIcon(QtGui.QIcon('icon/2.jpg'))
        self.recommend_button_2.setIconSize(QtCore.QSize(105, 105))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_3 = QtWidgets.QToolButton()
        self.recommend_button_3.setText("《枫桥夜泊》[唐]张继")
        self.recommend_button_3.setIcon(QtGui.QIcon('icon/3.jpg'))
        self.recommend_button_3.setIconSize(QtCore.QSize(105, 105))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_4 = QtWidgets.QToolButton()
        self.recommend_button_4.setText("《早发白帝城》[唐]李白")
        self.recommend_button_4.setIcon(QtGui.QIcon('icon/4.jpg'))
        self.recommend_button_4.setIconSize(QtCore.QSize(105, 105))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_5 = QtWidgets.QToolButton()
        self.recommend_button_5.setText("《春望》[唐]杜甫")
        self.recommend_button_5.setIcon(QtGui.QIcon('icon/5.jpg'))
        self.recommend_button_5.setIconSize(QtCore.QSize(105, 105))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_recommend_layout.addWidget(self.recommend_button_1,0,0)
        self.right_recommend_layout.addWidget(self.recommend_button_2,0,1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)

        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        self.right_newquestion_lable = QtWidgets.QLabel("最新题库")
        self.right_newquestion_lable.setObjectName('right_lable')

        self.right_playlist_lable = QtWidgets.QLabel("热门游戏")
        self.right_playlist_lable.setObjectName('right_lable')

        self.right_newquestion_widget = QtWidgets.QWidget()  # 最新题库部件
        self.right_newquestion_layout = QtWidgets.QGridLayout() # 最新题库部件网格布局
        self.right_newquestion_widget.setLayout(self.right_newquestion_layout)

        self.newquestion_button_1 = QtWidgets.QPushButton("2021衡中一轮复习基础知识点")
        self.newquestion_button_2 = QtWidgets.QPushButton("2021毛坦厂三轮复习冲刺压轴题")
        self.newquestion_button_3 = QtWidgets.QPushButton("黄冈大试卷语文古诗基础2021最新版")
        self.newquestion_button_4 = QtWidgets.QPushButton("上海市历年中考古诗题题库")
        self.newquestion_button_5 = QtWidgets.QPushButton("2021天一中学语文复习密卷")
        self.newquestion_button_6 = QtWidgets.QPushButton("百万名师高考古诗压轴题")
        self.right_newquestion_layout.addWidget(self.newquestion_button_1,0,1,)
        self.right_newquestion_layout.addWidget(self.newquestion_button_2, 1, 1, )
        self.right_newquestion_layout.addWidget(self.newquestion_button_3, 2, 1, )
        self.right_newquestion_layout.addWidget(self.newquestion_button_4, 3, 1, )
        self.right_newquestion_layout.addWidget(self.newquestion_button_5, 4, 1, )
        self.right_newquestion_layout.addWidget(self.newquestion_button_6, 5, 1, )

        self.right_playlist_widget = QtWidgets.QWidget() 
        self.right_playlist_layout = QtWidgets.QGridLayout() 
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.playlist_button_1 = QtWidgets.QToolButton()
        self.playlist_button_1.setText("体验一段小说中的剧情~")
        self.playlist_button_1.setIcon(QtGui.QIcon('icon/game.jpg'))
        self.playlist_button_1.setIconSize(QtCore.QSize(120, 100))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_2 = QtWidgets.QToolButton()
        self.playlist_button_2.setText("生死存亡之际，你会选择什么？")
        self.playlist_button_2.setIcon(QtGui.QIcon('icon/game.jpg'))
        self.playlist_button_2.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_3 = QtWidgets.QToolButton()
        self.playlist_button_3.setText("语滴倾力制作，剧情游戏！")
        self.playlist_button_3.setIcon(QtGui.QIcon('icon/game.jpg'))
        self.playlist_button_3.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_4 = QtWidgets.QToolButton()
        self.playlist_button_4.setText("OMG，听我的，玩它！")
        self.playlist_button_4.setIcon(QtGui.QIcon('icon/game.jpg'))
        self.playlist_button_4.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_playlist_layout.addWidget(self.playlist_button_1,0,0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)
        self.right_playlist_layout.addWidget(self.playlist_button_3, 1, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_4, 1, 1)

        self.right_layout.addWidget(self.right_newquestion_lable, 4, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_lable, 4, 5, 1, 4)
        self.right_layout.addWidget(self.right_newquestion_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小

        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QWidget#left_widget{
                background:#77ACF1;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid #0A1D37;font-weight:700;}
        ''')


        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                margin-top:20px;
                border:none;
                font-size:32px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #0A1D37;}
            ''')
        self.right_playlist_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #0A1D37;}
            ''')

        self.right_newquestion_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:16px;
                height:40px;
                padding-left:5px;
                padding-right:5px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')

        MainWindow.setWindowOpacity(0.95) # 设置窗口透明度
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        self.main_layout.setSpacing(0)
