import os
import re

# 사용자 레벨을 업데이트할 기준 파일 수와 대응하는 뱃지 URL을 정의합니다.
level_badges = {
    0: '<img src="https://img.shields.io/badge/LEVEL-0-lightgrey?style=flat-square" alt="Level 0"/>',
    1: '<img src="https://img.shields.io/badge/LEVEL-1-blue?style=flat-square" alt="Level 1"/>',
    2: '<img src="https://img.shields.io/badge/LEVEL-2-brightgreen?style=flat-square" alt="Level 2"/>',
    3: '<img src="https://img.shields.io/badge/LEVEL-3-orange?style=flat-square" alt="Level 3"/>',
    4: '<img src="https://img.shields.io/badge/LEVEL-4-red?style=flat-square" alt="Level 4"/>',
    5: '<img src="https://img.shields.io/badge/LEVEL-5-purple?style=flat-square" alt="Level 5"/>'
}

# 각 레벨에 해당하는 파일 수 범위를 정의합니다.
level_ranges = {
    0: (0, 0),
    1: (1, 20),
    2: (21, 40),
    3: (41, 60),
    4: (61, 80),
    5: (81, 100)
}

# README.md 파일을 업데이트하는 함수입니다.
def update_readme():
    readme_path = 'README.md'

    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()

    user_folders = [f for f in os.listdir('.') if os.path.isdir(f) and not f.startswith('.github')]

    for user in user_folders:
        file_count = sum(len(files) for _, _, files in os.walk(user))
        user_level = get_user_level(file_count)

        badge_pattern = re.compile(
            rf'<a href="https://github.com/{user}">\s*<img .*?\/>\s*<sub><b>{user}<\/b><\/sub>\s*<\/a>\s*<br\s*\/>\s*<img src=".*?" alt="Level \d"\/>',
            re.DOTALL
        )

        new_badge = (
            f'<a href="https://github.com/{user}">\n'
            f'      <img src="https://avatars.githubusercontent.com/{user}?v=4" width="100px;" alt=""/><br />\n'
            f'      <sub><b>{user}</b></sub>\n'
            f'    </a>\n'
            f'    <br />\n'
            f'    {level_badges[user_level]}'
        )

        content = re.sub(badge_pattern, new_badge, content)

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(content)

# 파일 수에 따른 사용자 레벨을 결정하는 함수입니다.
def get_user_level(file_count):
    for level, (min_files, max_files) in level_ranges.items():
        if min_files <= file_count <= max_files:
            return level
    return 0

if __name__ == "__main__":
    update_readme()
