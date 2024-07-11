import os
from github import Github

# 환경 변수에서 GitHub Token 가져오기
GITHUB_TOKEN = os.getenv('MY_GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable is not set.")
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
    contributor_data.append((contributor.login, level))

# README.md 파일 가져오기
readme = repo.get_readme()
readme_content = readme.decoded_content.decode('utf-8')

# 기존 기여자 섹션 삭제 및 새로운 내용 준비
start = readme_content.find("## ✅ 참여자와 진행도")
end = readme_content.find("## ✅ 소스코드 파일 이름 규칙")
if start == -1 or end == -1:
    raise ValueError("README.md does not contain the expected sections")

# 새로운 기여자 섹션 생성
new_contributors_section = "## ✅ 참여자와 진행도\n\n"
for login, level in contributor_data:
    new_contributors_section += f"- {login} (Level: {level})\n"

# 기존 내용 갱신
new_readme_content = readme_content[:start] + new_contributors_section + readme_content[end:]

# 업데이트된 README.md 파일 커밋 및 푸시
repo.update_file(readme.path, "Update README with contributors", new_readme_content, readme.sha)
