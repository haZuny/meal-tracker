"""R8 Release OCR 산출물 검증 스크립트의 회귀 테스트."""

from pathlib import Path
import tempfile
import unittest

import release_r8


class ReleaseR8Test(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        root = Path(self.directory.name)
        self.mapping_file = root / "mapping.txt"
        self.configuration_file = root / "configuration.txt"
        self.configuration_file.write_text(
            release_r8.REQUIRED_KEEP_RULE + "\n",
            encoding="utf-8",
        )

    def write_mapping(self, *, renamed=(), omitted=()):
        lines = []
        for index, class_name in enumerate(release_r8.REQUIRED_CLASSES):
            if class_name in omitted:
                continue
            target = f"a{index}" if class_name in renamed else class_name
            lines.append(f"{class_name} -> {target}:")
        self.mapping_file.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def test_accepts_kept_ocr_classes(self):
        self.write_mapping()

        release_r8.validate_release_outputs(self.mapping_file, self.configuration_file)

    def test_rejects_missing_keep_rule(self):
        self.write_mapping()
        self.configuration_file.write_text("", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "필수 규칙"):
            release_r8.validate_release_outputs(self.mapping_file, self.configuration_file)

    def test_rejects_removed_or_obfuscated_ocr_classes(self):
        self.write_mapping(renamed=(release_r8.REQUIRED_CLASSES[0],), omitted=(release_r8.REQUIRED_CLASSES[1],))

        with self.assertRaisesRegex(ValueError, "OCR 필수 클래스"):
            release_r8.validate_release_outputs(self.mapping_file, self.configuration_file)

    def test_rejects_missing_r8_outputs(self):
        with self.assertRaises(FileNotFoundError):
            release_r8.validate_release_outputs(self.mapping_file, self.configuration_file)


if __name__ == "__main__":
    unittest.main()
