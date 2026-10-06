import os
import sys
import json
import getpass
import subprocess
import urllib.request
import urllib.error

REPO_NAME = "AI"
REPO_DESCRIPTION = "SPPU T.Y.B.Sc.(C.S.) SEM-V Foundation of Artificial Intelligence and Machine Learning (CS-321-VSC-P) Practical Examination Solutions"

def get_token():
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        return sys.argv[1].strip()
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ.get("GITHUB_TOKEN").strip()
    try:
        token = getpass.getpass("Enter your GitHub Personal Access Token (hidden): ").strip()
        return token
    except (EOFError, KeyboardInterrupt):
        return None

def get_auth_user(token):
    req = urllib.request.Request(
        "https://api.github.com/user",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "AI-Exam-Automation"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            scopes_header = resp.headers.get("X-OAuth-Scopes", "")
            scopes = [s.strip() for s in scopes_header.split(",") if s.strip()]
            return data.get("login"), scopes
    except urllib.error.HTTPError as e:
        return None, []
    except Exception:
        return None, []

def create_or_check_repo(token, username):
    url = "https://api.github.com/user/repos"
    payload = json.dumps({
        "name": REPO_NAME,
        "description": REPO_DESCRIPTION,
        "private": False,
        "auto_init": False
    }).encode("utf-8")
    
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
            "User-Agent": "AI-Exam-Automation"
        }
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status == 201:
                return True, "Created repository"
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        if e.code == 422:
            return True, "Repository already exists"
        elif e.code == 404:
            return False, "Token lacks 'repo' scope"
        elif e.code == 401:
            return False, "Authentication failed"
        else:
            return False, f"API error HTTP {e.code}: {err_body}"
    except Exception as e:
        return False, f"Network error: {str(e)}"
        
    return True, "Ready"

def push_repository(repo_dir, token, username):
    git_env = os.environ.copy()
    git_env["GIT_TERMINAL_PROMPT"] = "0"
    git_env["GCM_INTERACTIVE"] = "never"
    
    auth_remote = f"https://{token}@github.com/{username}/{REPO_NAME}.git"
    clean_remote = f"https://github.com/{username}/{REPO_NAME}.git"
    
    try:
        subprocess.run(["git", "init"], cwd=repo_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        
        user_check = subprocess.run(["git", "config", "user.name"], cwd=repo_dir, stdout=subprocess.PIPE, text=True)
        if not user_check.stdout.strip():
            subprocess.run(["git", "config", "user.name", username], cwd=repo_dir, stdout=subprocess.PIPE, check=True)
            subprocess.run(["git", "config", "user.email", f"{username}@users.noreply.github.com"], cwd=repo_dir, stdout=subprocess.PIPE, check=True)
            
        subprocess.run(["git", "checkout", "-B", "main"], cwd=repo_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        subprocess.run(["git", "add", "."], cwd=repo_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        
        status_proc = subprocess.run(["git", "status", "--porcelain"], cwd=repo_dir, stdout=subprocess.PIPE, text=True)
        if status_proc.stdout.strip():
            commit_msg = "Complete AI and ML Practical Examination Solutions - CS-321-VSC-P"
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            
        subprocess.run(["git", "remote", "remove", "origin"], cwd=repo_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "remote", "add", "origin", auth_remote], cwd=repo_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        
        push_proc = subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=repo_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=git_env)
        
        subprocess.run(["git", "remote", "set-url", "origin", clean_remote], cwd=repo_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if push_proc.returncode != 0:
            return False, f"Push failed: {push_proc.stderr.strip()}"
            
        return True, "Repository pushed successfully"
    except Exception as e:
        subprocess.run(["git", "remote", "set-url", "origin", clean_remote], cwd=repo_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return False, f"Git error: {str(e)}"

def main():
    print("=" * 60)
    print("AI PRACTICAL REPOSITORY UPLOAD AUTOMATION")
    print(f"Target Repository: {REPO_NAME}")
    print("=" * 60)
    
    if len(sys.argv) > 1 and sys.argv[1] in ["--help", "-h"]:
        print("Usage: python upload_repository.py [YOUR_GITHUB_TOKEN]")
        print("Alternatively, provide token via GITHUB_TOKEN environment variable or interactive prompt.")
        sys.exit(0)
        
    token = get_token()
    if not token:
        print("Error: GitHub Personal Access Token is required.")
        print("Usage: python upload_repository.py <TOKEN>")
        print("   OR: set GITHUB_TOKEN environment variable")
        sys.exit(1)
        
    username, scopes = get_auth_user(token)
    if not username:
        print("Error: Authentication failed. Please verify your GitHub token.")
        sys.exit(1)
        
    print(f"Authenticated as: {username}")
    print(f"Token Scopes: {', '.join(scopes) if scopes else 'None'}")
    
    if scopes and not any(s in ['repo', 'public_repo'] for s in scopes):
        print("Error: Token lacks 'repo' or 'public_repo' scope!")
        sys.exit(1)
        
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.isdir(os.path.join(base_dir, "AI")):
        upload_dir = os.path.join(base_dir, "AI")
    else:
        upload_dir = base_dir
        
    print(f"Uploading files from: {upload_dir}")
    created, status_msg = create_or_check_repo(token, username)
    print(f"Remote repository status: {status_msg}")
    if not created:
        print(f"Error: {status_msg}")
        sys.exit(1)
        
    pushed, push_msg = push_repository(upload_dir, token, username)
    if pushed:
        print(f"SUCCESS: {push_msg}")
        print(f"Repository URL: https://github.com/{username}/{REPO_NAME}")
    else:
        print(f"ERROR: {push_msg}")
        sys.exit(1)

if __name__ == "__main__":
    main()
