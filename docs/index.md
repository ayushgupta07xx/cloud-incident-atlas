# Cloud Incident Atlas

Cross-vendor incident data for 25 providers. Corpus: **24,085 incidents**. Updated 2026-11-17.

## Last 30 days

- Incidents recorded: **520**
- Major or worse: **62**

## Reliability by provider (all time)

| Provider | Category | Incidents | Median MTTR | p90 MTTR |
| --- | --- | ---: | ---: | ---: |
| Atlassian | devtools | 39 | 120m | 2244m |
| Amazon Web Services | cloud | 97 | — | — |
| Microsoft Azure | cloud | 1 | — | — |
| CircleCI | devtools | 324 | 69m | 481m |
| Cloudflare | cdn | 6880 | 239m | 508m |
| Confluent Cloud | data | 268 | 194m | 1592m |
| Datadog | observability | 128 | 72m | 224m |
| DigitalOcean | cloud | 512 | 144m | 571m |
| Discord | comms | 228 | 56m | 295m |
| Elastic Cloud | observability | 265 | 192m | 1462m |
| Google Cloud Platform | cloud | 8 | 504m | — |
| GitHub | devtools | 674 | 67m | 283m |
| Grafana Cloud | observability | 805 | 93m | 1136m |
| HashiCorp Cloud | devtools | 47 | 160m | 1494m |
| MongoDB Atlas | data | 279 | 120m | 1403m |
| Netlify | paas | 235 | 41m | 236m |
| New Relic | observability | 112 | 63m | 306m |
| npm | devtools | 69 | 107m | 340m |
| OpenAI | ai | 144 | 111m | 726m |
| Sentry | observability | 354 | 84m | 354m |
| Snowflake | data | 216 | 121m | 598m |
| Supabase | paas | 466 | 148m | 1242m |
| Twilio | comms | 11326 | 272m | 1131m |
| Vercel | paas | 397 | 72m | 362m |
| Zoom | comms | 211 | 113m | 1448m |

## New since last run (32)

- **Cloudflare** — Network performance issues in Los Angeles (LAX) and Frankfurt (FRA) datacenters (`minor`)
- **Cloudflare** — Turnstile verification failures (`minor`)
- **Cloudflare** — Errors and stalled predictions on some models (`minor`)
- **Cloudflare** — Cloudflare One Gateway traffic unable to connect to Cloudflare domains that are regionalized (`minor`)
- **Cloudflare** — Elevated number of 5xx and 499 errors (`minor`)
- **Cloudflare** — Elevated number of 52x origin connectivity errors in Seoul (`minor`)
- **Cloudflare** — Network Performance Issues in Ashburn, US (`none`)
- **Cloudflare** — Network Performance Issues in Montreal, Canada (`minor`)
- **Cloudflare** — Errors creating predictions for some models (`minor`)
- **DigitalOcean** — App Platform Accessibility in Cloud Panel (`none`)
- **Snowflake** — INC20000351 (`minor`)
- **HashiCorp Cloud** — Remote Terraform runs failing (`minor`)
- **Supabase** — Projects in sa-east-1 experiencing delayed event ingestion (`none`)
- **Supabase** — ‘Project not specified’ errors reported for users in ap-northeast-2 (`minor`)
- **OpenAI** — Costs API data is delayed (`minor`)
- **Twilio** — Voice Call Post Dial Delay, Audio Quality Degradation, and Silent and One-Way Audio Between Twilio Phone Numbers and Brazil (`minor`)
- **Twilio** — SMS Delivery Failures between a Subset of Twilio Short Codes and Claro in Brazil (`minor`)
- **Twilio** — Customers Unable to View Balance in Console (`minor`)
- **Twilio** — SMS Delivery Delays from Twilio to Sky United Kingdom (`minor`)
- **Twilio** — Voice Call Audio Quality Degradation Between Twilio and Multiple Networks in United Kingdom (`minor`)
- **Twilio** — Gateway API (Lookup API) Failure Increase in Canada (`minor`)
- **Twilio** — SMS Delivery Delays from a Subset of Twilio Short Codes to Liberty Mobile Puerto Rico (`minor`)
- **Twilio** — SMS Delivery Delays from Twilio to Telenor Pakistan (`minor`)
- **Twilio** — Voice Call Audio Quality Degradation between Twilio and Multiple Networks in United Kingdom (`minor`)
- **Twilio** — SMS Delivery Delays from a Subset of Twilio Short Codes to T-Mobile United States (`minor`)

## Updated since last run (17)

- **GitHub** — Incident with Pull Requests → `resolved`
- **GitHub** — Incident with Webhooks API → `resolved`
- **GitHub** — Increased timeouts due to surge in anonymous users → `resolved`
- **GitHub** — Increase in timeouts for some unauthenticated users → `resolved`
- **GitHub** — Incident with Pull Requests, Git Operations and Issues → `resolved`
- **GitHub** — Increased task-related errors for Copilot Mission Control → `resolved`
- **GitHub** — Incident with API, Git, and Copilot requests → `resolved`
- **GitHub** — Elevated errors on GPT-5.4 Nano → `resolved`
- **GitHub** — Incident with Actions, Issues, API Requests and Pull Requests → `resolved`
- **GitHub** — Project updates delayed → `resolved`
- **GitHub** — Delays for Pull Requests and Webhook deliveries → `resolved`
- **Twilio** — SMS Delivery Receipt Failures from Twilio to Claro Costa Rica → `resolved`
- **Twilio** — SMS Delivery Receipt Delays from a Subset of Twilio Short Codes to Multiple Networks in New Zealand → `resolved`
- **Twilio** — SMS Delivery Delays from Twilio to MTN/Libertis Congo → `resolved`
- **Twilio** — Silent Network Authentication (SNA) Missing Redirects in Philippines → `resolved`
- **Twilio** — SMS Delivery Delays from Twilio to Brisanet Servicos De Telecomunicacoes SA Brazil → `monitoring`
- **Twilio** — Voice Call Silent and One-Way Audio from Colombia to a Subset of Twilio Phone Numbers → `identified`

---

*Generated by the automated ingest pipeline in this repository. See the README for how the automation works.*
