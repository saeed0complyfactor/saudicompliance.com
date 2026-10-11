---
title: Applying for a SAMA Open Banking Licence: File and Pitfalls
h1: Applying for a SAMA <em>open banking</em> licence
description: Applying for a SAMA open banking licence: SAR 500,000 (AIS) or SAR 1m (PIS) capital, the Appendix A file, and what SAMA's published texts leave open.
date: 2026-10-11
updated: 2026-10-11
hero: glass-tower
service: @/licensing/open-banking-licence/
service_label: Open banking licence support
tags: Open banking, SAMA licensing
---
To apply for a SAMA open banking licence, choose the AIS licence (SAR 500,000 of initial capital) or the PIS licence (SAR 1 million, which also covers AIS), confirm the legal form and bank guarantee with SAMA, and email an in-principle file built on Appendix A of the Licensing Guidelines to NBFI-LIC@SAMA.GOV.SA. SAMA decides within 90 calendar days of confirming the file is complete, and you then have 180 days to incorporate. The fee is SAR 20,000 for either licence, and every licence SAMA had announced by 11 October 2026 was for account information.

Two points are still open on the published texts: the legal form an AIS or PIS company must take, and whether the bank guarantee filed with the application is 100% or 20% of minimum capital. Ask SAMA about both before you incorporate or arrange the guarantee.

> **Key takeaways** We found no separate open banking licence or capital schedule: SAMA licenses AIS and PIS providers under the payments rules. AIS needs SAR 500,000 of initial capital and PIS SAR 1 million, each with a SAR 20,000 fee and mandatory professional indemnity insurance. Legal form and the size of the application bank guarantee are not settled in the published texts. Plain AIS and PIS models now have a licensing path, and the sandbox FAQ says it does not take models an existing licence already covers.

## SAMA's Open Banking Framework covers account information and payment initiation

SAMA released the Open Banking Framework for account information on 2 November 2022 and for payment initiation in September 2024, and began licensing providers on 26 March 2026 after the sandbox phase. The full timeline and the capital and fee table are on our [open banking licence](@/licensing/open-banking-licence/) page.

The technical standards and SAMA's Open Banking Lab are available on request to SAMA's Open Banking team, and eSAMA lists "requesting access to Open Banking services" among its services. On our reading of the official texts, the framework sets the technical standards, and the licence itself comes from the payments regime.

SAMA gave the names of its first two account information licensees in transliterated Arabic; press reports identify them as Neotek (New Technology for Software Solutions) and Lean Technologies. Later account information licences went to Tatbiq Darahem on 10 May 2026, which press reports identify as Drahim, and to Malaa on 22 July 2026.

## AIS and PIS providers need a SAMA payments licence

Article 4 of the Law of Payments and Payment Services says no person may provide payment services in the Kingdom unless SAMA has licensed them. Article 6 of the Implementing Regulations lists the regulated services, and payment initiation and payment account information are items 9 and 10. Each has its own licence type in the fee schedule (Article 23) and the capital article (Article 44).

Part 8 of the Regulations (Articles 95 to 100) holds the open banking operating rules. Payment account providers, which include banks, must give licensed PIS and AIS providers access with the customer's consent (Article 96). A PIS provider must never hold client funds and may not alter a transaction (Article 97). Both must make the disclosures in Article 98.

An account information service provider in Saudi Arabia whose product only reads account data with the customer's consent needs the AIS licence. If it also initiates payments from a customer's account, it needs the PIS licence, whose SAR 1 million of capital covers account information as well, so one licence does both.

### How open banking fits next to payment institution and e-money licences

The AIS and PIS licences sit in the same family as the payment institution and e-money licences, whose initial capital under Article 44 runs from SAR 1 million (Micro PI) to SAR 10 million (Major EMI). The boundary matters when a product does more than read data or send payment instructions. Executing payment transactions, acquiring and issuing e-money are separate Article 6 services and need a [payment institution licence](@/licensing/payment-institution-licence/) or an [e-money licence](@/licensing/e-money-licence/). Wamda reports that Lean Technologies, one of the first AIS licensees, also holds a Major Payment Institution licence. Licensed banks are exempt from payments licensing (Article 48).

