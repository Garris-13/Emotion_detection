# EmoCare 智能情绪识别与健康反馈系统

EmoCare 是一套面向连续情绪监测与心理健康辅助场景的软件系统。系统支持图片上传和摄像头实时采集，利用深度学习模型识别人脸表情，输出主要情绪类别、置信度和多类别情绪概率分布，并结合规则引擎、大语言模型和多智能体反馈流程生成健康建议、综合分析报告与对话式辅助回复。

本项目来源于西安交通大学省级大学生创新训练项目（企业命题），项目编号 `S202510698803`。

> 重要说明：本系统用于情绪记录、趋势解释和自助建议，不用于医学诊断、治疗决策或危机干预替代。

## 功能概览

- **用户注册与登录**：支持用户账号、基础画像和个人数据隔离。
- **图片上传识别**：上传本地人脸图片，自动完成检测、预处理、情绪分类和概率展示。
- **实时摄像头监测**：支持启动、暂停、恢复和停止监测，按采样间隔保存识别结果。
- **情绪可视化**：展示主情绪、置信度、概率分布、历史记录和统计信息。
- **健康建议生成**：基于规则库和历史情绪模式生成即时建议、日常建议和长期建议。
- **综合分析报告**：根据历史情绪记录生成趋势分析、风险提示和结构化反馈报告。
- **多智能体反馈**：通过数据分析师、心理评估师、行动规划师和报告主编生成综合报告。
- **智能对话辅助**：结合用户画像、近期情绪记录、会话摘要和上下文进行多轮对话。
- **系统设置**：管理 DeepSeek、DashScope 等大模型 API Key，并支持主题、亮度、字体等显示偏好。

## 演示截图

### 登录与注册

![登录界面](soft_copyright/screenshots/01_login.png)

![注册界面](soft_copyright/screenshots/02_register.png)

### 图片上传识别

![情绪识别主界面](soft_copyright/screenshots/03_emotion_main.png)

![图片上传识别结果与情绪概率展示](soft_copyright/screenshots/04_upload_result.png)

### 实时摄像头监测

![实时摄像头监测画面](soft_copyright/screenshots/05_camera_monitor.png)

![监测历史记录画面](soft_copyright/screenshots/06_monitor_history.png)

### 智能建议与综合分析

![智能建议生成界面](soft_copyright/screenshots/07_advice.png)

![综合分析报告页面](soft_copyright/screenshots/08_analysis_report.png)

### 智能对话与系统设置

![智能对话界面](soft_copyright/screenshots/09_chat.png)

![系统设置界面](soft_copyright/screenshots/10_settings.png)

## 技术架构

| 模块 | 技术 |
|------|------|
| 前端界面 | HTML5、JavaScript、Chart.js |
| 后端服务 | Python、Flask、REST API、SSE 流式接口 |
| 情绪识别 | PyTorch、ResNet18/ResNet50、OpenCV、Pillow |
| 人脸检测 | MTCNN，依赖不可用时回退 OpenCV Haar |
| 数据存储 | MySQL、本地监测文件 |
| 智能分析 | OpenAI Compatible SDK、DeepSeek、DashScope |
| 对话流程 | LangGraph、多轮会话、会话摘要 |
| 多智能体 | 数据分析师、心理评估师、行动规划师、报告主编 |

## 目录结构

```text
EmoCare/
├── backend/
│   ├── api/
│   │   ├── api_server.py
│   │   ├── camera_monitor.py
│   │   ├── langgraph_agent.py
│   │   └── api_client.py
│   ├── database/
│   │   ├── db_manager.py
│   │   ├── init_db.py
│   │   └── schema.sql
│   ├── models/
│   │   ├── emotion_model.py
│   │   └── health_advisor.py
│   └── multiAgent/
│       └── MultiAgentFlow.py
├── frontend/
│   └── examples/
│       └── emotion_ui.html
├── facenet/
├── data/
├── soft_copyright/
│   ├── screenshots/
│   └── source_code/
├── best_model.pth
├── start.bat
├── start_venv.bat
└── README.md
```

## 运行环境

- 操作系统：Windows 10/11、Linux、Orange Pi OS 或 Debian 系 Linux 系统
- Python：建议 Python 3.10 及以上
- 数据库：MySQL
- 浏览器：Chrome、Edge、Firefox 等现代浏览器
- 摄像头：实时监测功能需要
- GPU：可选，CPU 环境也可运行基础推理

## 快速开始

### 1. 配置环境变量

复制 `.env.example` 为 `.env`，并根据本地环境填写数据库和大模型接口配置。

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=你的MySQL密码
MYSQL_DATABASE=emocare
DASHSCOPE_API_KEY=你的DashScope密钥
DEEPSEEK_API_KEY=你的DeepSeek密钥
```

### 2. 安装依赖

使用 venv：

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r backend\requirements.txt
```

如需使用项目内人脸检测模块：

```bash
python -m pip install -e .\facenet
```

### 3. 初始化数据库

```bash
python backend/database/init_db.py
```

也可以在 MySQL 工具中手动执行：

```text
backend/database/schema.sql
```

### 4. 启动系统

Windows 一键启动：

```bash
start_venv.bat
```

手动启动：

```bash
python backend\api\api_server.py
python -m http.server 8000
```

### 5. 访问页面

浏览器访问：

```text
http://localhost:8000/frontend/examples/emotion_ui.html
```

请保留 `/frontend/examples/` 路径，否则前端资源可能无法正确加载。

## 数据库表

| 表名 | 说明 |
|------|------|
| `users` | 用户信息表 |
| `emotion_records` | 情绪监测记录表 |
| `conversation_sessions` | 对话会话表 |
| `conversation_history` | 对话历史表 |
| `session_summaries` | 会话总结表 |
| `user_personality_analysis` | 用户性格分析表 |
| `system_prompt_cache` | 系统提示词缓存表 |

## 主要接口

| 接口 | 说明 |
|------|------|
| `POST /predict` | 图片情绪识别 |
| `POST /predict_with_advice` | 图片识别并生成健康建议 |
| `GET /health` | 服务状态检查 |
| `POST /monitor/start` | 启动摄像头监测 |
| `POST /monitor/stop` | 停止摄像头监测 |
| `POST /analyze_comprehensive` | 综合情绪分析 |
| `POST /multi_agent_analysis` | 多智能体反馈报告 |
| `POST /langgraph/chat` | 智能对话 |
| `GET /conversation/sessions` | 获取会话列表 |

## 安全与隐私

- 不要提交真实 `.env`、API Key、数据库密码或真实用户数据。
- 截图、报告和软著材料中不应包含真实隐私信息或未经授权的人脸图片。
- API Key 由后端保存和调用，前端只显示配置状态或掩码。
- 系统输出的建议仅供参考，不替代专业医疗、心理咨询或危机干预。

## 软著材料

`soft_copyright/` 目录中整理了软件著作权登记相关材料，包括文档鉴别材料、程序鉴别材料、源代码副本、界面截图、权属说明和自申请情况说明等。

其中，`soft_copyright/文档鉴别材料_操作说明书.tex` 是本 README 演示内容的主要参考来源。
