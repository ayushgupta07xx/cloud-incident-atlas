# Providers

25 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 11307 | 4.5h | 18.8h | 1174.9h |
| Cloudflare | cdn | 6869 | 4.0h | 8.5h | 5350.4h |
| Grafana Cloud | observability | 805 | 1.6h | 18.9h | 2571.2h |
| GitHub | devtools | 673 | 1.1h | 4.7h | 62.0h |
| DigitalOcean | cloud | 511 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 464 | 2.5h | 20.9h | 2129.0h |
| Vercel | paas | 397 | 1.2h | 6.0h | 339.2h |
| Sentry | observability | 354 | 1.4h | 5.9h | 668.4h |
| CircleCI | devtools | 324 | 1.2h | 8.0h | 96.0h |
| MongoDB Atlas | data | 279 | 2.0h | 23.4h | 4467.0h |
| Confluent Cloud | data | 268 | 3.2h | 26.5h | 2821.4h |
| Elastic Cloud | observability | 265 | 3.2h | 24.4h | 708.5h |
| Netlify | paas | 235 | 41m | 3.9h | 347.3h |
| Discord | comms | 227 | 56m | 4.9h | 664.8h |
| Snowflake | data | 215 | 2.0h | 10.0h | 1844.0h |
| Zoom | comms | 205 | 1.9h | 24.9h | 1944.0h |
| OpenAI | ai | 143 | 1.8h | 11.3h | 93.5h |
| Datadog | observability | 128 | 1.2h | 3.7h | 49.9h |
| New Relic | observability | 112 | 1.0h | 5.1h | 52.3h |
| Amazon Web Services | cloud | 91 | — | — | — |
| npm | devtools | 69 | 1.8h | 5.7h | 20.9h |
| HashiCorp Cloud | devtools | 44 | 2.5h | 25.2h | 126.1h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| Google Cloud Platform | cloud | 8 | 8.4h | — | 516.0h |
| Microsoft Azure | cloud | 1 | — | — | — |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 143 | 18 |
| cdn | 1 | 6869 | 143 |
| cloud | 4 | 611 | 37 |
| comms | 3 | 11739 | 123 |
| data | 3 | 762 | 280 |
| devtools | 5 | 1149 | 248 |
| observability | 5 | 1664 | 596 |
| paas | 3 | 1096 | 250 |
