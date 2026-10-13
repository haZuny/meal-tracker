# NoshNote 개인정보처리방침 초안

> **게시 전 작성 필요:** 이 문서는 검토용 초안이다. `[대괄호]` 항목을 실제 값으로 채우고, 서비스 동작 및 게시자 정보를 확인한 뒤 공개한다. 공개 URL이 확정되면 앱 안에서도 이 방침에 접근할 수 있도록 연결한다.

## NoshNote 개인정보처리방침

공개 예정일: [개인정보처리방침을 실제 공개하는 날짜]  
앱: NoshNote (`com.hazuny.noshnote`)  
개발자/게시자: [Play Console에 표시될 개발자 이름]  
문의: [지원 이메일]

NoshNote는 식단 기록 앱입니다. 이 앱은 계정이나 서버 동기화를 제공하지 않으며, 앱에 입력한 식단 기록·음식 템플릿·목표를 사용자의 Android 기기에 저장합니다.

## 처리하는 정보와 목적

- **식단 기록:** 사용자가 입력한 음식명, 섭취량, 단위, 칼로리, 단백질, 날짜, 시각, 식사 태그를 기기에 저장해 날짜별 목록과 합계를 표시합니다.
- **음식 템플릿:** 사용자가 재사용을 위해 입력한 음식명, 단위, 칼로리, 단백질을 기기에 저장합니다.
- **영양 목표:** 사용자가 입력한 일일 칼로리·단백질 목표를 기기에 저장해 섭취 현황과 비교합니다.
- **카메라 영상 프레임:** 사용자가 영양성분표 스캔 기능을 열고 카메라 권한을 허용하면 실시간 카메라 프레임을 기기에서 처리해 문자 인식 후보를 만듭니다. 프레임과 인식 결과는 NoshNote 또는 Google 서버로 전송되지 않으며, 앱이 사진이나 동영상으로 저장하지 않습니다. 인식값을 기록에 반영하기 전 사용자가 확인하고 수정할 수 있습니다.
- **진단·사용 통계:** Google ML Kit SDK는 API 사용 시 기기 제조사·모델·Android 버전, 앱 패키지명·버전, 설치별 식별자, 처리 지연, API 설정, 입력·출력 크기, 기능 이벤트와 오류 코드를 진단·사용 분석 목적으로 Google에 보낼 수 있습니다. Google은 이 SDK 통계가 HTTPS로 암호화되고 제3자에게 전달되지 않는다고 안내합니다. 음식 기록, 영양 목표, 카메라 프레임과 인식 결과는 이 통계에 포함되지 않는다고 ML Kit가 설명합니다.
- **JSON 백업 파일:** 사용자가 직접 내보내기를 선택하면 식단 기록, 템플릿, 목표가 JSON 파일로 생성되어 사용자가 Android 파일 선택기에서 지정한 위치에 저장됩니다. 사용자가 선택한 다른 앱이나 클라우드 저장소의 처리에는 해당 서비스의 개인정보처리방침이 적용됩니다.

## 저장, 전송 및 제3자 제공

NoshNote는 계정, 광고, 자체 분석 서비스 또는 서버 동기화 기능을 제공하지 않습니다. 음식 기록, 템플릿, 목표, 카메라 프레임과 인식 결과를 NoshNote 서버로 전송하거나 판매·제공하지 않습니다. 다만 Google ML Kit SDK는 API 진단·사용 통계를 Google에 전송할 수 있습니다. Google은 해당 통계가 HTTPS로 암호화되고 제3자에게 전달되지 않는다고 안내합니다. 음식 기록과 목표는 앱의 로컬 데이터베이스에 저장됩니다. Android 자동 백업과 기기 간 자동 전송은 앱 설정에서 제외되어 있으므로, 기기를 바꾸기 전에 사용자가 JSON 백업을 직접 내보내야 합니다.

앱은 Google ML Kit의 앱 번들형 한국어 텍스트 인식 라이브러리를 사용합니다. 모델이 앱에 포함되며 영양성분표 텍스트 인식은 기기에서 수행됩니다. Google ML Kit는 입력 이미지·영상·텍스트와 처리 결과를 Google 서버에 보내지 않지만, 위에 설명한 진단·사용 통계를 Google 서버로 보낼 수 있습니다.

## 권한

- **카메라:** 영양성분표의 글자를 읽는 선택 기능에만 사용합니다. 카메라를 허용하지 않아도 모든 값을 직접 입력해 식단을 기록할 수 있습니다.

## 보유 기간과 삭제 방법

