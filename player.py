class Player():
    # 基础数据信息
    info_base = {
        "负重上限": 1200,
        "剩余时间": 30,
        "初始资金": 10000,
        "基础收益": 1000,
        "水": {"每箱质量": 3, "基准价格": 5, "晴朗": 5, "高温": 8, "沙暴": 10},
        "食物": {"每箱质量": 2, "基准价格": 10, "晴朗": 7, "高温": 6, "沙暴": 10}
    }

    Weather = ['高温', '高温', '晴朗', '沙暴', '晴朗', '高温', '沙暴', '晴朗', '高温', '高温',
               '沙暴', '高温', '晴朗', '高温', '高温', '高温', '沙暴', '沙暴', '高温', '高温',
               '晴朗', '晴朗', '高温', '晴朗', '沙暴', '高温', '晴朗', '晴朗', '高温', '高温']

    def __init__(self):
        self.time_re = self.info_base["剩余时间"]
        self.foo_re = 0
        self.wat_re = 0
        self.mon_re = self.info_base["初始资金"]
        self.wei_re = 0
        self.day = 0

        # 阶段性使用变量：路程计数
        self.step = 0

    def T_judge(self):
        if self.day >= 30:
            return False
        return True

    # 状态更新
    # def __update(self, cons_foo=0, cons_wat=0, cons_t=0, cons_mon=0, cons_wei=0, step=0):
    def __update(self, **kwargs):
        f = self.foo_re + kwargs.get('cons_foo', 0)
        wat = self.wat_re + kwargs.get('cons_wat', 0)
        t = self.time_re + kwargs.get('cons_t', 0)
        m = self.mon_re + kwargs.get('cons_mon', 0)
        w = self.wei_re + kwargs.get('cons_wei', 0)
        # 判断各种属性是否足够本次动作
        if f < 0 or wat < 0 or t < 0 or w < 0 or w > self.info_base["负重上限"]:
            return False
        self.foo_re, self.wat_re, self.time_re, self.mon_re, self.wei_re = f, wat, t, m, w

        self.step += kwargs.get('step', 0)
        return True

    # 基础消耗
    def __cons_base(self, day):
        return (self.info_base["水"][self.Weather[day]], self.info_base["食物"][self.Weather[day]])

    # 计算分数
    def score(self):
        i = self.foo_re * self.info_base['食物']['基准价格'] + self.wat_re * self.info_base['水']['基准价格']
        return i / 2 + self.mon_re

    # 行走
    def walk(self, day, ):
        if not self.T_judge():
            return False
        if self.Weather[day] == "沙暴":
            return self.rest(day)
        self.day += 1
        cons_foo, cons_wat = self.__cons_base(day)
        cons_foo = -2 * cons_foo
        cons_wat = -2 * cons_wat
        cons_t = -1
        cons_wei = (self.info_base['水']['每箱质量'] * cons_wat + self.info_base['食物']['每箱质量'] * cons_foo)
        return self.__update(cons_foo=cons_foo, cons_wat=cons_wat, cons_t=cons_t, cons_wei=cons_wei, step=1)

    # 休息
    def rest(self, day):
        if not self.T_judge():
            return False
        self.day += 1

        cons_foo, cons_wat = self.__cons_base(day)
        cons_foo = - cons_foo
        cons_wat = - cons_wat
        cons_t = -1
        cons_wei = (self.info_base['水']['每箱质量'] * cons_wat + self.info_base['食物']['每箱质量'] * cons_foo)
        return self.__update(cons_foo=cons_foo, cons_wat=cons_wat, cons_t=cons_t, cons_wei=cons_wei)

    # 挖矿
    def mining(self, day):
        if not self.T_judge():
            return False
        self.day += 1

        cons_foo, cons_wat = self.__cons_base(day)
        cons_foo = -3 * cons_foo
        cons_wat = -3 * cons_wat
        cons_t = -1
        cons_mon = +self.info_base["基础收益"]
        cons_wei = (self.info_base['水']['每箱质量'] * cons_wat + self.info_base['食物']['每箱质量'] * cons_foo)
        return self.__update(cons_foo=cons_foo, cons_wat=cons_wat, cons_t=cons_t, cons_mon=cons_mon, cons_wei=cons_wei)

    # 购买
    def buy(self, wat, foo, loc):
        """
        :param foo:
        :param wat:
        :param loc: 表示购买东西的位置，1为起点，2为村庄
        :return:
        """
        cons_foo = foo
        cons_wat = wat
        # cons_mon = -(self.info_base["水"]["基准价格"] * wat + self.info_base["食物"]["基准价格"] * foo)
        cons_mon = -(self.info_base["水"]["基准价格"] * wat + self.info_base["食物"]["基准价格"] * foo) if loc == 1\
            else -2 * (self.info_base["水"]["基准价格"] * wat + self.info_base["食物"]["基准价格"] * foo)
        cons_wei = +(self.info_base['水']['每箱质量'] * wat + self.info_base['食物']['每箱质量'] * foo)
        return self.__update(cons_foo=cons_foo, cons_wat=cons_wat, cons_mon=cons_mon, cons_wei=cons_wei)
