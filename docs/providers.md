# Providers

24 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 10962 | 4.5h | 18.1h | 1057.6h |
| Cloudflare | cdn | 6688 | 4.0h | 8.2h | 5350.4h |
| Grafana Cloud | observability | 757 | 1.5h | 18.9h | 2571.2h |
| GitHub | devtools | 622 | 1.1h | 4.8h | 62.0h |
| DigitalOcean | cloud | 506 | 2.4h | 9.6h | 304.2h |
| Supabase | paas | 401 | 2.6h | 17.7h | 2129.0h |
| Vercel | paas | 386 | 1.2h | 6.0h | 339.2h |
| Sentry | observability | 339 | 1.4h | 6.1h | 668.4h |
| CircleCI | devtools | 310 | 1.1h | 8.0h | 96.0h |
| MongoDB Atlas | data | 273 | 2.0h | 23.8h | 4467.0h |
| Elastic Cloud | observability | 256 | 3.2h | 24.4h | 364.1h |
| Confluent Cloud | data | 255 | 3.2h | 27.5h | 2821.4h |
| Discord | comms | 221 | 56m | 4.9h | 664.8h |
| Netlify | paas | 218 | 40m | 3.4h | 347.3h |
| Snowflake | data | 200 | 2.0h | 9.9h | 1801.6h |
| Zoom | comms | 160 | 2.0h | 33.0h | 1944.0h |
| Datadog | observability | 122 | 1.2h | 3.9h | 49.9h |
| New Relic | observability | 105 | 1.1h | 5.2h | 52.3h |
| Amazon Web Services | cloud | 70 | — | — | — |
| OpenAI | ai | 70 | 1.9h | 11.4h | 42.4h |
| npm | devtools | 63 | 1.7h | 5.4h | 20.9h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| HashiCorp Cloud | devtools | 36 | 3.6h | 25.0h | 120.0h |
| Google Cloud Platform | cloud | 6 | 7.4h | — | 516.0h |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 70 | 9 |
| cdn | 1 | 6688 | 131 |
| cloud | 3 | 582 | 34 |
| comms | 3 | 11343 | 118 |
| data | 3 | 728 | 263 |
| devtools | 5 | 1070 | 218 |
| observability | 5 | 1579 | 560 |
| paas | 3 | 1005 | 228 |
