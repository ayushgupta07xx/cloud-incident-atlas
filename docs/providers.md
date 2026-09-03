# Providers

24 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 10877 | 4.5h | 18.0h | 1057.6h |
| Cloudflare | cdn | 6648 | 4.0h | 8.2h | 5350.4h |
| Grafana Cloud | observability | 745 | 1.5h | 19.1h | 2571.2h |
| GitHub | devtools | 615 | 1.1h | 4.8h | 62.0h |
| DigitalOcean | cloud | 504 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 394 | 2.6h | 15.4h | 2129.0h |
| Vercel | paas | 381 | 1.2h | 6.1h | 339.2h |
| Sentry | observability | 337 | 1.5h | 6.1h | 668.4h |
| CircleCI | devtools | 305 | 1.1h | 8.0h | 96.0h |
| MongoDB Atlas | data | 270 | 2.0h | 23.3h | 308.9h |
| Confluent Cloud | data | 252 | 3.2h | 27.2h | 2821.4h |
| Elastic Cloud | observability | 252 | 3.2h | 23.5h | 364.1h |
| Netlify | paas | 215 | 41m | 3.6h | 347.3h |
| Discord | comms | 214 | 54m | 4.9h | 664.8h |
| Snowflake | data | 196 | 2.0h | 9.9h | 1801.6h |
| Zoom | comms | 150 | 2.2h | 36.0h | 1944.0h |
| Datadog | observability | 121 | 1.2h | 3.6h | 49.9h |
| New Relic | observability | 103 | 1.1h | 5.0h | 52.3h |
| Amazon Web Services | cloud | 64 | — | — | — |
| npm | devtools | 59 | 1.8h | 5.7h | 20.9h |
| OpenAI | ai | 50 | 2.2h | 13.2h | 42.4h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| HashiCorp Cloud | devtools | 33 | 2.7h | 25.2h | 120.0h |
| Google Cloud Platform | cloud | 6 | 7.4h | — | 516.0h |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 50 | 8 |
| cdn | 1 | 6648 | 131 |
| cloud | 3 | 574 | 34 |
| comms | 3 | 11241 | 115 |
| data | 3 | 718 | 255 |
| devtools | 5 | 1051 | 214 |
| observability | 5 | 1558 | 554 |
| paas | 3 | 990 | 225 |
