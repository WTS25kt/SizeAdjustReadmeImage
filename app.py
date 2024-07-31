import os

# 画像が保存されているディレクトリ
image_dir = './readme-image'
# 出力するREADMEファイル
readme_file = 'README.md'
# 画像の幅
image_width = 600

def generate_readme(image_dir, readme_file, image_width):
    # 既存のREADMEファイルの内容を読み込む
    if os.path.exists(readme_file):
        with open(readme_file, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    else:
        readme_content = "# 画像一覧\n\n"

    # ディレクトリ内のファイルを取得
    for filename in os.listdir(image_dir):
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            # 画像のパス
            image_path = os.path.join(image_dir, filename)
            # <img>タグを生成
            img_tag = f'<img src="{image_path}" alt="{filename}" width="{image_width}">\n'
            # READMEの内容に追加
            readme_content += img_tag

    # READMEファイルに書き込む
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)

# スクリプトを実行
generate_readme(image_dir, readme_file, image_width)