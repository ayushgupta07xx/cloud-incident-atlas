# Providers

24 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 10721 | 4.5h | 17.7h | 1057.6h |
| Cloudflare | cdn | 6590 | 4.0h | 8.2h | 5350.4h |
| Grafana Cloud | observability | 735 | 1.5h | 19.2h | 2571.2h |
| GitHub | devtools | 595 | 1.1h | 4.8h | 62.0h |
| DigitalOcean | cloud | 499 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 379 | 2.6h | 15.0h | 2129.0h |
| Vercel | paas | 373 | 1.2h | 6.1h | 339.2h |
| Sentry | observability | 326 | 1.4h | 6.0h | 668.4h |
| CircleCI | devtools | 299 | 1.1h | 8.1h | 96.0h |
| MongoDB Atlas | data | 267 | 2.0h | 23.0h | 308.9h |
| Confluent Cloud | data | 248 | 3.3h | 27.4h | 2821.4h |
| Elastic Cloud | observability | 243 | 3.1h | 22.1h | 364.1h |
| Netlify | paas | 213 | 41m | 3.6h | 347.3h |
| Discord | comms | 209 | 54m | 5.0h | 664.8h |
| Snowflake | data | 186 | 2.1h | 10.0h | 1801.6h |
| Zoom | comms | 135 | 3.0h | 78.5h | 1944.0h |
| Datadog | observability | 120 | 1.2h | 3.7h | 49.9h |
| New Relic | observability | 103 | 1.1h | 5.0h | 52.3h |
| npm | devtools | 59 | 1.8h | 5.7h | 20.9h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| Amazon Web Services | cloud | 39 | — | — | — |
| OpenAI | ai | 36 | 2.1h | 13.6h | 42.4h |
| HashiCorp Cloud | devtools | 30 | 3.0h | 24.6h | 120.0h |
| Google Cloud Platform | cloud | 4 | — | — | 516.0h |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 36 | 6 |
| cdn | 1 | 6590 | 129 |
| cloud | 3 | 542 | 30 |
| comms | 3 | 11065 | 109 |
| data | 3 | 701 | 244 |
| devtools | 5 | 1022 | 206 |
| observability | 5 | 1527 | 537 |
| paas | 3 | 965 | 214 |
