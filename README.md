## 项目分层

- __接口层__: 实现对接口的调用, 如httpclient, requests等
- __数据层__: 存放测试数据, 如用户注册, 登录等
- __业务层__: 实现测试用例的组装和处理, 如用户注册, 登录, 下单等
- __测试层__: 实现对业务层测试用例的执行, 包含断言, 日志, 报告等
- __工具层__: 常用的工具类, 如日期工具类, 字符串工具类等

## 项目结构

```
├── apis                           // 接口层, 用于封装各种接口请求
│   ├── data.yaml
│   └── test_data.yaml
├── base                            // 基础类, 如基础请求类, 基础测试类
│   ├── api.py
│   └── register.py
├── case                            // 业务层, 用于存放测试用例
│   ├── __init__.py
│   ├── test_login.py
│   └── test_register.py
├── common                          // 公共类, 如配置类, 日志类, 工具类
│   ├── config.py
│   ├── log.py
│   └── tools.py
├── docs                            // 文档层, 用于存放项目文档
│   ├── 需求文档.md
├── data                            // 数据层, 用于存放测试数据
│   ├── data.yaml
│   └── test_data.yaml
├── logs                            // 日志层, 用于存放日志
│   └── test.log
├── report                          // 测试报告
│   └── report.html
├── test                            // 测试层, 用于执行测试用例
│   ├── __init__.py
│   ├── test_login.py
│   └── test_register.py
├── tools                           // 工具层, 用于存放工具类
│   ├── date.py
│   └── string.py
├── README.md
├── requirements.txt
└── main.py  # 运行入口
``` 