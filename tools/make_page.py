"""Write docs/index.html (the public intro page) from the Escape From the Pit page's head/style.

usage: python -I make_page.py EFTP_INDEX_HTML OUT_HTML
"""
import sys

HEAD_REPL = [
    ('<title>Avernum: Escape From the Pit 日本語化パッチ</title>', '<title>Avernum 3: Ruined World 日本語化パッチ</title>'),
    ('「Avernum: Escape From the Pit」', '「Avernum 3: Ruined World」'),
    ('content="Avernum: Escape From the Pit 日本語化パッチ"', 'content="Avernum 3: Ruined World 日本語化パッチ"'),
    ('content="地下世界アヴァーナムを、日本語で。', 'content="災いに荒らされた地上世界ヴァロリムへ。アヴァーナムの冒険を、日本語で。'),
    ('https://higesho.github.io/avernum-efp-jp/img/worldmap.jpg', 'https://higesho.github.io/avernum3-rw-jp/img/worldmap.jpg'),
    ('--bg: #120f0c;', '--bg: #140d0b;'), ('--bg2: #1b1712;', '--bg2: #1d1310;'),
    ('--panel: #231d16;', '--panel: #261914;'), ('--line: #3a3026;', '--line: #43291f;'),
    ('--text: #e9e1d2;', '--text: #efe3d9;'), ('--muted: #b3a690;', '--muted: #bba596;'),
    ('--gold: #d9b26a;', '--gold: #e8935a;'), ('--gold2: #f0d79c;', '--gold2: #f6c39a;'),
    ('--accent: #7fb7a4;', '--accent: #9cc28a;'),
    ('rgba(18,15,12,.55) 0%, rgba(18,15,12,.82) 60%', 'rgba(20,13,11,.55) 0%, rgba(20,13,11,.84) 60%'),
    ('url("img/worldmap.jpg") center 30% / cover no-repeat;', 'url("img/worldmap.jpg") center 40% / cover no-repeat;'),
]

REPO = 'https://github.com/higesho/avernum3-rw-jp'
SHOTS = [
    ('worldmap.jpg', '地名を日本語にした大陸の地図', '大陸の地図', 'カーノルド地方・クリズサン地方などの地名を描き直し'),
]
STATS = [('17,624', '会話・本・イベントの文'), ('1,869', '人物・アイテム・呪文などの名前'),
         ('2,355', '地名・看板・場所の名前'), ('1,176', '画面・戦闘メッセージ')]


