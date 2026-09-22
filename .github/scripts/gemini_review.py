import json
import os
import subprocess
import sys
import urllib.request
import urllib.error

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
PR_NUMBER = os.environ["PR_NUMBER"]
BASE_SHA = os.environ["BASE_SHA"]
HEAD_SHA = os.environ["HEAD_SHA"]

MODEL = "gemini-3.6-flash"
MAX_DIFF_CHARS = 60000


def get_diff() -> str:
    result = subprocess.run(
        ["git", "diff", f"{BASE_SHA}...{HEAD_SHA}"],
        capture_output=True,
        text=True,
        check=True,
    )
    diff = result.stdout
    if len(diff) > MAX_DIFF_CHARS:
        diff = diff[:MAX_DIFF_CHARS] + "\n\n... (diff truncated)"
    return diff


def call_gemini(diff: str) -> str:
    prompt = (
        "당신은 숙련된 코드 리뷰어입니다. 아래 git diff를 검토하고 한국어로 리뷰해 주세요.\n"
        "- 버그, 엣지 케이스, 잠재적 오류를 우선적으로 지적하세요.\n"
        "- 개선하면 좋을 점(가독성, 효율성, 네이밍)은 간단히 덧붙이세요.\n"
        "- 지금 코드보다 더 나은 대안이 없다면, 다른 말 없이 정확히 'LGTM' 한 단어만 출력하세요.\n"
        "- Markdown 형식으로, too-long 하지 않게 핵심만 작성하세요.\n\n"
        f"```diff\n{diff}\n```"
    )

    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
        f"?key={GEMINI_API_KEY}"
    )
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"Gemini API error {e.code}: {body}", file=sys.stderr)
        raise

    candidates = data.get("candidates", [])
    if not candidates:
        return "Gemini API가 리뷰 내용을 반환하지 않았습니다."
    parts = candidates[0]["content"]["parts"]
    return "".join(p.get("text", "") for p in parts).strip()


def post_comment(body: str) -> None:
    url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
    payload = {"body": f"## 🤖 Gemini Code Review\n\n{body}"}
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        resp.read()


def main() -> None:
    diff = get_diff()
    if not diff.strip():
        print("Empty diff, skipping review.")
        return
    review = call_gemini(diff)
    post_comment(review)
    print("Review posted.")


if __name__ == "__main__":
    main()
