import os
import re

def count_files(user_dir):
    total_files = 0
    for root, dirs, files in os.walk(user_dir):
        total_files += len([file for file in files if not file.startswith('.')])
    return total_files

def determine_level(file_count):
    if file_count == 0:
        return 0
    elif file_count <= 20:
        return 1
    elif file_count <= 40:
        return 2
    elif file_count <= 60:
        return 3
    elif file_count <= 80:
        return 4
    elif file_count <= 100:
        return 5
    else:
        return 5

def get_level_badge(level):
    if level == 1:
        return '<img src="https://img.shields.io/badge/LEVEL-1-blue?style=flat-square" alt="Level 1"/>'
    elif level == 2:
        return '<img src="https://img.shields.io/badge/LEVEL-2-brightgreen?style=flat-square" alt="Level 2"/>'
    elif level == 3:
        return '<img src="https://img.shields.io/badge/LEVEL-3-orange?style=flat-square" alt="Level 3"/>'
    elif level == 4:
        return '<img src="https://img.shields.io/badge/LEVEL-4-red?style=flat-square" alt="Level 4"/>'
    elif level == 5:
        return '<img src="https://img.shields.io/badge/LEVEL-5-purple?style=flat-square" alt="Level 5"/>'
    else:
        return '<img src="https://img.shields.io/badge/LEVEL-0-lightgrey?style=flat-square" alt="Level 0"/>'

def update_readme(readme_path, user_levels):
    with open(readme_path, 'r') as file:
        content = file.read()

    for user, level in user_levels.items():
        badge = get_level_badge(level)
        content = re.sub(
            rf'(<sub><b>{user}</b></sub>\s*<br\s*/>\s*<img src="https://img\.shields\.io/badge/LEVEL-)[^"]*(")',
            rf'\1{level}-{badge.split("-")[2]}\2',
            content
        )

    with open(readme_path, 'w') as file:
        file.write(content)

def main():
    base_dir = '.'
    readme_path = os.path.join(base_dir, 'README.md')
    user_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(d) and not d.startswith('.')]

    user_levels = {}
    for user_dir in user_dirs:
        file_count = count_files(user_dir)
        level = determine_level(file_count)
        user_levels[user_dir] = level

    update_readme(readme_path, user_levels)

if __name__ == "__main__":
    main()
