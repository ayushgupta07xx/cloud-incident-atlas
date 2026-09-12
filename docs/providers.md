# Providers

24 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 10926 | 4.5h | 18.1h | 1057.6h |
| Cloudflare | cdn | 6675 | 4.0h | 8.2h | 5350.4h |
| Grafana Cloud | observability | 752 | 1.5h | 18.9h | 2571.2h |
| GitHub | devtools | 617 | 1.1h | 4.8h | 62.0h |
| DigitalOcean | cloud | 505 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 397 | 2.6h | 16.7h | 2129.0h |
| Vercel | paas | 383 | 1.2h | 6.1h | 339.2h |
| Sentry | observability | 339 | 1.4h | 6.1h | 668.4h |
| CircleCI | devtools | 307 | 1.1h | 8.0h | 96.0h |
| MongoDB Atlas | data | 272 | 2.0h | 24.0h | 4467.0h |
| Confluent Cloud | data | 254 | 3.2h | 27.5h | 2821.4h |
| Elastic Cloud | observability | 254 | 3.2h | 23.4h | 364.1h |
| Discord | comms | 217 | 56m | 4.9h | 664.8h |
| Netlify | paas | 217 | 39m | 3.5h | 347.3h |
| Snowflake | data | 199 | 2.0h | 9.9h | 1801.6h |
| Zoom | comms | 158 | 2.1h | 33.0h | 1944.0h |
| Datadog | observability | 122 | 1.2h | 3.9h | 49.9h |
| New Relic | observability | 103 | 1.1h | 5.0h | 52.3h |
| Amazon Web Services | cloud | 68 | — | — | — |
| npm | devtools | 61 | 1.8h | 5.6h | 20.9h |
| OpenAI | ai | 61 | 2.2h | 12.2h | 42.4h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| HashiCorp Cloud | devtools | 35 | 3.3h | 25.1h | 120.0h |
| Google Cloud Platform | cloud | 6 | 7.4h | — | 516.0h |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 61 | 8 |
| cdn | 1 | 6675 | 131 |
| cloud | 3 | 579 | 34 |
| comms | 3 | 11301 | 116 |
| data | 3 | 725 | 260 |
| devtools | 5 | 1059 | 216 |
| observability | 5 | 1570 | 558 |
| paas | 3 | 997 | 228 |
