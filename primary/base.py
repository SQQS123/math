# 使用python实现简单的计算功能,而且也顺便赠送了一些python的语法功能。
# 必须是单行的。

if __name__ == '__main__':
    formula = input()
    try:
        ans = eval(formula)
    except:
        # 这里可以不让多行python执行
        print("输入的不太合适")
        exit()
    print(ans)

    # 如果将上面的合成一句就是
    # print(eval(input()))，没有异常处理的话。