## What is confirmed and what is still unclear

Several figures that circulate online for open banking are not in anything SAMA has published. This table separates what the official texts say from what they leave open.

| Point | Position on the published texts |
|---|---|
| Initial capital | Confirmed in Art. 44: SAR 1m for PIS, SAR 500,000 for AIS. We found no separate open banking capital schedule, and secondary claims of a dedicated open banking capital figure are unconfirmed |
| Licence fee | Confirmed: SAR 20,000 each (Art. 23) |
| Professional indemnity insurance | Confirmed: mandatory, or a comparable guarantee (Art. 46) |
| Legal form | Unconfirmed. Art. 14 requires a joint stock company for Major PI, Micro EMI and Major EMI, and allows a JSC, simplified JSC or LLC for Micro PI. We found no stated form for AIS or PIS |
| Bank guarantee at application | Conflict. Art. 8 of the Regulations says equal to minimum capital; Appendix A of the current Licensing Guidelines says 20% of minimum capital |
| Decision timeline | Confirmed: 90 calendar days from SAMA's completeness notice, or a revised timeline SAMA notifies (Art. 11). Secondary claims of a fixed six-month open banking process are unconfirmed |
| Saudization ratio | No fixed percentage in the Regulations. Art. 29 requires compliance with the rules on non-Saudi employment, and the business plan must show the planned share of non-Saudi staff (Art. 8) |
| PIS licences granted | None announced by SAMA that we found as of 11 Oct 2026 |
| Application channel | Email under the Licensing Guidelines. eSAMA handles open banking access, sandbox and senior-position requests; we found no official statement that payments licence applications have moved to eSAMA |

The SAMA Rulebook says the Arabic version of its texts prevails, and some English pages state they are not the latest version. Check every figure you rely on against the Arabic page.

## Data protection and cyber security expectations

Open banking runs on customer account data. Article 37 of the Payments Implementing Regulations covers data protection and client confidentiality, and SAMA's rulebook has a section on PDPL adherence and data governance that applies to all supervised firms.

### PDPL obligations

The Personal Data Protection Law (Royal Decree M/19; secondary sources report an amendment by Royal Decree M/148) applies alongside SAMA's rules. Those sources also report that it has been fully enforceable since 14 September 2024 and describe the practical duties: controller registration on SDAIA's National Data Governance Platform, a data protection officer, transfer assessments and 72-hour breach notices.

Draft amendments to the PDPL Implementing Regulations were reported by Clyde & Co to be on consultation from 6 October to 5 November 2026, proposing default storage inside the Kingdom and mandatory controller registration. They are still a draft. See [PDPL compliance](@/pdpl-compliance-saudi-arabia/).

### SAMA and NCA cyber frameworks

Article 34 requires compliance with SAMA's Cyber Security Framework, whose scope covers payments and the sandbox. Article 33 brings in the Business Continuity Management Framework, and Article 35 SAMA's data and technology governance rules.

The NCA's Essential Cybersecurity Controls (ECC-2:2024) are mandatory for government entities and private operators of critical national infrastructure, which leaves most private fintechs outside their direct scope. Secondary sources report that bank and government clients map procurement checks to them, and cloud-hosted providers should look at the Cloud Cybersecurity Controls (CCC-2:2024). See [cybersecurity compliance in Saudi Arabia](@/cybersecurity-compliance-saudi-arabia/).

## The sandbox route now that licensing is open

Before March 2026, open banking providers in Saudi Arabia worked through SAMA's regulatory sandbox. SAMA said licensing began once the sandbox phase was complete. The sandbox FAQ says SAMA does not accept sandbox applications for business models that an existing licence already covers, and AIS and PIS now have one.

The [SAMA regulatory sandbox](@/licensing/sama-regulatory-sandbox/) still fits a model that the current rules do not cover. The stages are application (60 days, ending in a No Objection Letter for testing with dummy data), operational readiness (120 days, ending in a Letter of Acceptance), live testing for 6 to 12 months, and exit. SAMA expects the licence application to start after month 6 of testing and by month 9.

