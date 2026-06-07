from pathlib import Path


def find_md_files(folder_path):
    """주어진 폴더 안에서 .md 파일을 모두 찾아 목록으로 반환"""
    folder = Path(folder_path)
    
    if not folder.is_dir():
        print(f"폴더가 아니거나 존재하지 않음: {folder_path}")
        return []
    
    md_files = list(folder.glob("**/*.md"))
    return md_files


def main():
    # 본인 notes 폴더 경로 (본인 컴퓨터 기준으로 수정 필요)
    notes_folder = "ai-dev2026/notes"
    
    files = find_md_files(notes_folder)
    
    print(f"총 {len(files)}개의 마크다운 파일을 찾았습니다:\n")
    for f in files:
        print(f"  - {f}")


if __name__ == "__main__":
    main()
