# auto-test


本项目实现接口自动化的技术选型：**Python+Requests+Pytest+Allure** ，通过 Python+Requests 来发送和处理HTTP协议的请求接口，使用 Pytest 作为测试执行器，使用 Excel 来管理测试数据，使用 Allure 来生成测试报告。

## 项目说明

本项目在实现过程中，把整个项目拆分成请求方法封装、HTTP接口封装、关键字封装、测试用例等模块。

首先利用Python把HTTP接口封装成Python接口，接着把这些Python接口组装成一个个的关键字，再把关键字组装成测试用例，而测试数据则通过Excel文件进行统一管理，然后再通过Pytest测试执行器来运行这些脚本，并结合Allure输出测试报告。

## 安装与配置

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，命令行中执行命令：

```
pip3 install -r requirements.txt
```
快速启动，命令行中执行命令：
```
python run.py
```
在命令行执行命令：```python run.py``` 运行用例后，会自动生成测试报告，测试报告文件在 ```reports``` 目录下。
### 测试报告效果展示

1. 报告状态（下图status对应的颜色）：
 - Failed（失败）：测试用例未能通过所有的验证条件。
 - Broken（中断）：测试执行过程中出现了意外情况，导致测试无法继续执行。
 - Passed（通过）：测试用例成功通过了所有的验证条件。
 - Skipped（跳过）：测试用例因为某些条件不符合而被跳过执行。
 - Unknown（未知）：测试结果无法确定或未知。

![img.png](img.png)

## 项目结构
- common ====>> 各种工具类：操作mysql、redis、excel等工具或中间件
- config ====>> 配置文件
- core ====>> requests请求方法封装、关键字返回结果类
- data ====>> 测试数据文件管理
- locator ====>> UI元素定位文件
- logs ====>> 日志文件夹
- page ====>> UI页面元素操作封装
- reports ====>> 测试报告文件夹
- requirements.txt ====>> 相关依赖包文件
- testcases ====>> 测试用例

## 接口测试
![img_1.png](img_1.png)




