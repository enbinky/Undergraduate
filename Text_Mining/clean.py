import os
import re

folder_path = 'paper_pdf_library'  # 改成你的路径


def main():
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            name, ext = os.path.splitext(filename)
            new_name = clean_filename(name) + ext
            new_path = os.path.join(folder_path, new_name)
            try:
                os.rename(old_path, new_path)
            except Exception as e:
                print(f"❌ 找不到文件或路径超长: {filename}")
        else:
            print(f"❌ 找不到文件或路径超长: {filename}")
    print('任务完成')


def clean_filename(name):
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    name = name.replace(' ', '_')
    name = name.lower()
    return name[:150]  # 限制文件名长度防止超长


if __name__ == '__main__':
    main()
