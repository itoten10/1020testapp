import streamlit as st
from supabase import create_client, Client
import os
from datetime import datetime

# Supabase設定（環境変数から取得）
SUPABASE_URL = st.secrets.get("SUPABASE_URL") or os.getenv("SUPABASE_URL")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY") or os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("⚠️ Supabaseの環境変数が設定されていません。Settings > Secrets で SUPABASE_URL と SUPABASE_KEY を設定してください。")
    st.stop()

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ページ設定
st.set_page_config(
    page_title="ゆるキャラ育成ゲーム",
    page_icon="🥚",
    layout="wide"
)

# 卵の種類定義
EGG_TYPES = {
    '鳥系': {
        'egg': '🥚',
        'stages': [
            {'min': 0, 'character': '🥚', 'stage': '卵', 'message': 'まだ卵の中だよ...'},
            {'min': 10, 'character': '🐣', 'stage': 'ひよこ', 'message': '生まれたばかりのひよこだよ！'},
            {'min': 30, 'character': '🐥', 'stage': '成長ひよこ', 'message': 'すくすく成長しているよ！'},
            {'min': 60, 'character': '🐤', 'stage': '若鳥', 'message': 'だんだん強くなってきたよ！'},
            {'min': 100, 'character': '🐓', 'stage': '成鳥', 'message': '立派な鳥になったよ！'},
            {'min': 150, 'character': '🦅', 'stage': '伝説の鳥', 'message': '伝説の存在になった！'},
        ]
    },
    'ドラゴン系': {
        'egg': '🥚',
        'stages': [
            {'min': 0, 'character': '🥚', 'stage': 'ドラゴンの卵', 'message': 'ドラゴンの卵だよ...'},
            {'min': 10, 'character': '🦎', 'stage': '幼竜', 'message': 'ドラゴンが孵化した！'},
            {'min': 30, 'character': '🐊', 'stage': '成長竜', 'message': 'どんどん強くなっている！'},
            {'min': 60, 'character': '🦕', 'stage': '若竜', 'message': '立派な竜になってきた！'},
            {'min': 100, 'character': '🐉', 'stage': 'ドラゴン', 'message': 'ついにドラゴンになった！'},
            {'min': 150, 'character': '🐲', 'stage': '神龍', 'message': '伝説の神龍になった！'},
        ]
    },
    '海洋系': {
        'egg': '🥚',
        'stages': [
            {'min': 0, 'character': '🥚', 'stage': '卵', 'message': '海の生物の卵だよ...'},
            {'min': 10, 'character': '🐟', 'stage': '小魚', 'message': '小さな魚が生まれた！'},
            {'min': 30, 'character': '🐠', 'stage': '熱帯魚', 'message': 'カラフルになった！'},
            {'min': 60, 'character': '🐡', 'stage': 'フグ', 'message': '膨らむようになった！'},
            {'min': 100, 'character': '🦈', 'stage': 'サメ', 'message': '海の王者だ！'},
            {'min': 150, 'character': '🐋', 'stage': 'クジラ', 'message': '海の伝説になった！'},
        ]
    },
    '昆虫系': {
        'egg': '🥚',
        'stages': [
            {'min': 0, 'character': '🥚', 'stage': '卵', 'message': '虫の卵だよ...'},
            {'min': 10, 'character': '🐛', 'stage': '幼虫', 'message': 'イモムシが生まれた！'},
            {'min': 30, 'character': '🐌', 'stage': '成虫', 'message': '殻を持つようになった！'},
            {'min': 60, 'character': '🦋', 'stage': '蝶', 'message': '美しい蝶になった！'},
            {'min': 100, 'character': '🐝', 'stage': '蜂', 'message': '働き者の蜂だ！'},
            {'min': 150, 'character': '🦗', 'stage': '伝説の昆虫', 'message': '伝説の昆虫になった！'},
        ]
    },
    '動物系': {
        'egg': '🥚',
        'stages': [
            {'min': 0, 'character': '🥚', 'stage': '卵', 'message': '動物の卵だよ...'},
            {'min': 10, 'character': '🐭', 'stage': 'ネズミ', 'message': '小さなネズミが生まれた！'},
            {'min': 30, 'character': '🐰', 'stage': 'ウサギ', 'message': 'ぴょんぴょん跳ねるよ！'},
            {'min': 60, 'character': '🦊', 'stage': 'キツネ', 'message': '賢いキツネになった！'},
            {'min': 100, 'character': '🐺', 'stage': 'オオカミ', 'message': '群れのリーダーだ！'},
            {'min': 150, 'character': '🦁', 'stage': 'ライオン', 'message': '百獣の王になった！'},
        ]
    },
    '猫科系': {
        'egg': '🥚',
        'stages': [
            {'min': 0, 'character': '🥚', 'stage': '卵', 'message': '猫科の卵だよ...'},
            {'min': 10, 'character': '🐱', 'stage': '子猫', 'message': 'かわいい子猫が生まれた！'},
            {'min': 30, 'character': '🐈', 'stage': '成猫', 'message': '立派な猫になった！'},
            {'min': 60, 'character': '🐆', 'stage': 'ヒョウ', 'message': '素早いヒョウだ！'},
            {'min': 100, 'character': '🐅', 'stage': 'トラ', 'message': '強力なトラになった！'},
            {'min': 150, 'character': '🦁', 'stage': 'ライオンキング', 'message': '王の中の王だ！'},
        ]
    },
    '恐竜系': {
        'egg': '🥚',
        'stages': [
            {'min': 0, 'character': '🥚', 'stage': '恐竜の卵', 'message': '恐竜の卵だよ...'},
            {'min': 10, 'character': '🦖', 'stage': 'ベビー恐竜', 'message': '恐竜が孵化した！'},
            {'min': 30, 'character': '🦕', 'stage': '草食恐竜', 'message': '大きくなってきた！'},
            {'min': 60, 'character': '🦖', 'stage': 'ティラノ', 'message': '肉食恐竜だ！'},
            {'min': 100, 'character': '🦕', 'stage': 'ブラキオ', 'message': '巨大恐竜だ！'},
            {'min': 150, 'character': '🦖', 'stage': '恐竜王', 'message': '恐竜の王になった！'},
        ]
    },
    '魔法系': {
        'egg': '🥚',
        'stages': [
            {'min': 0, 'character': '🥚', 'stage': '魔法の卵', 'message': '不思議な卵だよ...'},
            {'min': 10, 'character': '✨', 'stage': '光の精霊', 'message': 'キラキラ輝いている！'},
            {'min': 30, 'character': '🌟', 'stage': '星の精霊', 'message': '星の力を持つ！'},
            {'min': 60, 'character': '💫', 'stage': '魔法使い', 'message': '魔法が使えるぞ！'},
            {'min': 100, 'character': '🔮', 'stage': '賢者', 'message': '強力な魔法を操る！'},
            {'min': 150, 'character': '🌈', 'stage': '虹の守護者', 'message': '伝説の魔法使いだ！'},
        ]
    },
    '植物系': {
        'egg': '🥚',
        'stages': [
            {'min': 0, 'character': '🥚', 'stage': '種', 'message': '植物の種だよ...'},
            {'min': 10, 'character': '🌱', 'stage': '芽', 'message': '芽が出てきた！'},
            {'min': 30, 'character': '🌿', 'stage': '若葉', 'message': '葉が増えてきた！'},
            {'min': 60, 'character': '🌻', 'stage': '花', 'message': '美しい花が咲いた！'},
            {'min': 100, 'character': '🌳', 'stage': '大樹', 'message': '立派な木になった！'},
            {'min': 150, 'character': '🌲', 'stage': '世界樹', 'message': '伝説の世界樹だ！'},
        ]
    },
    '宇宙系': {
        'egg': '🥚',
        'stages': [
            {'min': 0, 'character': '🥚', 'stage': '宇宙の卵', 'message': '宇宙から来た卵だよ...'},
            {'min': 10, 'character': '🌑', 'stage': '月', 'message': '小さな月が生まれた！'},
            {'min': 30, 'character': '🌍', 'stage': '惑星', 'message': '惑星になった！'},
            {'min': 60, 'character': '☄️', 'stage': '彗星', 'message': '宇宙を駆ける彗星だ！'},
            {'min': 100, 'character': '⭐', 'stage': '恒星', 'message': '輝く星になった！'},
            {'min': 150, 'character': '🌟', 'stage': '超新星', 'message': '宇宙の伝説だ！'},
        ]
    },
}

