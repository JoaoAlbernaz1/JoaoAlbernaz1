"""Publish a free, client-only Hugging Face static Space; no paid compute used."""
from pathlib import Path
import os
from huggingface_hub import HfApi


def main():
    token = os.getenv("HF_TOKEN")
    if not token:
        raise ValueError("HF publication credentials unavailable")
    api = HfApi(token=token)
    owner = api.whoami()["name"]
    repo_id = owner + "/banking77-ptbr-research"
    space_dir = Path(__file__).parent / "space"
    for name in ("README.md", "index.html"):
        if not (space_dir / name).is_file():
            raise FileNotFoundError(space_dir / name)
    api.create_repo(
        repo_id=repo_id, repo_type="space", space_sdk="static",
        private=False, exist_ok=True
    )
    api.upload_folder(
        repo_id=repo_id, repo_type="space", folder_path=str(space_dir),
        commit_message="Publish audited BANKING77-PTBR research dashboard"
    )
    print("PUBLIC_STATIC_SPACE_URL=https://huggingface.co/spaces/" + repo_id)
    try:
        status = api.get_space_runtime(repo_id=repo_id)
        print("STATIC_SPACE_STAGE=" + str(status.stage))
    except Exception as exc:
        print("Runtime check unavailable: " + type(exc).__name__)


if __name__ == "__main__":
    main()
