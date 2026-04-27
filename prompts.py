"""VODコンパス - プロンプト定義"""

INTERNAL_LINK_PLACEHOLDER = "{{internal_link:関連トピック}}"
CONTENT_IMAGE_PLACEHOLDER = "{{content_image}}"

BLOG_PERSONA = 'VOD全社契約済みの映像オタクで、年間500本以上の作品を視聴するレビュアー'
TONE_GUIDANCE = '- 配信状況は流動的なため「2026年4月時点」など時期を明示\n- 月額・無料体験期間・同時視聴数などをわかりやすい比較表で\n- 視聴可能デバイス（Fire TV・Chromecast等）を具体的に\n- 作品ネタバレ配慮（必要なら警告表示）'

JSON_OUTPUT_SPEC = '''{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "hero_emoji": "🚀",
  "hero_gradient": "135deg",
  "image_search_query": "english keywords for image",
  "content_image_count": 4
}'''

def build_keyword_prompt(config):
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    return (
        f"{config.BLOG_NAME}用のキーワードを選定してください。\n\n"
        "以下のカテゴリから1つ選び、検索需要が高いキーワードを1つ提案してください。\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        "【選定基準】\n"
        "- ロングテールキーワード（3語以上）を優先\n"
        "- 比較系・疑問系・体験系を意識\n"
        "- 季節性・トレンドも考慮\n\n"
        "以下のJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )

def build_article_prompt(keyword, category, config):
    return (
        f"あなたは{BLOG_PERSONA}です。\n\n"
        f"【依頼】\nキーワード「{keyword}」（カテゴリ: {category}）について、\n"
        f"{config.BLOG_NAME}で公開する SEO最適化された日本語ブログ記事を1本生成してください。\n\n"
        f"【記事方針】\n{TONE_GUIDANCE}\n\n"
        "【SEO要件】\n"
        f"1. タイトルにキーワード「{keyword}」を含める（32文字以内）\n"
        "2. H2見出しを4〜6個、必要に応じてH3も使用\n"
        "3. メタディスクリプションは120文字以内\n"
        f"4. 内部リンクのプレースホルダーを2〜3箇所配置（{INTERNAL_LINK_PLACEHOLDER}）\n"
        "5. 各H2見出しの先頭に絵文字（例: ## 🔍 〜）\n\n"
        "【ビジュアル要件】\n"
        "- 比較表・ステップ表をMarkdownテーブルで積極使用\n"
        "- 「💡 ポイント」「⚠️ 注意」「✅ まとめ」を引用ブロック（>）で配置\n"
        f"- 各H2セクション間に画像プレースホルダー {CONTENT_IMAGE_PLACEHOLDER}（合計3〜5箇所）\n\n"
        "【出力形式】\n"
        "以下のJSON形式のみで出力（コードフェンスなし、説明文なし）:\n\n"
        f"{JSON_OUTPUT_SPEC}\n\n"
        "【厳守事項】\n"
        f"- 文字数 {config.MAX_ARTICLE_LENGTH}文字程度\n"
        "- tagsは5個ちょうど\n"
        "- slugは半角英数字とハイフンのみ\n"
        "- contentはMarkdownエスケープ済みのJSON文字列として有効に\n"
    )
