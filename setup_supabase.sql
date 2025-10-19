-- ゆるキャラ育成ゲーム用テーブル作成

-- 育成中のキャラクター進捗管理テーブル
CREATE TABLE IF NOT EXISTS game_progress (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    egg_type TEXT NOT NULL,
    tap_count INTEGER DEFAULT 0,
    stage TEXT DEFAULT '卵',
    level INTEGER DEFAULT 0,
    hp INTEGER DEFAULT 50,
    attack INTEGER DEFAULT 10,
    defense INTEGER DEFAULT 5,
    character_name TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- コレクション（完成したキャラクター）テーブル
CREATE TABLE IF NOT EXISTS character_collection (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    egg_type TEXT NOT NULL,
    character TEXT NOT NULL,
    character_name TEXT NOT NULL,
    stage TEXT NOT NULL,
    level INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    tap_count INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- インデックス作成
CREATE INDEX IF NOT EXISTS idx_game_progress_created_at ON game_progress(created_at);
CREATE INDEX IF NOT EXISTS idx_game_progress_updated_at ON game_progress(updated_at);
CREATE INDEX IF NOT EXISTS idx_character_collection_created_at ON character_collection(created_at);
CREATE INDEX IF NOT EXISTS idx_character_collection_egg_type ON character_collection(egg_type);

-- RLS (Row Level Security) の設定
ALTER TABLE game_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE character_collection ENABLE ROW LEVEL SECURITY;

-- game_progressテーブル: 匿名ユーザーでも読み書き可能
CREATE POLICY "Enable read access for all users on game_progress" ON game_progress
    FOR SELECT USING (true);

CREATE POLICY "Enable insert access for all users on game_progress" ON game_progress
    FOR INSERT WITH CHECK (true);

CREATE POLICY "Enable update access for all users on game_progress" ON game_progress
    FOR UPDATE USING (true);

CREATE POLICY "Enable delete access for all users on game_progress" ON game_progress
    FOR DELETE USING (true);

-- character_collectionテーブル: 誰でも読めるが、書き込みも可能
CREATE POLICY "Enable read access for all users on collection" ON character_collection
    FOR SELECT USING (true);

CREATE POLICY "Enable insert access for all users on collection" ON character_collection
    FOR INSERT WITH CHECK (true);

CREATE POLICY "Enable update access for all users on collection" ON character_collection
    FOR UPDATE USING (true);

CREATE POLICY "Enable delete access for all users on collection" ON character_collection
    FOR DELETE USING (true);
