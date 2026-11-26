# Providers

25 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 11363 | 4.5h | 18.9h | 1174.9h |
| Cloudflare | cdn | 6919 | 4.0h | 8.5h | 5350.4h |
| Grafana Cloud | observability | 809 | 1.6h | 18.9h | 2571.2h |
| GitHub | devtools | 682 | 1.1h | 4.6h | 62.0h |
| DigitalOcean | cloud | 513 | 2.4h | 9.6h | 304.2h |
| Supabase | paas | 471 | 2.5h | 21.3h | 2129.0h |
| Vercel | paas | 399 | 1.2h | 6.0h | 339.2h |
| Sentry | observability | 356 | 1.4h | 5.9h | 668.4h |
| CircleCI | devtools | 328 | 1.2h | 8.0h | 96.0h |
| MongoDB Atlas | data | 279 | 2.0h | 23.4h | 4467.0h |
| Confluent Cloud | data | 269 | 3.2h | 26.4h | 2821.4h |
| Elastic Cloud | observability | 265 | 3.2h | 24.4h | 708.5h |
| Netlify | paas | 236 | 41m | 3.9h | 347.3h |
| Discord | comms | 228 | 56m | 4.9h | 664.8h |
| Zoom | comms | 219 | 1.7h | 23.8h | 1944.0h |
| Snowflake | data | 218 | 2.0h | 10.0h | 1844.0h |
| OpenAI | ai | 149 | 1.9h | 12.9h | 93.5h |
| Datadog | observability | 128 | 1.2h | 3.7h | 49.9h |
| New Relic | observability | 112 | 1.0h | 5.1h | 52.3h |
| Amazon Web Services | cloud | 97 | — | — | — |
| npm | devtools | 69 | 1.8h | 5.7h | 20.9h |
| HashiCorp Cloud | devtools | 51 | 2.7h | 27.5h | 126.1h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| Google Cloud Platform | cloud | 8 | 8.4h | — | 516.0h |
| Microsoft Azure | cloud | 1 | — | — | — |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 149 | 19 |
| cdn | 1 | 6919 | 146 |
| cloud | 4 | 619 | 37 |
| comms | 3 | 11810 | 123 |
| data | 3 | 766 | 282 |
| devtools | 5 | 1169 | 253 |
| observability | 5 | 1670 | 597 |
| paas | 3 | 1106 | 253 |