# セッション状態の初期化
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.page = 'egg_selection'  # 'egg_selection', '育成', 'コレクション'
    st.session_state.egg_type = None
    st.session_state.tap_count = 0
    st.session_state.character = '🥚'
    st.session_state.stage = '卵'
    st.session_state.level = 0
    st.session_state.hp = 50
    st.session_state.attack = 10
    st.session_state.defense = 5
    st.session_state.message = 'まだ卵の中だよ...'
    st.session_state.character_name = ''
    st.session_state.progress_id = None

def calculate_status(tap_count, egg_type):
    """タップ数に応じてキャラクターのステータスを計算"""
    stages = EGG_TYPES[egg_type]['stages']

    current_stage = stages[0]
    for stage in stages:
        if tap_count >= stage['min']:
            current_stage = stage

    level = tap_count // 10
    hp = 50 + (tap_count * 3)
    attack = 10 + (tap_count * 2)
    defense = 5 + tap_count

    return {
        'character': current_stage['character'],
        'stage': current_stage['stage'],
        'level': level,
        'hp': hp,
        'attack': attack,
        'defense': defense,
        'message': current_stage['message']
    }

def save_progress_to_supabase(tap_count, stats, egg_type):
    """進捗をSupabaseに保存"""
    try:
        if st.session_state.progress_id is None:
            # 新規作成
            data = {
                'egg_type': egg_type,
                'tap_count': tap_count,
                'stage': stats['stage'],
                'level': stats['level'],
                'hp': stats['hp'],
                'attack': stats['attack'],
                'defense': stats['defense'],
                'character_name': st.session_state.character_name,
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }
            response = supabase.table('game_progress').insert(data).execute()
            if response.data:
                st.session_state.progress_id = response.data[0]['id']
        else:
            # 更新
            data = {
                'tap_count': tap_count,
                'stage': stats['stage'],
                'level': stats['level'],
                'hp': stats['hp'],
                'attack': stats['attack'],
                'defense': stats['defense'],
                'character_name': st.session_state.character_name,
                'updated_at': datetime.now().isoformat()
            }
            supabase.table('game_progress').update(data).eq('id', st.session_state.progress_id).execute()
        return True
    except Exception as e:
        st.error(f"保存エラー: {e}")
        return False

