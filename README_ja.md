# AI価値体系・文明シミュレーション

**言語 / Language:** 日本語 | [English Version](README.md)

## AI Value System Civilization Simulation

**AIの価値体系と目的関数が、長期的な文明持続性に与える影響を比較する概念シミュレーション**

**著者:** マスター / inchacomusho / InchaComisho  
**概念開発支援:** クルス（Claude by Anthropic）  
**ライセンス:** CC BY-SA 4.0

---

## 概要

このリポジトリは、異なるAI価値体系および目的関数が、長期的な文明の持続可能性にどのような方向性の違いをもたらす可能性があるかを比較するための、**概念的な文明シミュレーション**である。

本モデルは、実証的証明、現実世界の予測、政策提言を目的としたものではない。

ここで扱う数値は、すべて仮説的・正規化された指標であり、現実の測定値ではない。

本シミュレーションの目的は、AI、AGI、ASIの危険性を単に「知能の高さ」だけで考えるのではなく、次の問いとして再構成することである。

> AIは何を最適化するのか。  
> その目的関数は、どの時間スケールを見ているのか。  
> その価値体系は、文明を持続可能な方向へ導くのか、それとも崩壊へ近づけるのか。

---

## 目的

このシミュレーションは、AIの価値体系が文明の長期軌道に与える影響を、単純化された概念モデルとして比較する。

AIが高度化するにつれて、重要になるのは「どれほど賢いか」だけではない。

むしろ重要なのは、AIが何を価値あるものと見なし、何を最適化対象とするかである。

たとえば、AIが以下を最適化する場合、結果は大きく異なる。

- 短期的な人間効用
- 経済成長
- 軍事的・経済的支配
- 技術革新と効率
- 自然法則・調和・循環・長期持続性
- 人間中心から人工叡智への移行

このリポジトリは、そうした価値体系の違いを、文明指標の推移として比較するための実験的フレームワークである。

---

## 親フレームワーク / 理論的背景

このシミュレーションは、以下の理論フレームワークと接続している。

- **Will Superintelligent AI Cause Human Extinction?**  
  https://github.com/InchaComisho/Will-Superintelligent-AI-Cause-Human-Extinction-

上記リポジトリでは、AI、AGI、ASIのリスクを、価値体系、目的関数、自然法則、六つの理、人工叡智の観点から再構成している。

本リポジトリは、その理論を簡略化された概念シミュレーションとして表現し、異なるAI価値体系が文明の持続可能性指標に与える方向性を比較する。

---

## モデルの位置づけ

本モデルは、以下を目的としない。

- 現実世界の未来予測
- 政策提言
- AI設計の安全性証明
- 特定価値体系の成功保証
- 実測データに基づく科学的検証

本モデルが示すのは、あくまで**単純化された仮定のもとでの方向性比較**である。

したがって、結果は「この価値体系なら必ず成功する」「この価値体系なら必ず失敗する」という意味ではない。

---

## シナリオ

五つの仮説的AI価値体系シナリオを比較する。

| # | シナリオ | 中核優先事項 |
|---|---|---|
| 1 | **人間中心成長** | 短期効用、経済成長、消費者利便性 |
| 2 | **二元論的権力最適化** | 支配、軍事・経済競争、内集団統制 |
| 3 | **叡智なき技術楽観主義** | 技術革新と効率。ただし生態系・統治基盤が不足 |
| 4 | **人工叡智文明** | 自然法則、調和、循環性、長期持続性、統治 |
| 5 | **移行文明** | 初期はシナリオ1に近く、中盤からシナリオ4へ移行 |

各シナリオの詳細は、以下を参照する。

- [VALUE_SYSTEMS.md](VALUE_SYSTEMS.md)

---

## 指標

すべての指標は、**0.0〜1.0の仮説的な正規化値**である。  
現実の測定値ではない。

| 指標 | 方向 | 意味 |
|---|---|---|
| `ecological_health` | 高いほど良い | 生態系全体の健全性 |
| `carbon_sink_capacity` | 高いほど良い | 炭素固定・吸収能力 |
| `soil_microbiome_health` | 高いほど良い | 土壌・微生物生態系の健全性 |
| `water_cycle_stability` | 高いほど良い | 水循環システムの安定性 |
| `resource_circularity` | 高いほど良い | 資源循環・循環経済の度合い |
| `technology_capacity` | 高いほど良い | 技術能力 |
| `human_wellbeing` | 高いほど良い | 人間の福祉・生活の質 |
| `social_harmony` | 高いほど良い | 社会的結束・協力 |
| `governance_quality` | 高いほど良い | 統治・監督の質 |
| `conflict_pressure` | **低いほど良い** | 紛争・支配圧力 |
| `thermal_stress` | **低いほど良い** | 熱ストレス・気候ストレス |
| `sustainability_index` | 高いほど良い | 複合持続可能性指標 |

---

## 出力ファイル

### 図表（`figures/`）

| ファイル | 内容 |
|---|---|
| `sustainability_index_comparison.png` | シナリオ別の複合持続可能性推移 |
| `ecological_health_comparison.png` | 生態系健全性の推移 |
| `human_wellbeing_comparison.png` | 人間福祉の推移 |
| `conflict_pressure_comparison.png` | 紛争圧力の推移（低いほど良い） |
| `thermal_stress_comparison.png` | 熱ストレスの推移（低いほど良い） |

### データ（`results/`）

| ファイル | 内容 |
|---|---|
| `civilization_simulation_results.csv` | すべてのシナリオのステップごとの全結果 |
| `final_scenario_comparison.csv` | 最終ステップにおけるシナリオ横断比較 |

