"""End-of-batch term fixes: replace drifted translations with the decided ones (STYLE.md 8).

usage: python -I batch_fix.py TRANS_DIR
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
REPL = [('ラクシャサ', 'ラクシャーサ'), ('インファーナル', '業火魔'), ('速射の炎', 'クイックファイア'), ('母サラ', 'マザー・サラ'),
        ('地獄犬', 'ヘルハウンド'), ('レンター・イルノ', 'レンタール・イルノ'), ('ジグラット', 'ジッグラト'),
        ('チトラック', 'チトラッチ'), ('波刃の剣', 'ウェーブブレード'), ('障壁', '結界'),
        ('ヴァグ・オブ・トア', 'Vag Obb Tor'), ('ヴェル・ネル・セム', 'Vel Ner Sem'), ('クラリス母', 'マザー・クラリス'),
        ('スース＝サース', 'シュー・スサス'), ('スス・スサス', 'シュー・スサス'), ('コースタル', 'コスタール'),
        ('黒玉', 'オニキス'), ('パイロッグ', 'パイログ'), ('眼球獣', '眼獣'), ('アイビースト', '眼獣'), ('目玉獣', '眼獣'), ('テレポート増強装置', '転移増幅器'), ('霊気のプリズム', '霊のプリズム'), ('霊魂のプリズム', '霊のプリズム'), ('『Sss-Thsss』', '『シュー・スサス』'), ('異星', '異形'), ('ピログ', 'パイログ'), ('丘巨人', '丘の巨人'), ('スクリバーン', 'スクリバン'), ('オルノサ', 'オルノタ'), ('スクリバネ', 'スクリバン'), ('アテーム', 'アサメイ'), ('検疫', '封鎖'), ('第三帝国軍', '帝国第三軍'), ('峬', '岬'), ('クローのハードブレード', 'クロー・ハードブレード'), ('ミドリ州', 'ミドリ地方'), ('神聖な金の教会', '聖なる金銭教会')]
RX = [(re.compile(r'・ボク(?!ッ)'), '・ボック'), (re.compile(r'グラー・ホス(?!ー)'), 'グラー・ホース')]


def main(tdir):
    d = os.path.join(tdir, 'ja')
    n = 0
    for fn in os.listdir(d):
        if fn.endswith('__known.json'):
            continue
        p = os.path.join(d, fn)
        s = open(p, encoding='utf-8').read()
        o = s
        for a, b in REPL:
            s = s.replace(a, b)
        for rx, b in RX:
            s = rx.sub(b, s)
        if s != o:
            open(p, 'w', encoding='utf-8').write(s)
            n += 1
    print(f'{n} files fixed')


if __name__ == '__main__':
    main(sys.argv[1])
