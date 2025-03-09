# file_reader.py

def read_text_file(file_path):
    """
    텍스트 파일을 읽어서 각 줄을 리스트로 반환
    파일이 없거나, 오류가 발생하면 오류 메시지를 반환
    """
    print(file_path)
    try:
        file = open(file_path, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        return [line.strip() for line in lines]

        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except Exception as e:
            return [f"Error reading file -- file_reader.py : {e}"]