SAMA may relax fees, capital and board composition in the sandbox, but data protection, AML/CFT, fitness and propriety and cyber security are unlikely to be relaxed. Applications go through eSAMA, and SAMA launched an enhanced sandbox e-service on 28 June 2026. Foreign innovators accepted directly register with the Ministry of Investment and the Ministry of Commerce. If you are mid-test, ask SAMA how and when to move to a licence.

## Steps to apply for an open banking licence

The process is the one in the Payments Implementing Regulations and the Guidelines to Apply for Payment Service Providers License.

1. Decide the licence type: AIS only, or PIS with or without AIS.
2. Confirm legal form and the bank guarantee amount with SAMA, using the enquiries address NBFI-LIC-INFO@SAMA.GOV.SA.
3. Complete SAMA's License Application Form and Fit and Proper Forms, and build the Appendix A file.
4. Email the in-principle application to NBFI-LIC@SAMA.GOV.SA.
5. Wait for SAMA to confirm the file is complete (Art. 11(1)), and answer any request for more information within 30 calendar days.
6. Receive SAMA's decision within 90 calendar days of the completeness notice, or a revised timeline.
7. Incorporate within 180 days of in-principle approval (Art. 14(3)). The approval is valid for up to one year, extendable by 180 days, and does not let you operate (Art. 15).
8. Meet the final requirements, including insurance, staff and capital, and pay the SAR 20,000 fee (Art. 23).
9. Receive the licence and appear on SAMA's public register (Art. 16), then request Open Banking Framework and Lab access through eSAMA if you have not already.

Renewal applications are due at least six months before the licence expires (Art. 17). A foreign-owned company also needs investment registration with the Ministry of Investment before it takes a SAMA licence. Our [Saudi financial regulators guide](@/insights/saudi-financial-regulators-guide/) explains how MISA, the Ministry of Commerce and SAMA fit together.

## Documents to prepare for the in-principle application

Appendix A of the Licensing Guidelines lists the in-principle file for all payment service providers. It includes:

- the application form and a board resolution
- draft articles of association and an organisation chart
- a shareholder list, with fit and proper forms for shareholders, senior positions and board and committee members
- a feasibility study
- the bank guarantee
- a three-year business plan with ICAAP, a liquidity assessment and a Saudization and recruitment plan
- draft policies: AML/CTF, business continuity, data protection, cyber security, consumer protection, safeguarding with the bank agreement, fraud, settlement, account opening and risk-based limits
- key contracts, the business continuity plan and the IT architecture
- three years of audited accounts where applicable

The list is written for every type of payment service provider. A PIS provider never holds client funds, so ask SAMA which items, such as the safeguarding policy, apply to your licence type. For open banking, add evidence of professional indemnity insurance and show how your consent, authentication and disclosure design meets Articles 96 to 98.

## Pitfalls to plan around

- Incorporating before SAMA confirms the legal form for AIS or PIS, then having to convert the company.
- Arranging the bank guarantee before SAMA confirms whether Article 8's 100% of minimum capital or the Licensing Guidelines' 20% applies.
- Treating sandbox status or a bilateral bank agreement as permission to operate. Clyde & Co commentary says these no longer suffice, and SAMA ties licensing to the end of the sandbox phase.
- Designing a PIS flow that holds customer money, which Article 97 forbids.
- Using account data to match customers with finance companies for a fee. On our reading, that may also need SAMA's [finance aggregation licence](@/licensing/finance-aggregation-licence/), a separate regime under the Finance Companies Control Law with SAR 2 million of capital.
- Hiring senior staff late. The Chief Compliance Officer, AML/CTF Director, Information or Cyber Security Director and IT Director are Saudi-only posts, and each needs SAMA's written non-objection before acting. See [compliance function](@/compliance-function/).
- Raising money without telling SAMA. A May 2026 circular to payment licensees requires notification before conducting investment rounds.

Saudi Compliance supports open banking applicants on licence scoping, the Appendix A file and the senior appointments SAMA must approve. For the full list of SAMA and CMA routes, start at [licensing](@/licensing/), or [contact us](@/contact/) to talk through your model.

