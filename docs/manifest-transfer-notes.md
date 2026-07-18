# ZeroRoomLab-manifest からの転送メモ

作成日: 2026-07-13

## 1. 受け取った方針

このリポジトリでは、AQC / IBD / SphereOS の責務分離を、以下のように整理しています。

- AQC Docker は歴史的プロトタイプとして扱う
- IBD は記憶・文脈・FAM trace・provenance を扱うバックエンド基盤として再定義する
- 哲学・神話・思想の文脈は技術実装に吸収せず、独立した文脈として保持する

## 2. 参照元

- [ZeroRoomLab-manifest の運用モデル](../../../ZeroRoomLab-manifest/ZeroRoomLab-manifest/docs/operations/manifest-operating-model.ja.md)
- [ZeroRoomLab-manifest のハブ文書](../../../ZeroRoomLab-manifest/ZeroRoomLab-manifest/note/20260713-1531__Quantaril%20Cloud%20Atlantis%E4%B8%96%E4%BB%A3%20%E2%80%95%20%E6%96%87%E6%9B%B8%E4%BD%93%E7%B3%BB%E3%83%9E%E3%83%83%E3%83%97(%E3%83%8F%E3%83%96).md)
- [Sphere Context Dimension OSアーキテクチャ](https://github.com/saitoomituru/ZeroRoomLab-manifest/blob/main/docs/theory/sphere-context-dimension-os.ja.md)
- [Context定規・因果・OAE横断監査規約](https://github.com/saitoomituru/ZeroRoomLab-manifest/blob/main/docs/operations/context-ruler-and-causality-audit.ja.md)
- [IBD: Context Dimension OSとIBDSDK](https://github.com/saitoomituru/IBD/blob/main/docs/architecture/context-dimension-os-and-ibdsdk.ja.md)

## 3. 運用上の扱い

この文書は、対象リポジトリ向けの要約です。実装内容・README・docs の更新は、必要に応じてこのリポジトリ側で追跡します。

## 4. 2026-07-18の追補

- 本リポジトリのruntime、schema、Docker構成へOAE、FAM Splitter SPI、IBDSDKを新規実装しない
- AQCの宗教・哲学運用方針は歴史的application profileとして保持し、Sphere Coreの普遍定規へしない
- FoldAccessMapper.proton.mdの本文は一次資料として変更せず、強い科学・数理・権利証明主張は別監査文書でscopeを示す
- 技術Layer `L`、Context Dimension `D`、FAMの`λ`、legacy `Q.layer`を同一視しない
- AQCのSIN記述を、IBDで研究中のSsC校正interfaceの実装済み根拠にしない

詳細は[FoldAccessMapper／AQC歴史的claim boundary](foldaccessmapper-historical-claim-boundary.ja.md)を参照する。
