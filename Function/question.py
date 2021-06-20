import random
from BaiduApiAccess.TTS_STT import say, listen
from DataAccess.questionAccess import getCHNQuestions


# 整体应当为循环，直到用户不想继续本功能再返回
def answer_questions():
    say("好的，现在开始随机问答。")
    questionList = getCHNQuestions()
    while(True):
        rid = random.randint(0, len(questionList)-1)
        question = questionList[rid]
        questionList.remove(question)
        say(question["question"])
        request = listen()
        if request.find(question["answer"]) != -1:
            say("回答正确！")
        else:
            say("正确答案是，" + question["answer"])
        if len(questionList) == 0:
            say("你太厉害了，题库已经作答完毕，下次再来吧。")
            return
        say("还要继续题目问答吗？")
        request = listen()
        if request.find("不") != -1:
            say("好的，我们下次再见")
            return
        else:
            say("加油，下一题")


if __name__ == "__main__":
    answer_questions()