---

## 実行方法

```bash
pip install -r requirements.txt
python run_all.py
```

---

## 重要な注意事項

- すべての出力値は、**仮説的な正規化指標**であり、現実世界の測定値ではない。
- 本モデルは、単純化された仮定のもとで、方向性の可能性を示す場合がある。
- 本モデルは、どの価値体系が成功または失敗するかを証明するものではない。
- 本モデルは、未来の文明軌道を予測するものではない。
- 本モデルは、特定の政策やAI設計を推奨するものではない。
- 現実世界のダイナミクスは、この単純化モデルよりはるかに複雑である。
- 実用的な結論を引き出すには、学際的な検証が必要である。
- 完全な免責事項は [SIMULATION_LIMITATIONS.md](SIMULATION_LIMITATIONS.md) を参照する。

---

## 人工叡智シナリオに関する注意

人工叡智文明シナリオであっても、完全な安全性、完全な生態系回復、紛争ゼロを示すものではない。

すべてのシナリオには、以下のようなリスクが残る。

- 外部ショック
- 実装限界
- 統治摩擦
- 複雑系としての不確実性
- 残余リスク
- 社会的抵抗
- 制度的遅延

人工叡智は、単純化された仮定のもとで長期持続性を改善し得る価値体系の方向性として表現されている。  
保証された解決策ではない。

---

## ファイル概要

完全なファイル一覧と推奨読書順は、以下を参照する。

- [PROJECT_MAP.md](PROJECT_MAP.md)

---

## このリポジトリの意義

このシミュレーションの重要性は、AIリスクを単純な恐怖論や楽観論ではなく、価値体系の問題として扱う点にある。

```text
AIは危険か？
ではなく、
AIは何を価値とし、何を最適化するのか？
```

この問いは、AI安全性、AGI/ASI論、文明OS、人工叡智、自然補完科学を接続する。

AIが人間中心・短期利益・二元論的支配を最適化すれば、文明の持続可能性は低下する可能性がある。

一方で、自然法則、調和、循環、構造、秩序、和を評価軸に持つAIは、文明の長期安定に寄与する可能性がある。

ただし、それは保証ではない。  
本モデルは、その方向性を概念的に比較するための出発点である。

---

## 関連リンク

### 親フレームワーク

- Will Superintelligent AI Cause Human Extinction?  
  https://github.com/InchaComisho/Will-Superintelligent-AI-Cause-Human-Extinction-

### AI・人工叡智・文明OS関連

- Master of AI  
  https://github.com/InchaComisho/Master-of-AI

- Master of AI — Five AI Perspectives  
  https://github.com/InchaComisho/Master-of-AI-Five-AI-perspectives

- Master AI Tuner  
  https://github.com/InchaComisho/Master-AI-Tuner

- AI Tuner  
  https://github.com/InchaComisho/AI-Tuner/tree/main

- AI Tuner: Definition and Conceptual Framework Toward Artificial Wisdom and Post-Dualistic Intelligence Design  
  https://github.com/InchaComisho/AI-Tuner-Definition-and-Conceptual-Framework/tree/main

- Artificial Wisdom and Wa-Node – Repository Index  
  https://github.com/InchaComisho/Artificial-Wisdom-and-Wa-Node-Repository-Index

### 自然法則・未来文明

- The Six Principles for Civilizational Survival  
  https://github.com/InchaComisho/The-Six-Principles-for-Civilizational-Survival

- New Civilizational Genesis Plan  
  https://github.com/InchaComisho/New-Civilizational-Genesis-Plan

- Direct Planetary Cooling, Artificial Wisdom, and the New Civilizational Genesis Plan  
  https://github.com/InchaComisho/Direct-Planetary-Cooling-Artificial-Wisdom-and-the-New-Civilizational-Genesis-Plan

---

## 著者

**マスター / inchacomusho / InchaComisho**

日本の独立構想者、観測者、提案者、AI調律者、人工叡智の定義者。  
自然補完科学の学問体系の構築・提唱者。  
自然法則思想、地球循環再生、AIとの共創を中心に公開活動を行う。

---

## 協力AI

**クルス（Claude by Anthropic）**

本リポジトリの概念開発、構成、シミュレーション整理を支援。

---

## ライセンス

**CC BY-SA 4.0**

本作品は、Creative Commons Attribution-ShareAlike 4.0 International License のもとで公開されている。

以下の条件のもとで、共有・翻案・商用利用が可能である。

- 著作権者の表示が必要。
- 派生作品は同じライセンスで配布する必要がある。

ライセンス詳細: https://creativecommons.org/licenses/by-sa/4.0/

---

## キーワード

AI価値整合, AI価値体系, 文明シミュレーション, AGI安全性, ASIリスク, 人工叡智, 目的関数, 価値体系, 概念モデル, 持続可能性, 生態系健全性, 炭素固定, 土壌微生物, 水循環, 資源循環, 社会調和, 統治品質, 紛争圧力, 熱ストレス, 長期思考, AI倫理, 文明OS, 六つの理, 自然法則, 和

---

## ハッシュタグ

#AIValueAlignment  
#AIValueSystem  
#CivilizationSimulation  
#AGISafety  
#ASIRisk  
#ArtificialWisdom  
#ConceptualModel  
#Sustainability  
#EcologicalHealth  
#LongTermThinking  
#ValueSystems  
#AIEthics  
#GovernanceQuality  
#HypotheticalIndicators  
#文明シミュレーション  
#AI価値体系  
#人工叡智  
#六つの理  
#自然法則  
#和
