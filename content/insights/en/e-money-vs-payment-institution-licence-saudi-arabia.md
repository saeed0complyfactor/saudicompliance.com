---
title: E-Money vs Payment Institution Licence in Saudi Arabia
h1: E-money or payment institution: <em>which licence</em> does your wallet need?
description: A Saudi wallet needs an e-money licence if users keep a balance to spend with others; a payment institution licence covers money you only move.
date: 2026-11-19
updated: 2026-11-19
hero: glass-tower
service: @/licensing/e-money-licence/
service_label: E-money licence support
tags: SAMA licensing, Payments
---
A Saudi wallet needs an e-money institution (EMI) licence when customers load money into it and keep a balance that they can later spend with merchants or people other than you. If your product only receives funds to carry out a specific payment, such as acquiring card payments for merchants or executing a transfer from a customer's payment account, a payment institution (PI) licence is the fit. SAMA's Payments Implementing Regulations draw the line in their definitions: a PI may provide any payment service except issuing electronic money, and among non-bank providers only an EMI may issue it (licensed banks are exempt from payment licensing under Article 48).

> **Key takeaways** Apply a three-part test to every balance in your product: stored value, a claim on you, accepted by others. All three mean e-money and an EMI licence. Every EMI must be a joint stock company with at least SAR 2 million of paid-up capital, against SAR 1 million and a possible LLC for a Micro PI. E-money carries product rules a PI does not face: no interest or holding rewards, no overdraft of its own, redemption at par on demand. On 19 November 2026, 15 of the 33 non-bank firms on SAMA's payments register carried the EMI label.

This guide works through the test product by product and sets out what the choice changes. For the application steps themselves, see [how to apply for a SAMA payment licence](@/insights/how-to-get-sama-payment-licence/); for the Micro and Major EMI categories in detail, see our [SAMA electronic money licence](@/licensing/e-money-licence/) page.

## The test is whether you issue electronic money

Article 1 of the Implementing Regulations defines electronic money as "electronically (including magnetically) stored monetary value as represented by a claim on the issuer, which is issued on receipt of Funds for the purpose of making Payment Transactions and accepted by a Person other than the issuer as means of payment (excluding virtual assets)". We read the Arabic text alongside the English; it says the same thing.

Break that definition into questions about your product:

- Do customers hand you money and receive a stored value in return?
- Is that value a claim on you, the issuer?
- Can customers use it to pay someone other than you?

If the answer to all three is yes, you are issuing e-money and need an EMI licence. The regulations define a payment institution as a provider licensed for "one or more Relevant Payment Services, except for the issuing of Electronic Money". A PI can still hold a payment account for a customer, which the regulations define as an account "used for the execution of Payment Transactions".

The safeguarding definitions show where each licence's money comes from. For a PI, safeguarded funds are those "received from, or for the benefit of, a Payment Service User for the execution of Payment Transactions". For an EMI, they are funds "received in exchange for Electronic Money that has been or is to be issued". On our reading, that is the practical dividing line: money parked as a spendable balance points to e-money, and money received to complete a particular payment points to a PI. The regulations give no worked examples, so put the analysis for any borderline product in writing and test it with SAMA before you file.

The exclusion of virtual assets from the definition matters too. A token balance that is a virtual asset is not e-money under these regulations; see [digital assets](@/digital-assets/) for where the perimeter sits.

## Which licence each product flow points to

| Product flow | Usual fit | Why |
|---|---|---|
| Consumer wallet that users top up and spend at many merchants or send to friends | EMI | Stored value, a claim on the issuer, accepted by others |
| Prepaid card usable across a card network | EMI | Same three elements as a wallet |
| Merchant acquiring or a payment gateway that settles card payments to merchants | PI | Funds are received to execute and settle payments; no stored value is issued |
| Payment aggregation for small merchants | PI | Aggregation is a listed payment service (Art 6); no e-money is issued |
| Transfers or bill payments from a payment account, with no balance kept for later | PI | Funds pass through for a specific payment; a Micro PI may not serve persons outside the Kingdom (Art 42) |
| Gift card or loyalty balance usable only in one retail group | Possibly excluded | Limited network services are outside the regulations (Art 7(10)), subject to SAMA registration |
| Account information or payment initiation (open banking) | AIS or PIS licence type under the same regulations | Capital and fee set in Arts 44 and 23; see [open banking licence](@/licensing/open-banking-licence/) |

