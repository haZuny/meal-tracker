"""축소된 Release 산출물에서 OCR 초기화에 필요한 ML Kit 클래스를 확인한다."""

from pathlib import Path


REQUIRED_CLASSES = (
    "com.google.mlkit.vision.text.TextRecognition",
    "com.google.mlkit.vision.text.internal.TextRegistrar",
    "com.google.mlkit.vision.text.internal.zzo",
)
REQUIRED_KEEP_RULE = "-keep class com.google.mlkit.** { *; }"


def validate_release_outputs(mapping_file: Path, configuration_file: Path) -> None:
    """R8 병합 설정과 매핑 결과에서 ML Kit 보존 규칙 적용을 검증한다."""
    for output in (mapping_file, configuration_file):
        if not output.is_file():
            raise FileNotFoundError(f"R8 산출물을 찾을 수 없습니다: {output}")

    configuration = configuration_file.read_text(encoding="utf-8")
    if REQUIRED_KEEP_RULE not in configuration.splitlines():
        raise ValueError(f"R8 병합 설정에 필수 규칙이 없습니다: {REQUIRED_KEEP_RULE}")

    preserved_classes = set()
    for line in mapping_file.read_text(encoding="utf-8").splitlines():
        if " -> " not in line or not line.endswith(":"):
            continue
        original, obfuscated = line[:-1].split(" -> ", maxsplit=1)
        if original == obfuscated:
            preserved_classes.add(original)

    missing_classes = [name for name in REQUIRED_CLASSES if name not in preserved_classes]
    if missing_classes:
        names = ", ".join(missing_classes)
        raise ValueError(f"R8 Release 매핑에서 OCR 필수 클래스가 보존되지 않았습니다: {names}")


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    output_dir = root / "app/build/outputs/mapping/release"
    validate_release_outputs(
        output_dir / "mapping.txt",
        output_dir / "configuration.txt",
    )
    print("R8 Release OCR 클래스 보존 검증을 통과했습니다.")


if __name__ == "__main__":
    main()