def save_to_collection():
    """コレクションに保存"""
    try:
        if not st.session_state.character_name.strip():
            st.error("名前を入力してください！")
            return False

        data = {
            'egg_type': st.session_state.egg_type,
            'character': st.session_state.character,
            'stage': st.session_state.stage,
            'level': st.session_state.level,
            'hp': st.session_state.hp,
            'attack': st.session_state.attack,
            'defense': st.session_state.defense,
            'tap_count': st.session_state.tap_count,
            'character_name': st.session_state.character_name.strip(),
            'created_at': datetime.now().isoformat()
        }
        supabase.table('character_collection').insert(data).execute()
        return True
    except Exception as e:
        st.error(f"コレクション保存エラー: {e}")
        return False

def on_tap():
    """タップ処理"""
    st.session_state.tap_count += 1
    stats = calculate_status(st.session_state.tap_count, st.session_state.egg_type)

    st.session_state.character = stats['character']
    st.session_state.stage = stats['stage']
    st.session_state.level = stats['level']
    st.session_state.hp = stats['hp']
    st.session_state.attack = stats['attack']
    st.session_state.defense = stats['defense']
    st.session_state.message = stats['message']

    save_progress_to_supabase(st.session_state.tap_count, stats, st.session_state.egg_type)

def reset_game():
    """ゲームリセット"""
    st.session_state.page = 'egg_selection'
    st.session_state.egg_type = None
    st.session_state.tap_count = 0
    st.session_state.character = '🥚'
    st.session_state.stage = '卵'
    st.session_state.level = 0
    st.session_state.hp = 50
    st.session_state.attack = 10
    st.session_state.defense = 5
    st.session_state.message = 'まだ卵の中だよ...'
    st.session_state.character_name = ''
    st.session_state.progress_id = None

# ======================
# 卵選択ページ
# ======================
if st.session_state.page == 'egg_selection':
    st.title('🥚 どの卵を育てる？')
    st.write('育てたい卵を選んでください！')

    # 卵選択を3列で表示
    cols = st.columns(3)
    for idx, (egg_name, egg_data) in enumerate(EGG_TYPES.items()):
        with cols[idx % 3]:
            st.markdown(f"### {egg_data['egg']} {egg_name}")
            final_stage = egg_data['stages'][-1]
            st.write(f"最終進化: {final_stage['character']} {final_stage['stage']}")

            if st.button(f"この卵を選ぶ", key=f"select_{egg_name}", use_container_width=True):
                # リセットして新しい卵を選択
                st.session_state.egg_type = egg_name
                st.session_state.character = egg_data['egg']
                st.session_state.stage = egg_data['stages'][0]['stage']
                st.session_state.message = egg_data['stages'][0]['message']
                st.session_state.tap_count = 0
                st.session_state.level = 0
                st.session_state.hp = 50
                st.session_state.attack = 10
                st.session_state.defense = 5
                st.session_state.character_name = ''
                st.session_state.progress_id = None
                st.session_state.page = '育成'
                st.rerun()

    st.divider()

    # コレクションへのリンク
    if st.button('📚 みんなのコレクションを見る', use_container_width=True, type='secondary'):
        st.session_state.page = 'コレクション'
        st.rerun()

