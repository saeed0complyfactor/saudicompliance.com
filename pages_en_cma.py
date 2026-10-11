# CMA licence service pages (English). Same dict schema as content_en.PAGES.
# Source of truth: seo/research/cma.md (research date 11 October 2026).

PAGES = [
# ---------------------------------------------------------------------------
# 1. Hub: all CMA routes
# ---------------------------------------------------------------------------
{
    "slug": "licensing/cma-licences",
    "stage": 1,
    "hero": "tower-bw",
    "title": "CMA Licence Saudi Arabia: Activities, Capital and Fees",
    "description": "CMA licences in Saudi Arabia: the five securities activities, capital in force, 2020 fees, registered persons and the May 2026 draft not yet adopted.",
    "h1": "CMA <em>licences</em> for fintech and investment firms",
    "lede": "Securities business in or into Saudi Arabia needs Capital Market Authority authorisation. This page maps every CMA route, the capital and fees in force today, and the draft changes that are still pending.",
    "blocks": [
        {"type": "prose", "h2": "Who needs a CMA licence", "body": [
            "Article 31 of the Capital Market Law says no person may carry on securities business in the Kingdom, or claim to, without a CMA licence. That holds even when the security is listed or traded on a foreign regulated market. The Securities Business Regulations add that only a CMA-authorised capital market institution (CMI) or an exempt person may carry on securities business.",
            "The perimeter reaches firms based abroad. Under Article 4 of the Securities Business Regulations, activity carried on with or for a person in the Kingdom is presumed to be carried on in the Kingdom, and securities advertisements aimed at people in Saudi Arabia, online ones included, must be made or approved by a CMI.",
            "The CMA prosecutes unlicensed activity. In March 2026 a person was convicted and fined SAR 250,000 for providing advisory services on social media without a licence.",
        ]},
        {"type": "steps", "h2": "Four routes for fintech and investment firms", "items": [
            ("FinTech Experimental Permit", "A time-limited permit to test a new securities-related product with real clients through the CMA FinTech Lab, for up to two years from commencement. See the <a href=\"@/licensing/cma-fintech-experimental-permit/\">FinTech Experimental Permit guide</a>."),
            ("Capital market institution licence", "The full licence for dealing, arranging, managing, advising or custody, with capital, legal form and registered persons set per activity. See the <a href=\"@/licensing/capital-market-institution-licence/\">CMI licence guide</a>."),
            ("Crowdfunding under an Arranging licence", "Equity crowdfunding since 2022 and debt-instrument crowdfunding since September 2025, both run by a CMI authorised for Arranging. See the <a href=\"@/licensing/crowdfunding-licence-saudi-arabia/\">crowdfunding licence guide</a>."),
            ("Robo-advisory under a Managing licence", "A regulated service since 5 March 2026, open only to CMIs licensed for Managing. See the <a href=\"@/licensing/robo-advisory-licence/\">robo-advisory guide</a>."),
        ]},
        {"type": "table", "h2": "The five securities activities and the capital in force", "head": ["Activity", "What it covers", "Minimum paid-up capital", "Legal form"], "rows": [
            ["Dealing", "Dealing in a security as principal or agent, including buying, selling, managing subscriptions and underwriting", "SAR 50 million", "Restricted forms (Art 6(f))"],
            ["Custody", "Safeguarding assets that include a security, and the related administration", "SAR 50 million", "Restricted forms (Art 6(f))"],
            ["Managing investments and operating funds", "Discretionary management of securities plus operating investment funds", "SAR 20 million", "Restricted forms (Art 6(f))"],
            ["Managing investments only", "Discretionary management of securities, no fund operation", "One year of expected expenses", "Restricted forms (Art 6(f))"],
            ["Arranging", "Introducing parties for an offering or underwriting, and advising on corporate finance; also the activity for securities crowdfunding", "One year of expected expenses", "Any legal form established in the Kingdom"],
            ["Advising", "Advice on a security, including financial planning and wealth management", "One year of expected expenses", "Any legal form established in the Kingdom"],
        ], "note": "Capital Market Institutions Regulations, Art 6(g), English text amended by CMA Board Resolution 2-3-2026 (7 January 2026). Ongoing capital adequacy is governed separately by the CMA Prudential Rules. Restricted forms include a joint stock company and a subsidiary of a local bank."},
        {"type": "callout", "title": "Plan on the figures in force", "body": "A May 2026 CMA draft proposes lower capital for dealing and custody. It had not been adopted when we last checked in October 2026, and the dealing cuts also need an amendment to the Capital Market Law. Build your capital plan and business case on the table above."},
        {"type": "table", "h2": "May 2026 draft capital figures (proposed, not in force)", "head": ["Activity", "In force today", "Proposed in the May 2026 draft"], "rows": [
            ["Dealing as principal, underwriting, managing subscriptions and margin", "SAR 50 million", "SAR 20 million"],
            ["Dealing as agent", "SAR 50 million", "SAR 10 million"],
            ["Custody", "SAR 50 million", "SAR 20 million"],
            ["Arranging that holds client money for securities crowdfunding", "One year of expected expenses", "One year of expected expenses, and at least SAR 2 million"],
            ["Managing investments and operating funds", "SAR 20 million", "Unchanged"],
            ["Managing investments only, arranging (other), advising", "One year of expected expenses", "Unchanged"],
        ], "note": "Consultation CMA_N_4054, published 18 May 2026 and closed 17 June 2026. Our scan of CMA news up to 5 October 2026 found no approval. Article 33 of the Capital Market Law still sets a SAR 50 million floor for brokerage companies."},
        {"type": "prose", "h2": "What else the May 2026 draft would change", "body": [
            "The draft would also cut the licensing and commencement documents, extend IT Officer registration to every CMI that uses a technology platform, link KYC to each client's money-laundering risk rating through three new forms, and let advising-only CMIs carry on other businesses. None of this applies until the CMA publishes an approved text.",
        ]},
        {"type": "table", "h2": "Licence fees: study fee and annual renewal", "head": ["Activity", "Application study fee (SAR)", "Annual renewal fee (SAR)"], "rows": [
            ["Dealing", "85,000", "85,000"],
            ["Managing investments and operating funds", "60,000", "60,000"],
            ["Managing investments", "30,000", "30,000"],
            ["Arranging", "20,000", "20,000"],
            ["Advising", "20,000", "20,000"],
            ["Custody", "15,000", "15,000"],
        ], "note": "CMA circular ص/1/6/5989/20 dated 27 October 2020, based on a Board decision of 24 August 2020. The circular is a scanned Arabic PDF with no English version. It is still linked from the CMA Forms page, but we cannot confirm the amounts are unchanged since 2020. Check before you pay."},
        {"type": "prose", "h2": "Renewal every year, per activity", "body": [
            "Each amount is charged as the study fee with the application and again every year as the renewal fee for that activity, due by 30 June. Renewal depends on the CMA having no concerns about the firm's capability and fitness, and on the firm still meeting financial adequacy and minimum capital. The FinTech Experimental Permit has no fee under the current Instructions.",
        ]},
        {"type": "list", "h2": "Registered persons every CMI needs", "items": [
            "At all times: a registered CEO, CFO, Compliance Officer and MLRO (CMIR Art 20(b)).",
            "An IT Officer, registered at all times, where the CMI offers robo-advisory. The IT Officer is also a registrable function for CMIs arranging securities crowdfunding.",
            "The CEO, CFO and Compliance Officer must be separate people unless the CMA approves otherwise, and the Compliance Officer may not perform a client function.",
            "A CMI limited to managing investments, arranging or advising may outsource the CFO, Compliance Officer or MLRO function within limits; see the <a href=\"@/licensing/capital-market-institution-licence/\">CMI licence guide</a>.",
            "Registered persons must be resident in the Kingdom unless the CMA grants an exemption (Art 24(b)), and must pass the CMA qualification exams or hold an exemption (Art 21(d)).",
        ]},
        {"type": "table", "h2": "CMA qualification exams by function", "head": ["Function", "Exams"], "rows": [
            ["General registrable functions", "CME-1A and CME-1B"],
            ["Compliance and AML/CTF route", "CME-1B, CME-2A and CME-2B"],
            ["Securities brokers", "CME-3A and CME-3B"],
            ["Managing activity (asset managers)", "CME-4A and CME-4B"],
            ["Corporate finance", "CME-5A and CME-5B"],
        ], "note": "The new exam series has been mandatory since 1 February 2023 and was developed with the Financial Academy and CISI. Holders of the old certificates can still register. The CMA guide names the route \"Compliance and AML/CTF\"; confirm with the CMA which route it expects for your MLRO."},
        {"type": "prose", "h2": "Foreign firms need a Saudi entity", "body": [
            "The CMIR have no branch route for a foreign securities firm. An applicant must be established in the Kingdom, and a CMI must keep its management and head office in the Kingdom. For dealing, custody and managing, a foreign group therefore needs a Saudi entity in one of the permitted legal forms. Arranging and advising can use any Saudi legal form, including a limited liability company. Entity set-up comes first; see <a href=\"@/incorporation/\">incorporation</a>.",
            "Foreign groups do use this route. In 2026 the CMA licensed Standard Chartered Capital Saudi Arabia, Brookfield Arabia and Neuberger Berman Saudi as Saudi entities.",
            "A separate Offshore Securities Business Licence, for CMIs holding a Ministry of Investment regional headquarters licence, was put out for consultation in May 2025 (CMA_N_3796, closed 28 June 2025). We found no approval through early October 2026, so it is not available today.",
        ]},
        {"type": "prose", "h2": "AML: the national law applies directly", "body": [
            "The CMA's own Anti-Money Laundering and Counter-Terrorist Financing Rules (Board Resolution 1-39-2008, last amended in 2017) were rescinded in November 2018. The CMA gave the new AML Law (Royal Decree M/20, 1439H), its Implementing Regulations and the Combating Terrorism and its Financing Law as the reason. The 2017 text is still hosted on aml.gov.sa without a rescission notice, so check the date of anything you are handed.",
            "Today a CMI's obligations come from the AML Law and its Implementing Regulations (the law was amended in April 2026), the counter-terrorist financing law, and the CMA's Investment Accounts Instructions on KYC and account opening. See <a href=\"@/compliance-function/\">building the compliance function</a>.",
        ]},
        {"type": "callout", "title": "No CMA licence for crypto", "body": "The CMA has issued no regulation on crypto-assets or security tokens, and has no licence category for crypto exchanges or custodians. <a href=\"@/digital-assets/\">What exists for digital assets</a>."},
        {"type": "faq", "h2": "Common questions", "items": [
            ("Can a foreign firm serve Saudi clients from abroad without a CMA licence?", "Usually not. Business carried on with or for a person in the Kingdom is presumed to be carried on in the Kingdom, so the firm needs a licence or an exemption."),
            ("Are the lower May 2026 capital figures in force?", "No. The consultation closed on 17 June 2026 and we found no CMA approval up to early October 2026. The dealing figures also depend on amending the SAR 50 million floor in Article 33 of the Capital Market Law."),
            ("How long does CMA licensing take?", "The CMA's service card gives 0 to 60 business days, varying by service. The full path is longer: information requests (with a 30-day window to respond), the Board's licence resolution, then commencement-of-business requirements before the firm starts."),
            ("Does the CMA require Saudi nationals in compliance roles?", "The CMIR contain no Saudization quota. They require registered persons to be resident in the Kingdom unless the CMA grants an exemption."),
        ]},
    ],
    "sources": [
        ("CMA: Capital Market Institutions Regulations (amended 2026)", "https://cma.gov.sa/en/RulesRegulations/Regulations/Documents/the_Capital_Market_Institutions_Regulations-en.pdf"),
        ("CMA: Securities Business Regulations", "https://cma.gov.sa/en/RulesRegulations/Regulations/Documents/Amended%20Securities%20Business%20Regulations.pdf"),
        ("CMA news: draft amendments to the CMI Regulations (May 2026)", "https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_4054.aspx"),
        ("CMA circular on licence fees (2020, Arabic)", "https://cma.gov.sa/RulesRegulations/circulars/Documents/circular77.pdf"),
        ("CMA news: AML/CTF Rules rescinded (2018)", "https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_2486.aspx"),
        ("CMA: qualification exams guide", "https://cma.gov.sa/en/AboutCMA/CME/Documents/CMEExamsGuidelineEN.pdf"),
    ],
    "related": ["cma-fintech-experimental-permit", "capital-market-institution-licence", "compliance-function"],
},

# ---------------------------------------------------------------------------
# 2. FinTech Experimental Permit
# ---------------------------------------------------------------------------
{
    "slug": "licensing/cma-fintech-experimental-permit",
    "stage": 1,
    "hero": "curved-glass",
    "title": "CMA FinTech Experimental Permit: 2026 Guide",
    "description": "How the CMA FinTech Experimental Permit works: who can apply, the process, the two-year limit, permit numbers and the April 2026 draft update.",
    "h1": "CMA FinTech <em>Experimental Permit</em>",
    "lede": "The CMA FinTech Lab lets a firm test a new securities-related product with real clients, under conditions the CMA sets, for up to two years before it needs a full licence.",
    "blocks": [
        {"type": "prose", "h2": "What the permit is", "body": [
            "The Financial Technology Experimental Permit is granted under the CMA's FinTech Experimental Permit Instructions, issued by Board Resolution 1-4-2018 and updated by Resolution 2-9-2021. The Lab opened in 2018 and took its first batch of applications in February that year.",
            "Anyone may apply, including a firm that is not a capital market institution, provided the product it wants to test relates to securities activities. A CMI that already holds the authorisation the product needs does not need a permit. A product that is mature and can comply with the full rules is expected to apply for a <a href=\"@/licensing/capital-market-institution-licence/\">capital market institution licence</a> instead.",
        ]},
        {"type": "list", "h2": "Eligibility: what the CMA tests", "items": [
            "The product involves a securities activity.",
            "It is genuinely innovative.",
            "It brings benefits to the market, to compliance or to clients.",
            "It is developed far enough to be tested with real clients.",
            "The applicant has adequate resources, is fit and proper and acts with integrity.",
            "The applicant has done its own regulatory due diligence.",
            "There is a client exit strategy if the test ends.",
        ]},
        {"type": "steps", "h2": "How an application runs", "items": [
            ("Submit the application", "Applications go in on the CMA's \"FINTECH application\" form by email to the FinTech Lab. They are accepted all year but assessed in announced batches; the eighth review had a cut-off of 31 December 2024."),
            ("Eligibility and conditions", "The CMA confirms eligibility and sets additional requirements for your test: client numbers and types, transaction sizes, suitability, protection of client assets, data, promotions, capital if any, and reporting."),
            ("Permit granted", "The CMA issues the permit with those conditions attached."),
            ("Commencement-of-business requirements", "Within the period the CMA sets, you establish a Saudi commercial entity, adopt conflict-of-interest policies, comply with the AML and counter-terrorist financing laws, test information security, and put key agreements and outsourcing governance in place."),
            ("Approval to start", "The CMA must approve before you begin operating with clients."),
        ]},
        {"type": "callout", "title": "AML applies before day one", "body": "Section 7 of the Instructions requires permit holders to comply with the AML and counter-terrorist financing laws before they commence business. Treat the AML programme as part of the application work. See <a href=\"@/compliance-function/\">the compliance function</a>."},
        {"type": "list", "h2": "Rules while you hold a permit", "items": [
            "Suspensions of the test may not total more than three months.",
            "No gifts or incentives to clients.",
            "No loss-sharing arrangements with clients.",
            "Owners may not exit the business during the permit period.",
            "The permit conditions on client numbers, transaction sizes and reporting apply for the whole test.",
        ]},
        {"type": "prose", "h2": "Duration, extensions and moving to a full licence", "body": [
            "A permit lasts up to two years from commencement of business. An extension request must be filed at least three months before expiry, and the CMA grants extensions only in exceptional cases. At expiry the firm either runs its client exit strategy or obtains a full licence.",
            "Debt-instrument crowdfunding shows how the move works. The model was tested in the Lab from the second quarter of 2021 and became a licensed activity in September 2025. Existing permit holders may continue until their permits expire and must then hold an Arranging licence, and the CMA now accepts new Lab applications for that model only where there is an innovative element to test. Robo-advisory, also tested in the Lab, became a regulated service in March 2026. See <a href=\"@/licensing/crowdfunding-licence-saudi-arabia/\">crowdfunding</a> and <a href=\"@/licensing/robo-advisory-licence/\">robo-advisory</a>.",
            "Plan the licence file during the test. The CMI licence needs capital, a permitted legal form for some activities, registered persons who have passed the CMA exams, and the Annex 3.1 documents, none of which you want to start in the last six months of a permit.",
        ]},
        {"type": "table", "h2": "How many permits: the numbers count different things", "head": ["Figure", "What it counts", "Source"], "rows": [
            ["17", "Permits granted by October 2021", "CMA press release"],
            ["53", "Permits granted from 2018 to the first half of 2024", "CMA press release, 5 December 2024"],
            ["68", "Permits by the end of the second quarter of 2025, with 50 firms registered and 36 operating", "September 2025 press release (not a CMA publication)"],
            ["45", "Companies on the CMA's live \"Authorized FinTech Test Companies\" list", "CMA website, page modified 19 July 2026"],
        ], "note": "The first three figures are cumulative permit totals since 2018. The 45 is a count of companies currently listed. A cumulative total keeps permits that have since ended, been cancelled or been replaced by a full licence, so the two series should not be compared as if they measured the same thing."},
        {"type": "prose", "h2": "What firms test in the Lab", "body": [
            "The live list covers debt instruments, fund distribution, robo-advisory, social trading, artificial intelligence in advisory, and a model the CMA calls \"Stock Ownership Transfer\". Earlier permits, listed in 2021, covered equity crowdfunding, robo-advisory, debt instruments, social trading and a platform using distributed ledger technology to arrange and offer securities and provide custody.",
            "The CMA's list does not describe the technology behind the Stock Ownership Transfer model, and the CMA has issued no rules on tokenisation. A Lab permit is a test permission for a named product. It does not create a digital-asset licence.",
        ]},
        {"type": "table", "h2": "Recent permit decisions", "head": ["Date", "Decision", "CMA announcement"], "rows": [
            ["4 May 2025", "Mekyal permit cancelled and licence suspended", "CMA_N_3788"],
            ["1 June 2025", "InvestSky permit for social trading", "CMA_N_3804"],
            ["8 December 2025", "Sindbad.Tech permit for AI in advisory", "CMA_N_3947"],
            ["30 July 2026", "Tatwir Aliddikhar robo-advisory permit cancelled at the company's request", "CMA_N_4095"],
            ["31 August 2026", "Lamha Tanbu permit for AI in advisory", "CMA_N_4110"],
        ]},
        {"type": "prose", "h2": "The April 2026 draft update is not adopted", "body": [
            "On 26 April 2026 the CMA consulted on new FinTech Experimental Permit Instructions (CMA_N_4030, consultation closed 27 May 2026). The FinTech Lab page still links only the 2021 Instructions, and we found no approval announcement, so the 2021 text governs applications today.",
            "The draft would move from batches to year-round submission and assessment, widen the scope to technology-based products related to securities business or the capital market, let the CMA charge a fee, impose a three-month wait before reapplying after a rejection (with all earlier observations addressed), and add governance and business-continuity requirements. The two-year validity is unchanged in the draft.",
        ]},
        {"type": "faq", "h2": "Common questions", "items": [
            ("Do we need a Saudi company to apply?", "Not to apply. Establishing a Saudi commercial entity is one of the commencement-of-business requirements you must meet after the permit is granted and before the CMA approves your start. Allow time for <a href=\"@/incorporation/\">incorporation</a> in your plan."),
            ("Can the permit be extended beyond two years?", "Only in exceptional cases, and the request must reach the CMA at least three months before expiry. Most firms should plan to be ready for a full licence or an orderly exit when the two years end."),
            ("Is there a fee for the permit?", "There is no fee under the current 2021 Instructions. The April 2026 draft would give the CMA power to charge one, but that draft has not been adopted."),
            ("When should we skip the Lab and apply for a licence?", "When the product already fits an existing licensed activity and can meet the full rules. Debt-instrument crowdfunding and robo-advisory now have licence routes, and the CMA expects mature, compliant products to apply for a CMI licence rather than a permit."),
        ]},
    ],
    "sources": [
        ("CMA: FinTech Experimental Permit Instructions (2021)", "https://cma.gov.sa/en/RulesRegulations/Regulations/Documents/FinTech_en.pdf"),
        ("CMA: FinTech Lab", "https://cma.gov.sa/en/Market/fintech/Pages/default.aspx"),
        ("CMA: Authorized FinTech test companies", "https://cma.gov.sa/en/Market/fintech/Pages/ExpFinTechs.aspx"),
        ("CMA: FinTech Lab FAQ", "https://cma.gov.sa/en/Market/Documents/FAQ_EN.pdf"),
        ("CMA news: draft FinTech Instructions update (April 2026)", "https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_4030.aspx"),
        ("CMA press release: eighth FinTech review", "https://cma.gov.sa/en/MediaCenter/PR/Pages/Eighth_Review_Fintech.aspx"),
    ],
    "related": ["cma-licences", "capital-market-institution-licence", "robo-advisory-licence"],
},

# ---------------------------------------------------------------------------
# 3. Capital market institution licence
# ---------------------------------------------------------------------------
{
    "slug": "licensing/capital-market-institution-licence",
    "stage": 1,
    "hero": "glass-tower",
    "title": "Capital Market Institution Licence: CMA 2026 Guide",
    "description": "CMA capital market institution licence in Saudi Arabia: the five activities, capital, Annex 3.1 documents, stages, registered persons and renewal.",
    "h1": "Capital market institution <em>licence</em>",
    "lede": "A CMI licence authorises one or more of five securities activities. The activities you choose fix your capital, your legal form, the people you must register and your annual fee.",
    "blocks": [
        {"type": "prose", "h2": "The rules behind the licence", "body": [
            "The licence rests on the Capital Market Law (Royal Decree M/30, 1424H), Articles 31 to 33, and the Securities Business Regulations, which define the five activities in Article 2 (new text in force since 1 January 2022). The detailed licensing rules are in the Capital Market Institutions Regulations (CMIR), first issued in 2005.",
            "The CMA's website carries two English copies of the CMIR at different amendment levels. The current text, amended by Board Resolution 2-3-2026 of 7 January 2026, is the file ending \"Regulations-en.pdf\". The copy ending \"Regulations_en.pdf\" still shows the September 2025 amendment. Work from the 2026 text.",
        ]},
        {"type": "table", "h2": "Each activity: scope, capital and fee", "head": ["Activity", "Scope", "Minimum capital (in force)", "Study fee and annual renewal (SAR)"], "rows": [
            ["Dealing", "Dealing in a security as principal or agent, including buying, selling, managing subscriptions and underwriting", "SAR 50 million", "85,000"],
            ["Managing investments and operating funds", "Discretionary management of securities and operating investment funds", "SAR 20 million", "60,000"],
            ["Managing investments", "Discretionary management of securities without operating funds", "One year of expected expenses", "30,000"],
            ["Arranging", "Introducing parties for offerings or underwriting, advising on corporate finance, and securities crowdfunding", "One year of expected expenses", "20,000"],
            ["Advising", "Advice on a security, including financial planning and wealth management", "One year of expected expenses", "20,000"],
            ["Custody", "Safeguarding assets that include a security, and the related administration", "SAR 50 million", "15,000"],
        ], "note": "Capital: CMIR Art 6(g). Fees: CMA circular of 27 October 2020 (Arabic only; amounts not confirmed as current). A May 2026 draft would lower dealing and custody capital; it is not in force."},
        {"type": "prose", "h2": "Choosing the activities", "body": [
            "Most fintech and wealth businesses fit a narrow set. A digital advice tool that recommends securities is Advising. A platform that runs discretionary portfolios, including robo-advisory, is Managing. A crowdfunding platform or a corporate finance boutique is Arranging. A brokerage app is Dealing, and holding client securities is Custody. The draft capital table and the full route map are on the <a href=\"@/licensing/cma-licences/\">CMA licences hub</a>.",
            "The choice has knock-on effects. Dealing, custody and managing require one of the restricted legal forms below and, for dealing and custody, SAR 50 million of paid-up capital. Arranging and advising accept any Saudi legal form and capital equal to a year of expected expenses. Firms limited to managing investments, arranging or advising also get lighter document and staffing rules, covered further down.",
            "Client money is the other decision. An arranging CMI may hold securities crowdfunding client money itself within caps; otherwise client money is held through a custody-licensed CMI. See <a href=\"@/licensing/crowdfunding-licence-saudi-arabia/\">crowdfunding</a>.",
        ]},
        {"type": "list", "h2": "Legal form for dealing, custody and managing (CMIR Art 6(f))", "items": [
            "A subsidiary of a local bank.",
            "A joint stock company.",
            "A subsidiary of a Saudi joint stock company engaged in financial services.",
            "A fourth option in the CMA's English text covers subsidiaries of certain foreign financial institutions licensed under the Banking Control Law. The English is an unofficial translation, so check the Arabic before relying on it.",
            "In every case the applicant must be established in the Kingdom, with its management and head office in the Kingdom (Art 6(h)). There is no branch route.",
        ]},
        {"type": "list", "h2": "What goes into the file", "items": [
            "The Authorisation Application, with the attachments listed in Annex 3.1 of the CMIR. Annex 3.1 covers both authorisation documents and commencement-of-business documents.",
            "Evidence for the Art 6(e) fit-and-proper test: adequate expertise and resources, management, systems, risk management and technology, and a qualified board and staff.",
            "A trade-name reservation from the Ministry of Commerce.",
            "Proof of payment of the study fee for each activity applied for.",
            "A Registration Application for each registrable function.",
            "Firms limited to managing investments, arranging or advising are excused some Annex 3.1 items. Robo-advisory applicants get a narrower exemption.",
        ]},
        {"type": "steps", "h2": "Application stages", "items": [
            ("Prepare", "Read the Capital Market Law, the implementing regulations and the CMA circulars that apply to your activities, then build the Annex 3.1 file. Foreign shareholders need the Saudi entity in place; see <a href=\"@/incorporation/\">incorporation</a>."),
            ("File on the portal", "Applications go through the Authorisation System on the CMA's Unified Business Sector Portal (eservices.cma.gov.sa), which also handles licence variations and registration of registrable functions. The CMA's service card gives 0 to 60 business days, varying by service."),
            ("Review and information requests", "The CMA may ask for more information and may refuse the application if it is not provided within 30 days (Art 7). Quick, complete answers keep the file moving."),
            ("Licence resolution", "The CMA Board issues a licence resolution. The firm cannot start business on the resolution alone."),
            ("Commencement of business", "The firm completes the commencement-of-business requirements. The CMA then publishes a second announcement that the firm is licensed and has completed those requirements."),
        ]},
        {"type": "prose", "h2": "Registered persons and minimum staffing", "body": [
            "Every CMI must have a registered CEO, CFO, Compliance Officer and MLRO at all times, plus a registered IT Officer if it offers robo-advisory (Art 20(b)). Other registrable functions include board members and partners, senior managers linked to securities business, and client-facing staff such as investment advisers, portfolio managers and brokerage professionals. The CEO, CFO and Compliance Officer must be different people unless the CMA approves otherwise, and the Compliance Officer may not carry out a client function.",
            "Smaller licences can run lean. A CMI limited to managing investments or arranging needs at least two registered persons, one of them the CEO; an advising-only CMI needs one registered CEO, with other functions outsourced (Art 20(f)). Managing licensees need at least two registered portfolio managers (Art 20(g)). Firms limited to managing investments, arranging or advising may outsource the CFO function to a SOCPA-licensed accounting firm, and the Compliance Officer or MLRO function to another CMI, a SOCPA-licensed accounting firm or a Saudi law firm. The individuals assigned must still pass the CMA exams or hold an exemption.",
            "Registered persons must be resident in the Kingdom unless exempted (Art 24(b)) and must pass the CMA qualification exams: CME-1A and CME-1B for general functions, CME-3A and 3B for brokers, CME-4A and 4B for managing, CME-5A and 5B for corporate finance, and CME-1B, 2A and 2B for the compliance and AML/CTF route.",
        ]},
        {"type": "list", "h2": "Obligations once licensed", "items": [
            "Renew each activity every year: the renewal fee is due by 30 June, and renewal depends on continuing fitness, financial adequacy and minimum capital.",
            "Meet ongoing capital adequacy under the CMA Prudential Rules, which sit alongside the entry capital in Art 6(g).",
            "Keep the CEO, CFO, Compliance Officer and MLRO (and IT Officer where required) registered at all times, and file registration changes through the portal.",
            "Make or approve every securities advertisement aimed at people in the Kingdom (SBR Art 17).",
            "Run KYC and account opening under the Investment Accounts Instructions, most recently amended on 6 January 2026, and the KYC forms in the CMIR annexes.",
            "Comply with the AML Law and counter-terrorist financing law directly; the CMA's own AML rules were rescinded in 2018. See <a href=\"@/compliance-function/\">the compliance function</a>.",
            "Follow the client money rules, including the client-money returns under Art 77 amended in 2024. Breaches of the Securities Business Regulations are offences under Article 60 of the Capital Market Law.",
        ]},
        {"type": "faq", "h2": "Common questions", "items": [
            ("Can a limited liability company hold a CMI licence?", "Yes for arranging or advising, which accept any legal form established in the Kingdom. Dealing, custody and managing require one of the forms in Art 6(f), such as a joint stock company or a subsidiary of a local bank."),
            ("Can we outsource the Compliance Officer and MLRO?", "Only if your activities are limited to managing investments, arranging or advising. The functions can then go to another CMI, a SOCPA-licensed accounting firm or a Saudi law firm, and the people doing the work must pass the CMA exams or hold an exemption."),
            ("How many CMIs are licensed?", "The CMA said there were 215 capital market institutions in the fourth quarter of 2025, up from 86 in 2017."),
            ("Can we add an activity later?", "Yes. The CMA portal handles licence variations as well as new applications. Fees and renewals are charged per activity, and the capital and legal form required for the new activity must be in place before it is added."),
        ]},
    ],
    "sources": [
        ("CMA: Capital Market Institutions Regulations (amended 2026)", "https://cma.gov.sa/en/RulesRegulations/Regulations/Documents/the_Capital_Market_Institutions_Regulations-en.pdf"),
        ("CMA: Securities Business Regulations", "https://cma.gov.sa/en/RulesRegulations/Regulations/Documents/Amended%20Securities%20Business%20Regulations.pdf"),
        ("CMA: Capital Market Law", "https://cma.gov.sa/en/RulesRegulations/CMALaw/Documents/CMA_Law.pdf"),
        ("CMA: Forms (authorisation and registration applications)", "https://cma.gov.sa/en/RulesRegulations/FormsSite/Pages/default.aspx"),
        ("CMA: Authorisation e-services", "https://cma.gov.sa/en/Services/Pages/PublicServices.aspx"),
        ("CMA: qualification exams guide", "https://cma.gov.sa/en/AboutCMA/CME/Documents/CMEExamsGuidelineEN.pdf"),
    ],
    "related": ["cma-licences", "compliance-function", "incorporation"],
},

# ---------------------------------------------------------------------------
# 4. Crowdfunding
# ---------------------------------------------------------------------------
{
    "slug": "licensing/crowdfunding-licence-saudi-arabia",
    "stage": 1,
    "hero": "lobby-city",
    "title": "Crowdfunding Licence Saudi Arabia: CMA Equity and Debt",
    "description": "CMA crowdfunding licence in Saudi Arabia: equity (2022) and debt (2025) platforms under an Arranging licence, offer limits and client money rules.",
    "h1": "Crowdfunding <em>licence</em> in Saudi Arabia",
    "lede": "Securities crowdfunding platforms, for shares and for debt instruments, are licensed by the CMA as capital market institutions authorised for Arranging. Lending-based crowdfunding sits with SAMA.",
    "blocks": [
        {"type": "table", "h2": "The two CMA models at a glance", "head": ["", "Equity crowdfunding", "Debt-instrument crowdfunding"], "rows": [
            ["Approved", "27 September 2022 (CMA_N_3164)", "8 September 2025 (CMA_N_3862)"],
            ["Licence", "CMI authorised for Arranging", "CMI authorised for Arranging"],
            ["Offer exemption", "OSCO Art (a)(10)", "OSCO Art (a)(11)"],
            ["Issuer", "Company that is not listed or wholly owned by a listed company; new shares only", "A company or a licensed special purpose entity"],
            ["Issuer limit", "SAR 10 million per class over 12 months, across platforms and private placements", "SAR 20 million outstanding (SAR 80 million for asset-backed issues)"],
            ["Retail limit", "SAR 25,000 per offering; no retail investment in non-Saudi issuers", "SAR 25,000 per issuer and SAR 100,000 per 12 months; no retail investment in asset-backed instruments"],
            ["Offer mechanics", "Offering document published at least 5 days before the offer", "Offer period of up to 45 days; at least 80% must be raised"],
        ], "note": "Rules on the Offer of Securities and Continuing Obligations (OSCO), as amended by Board Resolution 1-94-2025, and the CMIR."},
        {"type": "prose", "h2": "CMA or SAMA: start with what the investor holds", "body": [
            "The CMA regime applies when investors buy securities: shares in an issuer, or debt instruments such as sukuk issued by a company or a special purpose entity. The platform introduces issuers and investors for that offering, which is the Arranging activity, and the offering relies on an OSCO exemption.",
            "Debt-based crowdfunding licensed by SAMA is a lending activity under the Finance Companies Control Law, and the platform needs a <a href=\"@/licensing/finance-company-licence/\">finance company licence</a>. The two regimes have different capital, staffing and conduct rules, so the legal structure of the instrument has to be settled before you pick a regulator.",
        ]},
        {"type": "list", "h2": "Equity crowdfunding conditions (OSCO Art (a)(10))", "items": [
            "Only new shares may be offered.",
            "Proceeds may not be used for loans or investments.",
            "The issuer may not be listed, or wholly owned by a listed company.",
            "Total raised per class of shares is capped at SAR 10 million over 12 months, counting all platforms and private placements.",
            "A retail investor may put in up to SAR 25,000 per offering, and retail investors may not invest in non-Saudi issuers.",
            "The Annex 1 offering document must be published at least five days before the offer opens.",
            "The platform must have a valuation policy, check the issuer's credit record and hold an agreement with a credit bureau.",
        ]},
        {"type": "list", "h2": "Debt-instrument crowdfunding conditions (OSCO Art (a)(11))", "items": [
            "The issuer is a company or a licensed special purpose entity.",
            "Proceeds may not be used for loans, investments or repaying debt.",
            "The issuer's outstanding crowdfunding and private-placement financing may not exceed SAR 20 million, or SAR 80 million for asset-backed issues.",
            "A retail investor may invest up to SAR 25,000 per issuer and SAR 100,000 in any 12 months, and may not invest in asset-backed instruments.",
            "The platform acts as the debt-holders' representative.",
            "The offer period is at most 45 days. If less than 80% is raised, investors' money is returned within five days.",
        ]},
        {"type": "prose", "h2": "Holding client money", "body": [
            "Under CMIR Art 69(d), an arranging CMI may hold crowdfunding client money itself, up to SAR 80 million in total and SAR 100,000 per retail client. Above those limits, or if the platform prefers, client money must be held through a CMI licensed for custody.",
            "The May 2026 draft amendments would add a minimum capital of SAR 2 million for crowdfunding arrangers that hold client money. That figure is proposed only. The draft had not been adopted at our last check in October 2026, and today an arranging CMI needs capital equal to one year of expected expenses. See the <a href=\"@/licensing/cma-licences/\">CMA licences hub</a> for the full draft table.",
        ]},
        {"type": "table", "h2": "Capital, fees and people for a crowdfunding platform", "head": ["Item", "Requirement"], "rows": [
            ["Licence", "CMI authorised for Arranging, carried out as securities crowdfunding"],
            ["Legal form", "Any legal form established in the Kingdom"],
            ["Minimum capital", "One year of expected expenses (draft SAR 2 million floor for client-money holders is not in force)"],
            ["Study fee and annual renewal", "SAR 20,000 each"],
            ["Registered at all times", "CEO, CFO, Compliance Officer and MLRO"],
            ["IT Officer", "A registrable function for crowdfunding arrangers (CMIR Art 19(b)(8))"],
            ["Minimum headcount", "At least two registered persons, one of them the CEO, if the firm only arranges"],
            ["Outsourcing", "CFO to a SOCPA-licensed accounting firm; Compliance Officer or MLRO to another CMI, a SOCPA-licensed firm or a Saudi law firm"],
        ]},
        {"type": "prose", "h2": "From the FinTech Lab to a licence", "body": [
            "Both models were tested in the <a href=\"@/licensing/cma-fintech-experimental-permit/\">FinTech Lab</a> before they were regulated. Equity crowdfunding rules were consulted on for 45 days from April 2022 and approved in September 2022, amending the CMIR, the Investment Accounts Instructions, OSCO and the Glossary. Debt-instrument crowdfunding was tested from the second quarter of 2021; by 2024 there were 17 debt crowdfunding permits and about SAR 3.4 billion of sukuk issued through them. A draft framework followed in March 2025 and was approved in September 2025.",
            "Lab firms in debt crowdfunding may continue until their permits expire and then need an Arranging licence. New Lab applications for the model are accepted only where there is an innovative element to test, so a new debt platform goes straight to the licence. The CMA's 2025 annual report puts debt-platform offerings above SAR 5.1 billion in 2025.",
        ]},
        {"type": "steps", "h2": "Getting a platform licensed", "items": [
            ("Settle the instrument and regulator", "Confirm whether investors will hold shares or debt instruments (CMA) or loans (SAMA), and whether the platform will hold client money."),
            ("Set up the entity", "Any Saudi legal form works for Arranging. See <a href=\"@/incorporation/\">incorporation</a>."),
            ("Build the file", "The Arranging application with Annex 3.1 attachments, platform rules that reflect the OSCO limits, a valuation policy, issuer credit checks and the credit bureau agreement."),
            ("Register the people", "CEO, CFO, Compliance Officer, MLRO and IT Officer, with CMA exams passed or exemptions in hand."),
            ("Complete commencement", "Meet the commencement-of-business requirements after the Board's licence resolution, then launch."),
        ]},
        {"type": "faq", "h2": "Common questions", "items": [
            ("Do we need a FinTech Experimental Permit first?", "No for debt-instrument crowdfunding: the model now goes straight to an Arranging licence, and new Lab applications are accepted only if there is an innovative element to test. Equity crowdfunding has had its own framework under the Arranging activity since 2022."),
            ("Can retail investors back a foreign company through an equity platform?", "No. The equity exemption bars retail investment in non-Saudi issuers."),
            ("What happens if a debt offering does not reach 80%?", "The offering fails and investors' money must be returned within five days."),
            ("Is the SAR 2 million capital floor for client-money holders in force?", "No. It is part of the May 2026 draft, which had not been adopted at our last check in October 2026."),
        ]},
    ],
    "sources": [
        ("CMA news: equity crowdfunding framework approved (2022)", "https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_3164.aspx"),
        ("CMA news: debt crowdfunding framework approved (2025)", "https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_3862.aspx"),
        ("CMA: Rules on the Offer of Securities and Continuing Obligations", "https://cma.gov.sa/en/RulesRegulations/Regulations/Documents/RULES_ON_THE_OFFER_OF_SECURITIES_AND_CONTINUING_OBLIGATIONS-en.pdf"),
        ("CMA: Capital Market Institutions Regulations (amended 2026)", "https://cma.gov.sa/en/RulesRegulations/Regulations/Documents/the_Capital_Market_Institutions_Regulations-en.pdf"),
        ("CMA news: debt crowdfunding draft (March 2025)", "https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_3757.aspx"),
        ("CMA news: draft amendments to the CMI Regulations (May 2026)", "https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_4054.aspx"),
    ],
    "related": ["cma-licences", "capital-market-institution-licence", "cma-fintech-experimental-permit"],
},

# ---------------------------------------------------------------------------
# 5. Robo-advisory
# ---------------------------------------------------------------------------
{
    "slug": "licensing/robo-advisory-licence",
    "stage": 1,
    "hero": "riyadh-night",
    "title": "Robo-Advisory Licence Saudi Arabia: CMA Rules 2026",
    "description": "Robo-advisory in Saudi Arabia has been CMA-regulated since March 2026 and runs under a Managing licence. The conditions, IT Officer, capital and fees.",
    "h1": "Robo-advisory <em>licensing</em> in Saudi Arabia",
    "lede": "Since 5 March 2026 robo-advisory has been a regulated service under the CMA's Capital Market Institutions Regulations. It runs under a Managing licence, with extra conditions and a registered IT Officer.",
    "blocks": [
        {"type": "prose", "h2": "What changed in March 2026", "body": [
            "The CMA published a draft robo-advisory framework on 26 August 2025 (CMA_N_3852) and closed the consultation on 24 September 2025. On 5 March 2026 it announced Board approval (CMA_N_3994), with the amended CMIR and Glossary linked from the announcement. The Glossary amendment is Resolution 1-26-2026 of 2 March 2026. The CMIR file linked from the announcement cites Resolution 2-3-2026 of 7 January 2026, so the approval date and the announcement date differ.",
            "Before the framework, robo-advisory ran through the <a href=\"@/licensing/cma-fintech-experimental-permit/\">FinTech Lab</a>: it was among the permit models listed in 2021, and robo-advisory firms are still on the CMA's live list of test companies.",
        ]},
        {"type": "prose", "h2": "How the CMA defines it", "body": [
            "The Glossary defines a robo-advisory service as a licensed CMI's use of algorithms and modern technology to manage clients' investments according to pre-determined investment strategies, \"with no or limited human intervention\".",
            "Two points follow from that wording. The service is discretionary management of client investments, so it sits in the Managing activity. And it has to be delivered by a licensed CMI; there is no standalone robo-advisory licence for a firm to hold on its own.",
        ]},
        {"type": "table", "h2": "Which licence can offer it", "head": ["CMI licence", "Robo-advisory allowed?", "Minimum capital (in force)", "Study fee and annual renewal (SAR)"], "rows": [
            ["Managing investments", "Yes", "One year of expected expenses", "30,000"],
            ["Managing investments and operating funds", "Yes", "SAR 20 million", "60,000"],
            ["Advising only", "No", "One year of expected expenses", "20,000"],
            ["Arranging only", "No", "One year of expected expenses", "20,000"],
        ], "note": "Capital: CMIR Art 6(g). Fees: CMA circular of 27 October 2020 (Arabic only; amounts not confirmed as current)."},
        {"type": "list", "h2": "Conditions a robo-advisory service must meet", "items": [
            "No concentration in a single asset or a single issuer.",
            "Foreign securities only where they are supervised by a regulator with standards at least equivalent to the CMA's.",
            "Fair, clear disclosure on the platform of the role the algorithms play and the risks involved.",
            "Advance notice to the CMA of portfolio strategies and of material updates to them.",
            "Controls over algorithm integrity, with periodic testing completed at least 10 days before a strategy is offered to clients.",
            "Disclosure of the track record since inception, net of actual expenses, published on the firm's website.",
            "A registered IT Officer, kept registered at all times.",
        ]},
        {"type": "prose", "h2": "The IT Officer requirement", "body": [
            "The IT Officer is a registrable function under CMIR Art 19, and Art 20(b)(5) makes its registration mandatory at all times for a CMI that offers robo-advisory. It sits alongside the CEO, CFO, Compliance Officer and MLRO that every CMI must keep registered. The same function is registrable for CMIs arranging securities crowdfunding.",
            "Pick someone who can own the algorithm controls, the pre-launch testing and the information-security arrangements, and who can answer CMA questions on them. Registered persons must be resident in the Kingdom unless the CMA exempts them.",
            "The May 2026 draft amendments would extend IT Officer registration to every CMI that uses a technology platform and require technology and information-security arrangements to be tested at least annually. That draft had not been adopted at our last check in October 2026.",
        ]},
        {"type": "prose", "h2": "Legal form, people and documents", "body": [
            "Because robo-advisory needs a Managing licence, the firm must take one of the legal forms in CMIR Art 6(f), such as a joint stock company or a subsidiary of a local bank, established in the Kingdom with its head office there. A limited liability company that only holds an advising licence cannot offer the service.",
            "A CMI limited to managing investments needs at least two registered persons, one of them the CEO, and managing licensees need at least two registered portfolio managers. It may outsource the CFO function to a SOCPA-licensed accounting firm and the Compliance Officer or MLRO function to another CMI, a SOCPA-licensed accounting firm or a Saudi law firm. The CMA's exam route for the managing activity is CME-4A and CME-4B.",
            "Annex 3.1 of the CMIR lets firms limited to managing investments, arranging or advising skip some application documents. Robo-advisory applicants get a narrower version of that exemption, so expect to file more than a conventional managing-only applicant. Full detail is in the <a href=\"@/licensing/capital-market-institution-licence/\">CMI licence guide</a>.",
        ]},
        {"type": "prose", "h2": "AI advice and the edges of the perimeter", "body": [
            "The CMA continues to use the FinTech Lab for newer models. It granted permits for artificial intelligence in advisory to Sindbad.Tech in December 2025 and Lamha Tanbu in August 2026, and cancelled the Tatwir Aliddikhar robo-advisory permit at the company's request in July 2026. A product that fits the new robo-advisory rules and can comply with them is expected to seek a licence; a genuinely new model may still be a Lab candidate.",
            "Unlicensed advice is enforced. In March 2026 a person was fined SAR 250,000 after conviction for providing advisory services on social media without a licence.",
            "The market is growing quickly. CMA figures put assets managed on fintech platforms at SAR 6.41 billion in the fourth quarter of 2025, up 87% on a year earlier, across 534,571 portfolios.",
        ]},
        {"type": "steps", "h2": "From licence to launch", "items": [
            ("Hold the right licence", "A Managing licence, either new or as a variation of an existing CMI licence. See the <a href=\"@/licensing/cma-licences/\">CMA licences hub</a> for the route map."),
            ("Register the IT Officer", "File the registration through the CMA portal along with the CEO, CFO, Compliance Officer and MLRO."),
            ("Notify the strategies", "Give the CMA advance notice of each portfolio strategy, and of material updates later."),
            ("Test the algorithms", "Run and document integrity testing at least 10 days before the strategy is offered to clients."),
            ("Publish the disclosures", "Explain the algorithms' role and the risks on the platform, and publish the track record since inception net of actual expenses."),
        ]},
        {"type": "faq", "h2": "Common questions", "items": [
            ("Is there a separate robo-advisory licence?", "No. Robo-advisory is a service that only CMIs licensed for Managing Investments, or Managing Investments and Operating Funds, may offer."),
            ("Can an advising-only firm run a robo-advisor?", "No. The service manages client investments with discretion, which needs a Managing licence and one of the legal forms in CMIR Art 6(f)."),
            ("Can robo portfolios hold foreign securities?", "Yes, if the securities are supervised by a regulator whose standards are at least equivalent to the CMA's. Concentration in a single asset or issuer is not allowed."),
            ("How far ahead of launch must we test the algorithms?", "Testing must be done at least 10 days before a strategy is offered to clients, and the CMA must have had advance notice of the strategy."),
        ]},
    ],
    "sources": [
        ("CMA news: robo-advisory framework approved (March 2026)", "https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_3994.aspx"),
        ("CMA: Capital Market Institutions Regulations (amended 2026)", "https://cma.gov.sa/en/RulesRegulations/Regulations/Documents/the_Capital_Market_Institutions_Regulations-en.pdf"),
        ("CMA: Glossary of Defined Terms (March 2026)", "https://cma.gov.sa/en/RulesRegulations/Regulations/Documents/GlossaryofDefinedTermsUsed_03_2026_EN.pdf"),
        ("CMA news: robo-advisory consultation (August 2025)", "https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_3852.aspx"),
        ("CMA news: AI-in-advisory permit (August 2026)", "https://cma.gov.sa/en/MediaCenter/NEWS/Pages/CMA_N_4110.aspx"),
        ("CMA press release: 2025 annual report", "https://cma.gov.sa/en/MediaCenter/PR/Pages/CMA_2025_REPORT.aspx"),
    ],
    "related": ["cma-licences", "capital-market-institution-licence", "cma-fintech-experimental-permit"],
},
]
