# coding=utf-8
import os
import yaml
yaml.warnings({'YAMLLoadWarning': False})


class ReadURL:
    def Read(self):
        # Path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        # yamlPath = os.path.join(Path, "./URL.yaml")
        f = open("./URL.yaml", 'r', encoding='gbk')
        mes = f.read()
        mes = yaml.load(mes)
        print("-------------------------------")
        print(mes['test02']['url'])
        return mes

class ReadIP:
    def Read(self):
        # Path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        f = open("./IP.yaml", 'r', encoding='gbk')
        mes1 = f.read()
        mes1 = yaml.load(mes1)
        print("-------------------------------")
        print(mes1['test']['IP'])
        return mes1

class ReadAuthorization:
    def Read(self):
        # Path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        f = open("./IP.yaml", 'r', encoding='gbk')
        mes2 = f.read()
        mes2 = yaml.load(mes2)
        print("-------------------------------")
        print(mes2['test']['Authorization'])
        return mes2



ReadURL().Read()
ReadIP().Read()
ReadAuthorization().Read()



