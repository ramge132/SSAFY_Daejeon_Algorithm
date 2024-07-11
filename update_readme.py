import os
from github import Github

# 환경 변수에서 GitHub Token 가져오기
GITHUB_TOKEN = os.getenv('MY_GITHUB_TOKEN')
REPO_NAME = "ramge132/SSAFY_Daejeon_Algorithm"  # 저장소 이름으로 변경

# GitHub 클라이언트 초기화
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# 기여자 정보 가져오기
contributors = repo.get_contributors()
contributor_data = []

for contributor in contributors:
    # 기여자가 작성한 커밋 수 계산
    commits = repo.get_commits(author=contributor).totalCount
    # 레벨 계산
    level = min(commits // 10 + 1, 5)
    contributor_data.append((contributor.login, commits, level))

# README.md 파일 가져오기
readme = repo.get_readme()
readme_content = readme.decoded_content.decode('utf-8')

# 기존 기여자 섹션 삭제
start = readme_content.find("## ✅ 참여자와 진행도")
end = readme_content.find("## ✅ 소스코드 파일 이름 규칙")
new_content = readme_content[:start] + "## ✅ 참여자와 진행도\n\n"

# 새로운 기여자 섹션 추가
for login, commits, level in contributor_data:
    new_content += f"- {login} (Commits: {commits}, Level: {level})\n"

new_content += readme_content[end:]

# 업데이트된 README.md 파일 커밋 및 푸시
repo.update_file(readme.path, "Update README with contributors", new_content, readme.sha)
