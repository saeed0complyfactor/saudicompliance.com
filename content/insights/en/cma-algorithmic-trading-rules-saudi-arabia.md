---
title: CMA Algorithmic Trading Rules: The 20-Order Cap Explained
h1: CMA algorithmic trading rules: <em>the 20-order cap</em> and Article 54
description: CMA algorithmic trading rules: a 20 order-to-execution ratio per trader and security on Main Market securities from 1 Nov 2026, with firms given to 31 Dec.
date: 2026-11-20
updated: 2026-11-20
draft: false
hero: tower-bw
service: @/licensing/capital-market-institution-licence/
service_label: Capital market institution licence support
tags: CMA, Capital markets
---
Since 1 November 2026, the ratio of algorithmic orders to executed orders on a Main Market security must not exceed 20 in a trading day, measured for each registered trader and each security separately. The Capital Market Authority (CMA) set the cap in Circular No. 2613523 of 29 October 2026, which also tells every capital market institution (CMI) to comply with Article 54 of the Capital Market Institutions Regulations and lists four algorithmic-trading controls that compliance includes. Firms have until 31 December 2026 to bring their trading into line, and algorithmic orders linked to market making are covered from 1 January 2027.

> **Key takeaways** The cap is a formula: entered orders, plus amended orders counted twice, plus cancelled orders, divided by (executed orders plus one), then minus one. It applies only in the open market session, only to Main Market securities in four liquidity categories, and not to exchange-traded funds. The control side asks for pre-use testing, effective monitoring of entered orders with alerts and reports, a way to switch an algorithm off, and records kept for ten years. The Arabic circular is the official text; we found no English version on cma.gov.sa as of 19 November 2026.

## What the circular of 29 October 2026 says

The CMA addressed the circular to all capital market institutions and announced it the same day in an Arabic press release. It passes on a CMA Board decision dated 28 October 2026 and is signed by the CMA's deputy for market institutions. The press release says the circular is based on the draft the CMA put out for public comment on 24 September 2026.

| Item | Detail |
|---|---|
| Instrument | CMA circular to capital market institutions, subject "Algorithmic trading" |
| Number and date | 2613523, 29 October 2026 (18/05/1448H) |
| Legal basis | CMA Board decision dated 28 October 2026 |
| Ratio cap applies from | 1 November 2026 |
| Deadline to adjust | No later than 31 December 2026 |
| Market-making algorithmic orders | Covered from 1 January 2027 |
| Status as of 19 November 2026 | Approved and in force, within the adjustment period |

The circular has two parts. The first sets the order-to-execution cap. The second tells CMIs to comply with Article 54 of the Capital Market Institutions Regulations and lists what that means for algorithmic trading.

## How the 20-order ratio is calculated

The circular gives the formula in Arabic. In English it reads:

(entered orders + (amended orders x 2) + cancelled orders) / (executed orders + 1), minus 1

The result must not exceed 20 for any registered trader in any single security on a trading day, and the ratio is calculated at the end of the open trading session. A registered trader, in the circular's words, is a person registered with the Exchange who is responsible for carrying out trading for the Exchange member and its clients through access to the trading system.

Three features of the formula matter when you design a strategy:

- An amendment counts twice, the same as cancelling an order and entering a new one (one cancelled plus one entered), so a strategy that keeps repricing resting orders uses up its allowance at twice the rate of one that only enters new orders, whichever way it reprices.
- The "plus one" in the denominator means a trader with no executions still has some room. With zero executions, 21 entered orders give a ratio of 20, which is allowed; 22 give 21, which is over.
- The count is per security. A trader running the same algorithm across many names has a separate ratio for each, so one illiquid stock can breach while the rest are fine.

A worked example: a registered trader enters 100 orders in one security, amends 10 and cancels 50, and 9 orders execute. The ratio is (100 + 20 + 50) / (9 + 1) minus 1, which is 16, inside the cap.

## What the cap covers, and what it does not

The cap covers algorithmic orders on securities listed on the Main Market, during the open market session, which the circular calls the second session under the Exchange's trading and membership rules. It applies to securities in four liquidity categories: high, medium, low and very low, as set out in sub-paragraph 5.3.1 of the Exchange's Market-Making Procedures.

