# Python_Practice
## Python 解释器
### 虚拟环境解释器
1. **用途**
   - 为特定项目（如 PythonProject）提供隔离的运行环境。
   - 避免不同项目的依赖冲突。
2. **使用**
   - 打开 `Anaconda Prompt`
   - 切换到虚拟环境所在目录：`cd F:\Python\PythonProject`
   - 如果切换未成功，输入：`F:`
   - 激活虚拟环境：`.venv\Scripts\activate`
   - 使用清华镜像源安装 NumPy：`pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple`
   - 验证安装：`python -c "import numpy; print(numpy.__version__)"`
### Conda 环境解释器
1. **用途**
   - 管理复杂的依赖（如 NumPy、Pandas 等科学计算库）。
   - 环境间快速切换。
2. **使用**
   - 打开 `Anaconda Prompt`
   - 激活环境：`conda activate test`
   - 安装包：
     - 在当前环境中安装包 `conda install 包名称`
     - 指定版本号 `conda install 包名称=version`
     - 在指定环境中安装包 `conda install -n 环境名 包名称`
   - 当使用 conda install 无法安装时，可尝试使用 pip 安装
     - `pip install 包名称 -i https://pypi.tuna.tsinghua.edu.cn/simple  # 清华镜像`
     - `pip install 包名称 -i  https://pypi.douban.com/simple  # 豆瓣镜像`
### 全局解释器
1. **用途**
   - 运行全局 Python 脚本或简单任务。
   - 不适合项目管理（易造成依赖冲突）。
### 总结
|特性|虚拟环境解释器|Conda 环境解释器|全局解释器|
|---|---|---|---|
|环境类型|项目隔离（venv）|跨平台隔离（Conda）|系统全局|
|依赖管理|仅 Python 包|Python 包 + 非 Python 库（如 C 库）|所有包全局安装|
|激活方式|.\venv\Scripts\activate（Windows）|conda activate <环境名>|无需激活|
|适用场景|普通 Python 项目|科学计算、多语言依赖项目|临时脚本或学习|
|路径示例|F:/.../.venv/Scripts/python.exe|F:/anoconda3/envs/test/python.exe|C:/.../WindowsApps/python3.10.exe|
