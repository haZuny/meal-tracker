# NoshNote Google Play 출시 준비 자료

기준일: 2026-10-13  
기준 앱 버전: `1.0.2` (`versionCode` 3, `applicationId` `com.hazuny.noshnote`)  
초기 스토어 언어 제안: 한국어(대한민국)

이 문서는 현재 저장소 코드와 공식 Google Play 안내를 기준으로 만든 제출 초안이다. 대괄호 항목과 Play Console의 실제 상태를 확인한 뒤 제출한다.

## 1. 현재 상태와 출시 순서

- 앱 모듈은 `targetSdk 37`을 사용한다. 2026-08-31부터 신규 앱 제출에 필요한 API 36 이상을 충족한다.
- 현재 기본 브랜치 버전은 `1.0.2` / `versionCode 3`이다. Play에 먼저 업로드하는 번들도 code 3을 사용하고, 다음 업데이트부터 매번 증가시킨다.
- `.github/workflows/release.yml`은 `v1.0.2` 태그로 서명 APK와 AAB를 생성하는 흐름이다. 배포 파이프라인 문서에 적힌 서명 키를 계속 사용할지, Play Console에 등록한 키와 실제 GitHub Release의 인증서가 일치하는지 확인한다.
- 로컬 `app/release/app-release.apk`는 `output-metadata.json` 기준 `1.0.0` / code 1이다. 현재 제출 파일로 사용하지 않는다.
- 로컬에서 `bundleRelease`를 실행해 `app/build/outputs/bundle/release/app-release.aab`를 만들었다. 현재 환경에는 릴리스 서명 정보가 없어 이 AAB는 **unsigned**이며 Play 업로드에 사용할 수 없다. 서명된 `NoshNote-v1.0.2.aab`를 Release 초안 또는 Actions 산출물에서 확보하고 인증서 지문을 확인해야 한다.
- Play Console에서 앱을 `com.hazuny.noshnote`로 생성했는지 확인한다. 패키지명은 최초 생성 뒤 변경할 수 없으므로 정확히 일치시킨다.

### 계정에 따른 테스트 요건

개발자 계정은 **2023-11-13 이후 생성된 개인 계정**이다. Google Play의 현재 요건에 따라 공개 전 다음 절차를 거친다.

1. 내부 테스트 트랙에서 소수의 기기로 빠르게 설치·기능을 확인한다. 내부 테스트는 공개 자격 요건을 대신하지 않는다.
2. 앱 설정을 완료하고 비공개 테스트 트랙을 연다.
3. 테스터 최소 12명이 14일 동안 연속으로 참여 상태를 유지하도록 안내한다. 중간에 참여를 취소한 기간은 연속 일수에 포함되지 않는다.
4. 비공개 테스트 종료 후 Play Console 대시보드에서 프로덕션 액세스를 신청하고 테스트·앱 준비 질문에 답한다.
5. 프로덕션 액세스가 승인된 뒤 공개 출시를 진행한다.

## 2. 스토어 등록 문안 초안

초기 등록은 한국어(대한민국)를 기본으로 한다. 문안은 기능을 과장하지 않고, 수동 입력이 항상 가능하며 OCR 결과를 사용자가 확인한다는 점을 드러낸다.

### 한국어(대한민국)

- 앱 이름: `NoshNote` (30자 제한 이내)
- 짧은 설명: `먹은 음식의 칼로리와 단백질을 기록하고 목표와 비교해 보세요.`
- 전체 설명:

