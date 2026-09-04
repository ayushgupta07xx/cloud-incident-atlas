# Cloud Incident Atlas

Cross-vendor incident data for 24 providers. Corpus: **22,857 incidents**. Updated 2026-09-04.

## Last 30 days

- Incidents recorded: **495**
- Major or worse: **72**

## Reliability by provider (all time)

| Provider | Category | Incidents | Median MTTR | p90 MTTR |
| --- | --- | ---: | ---: | ---: |
| Atlassian | devtools | 39 | 120m | 2244m |
| Amazon Web Services | cloud | 68 | — | — |
| CircleCI | devtools | 305 | 66m | 482m |
| Cloudflare | cdn | 6651 | 239m | 495m |
| Confluent Cloud | data | 252 | 193m | 1633m |
| Datadog | observability | 122 | 74m | 234m |
| DigitalOcean | cloud | 504 | 145m | 571m |
| Discord | comms | 215 | 56m | 296m |
| Elastic Cloud | observability | 252 | 191m | 1412m |
| Google Cloud Platform | cloud | 6 | 444m | — |
| GitHub | devtools | 615 | 67m | 287m |
| Grafana Cloud | observability | 746 | 90m | 1146m |
| HashiCorp Cloud | devtools | 33 | 160m | 1515m |
| MongoDB Atlas | data | 271 | 120m | 1449m |
| Netlify | paas | 216 | 40m | 210m |
| New Relic | observability | 103 | 63m | 303m |
| npm | devtools | 61 | 105m | 338m |
| OpenAI | ai | 51 | 131m | 773m |
| Sentry | observability | 337 | 89m | 365m |
| Snowflake | data | 197 | 121m | 595m |
| Supabase | paas | 395 | 158m | 922m |
| Twilio | comms | 10885 | 270m | 1083m |
| Vercel | paas | 381 | 73m | 367m |
| Zoom | comms | 152 | 124m | 1980m |

## New since last run (27)

- **Cloudflare** — Workers Builds elevated queue times (`minor`)
- **Cloudflare** — Elevated number of R2 503 errors in Western North America region (`minor`)
- **Cloudflare** — Elevated connectivity degradation in NRT (`minor`)
- **Datadog** — Delayed CICD Optimization, Code Coverage, Code Security, and DORA data (`minor`)
- **npm** — npm audits endpoint is having issues (`minor`)
- **npm** — Intermittent Failures Impacting npm Publish (`minor`)
- **Snowflake** — INC20000199 (`critical`)
- **MongoDB Atlas** — Impaired Cluster operations in AWS me-central-1 and AWS me-south-1 (`major`)
- **Grafana Cloud** — Tempo and Mimir Read and Write Failures (`minor`)
- **Netlify** — Increased errors on High Performance Edge Network - FRA Region (`minor`)
- **Supabase** — Project Lifecycle Actions Showing increased error rates across all regions (`critical`)
- **OpenAI** — Users in APAC region may face increased error in ChatGPT, Work, image generation, file upload, Voice, and Codex Cloud (`minor`)
- **Twilio** — Multiple delivery failures to Microsoft (`maintenance`)
- **Twilio** — SMS Delivery Delays from Twilio to MobiFone Vietnam (`minor`)
- **Twilio** — MMS Delivery Delays from a Subset of Australia Subscribers to Twilio Australia Phone Numbers (`minor`)
- **Twilio** — SMS Delivery Delays and Failures from a Subset of Twilio Long Codes to Vivo and Claro Brazil (`minor`)
- **Twilio** — SMS Delivery Delays and Failures from Twilio to Africell and Qcell Gambia (`minor`)
- **Twilio** — Intermittent Delays and Failures in Message Delivery (`minor`)
- **Twilio** — Registration Notification Issues (`none`)
- **Twilio** — Retroactive Incident: Twilio Personalized Support Phone Line Affected (`none`)
- **Discord** — Some Servers Unavailable (`none`)
- **Zoom** — Service Degradation Affecting Zoom Phone Audio in Japan (`none`)
- **Zoom** — Service Degradation Affecting Zoom SMS delays in North America. (`none`)
- **Amazon Web Services** — Service is operating normally: [RESOLVED] Increased API Error Rates (`minor`)
- **Amazon Web Services** — Service impact: Increased API Error Rates (`minor`)

## Updated since last run (16)

- **Cloudflare** — HTTP/3 issue affecting R2 custom domains → `resolved`
- **GitHub** — Incident with Grok Copilot AI Model Provider → `resolved`
- **GitHub** — Elevated rate of errors for OpenAI models provided by Copilot → `resolved`
- **Snowflake** — INC20000182 → `postmortem`
- **Snowflake** — INC20000168 → `postmortem`
- **MongoDB Atlas** — Impaired Cluster Operations – AWS me-central-1 (United Arab Emirates)  and AWS me-south-1 (Bahrain) → `resolved`
- **Elastic Cloud** — Replication bug causing slow recoveries → `monitoring`
- **Elastic Cloud** — Ingestion issues for Managed OTLP and Managed Intake Service endpoints in the Azure Australia East region → `resolved`
- **OpenAI** — Elevated errors across ChatGPT and Codex → `resolved`
- **Twilio** — SMS Delivery Receipt Delays from a Subset of Twilio Phone Numbers to Telefonica El Salvador → `resolved`
- **Twilio** — Message Logs Performance Issues → `resolved`
- **Twilio** — SMS Delivery Delays from a Subset of Twilio Short Codes to C-Spire and Dish United States → `resolved`
- **Twilio** — MMS Delivery Receipt Delays From a Subset of Twilio Long Codes to GCI United States → `identified`
- **Twilio** — SMS Delivery Receipt Delays from Twilio to Three United Kingdom → `monitoring`
- **Discord** — Some servers unavailable → `resolved`
- **Google Cloud Platform** — Multiple products in us-central1-b are experiencing network service degradation. → `resolved`

---

*Generated by the automated ingest pipeline in this repository. See the README for how the automation works.*