Sources: Implementing Regulations, Articles 1, 6, 7, 23, 42 and 44. The "usual fit" column is our reading of the definitions; SAMA decides each case.

The closed-loop row needs the most care. The regulations define a closed loop account as stored value issued by a one-off issuer that "cannot be redeemed in cash or to any other account" and can only buy goods or services within a limited network in the same corporate group or brand. Restricted loop accounts work the same way across a defined network of providers with direct agreements with the issuer. Providers of these limited network services must register with SAMA, and must notify it once transactions exceed, or are expected to exceed, SAR 5 million in any 12 consecutive months or SAR 2 million in any month. SAMA may then require a licence (Article 49). A loyalty wallet that later lets users cash out, or spend at partner merchants outside the group, moves towards the e-money definition.

## One licence or two, and changing later

On our reading, a wallet that also acquires for merchants does not need a PI licence next to its EMI licence. The regulations define a licence (Article 1) as including "activities that are specified in the License", and they measure a Micro EMI by its average monthly payment transaction value as well as its outstanding e-money (Article 43), which assumes an EMI also executes payments. What matters is that every service you run is named in the licence SAMA grants, so list them all in the application and confirm the scope with SAMA.

Adding a stored balance to a live PI is a different matter. Article 20 lets a licensee apply to amend its licence to add or delete activities or services, with justification and supporting studies, and Article 23 says the licensee is then subject to re-evaluation. The regulations do not say whether moving from the PI category to the EMI category is handled as an amendment or as a new application, so ask SAMA before you build the feature. Either way the company must meet the EMI capital and legal form described below.

## How SAMA counts the limits for PIs and EMIs

The two licences are measured on different bases, and the definitions decide when a firm outgrows its category.

- Average monthly payment transaction value is a rolling monthly average over any 12 calendar months. It includes transactions executed by your agents and excludes the issuance and redemption of e-money, so top-ups and cash-outs do not count towards it. Both Micro PIs and Micro EMIs must stay at SAR 10 million or less on this measure (Articles 42 and 43).
- Total average outstanding e-money applies only to EMIs. It is the average of the EMI's e-money liabilities at the end of each calendar day over the last 12 months, and a Micro EMI must keep it at SAR 10 million or less.
- A Micro EMI also caps each user's holdings and monthly transactions, and moves to Major when it exceeds any one of its limits. A new Micro EMI, or one with less than 12 months of history, must show that its projected figures for the first 12 months stay within SAR 10 million.
- A Micro PI may not provide payment services cross-border to persons outside the Kingdom. Article 43 sets no such condition for a Micro EMI; confirm the position with SAMA before you rely on that silence.

The per-user caps and the jump to Major are covered on our page on [Micro and Major EMI limits](@/licensing/e-money-licence/).

## What moving from a Micro PI to an EMI adds

| Item | Micro PI | Micro EMI | Major EMI |
|---|---|---|---|
| Extra paid-up capital compared with a Micro PI | None (SAR 1m) | SAR 1m more (SAR 2m) | SAR 9m more (SAR 10m) |
| Legal form | JSC, simplified JSC or LLC | Joint stock company | Joint stock company |
| Issue fee | SAR 20,000 | SAR 20,000 | SAR 50,000 |
| Product rules in Article 69 | Do not apply | Apply | Apply |
| E-money distributors (Article 25) | Not available | Available | Available |

Sources: Implementing Regulations, Articles 14, 23, 25, 44 and 69.

The legal form row has the longest lead time. Only a Micro PI may be a limited liability company or simplified joint stock company, so a founder who sets up an LLC for a Micro PI and later adds a stored balance faces a change of legal form as well as a licence change. Incorporation must be completed within 180 days of SAMA's in-principle approval (Article 14); see [incorporation](@/incorporation/). A firm expecting to grow past the Micro PI volume limit should compare against the [Major payment institution](@/licensing/payment-institution-licence/) route, which needs SAR 3 million and a joint stock company.

## E-money rules that shape the product

An EMI licence comes with product rules in Article 69 that a PI does not face. Build them into the design before the business plan goes to SAMA.

