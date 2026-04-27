"""VODコンパス - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "VODコンパス"
BLOG_DESCRIPTION = "U-NEXT・Hulu・Netflix・Amazon Prime・Disney+ など主要VODを徹底比較。料金・配信作品・無料体験・視聴デバイスを網羅、目的別おすすめサービスを提案。"
BLOG_URL = "https://musclelove-777.github.io/vod-compass/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/vod-compass"

TARGET_CATEGORIES = [
    "VODサービス比較",
    "料金プラン徹底解説",
    "配信ジャンル別おすすめ",
    "視聴デバイス・テレビ接続",
    "無料体験・キャンペーン",
    "解約・乗り換えガイド",
    "話題作レビュー",
    "アニメ・映画・ドラマ特集",
]

THEME = {
    "primary": "#0f1419",
    "accent": "#e50914",
    "gradient_start": "#0f1419",
    "gradient_end": "#e50914",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