## Sources

- [SAMA: Open Banking Framework release 1 (news-794)](https://www.sama.gov.sa/en-US/MediaCenter/News/Pages/news-794.aspx)
- [SAMA: Open Banking Framework release 2, payment initiation (news-1036)](https://www.sama.gov.sa/en-US/MediaCenter/News/Pages/news-1036.aspx)
- [SAMA: Open Banking programme](https://www.openbanking.sama.gov.sa/index-en.html)
- [SAMA: eSAMA portal trial launch (news-1068)](https://www.sama.gov.sa/en-US/MediaCenter/News/Pages/news-1068.aspx)
- [SAMA: SAMA commences licensing of open banking services (news-1135)](https://www.sama.gov.sa/en-US/MediaCenter/News/Pages/news-1135.aspx)
- [SAMA: Two companies licensed for account information services (news-1136)](https://www.sama.gov.sa/en-US/MediaCenter/News/Pages/news-1136.aspx)
- [SAMA: Tatbiq Darahem account information licence (news-1148)](https://www.sama.gov.sa/en-US/MediaCenter/News/Pages/news-1148.aspx)
- [SAMA: Malaa account information licence (news-1161)](https://www.sama.gov.sa/en-US/MediaCenter/News/Pages/news-1161.aspx)
- [SAMA Rulebook: Law of Payments and Payment Services](https://rulebook.sama.gov.sa/en/node/1195)
- [SAMA Rulebook: Implementing Regulations of the Law of Payments and Payment Services](https://rulebook.sama.gov.sa/en/implementing-regulations-payments-and-payment-services-law)
- [SAMA Rulebook: Guidelines to Apply for Payment Service Providers License](https://rulebook.sama.gov.sa/en/node/10951)
- [SAMA Rulebook: License Application Form](https://rulebook.sama.gov.sa/en/node/9987)
- [SAMA Rulebook: Fit and Proper Form](https://rulebook.sama.gov.sa/en/node/2188)
- [SAMA Rulebook: Requirements for Appointments to Senior Positions (Arabic, latest)](https://rulebook.sama.gov.sa/ar/node/1997)
- [SAMA Rulebook: Payments sector circulars](https://rulebook.sama.gov.sa/en/payment-systems-and-payment-services-providers-circulars)
- [SAMA Rulebook: Cyber Security Framework](https://rulebook.sama.gov.sa/en/node/3837)
- [SAMA Rulebook: Business Continuity Management Framework](https://rulebook.sama.gov.sa/en/node/3709)
- [SAMA Rulebook: PDPL adherence and data governance](https://rulebook.sama.gov.sa/en/node/4725)
- [SAMA Rulebook: Regulatory Sandbox lifecycle](https://rulebook.sama.gov.sa/en/regulatory-sandbox-lifecycle)
- [SAMA Rulebook: Who can apply to the Regulatory Sandbox](https://rulebook.sama.gov.sa/en/who-can-apply-regulatory-sandbox)
- [SAMA Rulebook: Regulatory Sandbox exemptions and waivers](https://rulebook.sama.gov.sa/en/types-exemptions-waivers)
- [SAMA Rulebook: Regulatory Sandbox FAQ](https://rulebook.sama.gov.sa/en/regulatory-sandbox-faq)
- [SAMA: Enhanced Regulatory Sandbox e-service (news-1154)](https://www.sama.gov.sa/en-US/MediaCenter/News/Pages/news-1154.aspx)
- [SAMA Rulebook: Rules of Licensing Finance Support Activities](https://rulebook.sama.gov.sa/en/rules-licensing-finance-support-activities-0)
- [SDAIA: National Data Governance Platform](https://dgp.sdaia.gov.sa)
- [NCA: Essential Cybersecurity Controls (ECC-2:2024)](https://nca.gov.sa/en/regulatory-documents/controls-list/ecc/)
- [NCA: Cloud Cybersecurity Controls (CCC-2:2024)](https://nca.gov.sa/en/regulatory-documents/controls-list/ccc/)
- [Ministry of Investment](https://misa.gov.sa)
