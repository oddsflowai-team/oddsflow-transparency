import os
from huggingface_hub import HfApi

token = os.environ.get("HF_TOKEN")
repo_id = os.environ.get("HF_REPO_ID")
repo_type = os.environ.get("HF_REPO_TYPE", "model")

if not token:
    raise RuntimeError("Missing HF_TOKEN secret")
if not repo_id:
    raise RuntimeError("Missing HF_REPO_ID secret (e.g. Oddsflow-team/oddsflow-transparency)")

api = HfApi(token=token)

api.upload_folder(
    folder_path=".",
    repo_id=repo_id,
    repo_type=repo_type,
    ignore_patterns=[
        ".git/*",
        ".github/*",
        "**/__pycache__/*",
        ".DS_Store",
    ],
)

print(f"✅ Synced to Hugging Face: {repo_id} ({repo_type})")
