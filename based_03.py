# 程序员希望：每次不要改写代码，给我不同的输入，代码不修改，就可以解决这个问题。

import random # 产生随机数

grammer01 = """
复合句子=简单句子 连词 简单句子
简单句子 = 主语 谓语 宾语
连词 = 而且|但是|不过
主语 = 你| 我 | 他 
谓语 = 吃| 玩 | 喝
宾语 = 苹果|香蕉|篮球|纸巾
    
"""
def get_grammer(grammer_string):
    grammer_gen=dict()
    for line in grammer_string.split('\n'):
        if not line.strip():continue
        print("语法中有这一行：",line)
        stmt,expr=line.split("=")
        exprs=expr.split('|')
        grammer_gen[stmt.strip()]=[e.strip() for e in exprs]
    print("grammer是：",grammer_gen)
    return grammer_gen

def generate_sent(gram,target='简单句子'):
    if target not in gram:
        return target
    exp=random.choice(gram[target])
    return ''.join([generate_sent(gram,e) for e in exp.split()])

print("generated sentenses is：",generate_sent(get_grammer(grammer01),target='复合句子'))