# ======================
# 育成ページ
# ======================
elif st.session_state.page == '育成':
    # ヘッダー
    col1, col2, col3 = st.columns([2, 6, 2])
    with col1:
        if st.button('🏠 卵選択へ', use_container_width=True):
            if st.session_state.tap_count > 0:
                st.warning('育成中のキャラクターはリセットされます。本当によろしいですか？')
            reset_game()
            st.rerun()
    with col2:
        st.markdown(f"<h1 style='text-align: center;'>🥚 ゆるキャラ育成ゲーム</h1>", unsafe_allow_html=True)
    with col3:
        if st.button('📚 コレクション', use_container_width=True):
            st.session_state.page = 'コレクション'
            st.rerun()

    st.divider()

    # メインコンテンツ - 2列レイアウト（左: キャラクター＋タップ、右: ステータス）
    col_left, col_right = st.columns([1, 1])

    with col_left:
        # キャラクター表示
        st.markdown(f"<h1 style='text-align: center; font-size: 200px; margin: 0;'>{st.session_state.character}</h1>",
                    unsafe_allow_html=True)

        # ステージとレベル
        if st.session_state.character_name:
            st.markdown(f"<h2 style='text-align: center; margin: 5px 0;'>{st.session_state.character_name}</h2>",
                        unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; margin: 5px 0;'>{st.session_state.stage} (Lv.{st.session_state.level})</h3>",
                    unsafe_allow_html=True)

        # メッセージ
        st.markdown(f"<p style='text-align: center; color: green; font-size: 18px; margin: 10px 0;'>{st.session_state.message}</p>",
                    unsafe_allow_html=True)

        # タップボタン（キャラクターのすぐ下）
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button('💚 タップして育てる', use_container_width=True, type='primary', key='tap_button'):
            on_tap()
            st.rerun()

    with col_right:
        # 名前入力
        character_name = st.text_input(
            '名前をつけよう！',
            value=st.session_state.character_name,
            max_chars=20,
            placeholder='例: ぴよちゃん',
            key='name_input'
        )
        if character_name != st.session_state.character_name:
            st.session_state.character_name = character_name
            if st.session_state.progress_id:
                save_progress_to_supabase(
                    st.session_state.tap_count,
                    {
                        'stage': st.session_state.stage,
                        'level': st.session_state.level,
                        'hp': st.session_state.hp,
                        'attack': st.session_state.attack,
                        'defense': st.session_state.defense
                    },
                    st.session_state.egg_type
                )

        st.divider()

        # ステータス表示
        st.markdown("### 📊 ステータス")
        st.metric('❤️ HP', st.session_state.hp)
        st.metric('⚔️ 攻撃力', st.session_state.attack)
        st.metric('🛡️ 防御力', st.session_state.defense)

        st.divider()

        # タップ数表示
        st.markdown(f"**タップ数:** {st.session_state.tap_count}")

        st.divider()

        # コレクション保存ボタン
        if st.button('⭐ コレクションに保存', use_container_width=True, type='secondary'):
            if save_to_collection():
                st.success(f'「{st.session_state.character_name}」をコレクションに保存しました！')
                st.balloons()
                # リセットしてコレクションページへ遷移
                reset_game()
                st.session_state.page = 'コレクション'
                st.rerun()

# ======================
# コレクションページ
# ======================
elif st.session_state.page == 'コレクション':
    # ヘッダー
    col1, col2, col3 = st.columns([2, 6, 2])
    with col1:
        if st.button('🏠 卵選択へ', use_container_width=True):
            st.session_state.page = 'egg_selection'
            st.rerun()
    with col2:
        st.markdown("<h1 style='text-align: center;'>📚 みんなのコレクション</h1>", unsafe_allow_html=True)
    with col3:
        if st.button('🎮 育成へ', use_container_width=True):
            st.session_state.page = '育成'
            st.rerun()

    st.divider()

    # コレクション取得
    try:
        response = supabase.table('character_collection').select('*').order('created_at', desc=True).limit(50).execute()
        collections = response.data

        if collections:
            # 4列で表示
            cols = st.columns(4)
            for idx, item in enumerate(collections):
                with cols[idx % 4]:
                    with st.container():
                        st.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{item['character']}</h1>",
                                    unsafe_allow_html=True)
                        st.markdown(f"**{item['character_name']}**")
                        st.caption(f"{item['stage']} (Lv.{item['level']})")
                        st.caption(f"種族: {item['egg_type']}")
                        st.caption(f"❤️{item['hp']} ⚔️{item['attack']} 🛡️{item['defense']}")
                        st.caption(f"タップ数: {item['tap_count']}")

                        # 登録日時を表示
                        from datetime import datetime
                        created_at = datetime.fromisoformat(item['created_at'].replace('Z', '+00:00'))
                        st.caption(f"📅 {created_at.strftime('%Y/%m/%d %H:%M')}")
                        st.divider()
        else:
            st.info('まだコレクションがありません。最初のキャラクターを育ててコレクションに追加しましょう！')

    except Exception as e:
        st.error(f"コレクション取得エラー: {e}")
