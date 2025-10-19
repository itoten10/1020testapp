# 🥚 ゆるキャラ育成ゲーム

Streamlit + Supabaseで作成したシンプルな育成ゲームアプリです。

## 🎮 特徴

- タップして卵からキャラクターを育成
- 成長段階に応じてキャラクターが進化（卵→ひよこ→鳥→伝説の鳥）
- ステータス管理（HP、攻撃力、防御力）
- Supabaseで進捗データを自動保存

## 🚀 セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/itoten10/1020testapp.git
cd counter_app2
```

### 2. 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

### 3. Supabaseテーブルの作成

Supabaseダッシュボードで `setup_supabase.sql` の内容を実行してテーブルを作成してください。

### 4. アプリの起動

```bash
streamlit run app.py
```

## 📊 使用技術

- **Streamlit**: Webアプリケーションフレームワーク
- **Supabase**: バックエンドデータベース（PostgreSQL）
- **Python 3.8+**

## 🎯 遊び方

1. 「💚 タップして育てる」ボタンをクリック
2. タップ数に応じてキャラクターが成長
3. ステータスが上昇していきます
4. リセットボタンで最初からやり直せます

## 📝 進化段階

| タップ数 | キャラクター | ステージ |
|---------|------------|---------|
| 0-9     | 🥚         | 卵      |
| 10-29   | 🐣         | ひよこ  |
| 30-59   | 🐥         | 成長ひよこ |
| 60-99   | 🐤         | 若鳥    |
| 100-149 | 🐓         | 成鳥    |
| 150+    | 🦅         | 伝説の鳥 |

## 🔧 環境変数

- Supabase URL: `https://kmurmgiuxvjwmxupnhsc.supabase.co`
- API Key: アプリ内にハードコーディング（本番環境では環境変数を使用推奨）