```text
먹은 음식을 간단히 기록하고, 하루 칼로리와 단백질 섭취량을 목표와 비교해 보세요.

• 음식 이름과 먹은 양, 칼로리, 단백질을 직접 입력해 바로 기록할 수 있어요.
• 자주 먹는 음식은 템플릿으로 저장해 다음 기록에서 다시 사용할 수 있어요.
• 날짜별 기록과 하루 합계를 확인하고, 달력에서 지난 기록을 살펴볼 수 있어요.
• 영양성분표를 카메라로 비추면 칼로리와 단백질 입력을 도와줘요. 인식한 값은 확인하고 수정한 뒤 적용할 수 있어요.
• 식단 기록, 음식 템플릿, 목표를 JSON 파일로 내보내고 복원할 수 있어요.

NoshNote는 식단 기록을 위한 도구이며 의료 진단이나 치료를 제공하지 않습니다. 영양성분표 인식 결과는 직접 확인해 주세요.

기록과 목표는 기기에 저장됩니다. 앱을 삭제하거나 기기를 바꾸기 전 설정에서 JSON 백업을 내보내세요. JSON 가져오기는 현재 앱 데이터를 교체합니다.
```

### 영어(미국) 번역 초안

- App name: `NoshNote`
- Short description: `Log meals, track calories and protein, and compare them with your goals.`
- Full description:

```text
Log what you eat and compare your daily calorie and protein intake with your goals.

• Add a meal by entering its name, amount, calories, and protein.
• Save foods you eat often as templates and reuse them later.
• Review daily totals and past entries in the calendar.
• Point your camera at a nutrition label to help enter calories and protein. Review and edit recognized values before applying them.
• Export and restore meal entries, food templates, and goals as a JSON file.

NoshNote is a meal logging tool. It does not provide medical diagnosis or treatment. Please verify nutrition values recognized from labels.

Entries and goals are stored on your device. Export a JSON backup in Settings before uninstalling the app or changing devices. Importing a backup replaces the current app data.
```

## 3. 스토어 그래픽과 화면 캡처

Google Play 문서상 등록 기본 요건은 다음과 같다.

| 파일 | 준비 요건 | NoshNote 준비 상태 |
|---|---|---|
| 앱 아이콘 | PNG 512×512, 불투명 배경 | [`app-icon-512.png`](play-store-assets/app-icon-512.png) 준비 완료 |
| 기능 그래픽 | PNG/JPEG 1024×500, 투명도 없음 | [`feature-graphic-1024x500.png`](play-store-assets/feature-graphic-1024x500.png) 준비 완료 |
| 휴대전화 스크린샷 | 최소 2장, JPG/24-bit PNG, 각 변 320–3840 px, 긴 변은 짧은 변의 2배 이하 | 1080×2160 실제 앱 화면 4장 준비 완료 |
| 추천 노출용 스크린샷 | 세로 1080×1920 이상 4장 권장 | 아래 화면 중 4장을 캡처했으며 모두 최대 2:1 비율을 충족 |

캡처 파일은 [스토어 이미지 폴더](play-store-assets/)에 있다: 홈(`01-home.png`), 바로 기록(`02-quick-entry.png`), 달력(`03-calendar.png`), 설정(`04-settings.png`). 테스트용 식단 예시가 화면에 보인다. OCR 인식 결과 화면은 실제 라벨을 대상으로 추가 캡처하면 된다.

화면 캡처는 실제 앱 UI를 보여야 한다. 한국어 등록을 우선해 캡처 언어를 한국어로 맞췄다. 현재 캡처의 식단 기록은 스토어 미리보기용 합성 데이터다.

## 4. Play Console 선언 초안

앱 코드 및 의존성 검토 결과를 기준으로 한 초안이다. Play Console의 각 질문은 게시할 최종 AAB와 모든 포함 SDK를 다시 확인한 뒤 답한다.