- E-money must be issued at par value on receipt of funds.
- No interest, and no "other benefit", linked to how long the customer holds e-money. A reward that grows with how long the balance is held falls foul of this; check any cashback or points scheme against it.
- No overdraft from the EMI itself. Both the English and Arabic texts let an EMI partner with a bank or other licensed entity that provides the overdraft, after SAMA's prior approval.
- Safeguarded funds may not be used for any other purpose, including lending.
- Customers may redeem their balance at any time, at par. The contract must state redemption conditions and fees clearly, fees must be proportionate to your actual costs, and the remaining balance must be redeemed when the contract ends.

Article 70 requires every payment service provider to have a policy setting risk-based user transaction limits and limits on its total outstanding e-money, and to obtain SAMA's non-objection before changing it.

Distribution also differs. Both licence types may appoint agents with SAMA's non-objection (Article 24), but only an EMI may use e-money distributors, who sell or redeem e-money without providing any payment service. Appointing one needs a business plan sent to SAMA 30 calendar days before the distributor starts and a notice within 10 calendar days of signing (Article 25).

## SAMA's register: 15 EMIs and 18 PIs

SAMA's public list of licensed payments companies showed 33 non-bank licensees when we read it on 19 November 2026.

| Label on SAMA's register | Number of firms |
|---|---|
| Electronic Money Institution (EMI) | 15 |
| Payment Institution (PI) | 18 |
| Total | 33 |

Source: SAMA, Licensed Entities: Payments (non-banks), read 19 November 2026.

The total matches SAMA's own statement of 22 July 2026, when it licensed Malaa Company for Information Technology for payment account information services and said there were "now 33 licensed companies offering payment services in Saudi Arabia". Read the split with three limits in mind. The register shows licence expiry dates, not grant dates. It does not say whether each firm is Micro or Major. And the PI label also covers open banking licensees: Malaa appears on the register as a PI.

## Deciding in practice: steps for founders and compliance teams

1. Map every flow of customer money in the product, from top-up to payout, and mark where a balance is held and for how long.
2. Apply the three-part e-money test to each balance and record the answer and the reasoning.
3. Check the closed-loop exclusion strictly. If the balance can be cashed out or spent outside your group or network, assume it is e-money.
4. List every service the product will run, so the licence SAMA grants names them all.
5. Model 12 months of figures against the Micro limits, using the projection rule if you have no history.
6. Fix the legal form before incorporation. An EMI must be a joint stock company from the start.
7. Review product features against Article 69: interest, holding rewards, overdrafts, redemption fees.
8. Plan distribution and write the Article 70 limits policy, because changing it later needs SAMA's non-objection.

If two licences seem to fit, ask SAMA before filing, because the application, capital and legal form all follow from the category. Saudi Compliance prepares this analysis and the licence file for wallet and payments businesses through its [e-money licence](@/licensing/e-money-licence/) support.

## Status: in force, no amendment known

As of 19 November 2026, the Implementing Regulations of the Law of Payments and Payment Services (No. 000044093096, dated 13 June 2023, 24/11/1444H) are in force, and the SAMA Rulebook lists their status as "In-Force". We know of no published draft amending the PI and EMI categories. This guide was last reviewed on 19 November 2026, and we will update it when SAMA publishes a change to the categories, limits or capital.

## Sources

- [SAMA Rulebook: Implementing Regulations of the Law of Payments and Payment Services (English)](https://rulebook.sama.gov.sa/en/implementing-regulations-payments-and-payment-services-law)
- [SAMA Rulebook: اللائحة التنفيذية لنظام المدفوعات وخدماتها (Arabic)](https://rulebook.sama.gov.sa/ar/%D8%A7%D9%84%D9%84%D8%A7%D8%A6%D8%AD%D8%A9-%D8%A7%D9%84%D8%AA%D9%86%D9%81%D9%8A%D8%B0%D9%8A%D8%A9-%D9%84%D9%86%D8%B8%D8%A7%D9%85-%D8%A7%D9%84%D9%85%D8%AF%D9%81%D9%88%D8%B9%D8%A7%D8%AA-%D9%88%D8%AE%D8%AF%D9%85%D8%A7%D8%AA%D9%87%D8%A7)
- [SAMA: Licensed Entities, Payments](https://www.sama.gov.sa/en-US/Supervision/LicenseEntities/Pages/Licensed_Payment_Service_Providers_companies.aspx)
- [SAMA: SAMA Licenses Malaa Company for Information Technology to Provide Open Banking Services (22 July 2026)](https://www.sama.gov.sa/en-US/MediaCenter/News/Pages/news-1161.aspx)
