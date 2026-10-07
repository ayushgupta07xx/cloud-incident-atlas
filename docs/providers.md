# Providers

25 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 11068 | 4.5h | 18.2h | 1057.6h |
| Cloudflare | cdn | 6742 | 4.0h | 8.4h | 5350.4h |
| Grafana Cloud | observability | 769 | 1.5h | 18.9h | 2571.2h |
| GitHub | devtools | 633 | 1.1h | 4.8h | 62.0h |
| DigitalOcean | cloud | 508 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 413 | 2.5h | 19.6h | 2129.0h |
| Vercel | paas | 392 | 1.2h | 5.9h | 339.2h |
| Sentry | observability | 342 | 1.4h | 6.0h | 668.4h |
| CircleCI | devtools | 314 | 1.1h | 8.0h | 96.0h |
| MongoDB Atlas | data | 276 | 2.0h | 23.5h | 4467.0h |
| Confluent Cloud | data | 261 | 3.2h | 27.3h | 2821.4h |
| Elastic Cloud | observability | 259 | 3.2h | 26.0h | 708.5h |
| Discord | comms | 224 | 56m | 4.9h | 664.8h |
| Netlify | paas | 224 | 38m | 3.2h | 347.3h |
| Snowflake | data | 203 | 2.0h | 9.9h | 1801.6h |
| Zoom | comms | 181 | 2.0h | 26.8h | 1944.0h |
| Datadog | observability | 127 | 1.2h | 3.8h | 49.9h |
| New Relic | observability | 108 | 1.1h | 5.2h | 52.3h |
| OpenAI | ai | 100 | 1.8h | 9.9h | 45.4h |
| Amazon Web Services | cloud | 79 | — | — | — |
| npm | devtools | 64 | 1.8h | 5.8h | 20.9h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| HashiCorp Cloud | devtools | 39 | 3.0h | 24.8h | 120.0h |
| Google Cloud Platform | cloud | 6 | 7.4h | — | 516.0h |
| Microsoft Azure | cloud | 1 | — | — | — |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 100 | 13 |
| cdn | 1 | 6742 | 133 |
| cloud | 4 | 594 | 34 |
| comms | 3 | 11473 | 120 |
| data | 3 | 740 | 272 |
| devtools | 5 | 1089 | 225 |
| observability | 5 | 1605 | 570 |
| paas | 3 | 1029 | 236 |
