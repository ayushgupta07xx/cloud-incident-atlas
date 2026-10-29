# Cloud Incident Atlas

Cross-vendor incident data for 25 providers. Corpus: **23,783 incidents**. Updated 2026-10-29.

## Last 30 days

- Incidents recorded: **520**
- Major or worse: **73**

## Reliability by provider (all time)

| Provider | Category | Incidents | Median MTTR | p90 MTTR |
| --- | --- | ---: | ---: | ---: |
| Atlassian | devtools | 39 | 120m | 2244m |
| Amazon Web Services | cloud | 79 | — | — |
| Microsoft Azure | cloud | 1 | — | — |
| CircleCI | devtools | 323 | 70m | 481m |
| Cloudflare | cdn | 6826 | 239m | 504m |
| Confluent Cloud | data | 267 | 195m | 1599m |
| Datadog | observability | 128 | 72m | 224m |
| DigitalOcean | cloud | 511 | 144m | 571m |
| Discord | comms | 224 | 56m | 292m |
| Elastic Cloud | observability | 264 | 192m | 1470m |
| Google Cloud Platform | cloud | 8 | 504m | — |
| GitHub | devtools | 649 | 67m | 290m |
| Grafana Cloud | observability | 792 | 92m | 1133m |
| HashiCorp Cloud | devtools | 41 | 165m | 1525m |
| MongoDB Atlas | data | 279 | 120m | 1403m |
| Netlify | paas | 231 | 41m | 230m |
| New Relic | observability | 109 | 63m | 311m |
| npm | devtools | 68 | 108m | 342m |
| OpenAI | ai | 126 | 104m | 571m |
| Sentry | observability | 347 | 84m | 359m |
| Snowflake | data | 210 | 118m | 594m |
| Supabase | paas | 451 | 150m | 1331m |
| Twilio | comms | 11218 | 271m | 1117m |
| Vercel | paas | 395 | 72m | 364m |
| Zoom | comms | 197 | 113m | 1480m |

## New since last run (24)

- **Cloudflare** — Increased Errors for Durable Objects and Downstream Services in Eastern North America (ENAM) (`minor`)
- **Cloudflare** — Increased Durable Objects, D1 and Workflows Error Rates (`minor`)
- **Cloudflare** — Increased HTTP 429 Rate Limit Errors on Cloudflare Dashboard (`minor`)
- **Cloudflare** — Increased Worker services errors (`minor`)
- **Cloudflare** — Issues with Durable Objects availability in Eastern Europe (`minor`)
- **Cloudflare** — Increased errors and latency for CNI 2.0 traffic in LAX (`minor`)
- **Cloudflare** — Network Performance Issues in Queretaro, MX (`minor`)
- **Cloudflare** — Increased latency and error rate for R2 in ENAM (`minor`)
- **GitHub** — Disruption with Copilot Cloud services (`minor`)
- **GitHub** — Disruption with some Copilot services (`critical`)
- **Snowflake** — INC20000319 (`minor`)
- **CircleCI** — Delays for gen2 dedicated IP range jobs (`minor`)
- **Supabase** — Delayed Log Delivery from 14:10 - 15:30 UTC (`minor`)
- **Twilio** — SMS Delivery Delays from a Subset of Twilio Phone Numbers to Vivo Brazil (`minor`)
- **Twilio** — Voice Call Failures from a Subset of Twilio Phone Numbers to T-Mobile United States (`minor`)
- **Twilio** — MMS Delivery Receipt Delays from a Subset of Twilio Short Codes to T-Mobile United States (`minor`)
- **Twilio** — Gateway API (Lookup API) Failure Increase on Verizon in United States (`minor`)
- **Twilio** — Flex Agent Copilot Note Generation Issues (`minor`)
- **Twilio** — Link Shortening Redirect Errors on Branded Domains (`minor`)
- **Twilio** — SMS Delivery Delays from a Subset of Twilio Long Codes to Orange Belgium (`minor`)
- **Twilio** — Possible 503 Errors for Messaging Traffic in the Australia Region (`minor`)
- **Twilio** — Silent Network Authentication (SNA) Failure Increase and Gateway API (Lookup API) Failure Increase on EE in United Kingdom (`minor`)
- **Twilio** — Twilio Console Errors (`none`)
- **Zoom** — Service Degradation Affecting the Evaluations Acknowledge Button in Zoom Quality Management in the US Region (`minor`)

## Updated since last run (21)

- **Cloudflare** — Network Performance Issues in Ashburn, IAD → `resolved`
- **Cloudflare** — Increased Errors for Durable Objects in the Eastern North America region → `resolved`
- **Cloudflare** — Increased Errors for Durable Objects in the Eastern North America region → `resolved`
- **Cloudflare** — Network Performance Issues in Ashburn → `resolved`
- **Cloudflare** — Delayed audit log delivery for WARP and Zero Trust services → `resolved`
- **Cloudflare** — Elevated errors for some requests in Ashburn, Virginia → `resolved`
- **Cloudflare** — Elevated Error Rate for Durable Objects in Lisbon → `resolved`
- **Cloudflare** — Cloudflare Zero Trust connectivity → `resolved`
- **GitHub** — Delayed Actions status check results → `resolved`
- **GitHub** — Incident with Actions → `resolved`
- **Snowflake** — INC20000301 → `postmortem`
- **Snowflake** — INC20000299 → `postmortem`
- **Twilio** — SMS Delivery Delays and Failures from Twilio to MTC Namibia → `resolved`
- **Twilio** — Voice Call Failures From a Subset of Twilio Phone Numbers to Argentina → `resolved`
- **Twilio** — MMS Delivery Delays from a Subset of Twilio Long Codes to GCI United States → `resolved`
- **Twilio** — SMS Delivery Delays from Twilio to Surf Telecom Brazil → `resolved`
- **Twilio** — Silent Network Authentication (SNA) Failure Increase on Indosat in Indonesia → `identified`
- **Twilio** — MMS Delivery Delays from a Subset of Twilio Long Codes to C-Spire United States → `identified`
- **Twilio** — SMS Delivery Delays and Failures between a Subset of Twilio Brazil Phone Numbers and Multiple Networks in Brazil → `identified`
- **Twilio** — SMS Delivery Delays from a Subset of Twilio Short Codes to Docomo Pacific United States → `identified`
- **Twilio** — Voice Call Failures from Twilio Phone Numbers to Romania → `identified`

---

*Generated by the automated ingest pipeline in this repository. See the README for how the automation works.*
