# Providers

24 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 10888 | 4.5h | 18.1h | 1057.6h |
| Cloudflare | cdn | 6655 | 4.0h | 8.2h | 5350.4h |
| Grafana Cloud | observability | 749 | 1.5h | 19.0h | 2571.2h |
| GitHub | devtools | 617 | 1.1h | 4.8h | 62.0h |
| DigitalOcean | cloud | 504 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 395 | 2.6h | 15.4h | 2129.0h |
| Vercel | paas | 382 | 1.2h | 6.1h | 339.2h |
| Sentry | observability | 337 | 1.5h | 6.1h | 668.4h |
| CircleCI | devtools | 306 | 1.1h | 8.0h | 96.0h |
| MongoDB Atlas | data | 271 | 2.0h | 24.2h | 4467.0h |
| Confluent Cloud | data | 252 | 3.2h | 27.2h | 2821.4h |
| Elastic Cloud | observability | 252 | 3.2h | 23.5h | 364.1h |
| Netlify | paas | 216 | 40m | 3.5h | 347.3h |
| Discord | comms | 215 | 56m | 4.9h | 664.8h |
| Snowflake | data | 197 | 2.0h | 9.9h | 1801.6h |
| Zoom | comms | 153 | 2.1h | 33.0h | 1944.0h |
| Datadog | observability | 122 | 1.2h | 3.9h | 49.9h |
| New Relic | observability | 103 | 1.1h | 5.0h | 52.3h |
| Amazon Web Services | cloud | 68 | — | — | — |
| npm | devtools | 61 | 1.8h | 5.6h | 20.9h |
| OpenAI | ai | 51 | 2.2h | 12.9h | 42.4h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| HashiCorp Cloud | devtools | 34 | 3.0h | 25.2h | 120.0h |
| Google Cloud Platform | cloud | 6 | 7.4h | — | 516.0h |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 51 | 8 |
| cdn | 1 | 6655 | 131 |
| cloud | 3 | 578 | 34 |
| comms | 3 | 11256 | 115 |
| data | 3 | 720 | 257 |
| devtools | 5 | 1057 | 215 |
| observability | 5 | 1563 | 555 |
| paas | 3 | 993 | 226 |