Outside the cap, on the text of the circular:

- exchange-traded funds, which the circular excludes by name
- securities not in one of the four listed liquidity categories (the September consultation notice said the "very high liquidity" category was excluded, and the final circular does not list it)
- trading outside the open market session
- securities not listed on the Main Market
- algorithmic orders related to market-making activities, until 1 January 2027

On the market-making deferral, the circular links the later date to completing the evaluation of the market-making model. Firms that make markets should plan for 1 January 2027 and watch for any further CMA statement before then.

## Article 54 and the four control requirements

Article 54 of the Capital Market Institutions Regulations is a short, general article. Paragraph (a) requires a CMI to establish and maintain systems and controls appropriate to its business, sufficient to comply with the Capital Market Law and its Implementing Regulations. Paragraph (b) makes the governing body primarily responsible for compliance. The article itself does not mention algorithmic trading. The circular supplies the detail, saying compliance with Article 54 includes:

1. Systems and supervisory procedures that keep algorithmic trading sound and efficient, with no adverse effect on the market and no breach of the Capital Market Law or its Implementing Regulations.
2. Defined methodologies to develop and test systems, algorithms and strategies before they are used, so they do not disrupt trading and keep working in different market conditions, plus sufficient and continuous testing to confirm they are reliable, fit for purpose and accurate.
3. Policies and systems to oversee algorithmic trading carried out through the CMI's systems: effective monitoring of entered orders, alerts and reports, and the ability to switch off the algorithmic trading system or an individual algorithm when necessary.
4. Records of all algorithmic trading data and information, its systems, policies, procedures, strategies and controls, and the development and testing documents, kept for ten years after they stop being used or are amended. The CMA and Saudi Tadawul Company can ask for any of it.

Other articles in the same part of the Regulations are worth reading alongside. Article 55(c) already requires a CMI that deals as agent to have policies and systems to monitor clients' trading conduct. Article 56(a) requires the governing body to review systems and controls at least once every three years. The Article does not require an outside reviewer, but an [independent review](@/audit-review/) can give the governing body evidence for it. Robo-advisers have their own algorithm rules in Article 55(e), including annual testing by an independent party; the algorithmic trading circular does not mention robo-advisory.

## What changed between the draft and the final text

The final circular kept the shape of the 24 September draft and added several limits and dates.

| Point | September 2026 draft | Final circular, 29 October 2026 |
|---|---|---|
| Denominator in the formula | Executed transactions | Executed orders |
| Session | Not specified | Open market session (second session) only |
| Unit of measurement | Each registered trader, per security | Each registered trader and each security separately |
| Exchange-traded funds | Not mentioned | Excluded |
| Market-making orders | Not mentioned | Covered from 1 January 2027 |
| Adjustment period | Not mentioned | Until 31 December 2026 |
| When the ratio is calculated | Not specified | End of the open trading session |
| Article 54 controls | One paragraph | Four numbered requirements, same substance |

Comments on the draft closed on 24 October 2026 (13/05/1448H). If your models or vendor documentation were built from the draft, check the denominator and the session scope first.

## Who is affected in practice

The circular is addressed to all CMIs. Item 3 of the Article 54 list covers algorithmic trading carried out through a CMI's own systems; items 1, 2 and 4 are not limited that way. In practice the cap bites hardest on firms with a dealing licence whose registered traders carry algorithmic order flow on Main Market securities: proprietary desks, firms offering clients algorithmic or automated order entry, and market makers from 1 January 2027.

Because the ratio is measured per registered trader and the definition covers trading for both the Exchange member and its clients, client algorithmic flow that runs through your systems may count toward a trader's ratio on our reading. Confirm how your order routing maps to registered traders with the Exchange before you rely on any allocation.

A CMI licensed only for advising, arranging or managing investments still has the general Article 54 duty. The circular does not exempt any licence type from the four algorithmic items. On our reading they matter most where the firm develops or runs algorithmic trading strategies, whether the orders pass through its own systems or a broker's.

## Steps to take before 31 December 2026

