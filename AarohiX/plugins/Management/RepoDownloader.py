from pyrogram import Client, filters
import git
import shutil
import os
from AarohiX import app

@app.on_message(filters.command(["اسرق جيتهاب"]))
def download_repo(_, message):
    if len(message.command) != 2:
        message.reply_text("يرجى تقديم لينك لمستودع GitHub بعد الأمر. مثال: اسرق جيتهاب + ريبو")
        return

    repo_url = message.command[1]
    zip_path = download_and_zip_repo(repo_url)

    if zip_path:
        with open(zip_path, "rb") as zip_file:
            message.reply_document(zip_file)
        os.remove(zip_path)
    else:
        message.reply_text("غير قادر على تنزيل مستودع GitHub المحدد.")

def download_and_zip_repo(repo_url):
    try:
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        repo_path = f"{repo_name}"
        
        repo = git.Repo.clone_from(repo_url, repo_path)
        shutil.make_archive(repo_path, 'zip', repo_path)

        return f"{repo_path}.zip"
    except Exception as e:
        print(f"خطأ في تنزيل وضغط مستودع GitHub: {e}")
        return None
    finally:
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)
