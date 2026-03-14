import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import generate_weekly_growth_review as review


class GenerateWeeklyGrowthReviewTest(unittest.TestCase):
    def test_render_includes_core_sections_and_top_pages(self) -> None:
        snapshot = {
            "config": {
                "windows": {
                    "last": {"start": "2026-02-13", "end": "2026-03-14"},
                    "prev": {"start": "2026-01-14", "end": "2026-02-12"},
                }
            },
            "ga4": {
                "properties": [
                    {
                        "display_name": "neomindstd.github.io - GA4",
                        "last_period": {
                            "values": {
                                "activeUsers": 100,
                                "sessions": 120,
                                "screenPageViews": 220,
                                "engagedSessions": 55,
                                "engagementRate": 0.51,
                            }
                        },
                        "prev_period": {
                            "values": {
                                "activeUsers": 80,
                                "sessions": 100,
                                "screenPageViews": 180,
                                "engagedSessions": 40,
                                "engagementRate": 0.40,
                            }
                        },
                        "top_content": {
                            "rows": [
                                {"dimension": "/", "views": 30},
                                {"dimension": "/기타/frontier-models-comparison-2026/", "views": 6},
                                {"dimension": "/tools/docker-guide/", "views": 5},
                            ]
                        },
                    }
                ]
            },
            "adsense": {
                "accounts": [
                    {
                        "reports": [
                            {
                                "domain": "neomindstd.github.io",
                                "last_period": {
                                    "earnings_usd": 0.10,
                                    "ctr": 0.75,
                                    "page_views": 150,
                                    "impressions": 500,
                                    "clicks": 4,
                                    "page_rpm": 0.5,
                                },
                                "prev_period": {
                                    "earnings_usd": 0.05,
                                    "ctr": 0.40,
                                    "page_views": 100,
                                    "impressions": 300,
                                    "clicks": 2,
                                    "page_rpm": 0.4,
                                },
                            }
                        ]
                    }
                ]
            },
        }

        output = review.render(snapshot)

        self.assertIn("# 블로그 주간 성장 리뷰", output)
        self.assertIn("## 블로그 KPI", output)
        self.assertIn("## 상위 랜딩 페이지", output)
        self.assertIn("/기타/frontier-models-comparison-2026/", output)
        self.assertIn("/tools/docker-guide/", output)
        self.assertIn("ai_referral_visit", output)


if __name__ == "__main__":
    unittest.main()