식단 기록, 템플릿, 목표는 사용자가 앱에서 삭제하거나 수정할 때까지 기기에 보관됩니다. 개별 기록과 템플릿은 앱의 해당 관리 화면에서 삭제할 수 있습니다. Android 설정에서 NoshNote의 저장공간을 삭제하거나 앱을 제거하면 앱 데이터가 삭제될 수 있습니다. 내보낸 JSON 파일은 사용자가 선택한 위치에서 직접 삭제해야 합니다.

NoshNote는 서버 계정을 만들거나 서버에 사용자 기록을 보유하지 않으므로 서버 데이터 삭제 요청 절차는 없습니다.

## 아동의 개인정보

[실제 타깃 연령 정책에 맞춰 작성. 앱이 어린이를 대상으로 설계되지 않은 경우 해당 사실과 관련 법률상 보호자 동의 요건을 포함해 검토한다.]

## 방침 변경

앱의 데이터 처리 방식이 바뀌면 이 방침과 앱 내 접근 경로를 함께 갱신하고, 변경된 시행일을 표시합니다.

## 문의

개인정보 및 앱 지원 문의: [지원 이메일]

---

## English draft

**Not ready for publication:** Replace bracketed fields with verified publisher details and review this text against the release build. Publish it at a public, non-editable web page, then make it reachable from inside the app.

### NoshNote Privacy Policy

Planned publication date: [date this policy is made public]  
App: NoshNote (`com.hazuny.noshnote`)  
Developer/publisher: [name shown on Google Play]  
Contact: [support email]

NoshNote is a meal logging app. It does not provide accounts or server synchronization. Meal entries, food templates, and goals entered in the app are stored on the user's Android device.

### Information and purposes

- **Meal entries:** Food name, amount, unit, calories, protein, date, time, and meal tag entered by the user are stored on the device to show daily entries and totals.
- **Food templates:** Food names, units, calories, and protein entered by the user are stored locally so they can be reused.
- **Nutrition goals:** Daily calorie and protein goals entered by the user are stored locally and compared with recorded intake.
- **Camera frames:** If the user opens the nutrition label scanner and grants camera access, live camera frames are processed on the device to produce text recognition suggestions. Neither the frames nor recognized results are sent to NoshNote or Google servers, and NoshNote does not save them as photos or videos. Users can review and edit recognized values before using them in a meal entry.
- **Diagnostics and usage metrics:** When Google ML Kit is used, the SDK may send the device manufacturer/model/Android version, app package name/version, per-installation identifiers, processing latency, API configuration, input/output sizes, feature events, and error codes to Google for diagnostics and usage analytics. Google states that this SDK data is encrypted in transit using HTTPS and is not transferred to third parties. ML Kit states that meal entries, nutrition goals, camera frames, and recognition results are not sent to Google servers.
- **JSON backup files:** When the user chooses to export, meal entries, templates, and goals are written to a JSON file in a location selected through Android's file picker. The privacy practices of any other app or cloud service selected by the user are governed by that service's own policy.

### Storage, transfers, and third parties

NoshNote has no account, advertising, first-party analytics, or server synchronization features. It does not send meal entries, food templates, goals, camera frames, or recognition results to NoshNote servers or sell or provide them to third parties. Google ML Kit may send SDK diagnostics and usage metrics to Google as described above; Google states that these metrics are encrypted in transit and are not transferred to third parties. Entries and goals are stored in the app's local database. Android cloud backup and device-to-device transfer are excluded by the app, so users should export a JSON backup before changing devices.

NoshNote uses the bundled Korean text recognition library from Google ML Kit. The model is included with the app, and nutrition label recognition runs on the device. Google ML Kit states that it does not send input images, video, text, or recognition results to Google servers, although the SDK may send the diagnostics and usage metrics listed above.

### Permission

- **Camera:** Used only for the optional nutrition label text recognition feature. Users can deny camera access and continue logging meals manually.

### Retention and deletion

Meal entries, templates, and goals remain on the device until the user edits or deletes them. Individual entries and templates can be deleted in the app. Clearing NoshNote's storage in Android settings or uninstalling the app may delete app data. Exported JSON files must be deleted by the user from the location where they were saved.

NoshNote does not create server accounts or retain user entries on a server, so it has no server-side account data deletion request process.

### Children's privacy

[Complete this section after confirming the intended age groups and applicable requirements.]

### Changes and contact

If NoshNote's data practices change, this policy and the in-app access path will be updated, with a revised effective date.

Privacy and app support: [support email]
