# Providers

24 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 10765 | 4.5h | 18.0h | 1057.6h |
| Cloudflare | cdn | 6606 | 4.0h | 8.2h | 5350.4h |
| Grafana Cloud | observability | 737 | 1.5h | 19.2h | 2571.2h |
| GitHub | devtools | 603 | 1.1h | 4.8h | 62.0h |
| DigitalOcean | cloud | 500 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 382 | 2.6h | 14.9h | 2129.0h |
| Vercel | paas | 376 | 1.2h | 6.2h | 339.2h |
| Sentry | observability | 331 | 1.4h | 5.9h | 668.4h |
| CircleCI | devtools | 303 | 1.1h | 8.0h | 96.0h |
| MongoDB Atlas | data | 268 | 2.0h | 23.0h | 308.9h |
| Confluent Cloud | data | 248 | 3.3h | 27.4h | 2821.4h |
| Elastic Cloud | observability | 246 | 3.2h | 23.0h | 364.1h |
| Netlify | paas | 214 | 40m | 3.6h | 347.3h |
| Discord | comms | 210 | 52m | 4.9h | 664.8h |
| Snowflake | data | 189 | 2.0h | 10.0h | 1801.6h |
| Zoom | comms | 138 | 3.0h | 65.4h | 1944.0h |
| Datadog | observability | 120 | 1.2h | 3.7h | 49.9h |
| New Relic | observability | 103 | 1.1h | 5.0h | 52.3h |
| Amazon Web Services | cloud | 59 | — | — | — |
| npm | devtools | 59 | 1.8h | 5.7h | 20.9h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| OpenAI | ai | 39 | 2.2h | 13.2h | 42.4h |
| HashiCorp Cloud | devtools | 33 | 2.7h | 25.2h | 120.0h |
| Google Cloud Platform | cloud | 4 | — | — | 516.0h |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 39 | 6 |
| cdn | 1 | 6606 | 130 |
| cloud | 3 | 563 | 30 |
| comms | 3 | 11113 | 110 |
| data | 3 | 705 | 247 |
| devtools | 5 | 1037 | 210 |
| observability | 5 | 1537 | 545 |
| paas | 3 | 972 | 216 |
