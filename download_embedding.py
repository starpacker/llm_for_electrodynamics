from huggingface_hub import snapshot_download
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
# 下载整个模型的所有文件
local_dir = snapshot_download(repo_id="Snowflake/snowflake-arctic-embed-l", local_dir="/data/group_003/hyh")

print(f"Model directory downloaded to: {local_dir}")
