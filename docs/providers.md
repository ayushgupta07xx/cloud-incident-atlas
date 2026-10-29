# Providers

25 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 11218 | 4.5h | 18.6h | 1174.9h |
| Cloudflare | cdn | 6826 | 4.0h | 8.4h | 5350.4h |
| Grafana Cloud | observability | 792 | 1.5h | 18.9h | 2571.2h |
| GitHub | devtools | 649 | 1.1h | 4.8h | 62.0h |
| DigitalOcean | cloud | 511 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 451 | 2.5h | 22.2h | 2129.0h |
| Vercel | paas | 395 | 1.2h | 6.1h | 339.2h |
| Sentry | observability | 347 | 1.4h | 6.0h | 668.4h |
| CircleCI | devtools | 323 | 1.2h | 8.0h | 96.0h |
| MongoDB Atlas | data | 279 | 2.0h | 23.4h | 4467.0h |
| Confluent Cloud | data | 267 | 3.2h | 26.6h | 2821.4h |
| Elastic Cloud | observability | 264 | 3.2h | 24.5h | 708.5h |
| Netlify | paas | 231 | 41m | 3.8h | 347.3h |
| Discord | comms | 224 | 56m | 4.9h | 664.8h |
| Snowflake | data | 210 | 2.0h | 9.9h | 1801.6h |
| Zoom | comms | 197 | 1.9h | 24.7h | 1944.0h |
| Datadog | observability | 128 | 1.2h | 3.7h | 49.9h |
| OpenAI | ai | 126 | 1.7h | 9.5h | 70.7h |
| New Relic | observability | 109 | 1.1h | 5.2h | 52.3h |
| Amazon Web Services | cloud | 79 | — | — | — |
| npm | devtools | 68 | 1.8h | 5.7h | 20.9h |
| HashiCorp Cloud | devtools | 41 | 2.8h | 25.4h | 126.1h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| Google Cloud Platform | cloud | 8 | 8.4h | — | 516.0h |
| Microsoft Azure | cloud | 1 | — | — | — |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 126 | 17 |
| cdn | 1 | 6826 | 143 |
| cloud | 4 | 599 | 37 |
| comms | 3 | 11639 | 120 |
| data | 3 | 756 | 280 |
| devtools | 5 | 1120 | 235 |
| observability | 5 | 1640 | 588 |
| paas | 3 | 1077 | 250 |
