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
    """파일 수에 따른 사용자 레벨을 결정하는 함수"""
    for level, (min_files, max_files) in level_ranges.items():
        if min_files <= file_count <= max_files:
            return level
    return 0

def update_readme():
    """README.md 파일을 업데이트하는 함수"""
    readme_path = 'README.md'  # README.md 파일 경로

    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()  # README.md 파일 내용 읽기

    # 사용자 폴더와 파일 수를 수집
    user_data = []
    # 제외할 폴더 리스트
    excluded_folders = {'.git', '.github', '.source'}
    # 현재 디렉토리에서 제외할 폴더를 제외한 모든 폴더를 사용자 폴더로 간주
    user_folders = [f for f in os.listdir('.') if os.path.isdir(f) and f not in excluded_folders]
    for user in user_folders:
        # 사용자의 폴더 내 파일 수 계산
        file_count = sum(len(files) for _, _, files in os.walk(user))
        user_level = get_user_level(file_count)  # 파일 수에 따른 사용자 레벨 결정
        user_data.append((user, file_count, user_level))  # 사용자 데이터에 추가

    # 파일 수에 따라 내림차순으로 정렬
    user_data.sort(key=lambda x: x[1], reverse=True)

    # 테이블 시작 부분을 찾기 위한 패턴
    table_pattern = re.compile(r'(<table>.*?</table>)', re.DOTALL)
    table_match = table_pattern.search(content)
    if not table_match:
        print("Table not found in README.md")  # 테이블을 찾지 못한 경우 메시지 출력
        return False  # 테이블을 찾지 못하면 False 반환

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
    new_content = table_pattern.sub(new_table, content)

    # 새로운 내용이 기존 내용과 다른 경우 파일을 다시 씀
    if new_content != content:
        with open(readme_path, 'w', encoding='utf-8') as file:
            file.write(new_content)  # 새로운 내용을 README.md 파일에 씀
        return True  # 변경 사항이 있으면 True 반환
    return False  # 변경 사항이 없으면 False 반환

if __name__ == "__main__":
    if update_readme():
        print("README.md updated")  # 변경 사항이 있으면 메시지 출력
    else:
        print("No changes to README.md")  # 변경 사항이 없으면 메시지 출력
