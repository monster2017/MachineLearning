import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
import pandas as pd


"""
class Perceptron(object):
    def __init__(self,eta=0.01,n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self,x,y):
        self.w_ = np.zeros(1 + x.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi,target in zip(x,y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return  self

    def net_input(self,x):
        return  np.dot(x,self.w_[1:]) + self.w_[0]

    def predict(self,x):
        return np.where(self.net_input(x) >= 0.0, 1, -1)
"""

class Perceptron(object):
    def __init__(self, input_num, activator):
        """
        初始化感知器，设置输入参数的个数，以及激活函数。
        激活函数的类型为double -> double
        :param input_num:
        :param activator:
        """
        self.activator = activator
        #权重向量初始化为0, 每有一个参数就初始化一个0.0
        self.weights = [0.0 for _ in range(input_num)]
        #偏置项初始化为0
        self.bias = 0.0

    def __str__(self):
        """
        打印学习到的权重、偏置项
        :return:
        """
        return 'weights\t:%s\nbias\t:%f\n'  %(self.weights, self.bias)

    def predict(self, input_vec):
        """
        输入向量，输出感知器的计算结果
        :param input_vec:
        :return:
        """
        #把input_vec[x1,x2,x3 ...] 和 weights[w1,w2,w3 ...]打包在一起
        #变成[(x1,w1),(x2,w2),(x3,w3),...]
        #然后利用map函数计算[x1*w1, x2*w2, x3*w3]
        #最后利用reduce求和
        return  self.activator(
            reduce(lambda a,b:a+b,
                   map(lambda x,w:x*w, input_vec, self.weights)) + self.bias)

    def train(self, input_vecs, labels, iteration, rate):
        """
        输入训练数据：一组向量、与每个向量对应的label；以及训练轮数、学习率
        :param input_vecs:
        :param labels:
        :param iteration:
        :param rate:
        :return:
        """
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    def _one_iteration(self, input_vecs, labels, rate):
        """
        一次迭代，把所有的训练数据过一遍
        :param input_vecs:
        :param label:
        :param rate:
        :return:
        """
        #把输入和输出打包在一起，成为样本的列表[(input_vec,label),...]
        #而每个训练样本是(input_vec,label)
        samples = zip(input_vecs,labels)
        #对每个样本，按照感知器规则更新权重
        for (input_vec,label) in samples:
            #计算感知器在当前权重下的输出
            output = self.predict(input_vec)
            #更新权重
            self._update_weights(input_vec,output,label,rate)

    def _update_weights(self,input_vec,output,label,rate):
        """
        按照感知机更新权重
        :param input_vec:
        :param output:
        :param label:
        :param rate:
        :return:
        """
        #把input_vec[x1,x2,x3,...]和weights[w1,w2,w3,...]打包在一起
        #变成[(x1,w1),(x2,w2),(x3,w3),...]
        #然后利用感知器规则更新权重
        delta = label-output
        self.weights = list(map(
            lambda x, w : w + rate * delta * x,
            input_vec, self.weights))

        #更新bias
        self.bias += rate *delta



"""
实现and函数
"""

def f(x):
    '''
    定义激活函数f
    :param x:
    :return:
    '''
    return 1 if x > 0 else 0

def get_training_dataset():
    """
    基于and真值表构建训练数据
    :return:
    """
    #构建训练数据
    #输入向量列表
    input_vecs = [[1,1],[0,0],[1,0],[0,1]]
    #期望的输入列表，注意要与输入一一对应
    #[1,1] ->1,[0,0] ->0,[1,0] ->0,[0,1] ->0
    labels = [1,0,0,0]
    return input_vecs,labels

def train_and_perceptron():
    """
    使用and真值表训练感知器
    :return:
    """
    #创建感知器，输入参数个数为2（因为and是二元函数），激活函数为f
    p = Perceptron(2,f)
    #训练，迭代10轮，学习速率为0.1
    input_vecs,labels = get_training_dataset()
    p.train(input_vecs, labels, 10, 0.1)
    #返回训练好的感知器
    return p

if __name__ == '__main__':
    #训练and感知器
    and_perception = train_and_perceptron()
    #打印训练获得的权重
    print (and_perception)
    #测试
    print('1 and 1 = %d' %and_perception.predict([1,1]))
    print('0 and 0 = %d' %and_perception.predict([0,0]))
    print('1 and 0 = %d' %and_perception.predict([1,0]))
    print('0 and 1 = %d' %and_perception.predict([0,1]))