| 섹션 | 초안 응답 | 근거 / 확인 사항 |
|---|---|---|
| 앱 카테고리 | Health & Fitness | 식단 섭취량 및 영양 목표를 기록하는 기능 |
| 광고 | 아니요 | 광고 SDK와 광고 표시 코드가 저장소에서 확인되지 않음 |
| 앱 액세스 | 제한 없음 | 계정 또는 로그인 절차 없음 |
| 건강 앱 선언 | Health and fitness → Nutrition and Weight Management | 음식 섭취와 영양 목표 추적 기능이 해당 범주에 포함됨 |
| 의료 기능 | 없음 | 진단, 치료, 처방, 임상 의사결정, 의료기기 기능 없음. 의료 효과를 주장하지 않음 |
| 데이터 안전성: 수집 | 예 — 앱 정보 및 성능(진단), 기기 또는 기타 ID | ML Kit Android SDK는 진단·사용 통계로 기기/앱 정보, 설치별 식별자, 처리 지연, API 설정, 입력·출력 크기, 이벤트 종류, 오류 코드를 Google에 보낼 수 있다고 공개함 |
| 데이터 안전성: 공유 | 아니요(현재 SDK 자료 기준) | ML Kit는 이 통계를 제3자에게 전송하지 않는다고 안내함. JSON 내보내기는 사용자가 Android 파일 선택기에서 직접 시작하며, 선택한 다른 앱/저장소는 해당 업체 정책 적용 |
| 전송 중 암호화 | 예 — ML Kit 통계 | Google ML Kit는 해당 수집 데이터가 HTTPS로 암호화된다고 안내함 |
| 수집 목적 | Analytics / 진단 | Play Console에서 ML Kit 측의 진단·사용 통계 목적을 가장 잘 맞는 항목으로 매핑하고 선택 범위를 검토 |
| 사용자 입력 식단·목표·OCR 이미지 | 수집하지 않음(현재 구현 기준) | Room 로컬 저장과 카메라 OCR은 기기에서 처리. ML Kit는 입력 이미지·영상·텍스트와 결과물을 Google 서버에 보내지 않는다고 명시함 |
| 계정 삭제 URL | 해당 없음 | 앱 계정을 만들거나 서버 계정 데이터를 보유하지 않음 |
| 콘텐츠 등급 | IARC 설문 완료 필요 | 앱 기능, 광고 없음, 채팅·사용자 간 콘텐츠 공유 없음으로 답변 |
| 타깃 연령 | 개발자 확인 필요 | 어린이를 대상으로 설계한 앱인지 실제 제품 의도에 맞게 선택. 임의로 어린이 연령을 포함하지 않음 |
| 개인정보처리방침 | 공개 URL 필요 + 앱 내 링크 또는 전문 필요 | 건강 관련 기능 앱 정책에 따라 등록 페이지 및 앱에서 접근 가능하게 제공 |

영양 기록과 목표는 개인 건강·식생활 맥락의 데이터다. 저장소 기준으로 로컬 처리만 한다고 해서 개인정보처리방침과 건강 앱 선언이 면제되지는 않는다. ML Kit 자료상 앱 입력(이미지·영상·텍스트)과 인식 결과는 기기 밖으로 전송되지 않지만, SDK 진단·사용 통계는 Google로 전송될 수 있다. 앱 입력을 로컬 처리한다는 이유로 Data safety 응답을 “수집 없음”으로 표시하면 안 된다. 최종 AAB와 포함 SDK를 확인해 응답을 확정한다.

### 계정 유형 검토 — 공개 전 확인 필요

현재 계정은 2023-11-13 이후 생성된 개인 계정이다. Google Play 계정 유형 안내는 건강 앱을 조직 계정이 필요한 서비스로 안내하고, Play 건강 앱 범주에는 영양·체중 관리 앱이 포함된다. 이 공식 문서들을 함께 읽으면 NoshNote는 조직 계정 요건에 걸릴 가능성이 높다. **프로덕션 공개 전 Play Console 지원에 NoshNote의 `Nutrition and Weight Management` 범주가 개인 계정으로 게시 가능한지 확인하고, 조직 계정 전환이 필요하면 계정·앱 등록을 먼저 해결한다.** 확인 전에는 공개 제출 또는 14일 비공개 테스트 시작을 보류한다. 개인 계정 테스트 요건은 계정 유형 문제가 해결된 뒤에도 적용될 수 있다.

## 5. 개인정보처리방침 초안 상태

