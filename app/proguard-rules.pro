# ML Kit은 Firebase 컴포넌트 그래프와 메타데이터를 통해 내부 구현을 찾는다.
# OCR 런타임 의존성 그래프를 R8 축소 과정에서 제거하지 않도록 보존한다.
-keep class com.google.mlkit.** { *; }
