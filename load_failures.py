import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin
cred = credentials.Certificate(r'C:\Users\MOHAN\Documents\django\luffy\firebae-adminsdk.json')
 # assuming firebase_key.json is in same folder
firebase_admin.initialize_app(cred)

db = firestore.client()

# Your sample failures
failures = [
  
  {
    "startup": "Theranos",
    "industry": "HealthTech",
    "stage": "Series C+",
    "mistake": "Theranos misled investors, regulators, and the public by exaggerating the capabilities of its blood-testing technology, which was never scientifically validated. The company operated in secrecy, avoided peer review, and ignored regulatory standards, ultimately resulting in criminal charges for fraud and the collapse of the company.",
    "reference": "https://www.investopedia.com/articles/investing/020116/theranos-fallen-unicorn.asp"
  },
  {
    "startup": "Northvolt",
    "industry": "CleanTech / EV Batteries",
    "stage": "Series D+",
    "mistake": "Northvolt's aggressive vertical integration strategy and rapid scaling led to severe production bottlenecks, cost overruns, and operational inefficiencies. The company underestimated the complexity of battery manufacturing and supply chain management, which, combined with intense competition and market volatility, resulted in bankruptcy.",
    "reference": "https://www.businessinsider.com/northvolt-bankruptcy-redwood-materials-ev-batteries-2025-4"
  },
  {
    "startup": "Fisker Automotive",
    "industry": "Electric Vehicles",
    "stage": "Series C+",
    "mistake": "Fisker Automotive suffered from repeated execution failures, including software glitches, quality control issues, and delayed deliveries. The company's ambitious designs outpaced its manufacturing capabilities, leading to high costs, recalls, and an inability to compete with better-funded rivals, ultimately resulting in financial collapse.",
    "reference": "https://www.wsj.com/business/autos/fisker-ev-collapse-4df71216"
  },
  {
    "startup": "BrewPublik",
    "industry": "E-commerce / Alcohol Delivery",
    "stage": "Seed",
    "mistake": "BrewPublik expanded too quickly without securing sustainable funding or a scalable business model. The company failed to adapt to increasing competition and changing market dynamics, leading to mounting debts, operational inefficiencies, and eventual bankruptcy.",
    "reference": "https://www.axios.com/local/charlotte/2019/09/23/behind-the-sudden-bankruptcy-of-brewpublik-the-charlotte-startup-that-delivered-beer-to-google-and-wework-headquarters-180442"
  },
  {
    "startup": "Juicero",
    "industry": "Consumer Hardware",
    "stage": "Series A",
    "mistake": "Juicero invested heavily in developing a high-cost juicing machine that provided little added value over manual alternatives. The company failed to validate real customer demand and became a symbol of Silicon Valley excess after it was revealed that its juice packs could be squeezed by hand, leading to public ridicule and business failure.",
    "reference": "https://www.wired.com/story/why-do-startups-fail-because-hardware-is-hard"
  },
  {
    "startup": "LightSail Energy",
    "industry": "Energy Storage",
    "stage": "Series D",
    "mistake": "Despite significant venture capital investment, LightSail Energy was unable to deliver a commercially viable product. The company's compressed air energy storage technology lagged behind advancements in lithium-ion batteries, and management failed to pivot or secure strategic partnerships, resulting in obsolescence and closure.",
    "reference": "https://en.wikipedia.org/wiki/LightSail_Energy"
  },
  {
    "startup": "Munchery",
    "industry": "Food Delivery",
    "stage": "Series C",
    "mistake": "Munchery's overexpansion into new markets without achieving profitability in its core business led to unsustainable cash burn. The company struggled with high operational costs, food waste, and an inability to differentiate itself in a crowded food delivery market, ultimately leading to bankruptcy.",
    "reference": "https://en.wikipedia.org/wiki/Munchery"
  },
  {
    "startup": "Appster",
    "industry": "Software Development",
    "stage": "Growth",
    "mistake": "Appster's rapid international expansion was not matched by a stable project pipeline or effective financial controls. The company overhired, mismanaged cash flow, and failed to adapt to changing client demands, resulting in insolvency and liquidation.",
    "reference": "https://en.wikipedia.org/wiki/Appster"
  },
  {
    "startup": "Starsky Robotics",
    "industry": "Autonomous Vehicles",
    "stage": "Series B",
    "mistake": "Starsky Robotics faced insurmountable technical challenges in developing fully autonomous trucks and was unable to secure sufficient investor confidence as the AV sector cooled. The company underestimated the time and resources required for commercialization, leading to its shutdown.",
    "reference": "https://en.wikipedia.org/wiki/Starsky_Robotics"
  },
  {
    "startup": "Webvan",
    "industry": "E-commerce / Grocery Delivery",
    "stage": "IPO",
    "mistake": "Webvan's aggressive nationwide expansion before achieving product-market fit or operational efficiency led to massive infrastructure costs and unsustainable losses. The company's business model was ahead of its time, and it failed to adapt to market realities, resulting in one of the largest dot-com busts.",
    "reference": "https://en.wikipedia.org/wiki/Webvan"
  },
  {
    "startup": "Quibi",
    "industry": "Streaming Media",
    "stage": "Series D",
    "mistake": "Quibi misjudged consumer demand for short-form, mobile-only video content and invested heavily in content and marketing without validating its core assumptions. The platform failed to differentiate itself from established competitors and could not retain users, leading to a rapid shutdown.",
    "reference": "https://www.codica.com/blog/why-startups-fail/"
  },
  {
    "startup": "Picturelife",
    "industry": "Cloud Storage",
    "stage": "Acquired",
    "mistake": "Picturelife was unable to compete with tech giants like Google and Amazon, which offered superior cloud storage solutions at lower costs. The company struggled with scaling, user retention, and monetization, leading to its eventual shutdown after acquisition.",
    "reference": "https://www.navigatevc.com/insight/473-startup-failure-post-mortems/"
  },
  {
    "startup": "Hivebeat",
    "industry": "Event Management",
    "stage": "Seed",
    "mistake": "Hivebeat lacked a clear product-market fit and attempted to serve too many customer segments simultaneously. The company's unfocused strategy and inability to prioritize core features led to resource dilution and eventual failure.",
    "reference": "https://www.navigatevc.com/insight/473-startup-failure-post-mortems/"
  },
  {
    "startup": "Torquing Zano",
    "industry": "Consumer Drones",
    "stage": "Crowdfunded",
    "mistake": "Torquing Zano failed to deliver on its crowdfunding promises due to technical challenges, poor project management, and unrealistic timelines. The company's inability to communicate transparently with backers and resolve engineering issues led to its collapse.",
    "reference": "https://en.wikipedia.org/wiki/Torquing_Zano"
  },
  {
    "startup": "Yumist",
    "industry": "Food Delivery",
    "stage": "Series A",
    "mistake": "Yumist's high cash burn, inefficient operations, and inability to secure follow-on funding made it unsustainable. The company struggled to balance quality, scale, and cost in the competitive food delivery space, leading to its shutdown.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "Dial-A-Celeb",
    "industry": "Entertainment",
    "stage": "Seed",
    "mistake": "Dial-A-Celeb entered a crowded market without a compelling unique value proposition or sustainable customer acquisition strategy. The company failed to differentiate itself and could not achieve the scale needed to survive against larger competitors.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "Stayzilla",
    "industry": "Hospitality",
    "stage": "Series B",
    "mistake": "Stayzilla struggled with poor timing, insufficient funds, and intense competition from well-funded rivals. The company's inability to adapt its business model and manage cash flow led to its eventual closure.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "Roder",
    "industry": "Transportation",
    "stage": "Seed",
    "mistake": "Roder faced high operational costs, low customer retention, and fierce competition in the transportation sector. The company was unable to achieve the scale or efficiency required to survive, leading to its failure.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "Turant Delivery",
    "industry": "Logistics",
    "stage": "Seed",
    "mistake": "Turant Delivery was hampered by a lack of funding, poor cash flow management, and an inability to achieve operational efficiency. The company could not compete with larger logistics players and was forced to shut down.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "Finomena",
    "industry": "FinTech",
    "stage": "Series A",
    "mistake": "Finomena faced fierce competition in the fintech lending space and struggled with poor fund management. The company's risk assessment models were inadequate, leading to high default rates and eventual failure.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "MrNeeds",
    "industry": "E-commerce",
    "stage": "Seed",
    "mistake": "MrNeeds was unable to secure sufficient funding and faced intense competition from established e-commerce giants. The company's limited differentiation and inability to scale led to its shutdown.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "CardBack",
    "industry": "FinTech",
    "stage": "Seed",
    "mistake": "CardBack overestimated the growth of the credit card management market and expanded prematurely. The company failed to achieve product-market fit and could not sustain operations, resulting in failure.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "Overcart",
    "industry": "E-commerce",
    "stage": "Series A",
    "mistake": "Overcart suffered from poor customer service, operational inefficiencies, and negative user experiences. The company's inability to resolve these issues led to declining sales and eventual shutdown.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "RoomsTonite",
    "industry": "Hospitality",
    "stage": "Seed",
    "mistake": "RoomsTonite was unable to withstand intense competition and a tightening credit environment. The company's business model was not resilient enough to survive market pressures, leading to its closure.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "Doodhwala",
    "industry": "E-commerce",
    "stage": "Series A",
    "mistake": "Doodhwala struggled with insufficient funding, high operational costs, and strong competition from larger players. The company's inability to achieve profitability or secure additional investment led to its shutdown.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "Russsh",
    "industry": "Logistics",
    "stage": "Seed",
    "mistake": "Russsh faced persistent funding shortages and internal team challenges. The company was unable to scale its logistics operations or attract new investment, resulting in failure.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "Koinex",
    "industry": "Cryptocurrency",
    "stage": "Series A",
    "mistake": "Koinex was severely impacted by regulatory uncertainty and market instability in the cryptocurrency sector. The company's inability to adapt to changing legal frameworks and maintain user trust led to its shutdown.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "DocTalk",
    "industry": "HealthTech",
    "stage": "Series A",
    "mistake": "DocTalk's pivot to an electronic medical records (EMR) business was unsuccessful due to lack of product-market fit and strong competition. The company failed to gain traction with healthcare providers and could not sustain operations.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "LoanMeet",
    "industry": "FinTech",
    "stage": "Seed",
    "mistake": "LoanMeet was unable to secure sufficient funding and faced intense competition in the peer-to-peer lending space. The company's risk management practices were inadequate, leading to high default rates and eventual shutdown.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  },
  {
    "startup": "Houseparty",
    "industry": "Social Media",
    "stage": "Series C",
    "mistake": "Houseparty experienced a sharp decline in user engagement after the pandemic, faced funding challenges, and struggled with a shift in company focus. The platform could not maintain its growth momentum or adapt to changing user preferences, leading to its closure.",
    "reference": "https://startuptalky.com/why-startups-fail-case-study/"
  }
]

# Upload each failure
for failure in failures:
    db.collection('failures').add(failure)

print("Failures uploaded successfully!")