def body():
    shots = '\n'.join(f'''      <figure class="shot">
        <a href="img/{f}"><img src="img/{f}" alt="{alt}" loading="lazy"></a>
        <figcaption><b>{t}</b> — {c}</figcaption>
      </figure>''' for f, alt, t, c in SHOTS)
    stats = '\n'.join(f'      <div class="stat"><div class="num">{n}</div><div class="lbl">{l}</div></div>' for n, l in STATS)
    return f'''<body>

<header class="hero">
  <div class="wrap">
    <a class="parent-link" href="https://higesho.github.io/spiderweb-ja/">← スパイダーウェブ作品 日本語化（作品一覧）</a><br>
    <span class="eyebrow">非公式ファン翻訳 · ベータ版 v0.9.0</span>
    <h1>Avernum 3: Ruined World<small>日本語化パッチ</small></h1>
    <p class="lead">
      地下世界アヴァーナムの民が、ついに地上へ。異形の怪物と疫病に荒らされた帝国領ヴァロリムで、災いの源を突き止める——。
      Spiderweb Software の RPG を、会話・本・アイテム・画面・地図までほぼすべて日本語で遊べるようにするパッチです。
    </p>
    <div class="cta">
      <a class="btn btn-primary" href="{REPO}/releases/latest">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>
        パッチをダウンロード
      </a>
      <a class="btn btn-ghost" href="#install">インストール方法</a>
    </div>
    <p class="meta">Windows の Steam 版に対応 · ZIP 約 7MB · 元のゲームファイルは含みません</p>
  </div>
</header>

<main class="wrap">

  <section id="screens">
    <h2>日本語化した地図</h2>
    <div class="gallery" style="grid-template-columns:1fr">
{shots}
    </div>
  </section>

  <section id="features">
    <h2>日本語になるもの</h2>
    <div class="stats">
{stats}
    </div>
    <ul class="features">
      <li>すべての会話と選択肢、本やメモ、クエストの説明</li>
      <li>アイテム・呪文・スキル・特性・クリーチャーの名前と説明</li>
      <li>メニュー、ボタン、ツールチップ、戦闘ログなどの画面の文字</li>
      <li>町や地方の名前、看板、場所に入ったときの説明</li>
      <li>タイトル画面やパネル見出し、操作説明など、文字入りの画像</li>
      <li>ヴァロリム大陸の地図の地名と、導入の場面の地図</li>
    </ul>
    <p class="muted" style="margin-top:18px">
      「Avernum: Escape From the Pit」「Avernum 2: Crystal Souls」の日本語化パッチと同じ訳語でそろえています。
      日本語はメイリオ（変更可）で、英数字はゲーム本来のフォントで表示します。
    </p>
  </section>

  <section id="install">
    <h2>インストール方法</h2>
    <ol class="steps">
      <li>
        <h3>ダウンロード</h3>
        <p><a href="{REPO}/releases/latest">リリースページ</a>から <code>Avernum3RW_JP_v0.9.0.zip</code> をダウンロードし、展開します。</p>
      </li>
      <li>
        <h3>ゲームのフォルダにコピー</h3>
        <p>中身の <code>dsound.dll</code>・<code>avernum_jp.ini</code>・<code>avernum_jp</code> フォルダを、ゲームのフォルダ（<code>Avernum 3.exe</code> のある場所）にそのままコピーします。</p>
        <p class="muted">ゲームのフォルダは、Steam でゲームを右クリック →「管理」→「ローカルファイルを閲覧」で開けます。</p>
      </li>
      <li>
        <h3>Steam から起動</h3>
        <p>いつもどおり Steam からゲームを起動すれば日本語になります。初回の起動時に、お手元のゲームのファイルから日本語版のデータを作ります。</p>
      </li>
    </ol>
    <div class="note">
      ゲームの元のファイルは書き換えません。このパッチには元のゲームのファイルは入っておらず、お手元のファイルから日本語版のデータを作って
      <code>avernum_jp</code> フォルダに保存します。
    </div>
  </section>

  <section id="more">
    <h2>元に戻す・設定・注意</h2>
    <div class="cols">
      <div class="card">
        <h3>元に戻す</h3>
        <p>ゲームのフォルダから <code>dsound.dll</code>・<code>avernum_jp.ini</code>・<code>avernum_jp</code> フォルダを削除するだけで、英語版に戻ります。</p>
      </div>
      <div class="card">
        <h3>設定</h3>
        <p>ゲームフォルダの <code>avernum_jp.ini</code> で、日本語フォント・太さ・濃さ・大きさ・位置を変更できます。</p>
      </div>
    </div>
    <div class="note warn" style="margin-top:18px">
      <b>対応しているのは Steam 版です。</b>GOG 版・Humble 版など他のストアの版でも動くように作ってありますが、未確認です。
      対応できない版では日本語化を自動で止め、英語のまま普通に起動します。
      他のストアの版で試した方は、動いたかどうかを <code>avernum_jp\\avernum_jp.log</code> を添えて
      <a href="{REPO}/issues">Issues</a> でお知らせいただけると助かります。
    </div>
    <div class="cols">
      <div class="card">
        <h3>ベータ版について</h3>
        <ul>
          <li>誤訳や表示の崩れが残っていることがあります。</li>
          <li>起動時の解像度を選ぶ画面（Windows の標準の画面）は英語のままです。</li>
          <li>英語版のセーブデータを読み込むと、記録済みのメモやログは英語のまま表示されます。新しく始めるのがおすすめです。</li>
        </ul>
      </div>
      <div class="card">
        <h3>不具合・誤訳の報告</h3>
        <p>表示の崩れ、誤訳、不自然な言い回しなどは <a href="{REPO}/issues">GitHub の Issues</a> にお寄せください。
        どの場面か（町の名前、話し相手など）とスクリーンショットがあると助かります。</p>
      </div>
    </div>
  </section>

</main>

<footer>
  <div class="wrap">
    <p><a href="https://higesho.github.io/spiderweb-ja/">スパイダーウェブ作品 日本語化（作品一覧）</a></p>
    <p><a href="{REPO}">GitHub リポジトリ</a></p>
    <p>本パッチは非公式のファン翻訳であり、Spiderweb Software とは関係ありません。使用は自己責任でお願いします。</p>
    <p>Avernum は Spiderweb Software の商標です。スクリーンショット内のゲーム画像の権利は Spiderweb Software に帰属します。</p>
  </div>
</footer>

</body>
</html>
'''


def main(argv):
    src = open(argv[0], encoding='utf-8').read()
    head = src[:src.index('<body>')]
    for a, b in HEAD_REPL:
        if a not in head:
            raise SystemExit('not found: ' + a)
        head = head.replace(a, b)
    open(argv[1], 'w', encoding='utf-8').write(head + body())
    print('wrote', argv[1])


if __name__ == '__main__':
    main(sys.argv[1:])
