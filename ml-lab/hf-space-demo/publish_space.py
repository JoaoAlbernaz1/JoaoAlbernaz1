"""Publish a read-only model demo to the Hub; no secrets in repository content."""
from __future__ import annotations

import os
from pathlib import Path

from huggingface_hub import HfApi


def main() -> None:
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise ValueError("HF_TOKEN must be configured in the runner environment")
    api = HfApi(token=token)
    username = api.whoami()["name"]
    repo = f"{username}/banking77-ptbr-intent-explorer"
    local = Path(__file__).parent / "space"
    for name in ("README.md", "app.py", "requirements.txt"):
        if not (local / name).is_file():
            raise FileNotFoundError(local / name)

    api.create_repo(
        repo_id=repo,
        repo_type="space",
        space_sdk="gradio",
        exist_ok=True,
        private=False,
    )
    api.upload_folder(
        repo_id=repo,
        repo_type="space",
        folder_path=str(local),
        commit_message="Publish reproducible BANKING77-PTBR interactive NLP demo",
    )
    print(f"PUBLIC_SPACE_URL=https://huggingface.co/spaces/{repo}")
    try:
        runtime = api.get_space_runtime(repo_id=repo)
        print(f"SPACE_RUNTIME_STAGE={runtime.stage}")
    except Exception as exc:
        print(f"Runtime status could not be checked: {exc.__class__.__name__}")


if __name__ == "__main__":
    main()