기기 내 저장, 카메라 OCR, JSON 백업을 설명하는 한국어 초안을 [개인정보처리방침 초안](play-store-privacy-policy-draft.md)에 둔다. 제출 전에 다음을 채우고 공개해야 한다.

- 게시자/개발자 표시 이름: `[Play Console에 표시될 개발자 이름]`
- 지원 이메일: `[사용자 제공 예정]`
- 공개 URL: `[사용자 제공 예정]`
- 앱 내에서 해당 정책을 열 수 있는 항목 또는 전문: 현재 앱에 추가 필요

정책 URL은 로그인 없이 공개적으로 열리고, 지역 제한이 없으며, PDF가 아닌 수정 가능한 텍스트 웹 페이지여야 한다. URL을 받으면 앱 설정에 개인정보처리방침 접근 경로를 추가하고, 지원 언어 리소스를 확인한다.

## 6. 서명·AAB 업로드 점검

1. Play Console에서 앱을 `com.hazuny.noshnote`로 생성한다.
2. Play App Signing 단계에서 기존 앱 서명 키를 제공하는 계획이라면 문서의 PEPK 절차를 사용한다. 업로드 키/앱 서명 키 선택 사항은 Play Console에 표시된 지문과 GitHub Release 메타데이터를 대조해 결정한다.
3. `v1.0.2` Release 산출물의 `signingCertificateSha256`를 확인하고 Play Console의 앱 서명 인증서 지문과 일치 여부를 기록한다.
4. AAB의 `applicationId`, `versionName`, `versionCode`, `targetSdk`를 확인한다.
5. AAB를 내부 테스트에 업로드해 배포한다. Android 37을 대상으로 하는 현재 앱은 Android 16/API 36 신규 제출 기준 이상이다.
6. 테스터 설치 링크로 실제 설치, 첫 실행, 식단 추가·수정·삭제, 목표, 날짜 탐색, 카메라 권한 거부와 승인, OCR 결과 수정, JSON 백업/복원을 확인한다.
7. 개인 계정 요건을 위해 비공개 테스트를 별도로 시작하고 최소 12명의 연속 참여 기간을 기록한다.

## 7. 사용자 확인이 필요한 항목

- 스토어 공개 지원 이메일과 개인정보처리방침 URL
- 최초 공개 국가/지역 및 기본 스토어 언어 (현재 초안은 대한민국/한국어)
- 타깃 연령 (어린이 대상이 아닌 일반 성인용인지 확인)
- Play Console 앱 생성 여부 및 Play App Signing 화면의 키 등록 상태
- 비공개 테스트를 진행할 최소 12명 테스터 모집 및 연락 경로

## 8. 공식 자료

- [Play Console: 앱 설정 및 스토어 등록](https://support.google.com/googleplay/android-developer/answer/9859152)
- [Play Console: 새 개인 계정의 테스트 요건](https://support.google.com/googleplay/android-developer/answer/14151465)
- [Play Console: 개발자 계정 유형 및 조직 계정 대상 서비스](https://support.google.com/googleplay/android-developer/answer/13634885)
- [Play Console: 타깃 API 수준 요건](https://support.google.com/googleplay/android-developer/answer/11926878)
- [Play Console: Data safety 작성](https://support.google.com/googleplay/android-developer/answer/10787469)
- [Play Console: Health 앱 선언](https://support.google.com/googleplay/android-developer/answer/14738291)
- [Play Console: 건강 콘텐츠 및 서비스 정책](https://support.google.com/googleplay/android-developer/answer/16679511)
- [Play Console: 미리보기 그래픽 등록 요건](https://support.google.com/googleplay/android-developer/answer/9866151)
- [Google ML Kit: Android 텍스트 인식](https://developers.google.com/ml-kit/vision/text-recognition/v2/android)
- [Google ML Kit: Play Data safety 공개 자료](https://developers.google.com/ml-kit/android-data-disclosure)
- [Google ML Kit: 약관 및 개인정보 처리](https://developers.google.com/ml-kit/terms)