1. List every source of algorithmic orders, including own-account strategies, client algorithmic access and market-making, and map each to the registered trader it runs under.
2. Rebuild the daily calculation with the circular's formula, per trader and per security, for the open session only, excluding ETFs and securities outside the four liquidity categories.
3. Run the formula against recent trading days to find the strategies and securities that would have breached 20, and redesign or throttle them.
4. Add pre-trade or intraday checks that warn traders before the ratio nears the cap, since the ratio is calculated at the end of the session.
5. Write the development and testing methodology for each algorithm and record the tests done before go-live and on an ongoing basis.
6. Test the switch-off for both the whole algorithmic system and single algorithms, and record who may use it.
7. Set a retention rule of ten years after an algorithm, policy or control is retired or amended, and check you can produce data quickly if the CMA or Saudi Tadawul Company asks.
8. Take the updated policies to the governing body, which Article 54(b) makes primarily responsible for compliance, and add the ratio to your [ongoing compliance](@/ongoing-compliance/) monitoring plan.

## Status and next milestone

As of 19 November 2026, Circular No. 2613523 is in force: the cap has applied since 1 November 2026, and CMIs are inside the adjustment period that ends on 31 December 2026. The next fixed date is 1 January 2027, when market-making algorithmic orders come under the cap. The Capital Market Institutions Regulations we read are the text amended by Board Resolution 2-3-2026 of 7 January 2026. We will update this guide if the CMA amends the circular, publishes an English version, or issues anything on the market-making evaluation.

This guide summarises the CMA's documents and is not legal advice. Saudi Compliance helps CMIs set up the governance, testing and monitoring files that sit behind these controls, alongside its [capital market institution licence](@/licensing/capital-market-institution-licence/) work; for the wider licence picture see [CMA licences](@/licensing/cma-licences/) and the [compliance function](@/compliance-function/).

## Sources

- [CMA: CMA circulates to CMIs the requirement to comply with the rules on algorithmic trading (Arabic press release, 29 October 2026: هيئة السوق المالية تعمم على مؤسسات السوق المالية ضرورة الالتزام بالأحكام والضوابط المنظمة للتداولات الخوارزمية)](https://cma.gov.sa/MediaCenter/PR/Pages/Algorithmic_Trading.aspx)
- [CMA: Circular No. 2613523 to capital market institutions on algorithmic trading (Arabic, 29 October 2026)](https://cma.gov.sa/RulesRegulations/circulars/Documents/Circular149.pdf)
- [CMA: Circulars (Arabic listing)](https://cma.gov.sa/RulesRegulations/circulars/Pages/default.aspx)
- [CMA: The CMA Calls for Public Consultation on the Draft Regulatory Provisions for the Restrictions on Algorithmic Trading (24 September 2026)](https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_4125.aspx)
- [CMA: public consultation on the draft restrictions on algorithmic trading (Arabic announcement: هيئة السوق المالية تستطلع آراء العموم حيال الأحكام التنظيمية المتعلقة بمشروع القيود على التداولات الخوارزمية)](https://cma.gov.sa/MediaCenter/NEWS/Pages/CMA_N_4125.aspx)
- [CMA: Regulatory Provisions for the Restrictions on Algorithmic Trading (draft, English)](https://cma.gov.sa/en/MediaCenter/NEWS/Documents/Algorithmic_Trading.pdf)
- [CMA: draft regulatory provisions on the restrictions on algorithmic trading (Arabic: الأحكام التنظيمية المتعلقة بمشروع القيود على التداولات الخوارزمية)](https://cma.gov.sa/MediaCenter/NEWS/Documents/AlgoTrading.pdf)
- [CMA: Capital Market Institutions Regulations (English translation, amended 7 January 2026)](https://cma.gov.sa/en/RulesRegulations/Regulations/Documents/the_Capital_Market_Institutions_Regulations-en.pdf)
- [CMA: Capital Market Institutions Regulations (official Arabic text: لائحة مؤسسات السوق المالية)](https://cma.gov.sa/RulesRegulations/Regulations/Documents/the_Capital_Market_Institutions_Regulations-ar.pdf)
