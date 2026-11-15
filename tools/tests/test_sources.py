# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileCopyrightText: 2026 Dmitry Veremeev (BarabashkaD), https://github.com/BarabashkaD
"""docs/sources.md against the top tables of the computers' indexes."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def table_ids(text, stop_at_heading):
    """{ID: Home} of the table rows whose first cell is a bracket ID; with stop_at_heading, only
    the rows before the first '## ' heading (the top table of an index)."""
    out = {}
    for line in text.splitlines():
        if stop_at_heading and line.startswith("## "):
            break
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 2 and cells[0].startswith("[") and cells[0].endswith("]"):
            out[cells[0]] = cells[1]
    return out


def sources():
    return table_ids((ROOT / "docs" / "sources.md").read_text(encoding="utf-8"), False)


def indexes():
    return sorted((ROOT / "computers").glob("*/index.md"))


class Sources(unittest.TestCase):
    def test_indexes_exist(self):
        self.assertTrue(indexes())

    def test_every_index_id_registered(self):
        known = sources()
        for index in indexes():
            ids = table_ids(index.read_text(encoding="utf-8"), True)
            self.assertTrue(ids, index)
            missing = sorted(set(ids) - set(known))
            self.assertEqual(missing, [], "%s: not in docs/sources.md" % index.relative_to(ROOT))

    def test_homes_agree(self):
        """An index's own ID ('this index') has that index as its Home in docs/sources.md, and an
        ID registered with an index as its Home is in that index's top table as 'this index'."""
        known = sources()
        for index in indexes():
            rel = index.relative_to(ROOT).as_posix()
            ids = table_ids(index.read_text(encoding="utf-8"), True)
            for sid, home in ids.items():
                if home == "this index":
                    self.assertEqual(known.get(sid), rel, sid)
                else:
                    self.assertEqual(known.get(sid), home, sid)
            own = sorted(s for s, h in known.items() if h == rel)
            self.assertEqual(own, sorted(s for s, h in ids.items() if h == "this index"), rel)


if __name__ == "__main__":
    unittest.main()
