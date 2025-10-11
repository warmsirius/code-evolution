# 题目:
#   n人 各100元
#   每轮 将1元 随机给别人，
#   if wealth=0，可不给，只接收。
#   t轮，财富分布


import random


class Experiment:
    @classmethod
    def experiment(cls, n: int, t: int) -> None:
        """
        n: number of people
        t: number of trials
        """
        wealth = [100] * n
        for _ in range(t):
            for i in range(n):
                if wealth[i] > 0:
                    j = random.randint(0, n - 1)
                    while j == i:
                        j = random.randint(0, n - 1)
                    wealth[i] -= 1
                    wealth[j] += 1
        
        wealth.sort()
        print("列出每个人的财富(从贫穷到富有):")
        for i in range(n):
            print(wealth[i], end=" ")
            if i % 9 == 0:
                print()
        print()
        print("这个社会的基尼系数为: ", cls.calculate_gini(wealth))
        return 
    
    @classmethod
    def calculate_gini(cls, wealth: list[int]) -> float:
        """计算基尼系数"""
        n = len(wealth)
        if n == 0:
            return 0.0
        
        total_wealth = 0
        abs_diff_wealth = 0
        for i in wealth:
            total_wealth += i
            for j in wealth:
                abs_diff_wealth += abs(i - j)
        
        if total_wealth == 0:
            return 0.0
        
        gini_index = abs_diff_wealth / (2 * n * total_wealth)
        return gini_index
    
    @classmethod
    def main(cls):
        n = 100
        t = 1000000
        cls.experiment(n, t)


if __name__ == "__main__":
    Experiment.main()
