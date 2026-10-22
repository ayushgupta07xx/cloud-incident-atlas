# Providers

25 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 11159 | 4.5h | 18.2h | 1057.6h |
| Cloudflare | cdn | 6794 | 4.0h | 8.4h | 5350.4h |
| Grafana Cloud | observability | 787 | 1.6h | 18.9h | 2571.2h |
| GitHub | devtools | 642 | 1.1h | 4.8h | 62.0h |
| DigitalOcean | cloud | 510 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 448 | 2.5h | 21.6h | 2129.0h |
| Vercel | paas | 394 | 1.2h | 6.1h | 339.2h |
| Sentry | observability | 347 | 1.4h | 6.0h | 668.4h |
| CircleCI | devtools | 322 | 1.2h | 8.0h | 96.0h |
| MongoDB Atlas | data | 279 | 2.0h | 23.4h | 4467.0h |
| Confluent Cloud | data | 267 | 3.2h | 26.6h | 2821.4h |
| Elastic Cloud | observability | 263 | 3.2h | 25.1h | 708.5h |
| Netlify | paas | 228 | 40m | 3.4h | 347.3h |
| Discord | comms | 224 | 56m | 4.9h | 664.8h |
| Snowflake | data | 209 | 2.0h | 9.9h | 1801.6h |
| Zoom | comms | 194 | 1.8h | 25.1h | 1944.0h |
| Datadog | observability | 127 | 1.2h | 3.8h | 49.9h |
| OpenAI | ai | 118 | 1.8h | 10.4h | 70.7h |
| New Relic | observability | 108 | 1.1h | 5.2h | 52.3h |
| Amazon Web Services | cloud | 79 | — | — | — |
| npm | devtools | 67 | 1.8h | 5.7h | 20.9h |
| HashiCorp Cloud | devtools | 40 | 3.0h | 27.5h | 126.1h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| Google Cloud Platform | cloud | 8 | 8.4h | — | 516.0h |
| Microsoft Azure | cloud | 1 | — | — | — |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 118 | 17 |
| cdn | 1 | 6794 | 139 |
| cloud | 4 | 598 | 36 |
| comms | 3 | 11577 | 120 |
| data | 3 | 755 | 280 |
| devtools | 5 | 1110 | 232 |
| observability | 5 | 1632 | 583 |
| paas | 3 | 1070 | 249 |
