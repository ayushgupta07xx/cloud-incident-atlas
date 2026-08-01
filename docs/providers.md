# Providers

24 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 10662 | 4.5h | 17.6h | 1057.6h |
| Cloudflare | cdn | 6565 | 4.0h | 8.2h | 5350.4h |
| Grafana Cloud | observability | 728 | 1.5h | 19.2h | 2571.2h |
| GitHub | devtools | 586 | 1.1h | 4.7h | 62.0h |
| DigitalOcean | cloud | 494 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 377 | 2.6h | 14.1h | 2129.0h |
| Vercel | paas | 372 | 1.2h | 6.1h | 339.2h |
| Sentry | observability | 324 | 1.4h | 6.0h | 668.4h |
| CircleCI | devtools | 295 | 1.1h | 8.2h | 96.0h |
| MongoDB Atlas | data | 265 | 2.0h | 23.1h | 308.9h |
| Confluent Cloud | data | 248 | 3.3h | 27.4h | 2821.4h |
| Elastic Cloud | observability | 241 | 3.1h | 22.1h | 364.1h |
| Netlify | paas | 212 | 41m | 3.7h | 347.3h |
| Discord | comms | 207 | 54m | 5.0h | 664.8h |
| Snowflake | data | 183 | 2.0h | 10.0h | 1801.6h |
| Zoom | comms | 129 | 3.6h | 95.8h | 1944.0h |
| Datadog | observability | 119 | 1.2h | 3.7h | 49.9h |
| New Relic | observability | 102 | 1.1h | 5.1h | 52.3h |
| npm | devtools | 59 | 1.8h | 5.7h | 20.9h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| Amazon Web Services | cloud | 39 | — | — | — |
| OpenAI | ai | 26 | 1.8h | 15.4h | 42.4h |
| HashiCorp Cloud | devtools | 25 | 6.2h | 24.4h | 120.0h |
| Google Cloud Platform | cloud | 4 | — | — | 516.0h |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 26 | 6 |
| cdn | 1 | 6565 | 129 |
| cloud | 3 | 537 | 30 |
| comms | 3 | 10998 | 106 |
| data | 3 | 696 | 241 |
| devtools | 5 | 1004 | 202 |
| observability | 5 | 1514 | 532 |
| paas | 3 | 961 | 213 |
