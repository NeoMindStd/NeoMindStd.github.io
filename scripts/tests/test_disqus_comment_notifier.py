import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import disqus_comment_notifier as notifier


class DisqusCommentNotifierTest(unittest.TestCase):
    def test_strip_html_tags(self) -> None:
        text = notifier.strip_html_tags("<p>Hello&nbsp;<strong>World</strong>!</p>\n")
        self.assertEqual(text, "Hello World!")

    def test_normalize_comment_uses_thread_link(self) -> None:
        raw = {
            "id": "42",
            "createdAt": "2026-03-12T11:22:33",
            "message": "<p>Nice post!</p>",
            "author": {"name": "Neo"},
            "thread": {
                "title": "A Blog Post",
                "link": "https://neomindstd.github.io/posts/a-blog-post/",
            },
        }
        item = notifier.normalize_comment(raw, "https://neomindstd.github.io")
        self.assertIsNotNone(item)
        assert item is not None
        self.assertEqual(item.comment_id, "42")
        self.assertEqual(item.author_name, "Neo")
        self.assertEqual(item.thread_title, "A Blog Post")
        self.assertEqual(
            item.thread_link, "https://neomindstd.github.io/posts/a-blog-post/"
        )
        self.assertEqual(item.message, "Nice post!")

    def test_normalize_comment_falls_back_to_slug(self) -> None:
        raw = {
            "id": "100",
            "author": {"username": "guest"},
            "thread": {"title": "Fallback", "slug": "posts/fallback"},
            "message": "hello",
        }
        item = notifier.normalize_comment(raw, "https://neomindstd.github.io/")
        self.assertIsNotNone(item)
        assert item is not None
        self.assertEqual(item.thread_link, "https://neomindstd.github.io/posts/fallback/")

    def test_select_new_comments_filters_and_orders_old_to_new(self) -> None:
        items = [
            notifier.CommentItem(
                comment_id="3",
                created_at="2026-03-12T12:00:00",
                author_name="a",
                message="m",
                thread_title="t",
                thread_link="https://example.com/t",
            ),
            notifier.CommentItem(
                comment_id="2",
                created_at="2026-03-12T11:00:00",
                author_name="a",
                message="m",
                thread_title="t",
                thread_link="https://example.com/t",
            ),
            notifier.CommentItem(
                comment_id="1",
                created_at="2026-03-12T10:00:00",
                author_name="a",
                message="m",
                thread_title="t",
                thread_link="https://example.com/t",
            ),
        ]
        selected = notifier.select_new_comments(items, {"2"})
        self.assertEqual([item.comment_id for item in selected], ["1", "3"])

    def test_build_next_known_ids_uses_latest_first_without_duplicates(self) -> None:
        latest = [
            notifier.CommentItem(
                comment_id="7",
                created_at="2026-03-12T12:00:00",
                author_name="a",
                message="m",
                thread_title="t",
                thread_link="https://example.com/t",
            ),
            notifier.CommentItem(
                comment_id="6",
                created_at="2026-03-12T11:00:00",
                author_name="a",
                message="m",
                thread_title="t",
                thread_link="https://example.com/t",
            ),
        ]
        next_ids = notifier.build_next_known_ids(latest, ["6", "5", "4"], max_ids=4)
        self.assertEqual(next_ids, ["7", "6", "5", "4"])


if __name__ == "__main__":
    unittest.main()
