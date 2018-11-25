import os


def read_txt(filename):
    with open(os.getcwd()+os.sep+"Data"+os.sep+filename,'r',encoding="utf-8")as f:
        arrs=[]
        for line in f.readlines():
            arrs.append(tuple(line.strip().split(",")))
        return arrs


def read_txt1():
    with open("../Data/login.txt",'r',encoding="utf-8")as f:
        arrs=[]

        for line in f.readlines():
            arrs.append(tuple(line.strip().split(",")))
        return arrs
if __name__ == '__main__':
    print(read_txt1())