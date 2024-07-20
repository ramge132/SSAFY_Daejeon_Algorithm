import os

def get_file_count(folder_path):
    file_count = 0
    for root, dirs, files in os.walk(folder_path):
        file_count += len(files)
    return file_count

def determine_level(file_count):
    if file_count == 0:
        return 0
    elif 1 <= file_count <= 20:
        return 1
    elif 21 <= file_count <= 40:
        return 2
    elif 41 <= file_count <= 60:
        return 3
    elif 61 <= file_count <= 80:
        return 4
    elif 81 <= file_count <= 100:
        return 5
    else:
        return 5  # 파일 수가 100개를 넘으면 최대 레벨로 설정

def get_level_badge(level):
    badges = {
        0: '<img src="https://img.shields.io/badge/LEVEL-0-lightgrey?style=flat-square" alt="Level 0"/>',
        1: '<img src="https://img.shields.io/badge/LEVEL-1-blue?style=flat-square" alt="Level 1"/>',
        2: '<img src="https://img.shields.io/badge/LEVEL-2-brightgreen?style=flat-square" alt="Level 2"/>',
        3: '<img src="https://img.shields.io/badge/LEVEL-3-orange?style=flat-square" alt="Level 3"/>',
        4: '<img src="https://img.shields.io/badge/LEVEL-4-red?style=flat-square" alt="Level 4"/>',
        5: '<img src="https://img.shields.io/badge/LEVEL-5-purple?style=flat-square" alt="Level 5"/>',
    }
    return badges[level]

def update_readme(readme_path, user_levels):
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    start_idx = None
    end_idx = None
    for i, line in enumerate(content):
        if '<table>' in line:
            start_idx = i
        if '</table>' in line:
            end_idx = i
            break

    if start_idx is None or end_idx is None:
        print("README.md 파일의 <table> 태그를 찾을 수 없습니다.")
        return

    table_content = content[start_idx:end_idx + 1]
    updated_table_content = []

    for line in table_content:
        updated_line = line
        for user, level in user_levels.items():
            if f'<sub><b>{user}</b></sub>' in line:
                badge = get_level_badge(level)
                updated_line = line.split('<br />')[0] + '<br />\n    ' + badge + '\n  </td>'
        updated_table_content.append(updated_line)

    updated_content = content[:start_idx] + updated_table_content + content[end_idx + 1:]

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_content)

def main():
    base_path = './'  # 사용자 폴더들이 위치한 경로
    readme_path = 'README.md'
    
    user_levels = {}
    for user_folder in os.listdir(base_path):
        user_folder_path = os.path.join(base_path, user_folder)
        if os.path.isdir(user_folder_path) and not user_folder.startswith('.'):
            file_count = get_file_count(user_folder_path)
            level = determine_level(file_count)
            user_levels[user_folder] = level

    update_readme(readme_path, user_levels)

if __name__ == '__main__':
    main()
