from fastapi import APIRouter
import requests
import os

router = APIRouter()


@router.get("/repository/{user_id}")
async def get_user_repo(user_id: str):

    url = f"https://api.github.com/users/{user_id}/repos"

    print(url)

    resp = requests.get(url)
    json_resp = resp.json()
    json_resp_updated = {
        "username": user_id,
        "number_of_public_repo": len(json_resp)
    }
    return json_resp_updated



@router.get("/repository/{user_id}/private")
async def get_user_private_repo(user_id: str):

    GITHUB_AUTH_TOKEN = os.getenv('GITHUB_AUTH_TOKEN')

    repo_name = "RMS"

    url = f"https://api.github.com/repos/{user_id}/{repo_name}"
    headers = {"Authorization": f"Bearer {GITHUB_AUTH_TOKEN}", 
               "Accept": "application/vnd.github.v3+json"}

    resp = requests.get(url, headers=headers)
    json_resp = resp.json()
    print(len(json_resp))

    return {"user": user_id, "url": url, "json_resp": json_resp}

