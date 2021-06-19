import random
from BaiduApiAccess.TTS_STT import say, listen
from DataAccess.gameAccess import getGames, getGamePlot, getGameByTitle


#  参数为主循环中的client
#  整体应当为一个循环，直到用户不想继续本功能再返回
def play_game():
    say("好的，开始游戏吧。")
    gameList = getGames()
    rid = random.randint(0, len(gameList) - 1)
    game = gameList[rid]
    say("本游戏的题目是" + game["title"] + "，" + game["intro"])
    plot = getGamePlot(game["startPlot"])
    while(True):
        say(plot["content"])
        if plot["isEnding"] == 1:
            say("游戏结束，我们下次再见。")
            return
        while(True):
            request = listen()
            plotId = 0
            for choice, id in plot["choices"].items():
                if request.find(choice) != -1:
                    plotId = id
                    break
            if plotId > 0:
                plot = getGamePlot(plotId)
                break
            else:
                say("对不起，我没有听清你的选择，请再说一次")


if __name__ == "__main__":
    play_game()