import os
import re

# 사용자 레벨을 업데이트할 기준 파일 수와 대응하는 뱃지 URL을 정의
level_badges = {
    0: '<img src="https://img.shields.io/badge/LEVEL-0-lightgrey?style=flat-square" alt="Level 0"/>',
    1: '<img src="https://img.shields.io/badge/LEVEL-1-blue?style=flat-square" alt="Level 1"/>',
    2: '<img src="https://img.shields.io/badge/LEVEL-2-brightgreen?style=flat-square" alt="Level 2"/>',
    3: '<img src="https://img.shields.io/badge/LEVEL-3-orange?style=flat-square" alt="Level 3"/>',
    4: '<img src="https://img.shields.io/badge/LEVEL-4-red?style=flat-square" alt="Level 4"/>',
    5: '<img src="https://img.shields.io/badge/LEVEL-5-purple?style=flat-square" alt="Level 5"/>'
}

# 각 레벨에 해당하는 파일 수 범위를 정의
level_ranges = {
    0: (0, 0),
    1: (1, 20),
    2: (21, 40),
    3: (41, 60),
    4: (61, 80),
    5: (81, 100)
}

def get_user_level(file_count):
    """파일 수에 따른 사용자 레벨을 결정하는 함수."""
    for level, (min_files, max_files) in level_ranges.items():
        if min_files <= file_count <= max_files:
            return level
    return 0

def update_readme():
    """README.md 파일을 업데이트하는 함수."""
    readme_path = 'README.md'

    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 사용자 폴더와 파일 수를 수집
    user_data = []
    user_folders = [f for f in os.listdir('.') if os.path.isdir(f) and not f.startswith('.github')]
    for user in user_folders:
        file_count = sum(len(files) for _, _, files in os.walk(user))
        user_level = get_user_level(file_count)
        user_data.append((user, file_count, user_level))

    # 파일 수에 따라 내림차순으로 정렬
    user_data.sort(key=lambda x: x[1], reverse=True)

    # 테이블 시작 부분을 찾기 위한 패턴
    table_pattern = re.compile(r'(<table>.*?</table>)', re.DOTALL)
    table_match = table_pattern.search(content)
    if not table_match:
        print("Table not found in README.md")
        return

    # 기존 테이블 부분을 대체할 새로운 테이블 생성
    new_table = "<table>\n<tr>\n"
    for user, file_count, user_level in user_data:
        new_table += (
            f'  <td align="center">\n'
            f'    <a href="https://github.com/{user}">\n'
            f'      <img src="https://avatars.githubusercontent.com/{user}?v=4" width="100px;" alt=""/><br />\n'
            f'      <sub><b>{user}</b></sub>\n'
            f'    </a>\n'
            f'    <br />\n'
            f'    {level_badges[user_level]}\n'
            f'  </td>\n'
        )
    new_table += "</tr>\n</table>"

    # 기존 테이블을 새 테이블로 대체
    content = table_pattern.sub(new_table, content)

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    update_readme()
