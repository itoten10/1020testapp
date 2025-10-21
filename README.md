# 🥚 ゆるキャラ育成ゲーム

Streamlit + Supabaseで作成したシンプルな育成ゲームアプリです。

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

## 🎮 主な機能

- **10種類の卵から選択**: 鳥系、ドラゴン系、海洋系、昆虫系、動物系、猫科系、恐竜系、魔法系、植物系、宇宙系
- **キャラクターに名前付け**: 自分だけのオリジナルキャラクターを育成
- **タップで育成**: 6段階の進化システム（卵→幼体→成長期→若年期→成体→伝説）
- **ステータス成長**: HP、攻撃力、防御力がタップで上昇
- **コレクション機能**: 育てたキャラクターを保存・共有
- **みんなのコレクション**: 全プレイヤーのキャラクターを閲覧可能
- **削除機能**: 不要なコレクションを削除
- **日本時間対応**: 登録日時をJSTで表示
- **スマホ対応**: レスポンシブデザイン

詳しいゲーム内容は [GAME_OVERVIEW.md](GAME_OVERVIEW.md) をご覧ください。

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

### 3. 環境変数の設定

Streamlit Cloudの場合、Settings > Secrets に以下を設定：

```toml
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_anon_key"
```

ローカル環境の場合、環境変数を設定：

```bash
export SUPABASE_URL="your_supabase_url"
export SUPABASE_KEY="your_supabase_anon_key"
```

### 4. Supabaseテーブルの作成

Supabaseダッシュボードで `setup_supabase.sql` の内容を実行してテーブルを作成してください。

### 5. アプリの起動

```bash
streamlit run app.py
```

## 📊 使用技術

- **Streamlit**: Webアプリケーションフレームワーク
- **Supabase**: バックエンドデータベース（PostgreSQL）
- **Python 3.8+**

## 🎯 遊び方

1. **卵を選ぶ**: 10種類から好きな卵を選択
2. **名前をつける**: キャラクターに名前をつける
3. **タップして育てる**: 💚ボタンをタップして成長させる
4. **コレクションに保存**: ⭐ボタンで完成したキャラクターを保存
5. **みんなのコレクションを見る**: 他のプレイヤーのキャラクターを閲覧

## 📝 キャラクター進化例

### 🐣 鳥系
| タップ数 | キャラクター | ステージ |
|---------|------------|---------|
| 0-9     | 🥚         | 卵      |
| 10-29   | 🐣         | ひよこ  |
| 30-59   | 🐥         | 成長ひよこ |
| 60-99   | 🐤         | 若鳥    |
| 100-149 | 🐓         | 成鳥    |
| 150+    | 🦅         | 伝説の鳥 |

### 🐉 ドラゴン系
🥚 → 🦎 幼竜 → 🐊 成長竜 → 🦕 若竜 → 🐉 ドラゴン → 🐲 神龍

### 🌟 宇宙系
🥚 → 🌑 月 → 🌍 惑星 → ☄️ 彗星 → ⭐ 恒星 → 🌟 超新星

## 📁 プロジェクト構成

```
counter_app2/
├── app.py                  # メインアプリケーション
├── requirements.txt        # Python依存パッケージ
├── setup_supabase.sql      # データベーススキーマ
├── README.md              # このファイル
├── GAME_OVERVIEW.md       # ゲーム詳細説明
└── .gitignore             # Git除外設定
```

## 🗄️ データベース構造

### game_progress テーブル
育成中のキャラクター進捗管理

### character_collection テーブル
完成したキャラクターのコレクション

詳細は [setup_supabase.sql](setup_supabase.sql) を参照

## 🔐 セキュリティ

- 環境変数を使用した認証情報の管理
- Supabase Row Level Security (RLS) による読み書き制限

## 📄 ライセンス

このプロジェクトはオープンソースです。

## 🙏 謝辞

- Streamlit コミュニティ
- Supabase チーム
- Claude Code

---

**🎮 今すぐプレイして、あなただけの最強キャラクターを育てよう！**
