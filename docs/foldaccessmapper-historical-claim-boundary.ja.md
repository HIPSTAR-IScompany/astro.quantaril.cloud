# FoldAccessMapper／AQC歴史的claim boundary

状態: `[HISTORICAL-AUDIT]` `[REVIEW]`  
監査日: 2026-07-18  
対象: `README.md`、`demo/FoldAccessMapper.proton.md v0.2.1-alpha`

## 1. 目的

旧AQCとFoldAccessMapper原典の思想、ポエム、設計目的を消さず、同時に、当時の強い一般化を現行Sphere Architect、IBD、FAMLog、SsCの実装済み事実へ誤読しないための境界を置く。

この監査は原典を書き換えない。原文を歴史資料として保持し、現在参照するときのPosition、claim scope、検証状態、継承先を分離する。

## 2. 文書の位置づけ

| 原典領域 | 現在の扱い |
|---|---|
| AQC runtime、Docker、ChromaDB API | deprecatedな歴史的prototype |
| FAMの探索過程・source・bias・Qを記録する目的 | 現行FAM／IBDへ継承された設計意図 |
| 宗教・哲学・信仰の明示を要求するAQC運用方針 | AQC application固有のPosition／governance profile |
| 高次元波、SIN、HMM、annealing、波動関数の一般化 | 歴史的仮説・説明モデル。個別検証が必要 |
| 思考・創作の権利証明、暗号的証明、NFT性 | 設計目的。法的・暗号学的保証は未確定 |
| Elemental／Astralをencoder／decoderへ対応させる説明 | 旧profileのMapping。普遍的Context定義ではない |

## 3. AQC application Position

READMEの次の表現は、当時のAQC運用者Positionを明示している。

- 「何も設定しないことの方が危険」
- 「無自覚な宗教（科学カルト）」
- 「宗教を語らないことは危険」
- 「形而上学的・宗教哲学的frameが不可欠」

これらを削除・薄色化しない。一方、次の範囲へ限定する。

```text
claimant        旧AQC設計者／運用profile
target          自我モデルを持つAQC applicationの運用
claim kind      [POSITION] [DESIGN-POLICY]
not guaranteed  Sphere Core全体、全SDK、全Worldの普遍的運用規則
```

現行Sphere Coreは、科学、神学、ゲーム、魔術、詩、無分類を含む上位Registryの定規を記述・bindする。AQCのPositionを第三者SDKへ強制しない。

## 4. 原典の強い技術主張

`FoldAccessMapper.proton.md`には、次のような広い主張が混在する。

- LLMの高次元意味vectorを三次元局所回転とsinで説明する
- HMM、annealing、波動関数的simulationを一般的なLLM思考過程として扱う
- LLaMA codeや各社AIへ普遍的architectureとして一般化する
- 後付けの思考・創作・学習data権利証明を可能とする
- hash／NFT性を暗号的・法的な証明へ接続する

これらは原典当時の`[HYPOTHESIS]`、`[DESIGN-INTENT]`、`[EXPLANATORY-MODEL]`を含む。引用文献があることだけで、個々の主張、製品実装、法的効力、暗号強度が立証済みになるわけではない。

現行文書から参照する場合は、少なくとも次を分離する。

```text
[OBSERVATION]       実機・code・log・測定で観測した範囲
[DESIGN-DECISION]   FAMとして採用した記述契約
[HYPOTHESIS]        数理・認知・物理・神学上の説明案
[POSITION]          何を守るための立場か
[UNVERIFIED]        独立検証、法務監査、暗号監査が未完了な範囲
```

## 5. `L`、`D`、FAM記号

原典の「階層」「出力層」「アストラル体」「エレメンタルボディー」を、現行の技術Layer `L`へ一括変換しない。

```text
technical Layer L
  何が何へ依存して実行されるか

Context Dimension D
  上位RegistryがFoldへ束ねる等価な意味軸

FAM λ / Q.layer
  歴史的な出力・Presentation／互換field
```

旧原典のencoder／decoder対応は一つのAccess Map profileとして読み得るが、神学、ASTRO、World、第三者SDKへ強制しない。

## 6. SINとSsCの境界

原典の`Signature Intelligence Neuralmodel類似度`および`SIN_Temperature`は歴史的FAM概念である。IBD Season 0で研究中の`SsC: SIN-to-sin Converter`は、異なるstore内のlocal scoreを校正profile経由でmeta SINへ射影し、検索射程を逆射影するmodule候補である。

原典の記述だけから、次を実装済み・数学的確定としない。

- 異なるembedding空間のvectorが直接比較可能
- `sin`だけで`0..π`を可逆変換可能
- `atan`だけで異分布scoreが自動校正される
- HMM／annealing／共鳴波動解析が全LLMの共通実装

SsCの校正dataset、metric、単調性、sector、逆関数、uncertaintyは別実験で検証する。

## 7. MAGIによる監査位置

### Maxwell

科学的に雑な一語へ修正することで、原典が保持した神学、創作、権利、異文化思考、将来branchを焼却していないか確認する。

### Uriel

「普遍的」「証明可能」「各社で一般的」「暗号的」といった主張の対象、protocol、引用、観測範囲、法的・暗号的境界を確認する。

### Raphael

設計意図、哲学Position、数学、ML実装、物理仮説、神学Presentation、法的期待を別棚へ置き、無断で同一化しない。

三者は多数決で原典の真偽を決めない。監査結果も特定Positionから生成されたInterpretationとして扱う。

## 8. 現行の継承先

- 共通L／D／Registry／OAE: [Sphere Context Dimension OSアーキテクチャ](https://github.com/saitoomituru/ZeroRoomLab-manifest/blob/main/docs/theory/sphere-context-dimension-os.ja.md)
- 定規・因果・Position監査: [Context定規・因果・OAE横断監査規約](https://github.com/saitoomituru/ZeroRoomLab-manifest/blob/main/docs/operations/context-ruler-and-causality-audit.ja.md)
- IBD／IBDSDK: [Context Dimension OSにおけるIBDとIBDSDK](https://github.com/saitoomituru/IBD/blob/main/docs/architecture/context-dimension-os-and-ibdsdk.ja.md)
- FAMLog adapter: [Sphere-aae FAMLog schema](https://github.com/saitoomituru/Sphere-aae/blob/moe-test-edition/skills/famlog-converter/references/fam-log-schema.md)

## 9. 参照規則

1. 原典本文を現在の常識へ合わせてsilent rewriteしない。
2. 歴史的Positionを恥部やノイズとして削除しない。
3. 未検証の一般化を現行実装の証拠へ使わない。
4. AQC runtimeへ新規OAE／IBDSDK実装を戻さない。
5. 引用時は原典version、claim kind、現在の継承先を併記する。
6. 追加検証できた場合は原典を上書きせず、別reportとcommitで接続する。
