#!/usr/bin/env python3
"""GitHub Actions / ローカル両対応の自動記事生成スクリプト"""
import logging
import sys
from pathlib import Path

# パス解決:
#   ローカル: parent.parent.parent (007_自動投稿ブログ) に blog_engine/ がある
#   CI:       repo root に blog_engine/ をチェックアウト済（actions/checkout の path: blog_engine）
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent))  # for CI: blog_engine 親
sys.path.insert(0, str(HERE.parent.parent.parent))  # for ローカル

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

import config
import prompts

try:
    from blog_engine.generate_and_build import run
except ImportError as e:
    logger.error("blog_engine の import に失敗: %s", e)
    raise

if __name__ == "__main__":
    run(config, prompts)
