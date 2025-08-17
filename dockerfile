FROM python:3.11-slim

# 安装依赖
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# 复制脚本
COPY entrypoint.py /entrypoint.py

# 设置入口
ENTRYPOINT ["python", "/entrypoint.py"]
