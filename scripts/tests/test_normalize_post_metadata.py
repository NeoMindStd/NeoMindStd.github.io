import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import normalize_post_metadata as normalizer


class NormalizePostMetadataTest(unittest.TestCase):
    def test_update_front_matter_inserts_description_after_excerpt(self) -> None:
        front = 'title: "t"\nexcerpt: "요약"\ncategories:\n  - 기타\n'
        updated, changed = normalizer.update_front_matter(front, "요약")
        self.assertTrue(changed)
        self.assertIn('excerpt: "요약"\ndescription: "요약"\n', updated)

    def test_process_file_skips_when_description_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "post.md"
            path.write_text(
                "---\n"
                'title: "t"\n'
                'excerpt: "요약"\n'
                'description: "이미 있음"\n'
                "---\nbody\n",
                encoding="utf-8",
            )
            result = normalizer.process_file(path, write=True)
            self.assertFalse(result.updated)
            self.assertEqual(result.reason, "skip:already_has_description")

    def test_process_file_updates_blank_description(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "post.md"
            path.write_text(
                "---\n"
                'title: "t"\n'
                'excerpt: "요약"\n'
                "description:\n"
                "---\nbody\n",
                encoding="utf-8",
            )
            result = normalizer.process_file(path, write=True)
            self.assertTrue(result.updated)
            self.assertEqual(result.reason, "updated")
            text = path.read_text(encoding="utf-8")
            self.assertIn('description: "요약"', text)


if __name__ == "__main__":
    unittest.main()
