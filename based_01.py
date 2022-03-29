# 基于传统的模板匹配的方式进行nlp

import random # 产生随机数

rules01 = """
句子 = 主语 谓语 宾语
主语 = 你| 我 | 他 
谓语 = 吃| 玩 
宾语 = 苹果|香蕉|篮球
    
"""

def generate_verb():
    return random.choice("吃| 玩 ".split("|"))

def generate_binyu():
    return random.choice("苹果|香蕉|篮球".split("|"))

        
print(generate_binyu()+generate_verb())

# 可以看到，如果有一个rule02（语法），就还需要重新写很多代码。
